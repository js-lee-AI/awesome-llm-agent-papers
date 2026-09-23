#!/usr/bin/env python3
"""Keep the translated READMEs line-for-line in step with README.md.

README.md is the source. README.ko.md, README.zh-CN.md, README.ja.md,
README.pt-BR.md and README.es.md translate it one line at a time: line N of a
translation is line N of the English file in another language. That makes
drift easy to see. A paper added
to one file and not the others, a count bumped in English only, a code link
fixed in one place: each of these shows up as a line that no longer matches.

Per line, a translation must keep what isn't language:

  links     every link target, href and src, as a multiset
  anchors   every <a id>, so Contents and "Back to Contents" still land
  entries   title, link, author/venue parenthesis and [code] tail verbatim;
            only the italic gloss is translated, and it must end a sentence
  code      inline code spans, and fenced blocks line for line
  shape     blank lines, heading levels, table cells
  titles    section titles, "Show N papers" and "Back to Contents" read
            exactly as fixed below, so every edition names things one way
  counts    the number in every heading, Contents line and toggle

It also rejects dashes (the list uses none in any language) and the native
renderings of terms that stay in English (scripts/i18n_terms.json).

Numbers elsewhere in a line are compared too, but only as a warning: a
translation can legitimately write "three" as a digit.

    python3 scripts/check_i18n.py            # check all translations, exit 1 on error
    python3 scripts/check_i18n.py --fix      # rewrite stale counts from README.md, then check
    python3 scripts/check_i18n.py -w         # also print warnings
    python3 scripts/check_i18n.py --src A --tr B --lang ko   # check one pair
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LANGS = {"ko": "README.ko.md", "zh": "README.zh-CN.md", "ja": "README.ja.md",
         "pt": "README.pt-BR.md", "es": "README.es.md"}
TERMS = ROOT / "scripts" / "i18n_terms.json"

# Section and page titles, fixed per language. Keys are the English text with
# any trailing "(N)" count removed.
TITLES = {
    "✨ Highlights": {"ko": "✨ 한눈에 보기", "zh": "✨ 亮点", "ja": "✨ ハイライト", "pt": "✨ Destaques", "es": "✨ Destacados"},
    "⭐ Starter Kit": {"ko": "⭐ 스타터 키트", "zh": "⭐ 入门必读", "ja": "⭐ スターターキット", "pt": "⭐ Kit inicial", "es": "⭐ Kit de inicio"},
    "🔥 10 to Watch (2026)": {"ko": "🔥 주목할 10편 (2026)", "zh": "🔥 值得关注的 10 篇 (2026)", "ja": "🔥 注目の10本 (2026)", "pt": "🔥 10 artigos para acompanhar (2026)", "es": "🔥 10 artículos para seguir (2026)"},
    "Contents": {"ko": '<a id="contents"></a>목차', "zh": '<a id="contents"></a>目录', "ja": '<a id="contents"></a>目次', "pt": '<a id="contents"></a>Sumário', "es": '<a id="contents"></a>Índice'},
    "🧭 Background": {"ko": "🧭 배경", "zh": "🧭 背景", "ja": "🧭 背景", "pt": "🧭 Fundamentos", "es": "🧭 Fundamentos"},
    "📚 Surveys & Position Papers": {"ko": "📚 서베이와 포지션 페이퍼", "zh": "📚 综述与立场论文", "ja": "📚 サーベイとポジションペーパー", "pt": "📚 Surveys e artigos de posicionamento", "es": "📚 Revisiones y artículos de posición"},
    "🏗️ Agent Architectures & Frameworks": {"ko": "🏗️ 에이전트 아키텍처와 프레임워크", "zh": "🏗️ 智能体架构与框架", "ja": "🏗️ エージェントのアーキテクチャとフレームワーク", "pt": "🏗️ Arquiteturas e frameworks de agentes", "es": "🏗️ Arquitecturas y frameworks de agentes"},
    "🧱 Part I: Core Components": {"ko": "🧱 제1부: 핵심 구성 요소", "zh": "🧱 第一部分：核心组成", "ja": "🧱 第1部：中核となる構成要素", "pt": "🧱 Parte I: Componentes centrais", "es": "🧱 Parte I: Componentes principales"},
    "🧠 Planning & Reasoning": {"ko": "🧠 계획과 추론", "zh": "🧠 规划与推理", "ja": "🧠 計画と推論", "pt": "🧠 Planejamento e raciocínio", "es": "🧠 Planificación y razonamiento"},
    "💾 Memory": {"ko": "💾 메모리", "zh": "💾 记忆", "ja": "💾 メモリ", "pt": "💾 Memória", "es": "💾 Memoria"},
    "🔧 Tool Use": {"ko": "🔧 도구 사용", "zh": "🔧 工具使用", "ja": "🔧 ツール利用", "pt": "🔧 Uso de ferramentas", "es": "🔧 Uso de herramientas"},
    "🤝 Multi-Agent Systems": {"ko": "🤝 다중 에이전트 시스템", "zh": "🤝 多智能体系统", "ja": "🤝 マルチエージェントシステム", "pt": "🤝 Sistemas multiagente", "es": "🤝 Sistemas multiagente"},
    "🌍 Part II: Agents in Context": {"ko": "🌍 제2부: 환경과 응용 속의 에이전트", "zh": "🌍 第二部分：环境与应用中的智能体", "ja": "🌍 第2部：環境と応用のなかのエージェント", "pt": "🌍 Parte II: Agentes em ambientes e aplicações", "es": "🌍 Parte II: Agentes en entornos y aplicaciones"},
    "🌐 Interactive Environments": {"ko": "🌐 상호작용 환경", "zh": "🌐 交互环境", "ja": "🌐 インタラクティブ環境", "pt": "🌐 Ambientes interativos", "es": "🌐 Entornos interactivos"},
    "🚀 Applications": {"ko": "🚀 응용 분야", "zh": "🚀 应用领域", "ja": "🚀 応用分野", "pt": "🚀 Aplicações", "es": "🚀 Aplicaciones"},
    "⚖️ Part III: Cross-Cutting Concerns": {"ko": "⚖️ 제3부: 전반에 걸친 과제", "zh": "⚖️ 第三部分：贯穿全局的问题", "ja": "⚖️ 第3部：横断的な課題", "pt": "⚖️ Parte III: Questões transversais", "es": "⚖️ Parte III: Cuestiones transversales"},
    "📊 Evaluation & Benchmarks": {"ko": "📊 평가와 벤치마크", "zh": "📊 评估与基准", "ja": "📊 評価とベンチマーク", "pt": "📊 Avaliação e benchmarks", "es": "📊 Evaluación y benchmarks"},
    "🛡️ Safety & Alignment": {"ko": "🛡️ 안전과 정렬", "zh": "🛡️ 安全与对齐", "ja": "🛡️ 安全性とアライメント", "pt": "🛡️ Segurança e alinhamento", "es": "🛡️ Seguridad y alineación"},
    "🔗 Related Awesome Lists": {"ko": "🔗 관련 Awesome 리스트", "zh": "🔗 相关 Awesome 列表", "ja": "🔗 関連するAwesomeリスト", "pt": "🔗 Listas Awesome relacionadas", "es": "🔗 Listas Awesome relacionadas"},
    "📄 Citation": {"ko": "📄 인용", "zh": "📄 引用", "ja": "📄 引用", "pt": "📄 Como citar", "es": "📄 Cómo citar"},
    "🤝 Contributing": {"ko": "🤝 기여하기", "zh": "🤝 参与贡献", "ja": "🤝 コントリビュート", "pt": "🤝 Como contribuir", "es": "🤝 Cómo contribuir"},
    "👥 Contributors": {"ko": "👥 기여자", "zh": "👥 贡献者", "ja": "👥 コントリビューター", "pt": "👥 Colaboradores", "es": "👥 Colaboradores"},
    "📜 License": {"ko": "📜 라이선스", "zh": "📜 许可证", "ja": "📜 ライセンス", "pt": "📜 Licença", "es": "📜 Licencia"},
    "🗓️ Updates": {"ko": "🗓️ 업데이트 기록", "zh": "🗓️ 更新记录", "ja": "🗓️ 更新履歴", "pt": "🗓️ Atualizações", "es": "🗓️ Actualizaciones"},
}

SUMMARY = {
    "papers": {"ko": "<summary><b>논문 {n}편 보기</b></summary>",
               "zh": "<summary><b>展开 {n} 篇论文</b></summary>",
               "ja": "<summary><b>{n}本の論文を表示</b></summary>",
               "pt": "<summary><b>Mostrar {n} artigos</b></summary>",
               "es": "<summary><b>Mostrar {n} artículos</b></summary>"},
    "contributors": {"ko": "<summary><b>기여자 {n}명 보기</b></summary>",
                     "zh": "<summary><b>展开 {n} 位贡献者</b></summary>",
                     "ja": "<summary><b>{n}人のコントリビューターを表示</b></summary>",
                     "pt": "<summary><b>Mostrar {n} colaboradores</b></summary>",
                     "es": "<summary><b>Mostrar {n} colaboradores</b></summary>"},
}
BACK = {"ko": "↑ 목차로 돌아가기", "zh": "↑ 返回目录", "ja": "↑ 目次に戻る",
        "pt": "↑ Voltar ao sumário", "es": "↑ Volver al índice"}

# The line under each section heading that maps it to the survey's chapters.
FIXED_LINES = {
    "*Corresponds to §1-§3 (Introduction, Background, Taxonomy).*": {
        "ko": "*서베이 §1-§3(서론, 배경, 분류 체계)에 해당합니다.*",
        "zh": "*对应综述 §1-§3（引言、背景、分类体系）。*",
        "ja": "*サーベイの§1-§3（序論、背景、分類体系）に対応します。*",
        "pt": "*No survey: §1-§3 (Introdução, Fundamentos, Taxonomia).*",
        "es": "*En la revisión: §1-§3 (Introducción, Fundamentos, Taxonomía).*"},
    "*Corresponds to §2 (Background) and the running examples throughout.*": {
        "ko": "*서베이 §2(배경)와 서베이 전체에서 이어지는 예시에 해당합니다.*",
        "zh": "*对应综述 §2（背景）以及贯穿全文的示例。*",
        "ja": "*サーベイの§2（背景）と、全体を通して使う例に対応します。*",
        "pt": "*No survey: §2 (Fundamentos) e os exemplos usados ao longo do texto.*",
        "es": "*En la revisión: §2 (Fundamentos) y los ejemplos que se usan a lo largo del texto.*"},
    "*Corresponds to §4 (Planning and Reasoning).*": {
        "ko": "*서베이 §4(계획과 추론)에 해당합니다.*",
        "zh": "*对应综述 §4（规划与推理）。*",
        "ja": "*サーベイの§4（計画と推論）に対応します。*",
        "pt": "*No survey: §4 (Planejamento e raciocínio).*",
        "es": "*En la revisión: §4 (Planificación y razonamiento).*"},
    "*Corresponds to §5 (Memory).*": {
        "ko": "*서베이 §5(메모리)에 해당합니다.*",
        "zh": "*对应综述 §5（记忆）。*",
        "ja": "*サーベイの§5（メモリ）に対応します。*",
        "pt": "*No survey: §5 (Memória).*",
        "es": "*En la revisión: §5 (Memoria).*"},
    "*Corresponds to §6 (Tool Use and Action Execution).*": {
        "ko": "*서베이 §6(도구 사용과 행동 실행)에 해당합니다.*",
        "zh": "*对应综述 §6（工具使用与行动执行）。*",
        "ja": "*サーベイの§6（ツール利用と行動実行）に対応します。*",
        "pt": "*No survey: §6 (Uso de ferramentas e execução de ações).*",
        "es": "*En la revisión: §6 (Uso de herramientas y ejecución de acciones).*"},
    "*Corresponds to §7 (Multi-Agent Systems).*": {
        "ko": "*서베이 §7(다중 에이전트 시스템)에 해당합니다.*",
        "zh": "*对应综述 §7（多智能体系统）。*",
        "ja": "*サーベイの§7（マルチエージェントシステム）に対応します。*",
        "pt": "*No survey: §7 (Sistemas multiagente).*",
        "es": "*En la revisión: §7 (Sistemas multiagente).*"},
    "*Corresponds to §8 (Agents in Interactive Environments).*": {
        "ko": "*서베이 §8(상호작용 환경의 에이전트)에 해당합니다.*",
        "zh": "*对应综述 §8（交互环境中的智能体）。*",
        "ja": "*サーベイの§8（インタラクティブ環境のエージェント）に対応します。*",
        "pt": "*No survey: §8 (Agentes em ambientes interativos).*",
        "es": "*En la revisión: §8 (Agentes en entornos interactivos).*"},
    "*Corresponds to §10 (Applications).*": {
        "ko": "*서베이 §10(응용 분야)에 해당합니다.*",
        "zh": "*对应综述 §10（应用领域）。*",
        "ja": "*サーベイの§10（応用分野）に対応します。*",
        "pt": "*No survey: §10 (Aplicações).*",
        "es": "*En la revisión: §10 (Aplicaciones).*"},
    "*Corresponds to §9 (Evaluation and Benchmarks).*": {
        "ko": "*서베이 §9(평가와 벤치마크)에 해당합니다.*",
        "zh": "*对应综述 §9（评估与基准）。*",
        "ja": "*サーベイの§9（評価とベンチマーク）に対応します。*",
        "pt": "*No survey: §9 (Avaliação e benchmarks).*",
        "es": "*En la revisión: §9 (Evaluación y benchmarks).*"},
    "*Corresponds to §11 (Safety, Security, and Trustworthiness).*": {
        "ko": "*서베이 §11(안전·보안·신뢰성)에 해당합니다.*",
        "zh": "*对应综述 §11（安全、安全防护与可信性）。*",
        "ja": "*サーベイの§11（安全性・セキュリティ・信頼性）に対応します。*",
        "pt": "*No survey: §11 (Segurança, proteção e confiabilidade).*",
        "es": "*En la revisión: §11 (Seguridad, protección y confiabilidad).*"},
}

ENTRY = re.compile(
    r"^- \*\*\[(?P<title>.+?)\]\((?P<url>[^)]+)\)\*\*"
    r" \((?P<who>[^)]*)\) - \*(?P<gloss>.*?)\*(?P<tail>(?: ⭐)?(?: \[\[code\]\([^)]+\)\])*)\s*$"
)
HEADING = re.compile(r"^(#{1,6}) (.*?)(?: \((\d+)\))?\s*$")
TOC = re.compile(r"^(\s*)- \[(.*?)(?: \((\d+)\))?\]\(#([\w-]+)\)\s*$")
TOC_GROUP = re.compile(r"^- \*\*(.*?)\*\*\s*$")
SUMMARY_EN = re.compile(r"^<summary><b>Show (\d+) (papers|contributors)</b></summary>\s*$")
BACK_EN = '<sub><a href="#contents">↑ Back to Contents</a></sub>'
LINK = re.compile(r"\]\(([^)\s]+)\)|(?:href|src)=\"([^\"]+)\"")
ANCHOR = re.compile(r'<a id="([^"]+)"></a>')
CODE = re.compile(r"`([^`]+)`")
NUM = re.compile(r"\d+(?:[.,]\d+)*")
# The Latin-script editions write 7,7 and 39.000 where English writes 7.7 and
# 39,000, and their forbidden renderings are matched as whole words.
LATIN = ("pt", "es")
DASHES = ("—", "–", "―", "——")
END = {"ko": (".", "!", "?"), "zh": ("。", "！", "？", "."), "ja": ("。", "！", "？", "."),
       "pt": (".", "!", "?"), "es": (".", "!", "?")}


def load_forbidden(path: Path = TERMS) -> dict[str, list[tuple[str, str]]]:
    if not path.exists():
        return {k: [] for k in LANGS}
    data = json.loads(path.read_text(encoding="utf-8"))
    out: dict[str, list[tuple[str, str]]] = {k: [] for k in LANGS}
    for term in data["english"]:
        for lang in LANGS:
            for bad in term.get(lang, []):
                out[lang].append((term["en"], bad))
    return out


# The language switcher at the top differs in every file by design: each
# edition bolds itself and links the others.
EDITIONS = (("en", "README.md", "English"), ("ko", "README.ko.md", "한국어"),
            ("zh", "README.zh-CN.md", "简体中文"), ("ja", "README.ja.md", "日本語"),
            ("pt", "README.pt-BR.md", "Português"), ("es", "README.es.md", "Español"))


def switcher(lang: str) -> str:
    parts = [f"<b>{label}</b>" if code == lang else f'<a href="{name}">{label}</a>'
             for code, name, label in EDITIONS]
    return '<p align="center">' + " · ".join(parts) + "</p>"


def numbers(line: str, lang: str) -> Counter:
    thousands, decimal = (".", ",") if lang in LATIN else (",", ".")
    out = Counter()
    for n in NUM.findall(line):
        if re.fullmatch(r"\d{1,3}(?:" + re.escape(thousands) + r"\d{3})+", n):
            n = n.replace(thousands, "")
        elif re.fullmatch(r"\d+" + re.escape(decimal) + r"\d+", n):
            n = n.replace(decimal, ".")
        out[n] += 1
    return out


def links(line: str) -> Counter:
    # Each edition of the book lives in its own GitBook space, so a GitBook
    # link is expected to differ; only its presence is compared.
    found = (a or b for a, b in LINK.findall(line))
    return Counter("<gitbook>" if "gitbook.io" in u else u for u in found)


def check_pair(src: list[str], tr: list[str], lang: str, forbidden) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warns: list[str] = []
    if len(src) != len(tr):
        errors.append(f"line count differs: English {len(src)}, translation {len(tr)}")
        return errors, warns

    in_fence = False
    for i, (en, t) in enumerate(zip(src, tr), 1):
        err = lambda msg: errors.append(f"{i}: {msg}")
        warn = lambda msg: warns.append(f"{i}: {msg}")

        if en.startswith("```"):
            in_fence = not in_fence
            if t != en:
                err("code fence must be identical")
            continue
        if in_fence:
            if t != en:
                err("line inside a code block must be identical")
            continue
        if not en.strip():
            if t.strip():
                err("English line is blank, translation is not")
            continue
        if not t.strip():
            err("translation is blank")
            continue
        if en.strip() == switcher("en"):
            if t.strip() != switcher(lang):
                err(f"language switcher should read {switcher(lang)!r}")
            continue

        for d in DASHES:
            if d in t:
                err(f"dash {d!r} (use a colon, comma or parentheses)")
                break
        for en_term, bad in forbidden[lang]:
            # "시스템 1" (System One) must not match "시스템 12개".
            # Case-insensitive, so a gloss that opens with "Memória de longo prazo" counts.
            # "observações externas" is not "ações externas".
            edges = (r"(?<!\w)", r"(?!\w)") if lang in LATIN else ("", r"(?!\d)" if bad[-1].isdigit() else "")
            if re.search(edges[0] + re.escape(bad) + edges[1], t, re.I):
                err(f"'{bad}' is a translation of '{en_term}', which stays in English")

        fixed_line = False

        # Headings: level, fixed title, count.
        h_en = HEADING.match(en)
        if h_en:
            h_tr = HEADING.match(t)
            if not h_tr or h_tr.group(1) != h_en.group(1):
                err("heading level differs")
            else:
                title = h_en.group(2)
                if title in TITLES and h_tr.group(2) != TITLES[title][lang]:
                    err(f"title should read {TITLES[title][lang]!r}")
                if h_en.group(3) != h_tr.group(3):
                    err(f"count ({h_en.group(3)}) differs: ({h_tr.group(3)})")
                fixed_line = title in TITLES

        # Contents lines.
        c_en = TOC.match(en)
        if c_en:
            c_tr = TOC.match(t)
            if not c_tr or c_tr.group(4) != c_en.group(4) or c_tr.group(1) != c_en.group(1):
                err("Contents line must keep its indent and #anchor")
            else:
                title = c_en.group(2)
                if title in TITLES and c_tr.group(2) != TITLES[title][lang].replace('<a id="contents"></a>', ""):
                    err(f"Contents title should read {TITLES[title][lang]!r}")
                if c_en.group(3) != c_tr.group(3):
                    err(f"count ({c_en.group(3)}) differs: ({c_tr.group(3)})")
            fixed_line = True
        g_en = TOC_GROUP.match(en)
        if g_en and g_en.group(1) in TITLES:
            if t.strip() != f"- **{TITLES[g_en.group(1)][lang]}**":
                err(f"should read '- **{TITLES[g_en.group(1)][lang]}**'")
            fixed_line = True

        s_en = SUMMARY_EN.match(en)
        if s_en:
            want = SUMMARY[s_en.group(2)][lang].format(n=s_en.group(1))
            if t.strip() != want:
                err(f"toggle should read {want!r}")
            continue
        if en.strip() in FIXED_LINES:
            want = FIXED_LINES[en.strip()][lang]
            if t.strip() != want:
                err(f"should read {want!r}")
            continue
        if en.strip() == BACK_EN:
            want = BACK_EN.replace("↑ Back to Contents", BACK[lang])
            if t.strip() != want:
                err(f"should read {want!r}")
            continue

        # Links and anchors.
        if links(en) != links(t):
            miss = links(en) - links(t)
            extra = links(t) - links(en)
            err(f"links differ: missing {sorted(miss)} extra {sorted(extra)}")
        a_en, a_tr = Counter(ANCHOR.findall(en)), Counter(ANCHOR.findall(t))
        if h_en and h_en.group(2) == "Contents":
            a_tr -= Counter(["contents"])
        if a_en != a_tr:
            err("anchors differ")
        if Counter(CODE.findall(en)) != Counter(CODE.findall(t)):
            err("inline code differs")
        if en.lstrip().startswith("|") and en.count("|") != t.count("|"):
            err("table row has a different number of cells")

        # Entries.
        e_en = ENTRY.match(en)
        if e_en:
            e_tr = ENTRY.match(t)
            if not e_tr:
                err("entry format broken: - **[Title](link)** (Who) - *gloss.* [[code](link)]")
                continue
            for part in ("title", "url", "who", "tail"):
                if e_tr.group(part) != e_en.group(part):
                    err(f"entry {part} must be copied verbatim")
            g = e_tr.group("gloss").strip()
            if g == e_en.group("gloss").strip():
                err("gloss is untranslated")
            if not g.endswith(END[lang]):
                err("gloss does not end a sentence")
            for o, c in (("(（", ")）"), ("[「【", "]」】")):
                if sum(g.count(x) for x in o) != sum(g.count(x) for x in c):
                    err("gloss has unbalanced brackets")
        elif (t == en and len(re.findall(r"[A-Za-z]{3,}", LINK.sub("", en))) >= 6
              and not en.startswith("<h1") and "<sub><i>" not in en and "img.shields.io" not in en):
            warn("line looks untranslated")

        if not fixed_line:
            n_en, n_tr = numbers(en, "en"), numbers(t, lang)
            if n_en != n_tr:
                warn(f"numbers differ: missing {sorted((n_en - n_tr).elements())} extra {sorted((n_tr - n_en).elements())}")

    return errors, warns


def fix_counts(src: list[str], tr: list[str]) -> tuple[list[str], int]:
    """Copy counts from the English line into the matching translated line."""
    out, n = list(tr), 0
    for i, en in enumerate(src):
        if i >= len(out):
            break
        new = out[i]
        for rx in (HEADING, TOC):
            m = rx.match(en)
            if m and m.group(3):
                new = re.sub(r"\((\d+)\)(?=\]\(#|\s*$)", f"({m.group(3)})", new)
        s = SUMMARY_EN.match(en)
        if s:
            new = re.sub(r"\d+", s.group(1), new, count=1)
        if new != out[i]:
            out[i], n = new, n + 1
    return out, n


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--fix", action="store_true", help="copy stale counts from README.md first")
    ap.add_argument("-w", "--warnings", action="store_true", help="print warnings too")
    ap.add_argument("--src")
    ap.add_argument("--tr")
    ap.add_argument("--lang", choices=sorted(LANGS))
    ap.add_argument("--terms", default=str(TERMS))
    args = ap.parse_args()
    forbidden = load_forbidden(Path(args.terms))

    if args.src:
        pairs = [(Path(args.src), Path(args.tr), args.lang)]
    else:
        pairs = [(ROOT / "README.md", ROOT / name, lang) for lang, name in LANGS.items()]

    failed = False
    for src_path, tr_path, lang in pairs:
        src = src_path.read_text(encoding="utf-8").split("\n")
        if not tr_path.exists():
            print(f"{tr_path.name}: missing")
            failed = True
            continue
        tr = tr_path.read_text(encoding="utf-8").split("\n")
        if args.fix:
            tr, n = fix_counts(src, tr)
            if n:
                tr_path.write_text("\n".join(tr), encoding="utf-8")
                print(f"{tr_path.name}: {n} count line(s) synced from {src_path.name}")
        errors, warns = check_pair(src, tr, lang, forbidden)
        for e in errors:
            print(f"{tr_path.name}:{e}")
        if args.warnings:
            for w in warns:
                print(f"{tr_path.name}:{w}  (warning)")
        print(f"{tr_path.name}: {len(errors)} error(s), {len(warns)} warning(s)")
        failed |= bool(errors)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
