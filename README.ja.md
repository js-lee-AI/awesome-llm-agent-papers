<h1 align="center">🤖 Awesome LLM Agent Papers</h1>

<p align="center"><a href="README.md">English</a> · <a href="README.ko.md">한국어</a> · <a href="README.zh-CN.md">简体中文</a> · <b>日本語</b></p>

<p align="center">
<b>必読論文 200 本以上、随時追加中</b>：計画し、記憶し、ツールを使い、互いに協力する<br>
LLMエージェントを作るための、注釈付きの読書リストです。サーベイ「<i>LLM Agents: A Survey</i>」と対になっています。
</p>

<!-- Identity & credibility -->
<p align="center">
<a href="https://awesome.re"><img src="https://awesome.re/badge.svg" alt="Awesome"></a>
<img src="https://img.shields.io/badge/papers-200%2B-8B2635?style=flat-square&labelColor=2b2b2b" alt="200+ curated papers">
<a href="https://doi.org/10.20944/preprints202608.0265.v1"><img src="https://img.shields.io/badge/DOI-10.20944%2Fpreprints202608.0265.v1-8B2635?style=flat-square&labelColor=2b2b2b" alt="DOI: 10.20944/preprints202608.0265.v1"></a>
<a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-8B2635?style=flat-square&labelColor=2b2b2b" alt="License: MIT"></a>
<a href="CONTRIBUTING.md"><img src="https://img.shields.io/badge/PRs-welcome-8B2635?style=flat-square&labelColor=2b2b2b" alt="PRs welcome"></a>
</p>

<!-- Live star / fork counts. -->
<p align="center">
<a href="https://github.com/js-lee-AI/awesome-llm-agent-papers/stargazers"><img src="https://img.shields.io/github/stars/js-lee-AI/awesome-llm-agent-papers?style=flat-square&labelColor=2b2b2b&color=8B2635" alt="GitHub stars"></a>
<a href="https://github.com/js-lee-AI/awesome-llm-agent-papers/network/members"><img src="https://img.shields.io/github/forks/js-lee-AI/awesome-llm-agent-papers?style=flat-square&labelColor=2b2b2b&color=8B2635" alt="GitHub forks"></a>
</p>

<p align="center">
📄 <b><a href="https://www.preprints.org/manuscript/202608.0265">サーベイを読む →「LLM Agents: A Survey」</a></b> &nbsp;·&nbsp; <a href="paper/llm-agents-a-survey.pdf">このリポジトリにあるPDF</a> &nbsp;·&nbsp; ⭐ <b><a href="#starter-kit">まずは 10 本のスターターキットから</a></b>
</p>

<p align="center"><sub><i> LLM agents · LLM agent papers · autonomous agents · agentic AI · multi-agent systems · tool use · ReAct · planning · memory · agent benchmarks · agent safety &amp; prompt injection</i></sub></p>

<p align="center"><img src="assets/taxonomy.png" width="460" alt="LLMエージェント研究の分類体系"></p>

## ✨ ハイライト

| | 内容 |
|---|---|
| 📚 **サーベイの文献をすべて収録** | *LLM Agents: A Survey*が引用する参考文献 228 本に、論文の内容が固まったあとで検証して追加した研究を合わせたものです。論文はある時点で止まった記録ですが、このリストは今も更新を続けています。 |
| 🧭 **機能別に整理** | サーベイの構成に沿って 10 のセクションに分けています。サーベイ、アーキテクチャ、計画、メモリ、ツール利用、マルチエージェント、環境、応用、評価、安全性です。 |
| ✍️ **注釈付き** | 各項目に、その論文が何をもたらしたかを述べた一行の説明文と、学会・論文誌と年を載せています。公式実装があれば`[code]`リンクも付けています。 |
| ⭐ **スターターキット** | 全体像をつかむための[10 本のリスト](#starter-kit)です。それぞれに、最初に読む価値がある理由を添えました。 |
| 🔎 **たどりやすい構成** | セクションごとの論文数を載せた[目次](#contents)があり、各セクションは折りたたんで表示されます。 |

**扱うトピック**：cognitive architecture · ReActと推論・行動の統合 · long-horizonな計画 · エージェントのメモリ · ツールで拡張したLLM · マルチエージェントの協調 · Web／コード／embodiedのエージェント · エージェントのベンチマークと評価 · 安全性、アライメント、間接的なprompt injection。

> 🔁 **姉妹編の深掘りリストを公開しました**：[**Awesome Agent Loop Papers**](https://github.com/js-lee-AI/awesome-agent-loop-papers)は、構成要素のさらに下にあるループそのものを扱います。論文 524 本と、オープンソースの成果物 60 件（フレームワーク、コーディング用のharness、メモリやsandboxの基盤、skillライブラリ、レジストリ）を収めています。サーベイ*The Agent Loop: A Survey of Control Strategies, Skills, and Harnesses for LLM Agents*と対になるリストです。

このリポジトリは、**LLMベースのエージェント**の必読論文を集めたものです。ここでいうエージェントとは、計画、メモリ、ツール利用、マルチエージェントの協調を備え、長い時間をかけて目標を追いかける言語モデルのことです。論文は対応するサーベイの分類体系に沿って並べてあり、エージェントの中核となる構成要素、エージェントが実際に動く環境と応用、そして評価と安全性という横断的な課題までをカバーしています。各項目には論文へのリンクがあり、公式実装があればコードへのリンクも添えています。

このリストは**厳選し、随時更新しているセレクション**です。サーベイの参考文献をそのまま写したものではなく、それをすべて含んだうえで、さらに広げています。論文が引用する参考文献は 228 本で、どれも一次資料と照らし合わせて確かめてあります。このリストには、論文の内容が固まったあとに出た研究を同じ基準で確かめて加えてきたので、今ではその数を大きく超えています。各セクションは、はじめは閉じた状態になっています。**N本の論文を表示**をクリックすると開きます。

> **凡例**：⭐ = [スターターキット](#starter-kit)に選んだ論文（最初に読むもの） · `[code]` = 公式実装へのリンク。

<a id="starter-kit"></a>
## ⭐ スターターキット

この分野が初めてなら、まずはこの十本から読むのがおすすめです。

| # | 論文 | 分野 | 最初に読む理由 |
|---|-------|------|----------------|
| 1 | [ReAct: Synergizing Reasoning and Acting](https://arxiv.org/abs/2210.03629) | 計画 | 推論と行動を交互に行う、現代のエージェントのループの原型 |
| 2 | [Reflexion: Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366) | 計画 | Self-reflectionの結果をメモリに蓄え、勾配を使わずに改善を重ねるループ |
| 3 | [Toolformer: LMs Can Teach Themselves to Use Tools](https://arxiv.org/abs/2302.04761) | ツール利用 | 自己教師ありのツール利用を切り開いた代表的な論文 |
| 4 | [Generative Agents: Interactive Simulacra](https://arxiv.org/abs/2304.03442) | マルチエージェント | メモリとreflectionを集団の規模で動かした、エージェントのメモリ設計の定番 |
| 5 | [Voyager: An Open-Ended Embodied Agent](https://arxiv.org/abs/2305.16291) | メモリ / 環境 | 実行可能なskillのライブラリを増やしながら続ける生涯学習 |
| 6 | [Cognitive Architectures for Language Agents (CoALA)](https://arxiv.org/abs/2309.02427) | 基礎 | このリストの構成の土台になっている語彙（メモリ、action space、意思決定のループ） |
| 7 | [A Survey on LLM-based Autonomous Agents](https://arxiv.org/abs/2308.11432) | サーベイ | この分野の総合サーベイの定番 |
| 8 | [LLM-based Multi-Agents: A Survey](https://arxiv.org/abs/2402.01680) | マルチエージェント | マルチエージェント分野の標準的な参考文献 |
| 9 | [AgentBench: Evaluating LLMs as Agents](https://arxiv.org/abs/2308.03688) | 評価 | 複数の環境にまたがる、エージェントの標準的なベンチマーク |
| 10 | [Not what you've signed up for (Indirect Prompt Injection)](https://arxiv.org/abs/2302.12173) | 安全性 | エージェントのセキュリティにおける脅威モデルを確立した論文 |

<a id="to-watch"></a>
## 🔥 注目の10本 (2026)

2026 年に出たばかりで、すでに注目を集めている研究です。

| 論文 | 分野 | Stars |
|-------|------|-------|
| [GenericAgent: A Token-Efficient Self-Evolving LLM Agent via Contextual Information Density Maximization](https://arxiv.org/abs/2604.17091) | アーキテクチャ | ![stars](https://img.shields.io/github/stars/lsdefine/GenericAgent?style=flat&label=%E2%AD%90&labelColor=2B2926&color=7A1F2B) |
| [SimpleMem: Efficient Lifelong Memory for LLM Agents](https://arxiv.org/abs/2601.02553) | メモリ | ![stars](https://img.shields.io/github/stars/aiming-lab/SimpleMem?style=flat&label=%E2%AD%90&labelColor=2B2926&color=7A1F2B) |
| [AutoSci: A Memory-Centric Agentic System for the Full Scientific Research Lifecycle](https://arxiv.org/abs/2605.31468) | 応用 | ![stars](https://img.shields.io/github/stars/skyllwt/AutoSci?style=flat&label=%E2%AD%90&labelColor=2B2926&color=7A1F2B) |
| [Mobile-Agent-v3.5: Multi-platform Fundamental GUI Agents](https://arxiv.org/abs/2602.16855) | 環境 | ![stars](https://img.shields.io/github/stars/X-PLUG/MobileAgent?style=flat&label=%E2%AD%90&labelColor=2B2926&color=7A1F2B) |
| [AgentDoG: A Diagnostic Guardrail Framework for AI Agent Safety and Security](https://arxiv.org/abs/2601.18491) | 安全性 | ![stars](https://img.shields.io/github/stars/AI45Lab/AgentDoG?style=flat&label=%E2%AD%90&labelColor=2B2926&color=7A1F2B) |
| [Agentic Reasoning for Large Language Models](https://arxiv.org/abs/2601.12538) | サーベイ | ![stars](https://img.shields.io/github/stars/weitianxin/Awesome-Agentic-Reasoning?style=flat&label=%E2%AD%90&labelColor=2B2926&color=7A1F2B) |
| [UniToolCall: Unifying Tool-Use Representation, Data, and Evaluation for LLM Agents](https://arxiv.org/abs/2604.11557) | ツール利用 | ![stars](https://img.shields.io/github/stars/EIT-NLP/UniToolCall?style=flat&label=%E2%AD%90&labelColor=2B2926&color=7A1F2B) |
| [Graph-of-Agents: A Graph-based Framework for Multi-Agent LLM Collaboration](https://arxiv.org/abs/2604.17148) | マルチエージェント | ![stars](https://img.shields.io/github/stars/UNITES-Lab/GoA?style=flat&label=%E2%AD%90&labelColor=2B2926&color=7A1F2B) |
| [Can AI Agents Answer Your Data Questions? A Benchmark for Data Agents (DataAgentBench)](https://arxiv.org/abs/2603.20576) | 評価 | ![stars](https://img.shields.io/github/stars/ucbepic/DataAgentBench?style=flat&label=%E2%AD%90&labelColor=2B2926&color=7A1F2B) |
| [Harness Updating Is Not Harness Benefit: Disentangling Evolution Capabilities in Self-Evolving LLM Agents](https://arxiv.org/abs/2605.30621) | 計画 | ![stars](https://img.shields.io/github/stars/A-EVO-Lab/a-evolve?style=flat&label=%E2%AD%90&labelColor=2B2926&color=7A1F2B) |

<sub><a href="#contents">↑ 目次に戻る</a></sub>

## <a id="contents"></a>目次

- [⭐ スターターキット](#starter-kit)
- [🔥 注目の10本 (2026)](#to-watch)
- **🧭 背景**
  - [📚 サーベイとポジションペーパー (57)](#surveys)
  - [🏗️ エージェントのアーキテクチャとフレームワーク (51)](#architectures)
- **🧱 第1部：中核となる構成要素**
  - [🧠 計画と推論 (51)](#planning)
  - [💾 メモリ (56)](#memory)
  - [🔧 ツール利用 (46)](#tools)
  - [🤝 マルチエージェントシステム (51)](#multi-agent)
- **🌍 第2部：環境と応用のなかのエージェント**
  - [🌐 インタラクティブ環境 (57)](#environments)
  - [🚀 応用分野 (54)](#applications)
- **⚖️ 第3部：横断的な課題**
  - [📊 評価とベンチマーク (50)](#evaluation)
  - [🛡️ 安全性とアライメント (59)](#safety)

## 🧭 背景

<a id="surveys"></a>
### 📚 サーベイとポジションペーパー (57)
*サーベイの§1-§3（序論、背景、分類体系）に対応します。*

<details>
<summary><b>57本の論文を表示</b></summary>

- **[A Survey on Large Language Model based Autonomous Agents](https://arxiv.org/abs/2308.11432)** (Wang et al., arXiv 2023) - *LLMエージェントの総合サーベイの定番で、引用数も最も多い。* ⭐ [[code](https://github.com/Paitesanshi/LLM-Agent-Survey)]
- **[The Rise and Potential of Large Language Model Based Agents: A Survey](https://arxiv.org/abs/2309.07864)** (Xi et al., arXiv 2023) - *Wang et al. 2023と並んで分野の土台を築いた、二大総合サーベイの一つ。* [[code](https://github.com/WooooDyy/LLM-Agent-Paper-List)]
- **[Cognitive Architectures for Language Agents](https://arxiv.org/abs/2309.02427)** (Sumers et al., TMLR 2023) - *LLMエージェントを記述するための概念とアーキテクチャの語彙として、最も広く採用されている。* ⭐ [[code](https://github.com/ysymyth/awesome-language-agents)]
- **[ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)** (Yao et al., ICLR 2023) - *現代のLLMエージェントにつながる技術的な先行研究のなかで、最も多く引用されている論文。* ⭐ [[code](https://github.com/ysymyth/ReAct)]
- **[Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366)** (Shinn et al., NeurIPS 2023) - *「self-reflectionとメモリ」のループを、勾配ベースのRLに代わるエージェントの自己改善の方法として確立した。* ⭐ [[code](https://github.com/noahshinn/reflexion)]
- **[Toolformer: Language Models Can Teach Themselves to Use Tools](https://arxiv.org/abs/2302.04761)** (Schick et al., NeurIPS 2023) - *LLMエージェントの分類体系で「ツールによる拡張」という柱の起点になった、ツール利用の代表的な論文。* ⭐
- **[Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442)** (Park et al., arXiv 2023) - *LLMが動かすエージェントの社会とシミュレーションを示した、基礎となる研究。* ⭐ [[code](https://github.com/joonspk-research/generative_agents)]
- **[Voyager: An Open-Ended Embodied Agent with Large Language Models](https://arxiv.org/abs/2305.16291)** (Wang et al., TMLR 2023) - *Embodiedな環境で、コードとして書いたskillを積み上げながら生涯学習するLLMエージェントの先駆的な例。* ⭐ [[code](https://github.com/MineDojo/Voyager)]
- **[HuggingGPT: Solving AI Tasks with ChatGPT and its Friends in Hugging Face](https://arxiv.org/abs/2303.17580)** (Shen et al., NeurIPS 2023) - *「LLMがツールやモデルを束ねるorchestratorになる」というエージェントの型を示した、基礎的な例。* [[code](https://github.com/microsoft/JARVIS)]
- **[MRKL Systems: A Modular, Neuro-Symbolic Architecture that Combines Large Language Models, External Knowledge Sources and Discrete Reasoning](https://arxiv.org/abs/2205.00445)** (Karpas et al., arXiv 2022) - *LLMのツール利用やエージェントのアーキテクチャにつながるニューロシンボリックな先行研究で、広く引用されているもののなかでは最も早い。*
- **[Agent AI: Surveying the Horizons of Multimodal Interaction](https://arxiv.org/abs/2401.03568)** (Durante et al., arXiv 2024) - *LLMエージェントのサーベイが扱う範囲を、multimodalやembodiedなAgent AIにまで広げた。*
- **[Igniting Language Intelligence: The Hitchhiker's Guide From Chain-of-Thought Reasoning to Language Agents](https://arxiv.org/abs/2311.11797)** (Zhang et al., arXiv 2023) - *推論（CoT）の研究とエージェントの研究をつなぐ。* [[code](https://github.com/Zoeyyao27/CoT-Igniting-Agent)]
- **[Large Language Model based Multi-Agents: A Survey of Progress and Challenges](https://arxiv.org/abs/2402.01680)** (Guo et al., IJCAI 2024) - *LLMエージェントのうちマルチエージェント分野に絞った、標準的な参考サーベイ。* ⭐ [[code](https://github.com/taichengguo/LLM_MultiAgents_Survey_Papers)]
- **[Understanding the Planning of LLM Agents: A Survey](https://arxiv.org/abs/2402.02716)** (Huang et al., arXiv 2024) - *基礎的なサーベイ群に欠けていた、計画に特化した部分を埋める。*
- **[Tool Learning with Large Language Models: A Survey](https://arxiv.org/abs/2405.17935)** (Qu et al., arXiv 2024) - *LLMエージェントの柱の一つであるツール利用を扱う、決定版のサーベイ。* [[code](https://github.com/quchangle1/LLM-Tool-Survey)]
- **[A Survey on the Memory Mechanism of Large Language Model based Agents](https://arxiv.org/abs/2404.13501)** (Zhang et al., arXiv 2024) - *LLMエージェントのメモリ機構を扱う標準的なサーベイ。* [[code](https://github.com/nuster1128/LLM_Agent_Memory_Survey)]
- **[Agentic Large Language Models, a Survey](https://arxiv.org/abs/2503.23037)** (Plaat et al., arXiv 2025) - *推論・行動・相互作用というコンパクトな分類体系を示した最近の総合サーベイで、広く参照されている。*
- **[Large Language Model Agent: A Survey on Methodology, Applications and Challenges](https://arxiv.org/abs/2503.21460)** (Luo et al., arXiv 2025) - *最も包括的で新しい（2025 年）総合サーベイの一つ。* [[code](https://github.com/luo-junyu/Awesome-Agent-Papers)]
- **[Fully Autonomous AI Agents Should Not Be Developed](https://arxiv.org/abs/2502.02649)** (Mitchell et al., arXiv 2025) - *エージェントの自律性に異を唱えたポジションペーパーで、大きな注目と議論を呼んだ。*
- **[AI Agents vs. Agentic AI: A Conceptual Taxonomy, Applications and Challenges](https://arxiv.org/abs/2505.10468)** (Sapkota et al., arXiv 2025) - *分野のなかで言葉の使い方がばらついているため、用語と概念を整理した論文として引用が増えている。*
- **[LLM-Based Human-Agent Collaboration and Interaction Systems: A Survey](https://arxiv.org/abs/2505.00753)** (Zou et al., arXiv 2025) - *最初期の基礎的なサーベイが挙げていた、人とエージェントの協働という分野を扱う。* [[code](https://github.com/HenryPengZou/Awesome-Human-Agent-Collaboration-Interaction-Systems)]
- **[Levels of Autonomy for AI Agents](https://arxiv.org/abs/2506.12469)** (Feng et al., arXiv 2025) - *LLMエージェントのシステム同士で自律性を比べるための実用的な枠組みを示し、広く引用されている。*
- **[Advances and Challenges in Foundation Agents: From Brain-Inspired Intelligence to Evolutionary, Collaborative, and Safe Systems](https://arxiv.org/abs/2504.01990)** (Liu et al., arXiv 2025) - *48 人の著者が参加した、この分野の節目となるサーベイ。脳に着想を得た認知モジュール、自己進化、集合知、安全性を軸に分野を整理する。*
- **[The Landscape of Agentic Reinforcement Learning for LLMs: A Survey](https://arxiv.org/abs/2509.02547)** (Zhang et al., arXiv 2025) - *Agentic RLの定番サーベイ。LLMを受け身の生成器ではなく、意思決定を行うエージェントとして学習させる研究を扱う。*
- **[A Comprehensive Survey of Self-Evolving AI Agents: A New Paradigm Bridging Foundation Models and Lifelong Agentic Systems](https://arxiv.org/abs/2508.07407)** (Fang et al., arXiv 2025) - *エージェントが相互作用のデータから自分の構成要素を最適化する手法を整理し、基盤モデルと、長く学び続けるagenticなシステムとを橋渡しする。*
- **[Deep Research Agents: A Systematic Examination and Roadmap](https://arxiv.org/abs/2506.18096)** (Huang et al., arXiv 2025) - *Long-horizonで自律的に動くリサーチエージェント（検索、ツール利用、レポート作成）を扱った、初めての体系的なサーベイ。*
- **[A Survey of AI Agent Protocols](https://arxiv.org/abs/2504.16736)** (Yang et al., arXiv 2025) - *生まれつつあるプロトコル層（MCP、A2Aとその後継）を見渡し、エージェントの相互運用性の標準を評価するための観点を提案する。*

- **[Agentic Reasoning for Large Language Models](https://arxiv.org/abs/2601.12538)** (Wei et al., arXiv 2026) - *Agentic reasoningを単一エージェント、自己進化、マルチエージェントの各層に整理したサーベイ。In-contextの推論とpost-trainingをつなぐ。* [[code](https://github.com/weitianxin/Awesome-Agentic-Reasoning)]
- **[Memory for Autonomous LLM Agents: Mechanisms, Evaluation, and Emerging Frontiers](https://arxiv.org/abs/2603.07670)** (Du et al., arXiv 2026) - *エージェントのメモリを「書き込み、管理、読み出し」のループとして捉え、仕組み、ベンチマーク、応用にまたがる分類体系を示す。*
- **[Anatomy of Agentic Memory: Taxonomy and Empirical Analysis of Evaluation and System Limitations](https://arxiv.org/abs/2602.19320)** (Jiang et al., arXiv 2026) - *エージェントのメモリ構造を分類し、ベンチマークの飽和と評価指標の妥当性という問題がシステムをまたいで起きていることを実証的に示す。*
- **[Beyond Individual Intelligence: Surveying Collaboration, Failure Attribution, and Self-Evolution in LLM-based Multi-Agent Systems](https://arxiv.org/abs/2605.14892)** (Qi et al., arXiv 2026) - *マルチエージェントの協調、failure attribution、自己進化をまとめて扱う統一的な枠組み「LIFE」（foundation、integrate、find faults、evolve）を提案する。*
- **[A Technical Taxonomy of LLM Agent Communication Protocols](https://arxiv.org/abs/2606.19135)** (Sander et al., arXiv 2026) - *九つのオープンなエージェント間プロトコルを五つの観点から分析し、連合型のプロトコルスタックに収束していくと予測する。*
- **[Bridging the Agent-World Gap: Text World Models for LLM-based Agents](https://arxiv.org/abs/2606.09032)** (Li et al., arXiv 2026) - *テキストによる世界モデル（LLM-as-WMとcode-as-WM）を体系化する。これにより、エージェントは計画や検証のために環境を明示的に予測できる。* [[code](https://github.com/sustech-nlp/awesome-text-world-models)]
- **[Agents That Know Too Much: A Data-Centric Survey of Privacy in LLM Agents](https://arxiv.org/abs/2606.26627)** (Lahjouji et al., arXiv 2026) - *エージェントのプライバシー研究を、攻撃の種類ではなくデータの接点ごとに整理した、データ中心のサーベイ。ガバナンスの抜けも洗い出す。*
- **[Self-Improvements in Modern Agentic Systems: A Survey](https://arxiv.org/abs/2607.13104)** (Ren et al., arXiv 2026) - *現代のエージェントを基盤モデルと実行用のscaffoldの組み合わせとして捉え、自己改善を「何を更新するか（重みかscaffoldか）」と「どのシグナルが変化を起こすか」で整理する。* [[code](https://github.com/selfimproving-agent/awesome-Self-Improving-Agents)]
- **[Dynamic Agent Skills: A Lifecycle Survey and Taxonomy of Evolving Skill Libraries](https://arxiv.org/abs/2607.10113)** (Li et al., arXiv 2026) - *進化するskillライブラリを、ライフサイクルで管理される成果物の保管庫と見なして 124 本の論文を整理する。決め手になる段階は獲得ではなく、受け入れと修復だと論じる。*
- **[From Question Answering to Task Completion: A Survey on Agent System and Harness Design](https://arxiv.org/abs/2606.20683)** (Guo et al., arXiv 2026) - *エージェントを「モデルかharnessか」という視点で読み解き、harnessを実行時の六つの役割に分解して、性能のボトルネックが実際にどこにあるのかを問う。* [[code](https://github.com/ggjy/Awesome-Agent-Engineering)]
- **[Isolation as a First-Class Principle for LLM-Agent System Safety: Concepts, Taxonomy, Challenges and Future Directions](https://arxiv.org/abs/2607.12406)** (Jing et al., arXiv 2026) - *Prompt injection、ツールの誤用、memory poisoningを一つの構造的な問題として捉え直すポジションペーパー。原因は、エージェントの五つのインターフェースにわたって隔離の境界が欠けていることだとする。*
- **[Always-On Agents: A Survey of Persistent Memory, State, and Governance in LLM Agents](https://arxiv.org/abs/2606.30306)** (Ding et al., arXiv 2026) - *セッションをまたいで状態を持ち続けるエージェントの研究 435 本を調べ、文献が蓄積と検索に偏る一方で、ガバナンスと回復をおろそかにしていることを見いだした。*
- **[Externalization in LLM Agents: A Unified Review of Memory, Skills, Protocols and Harness Engineering](https://arxiv.org/abs/2604.08224)** (Zhou et al., arXiv 2026) - *エージェントの発展を「外部化」として捉える。能力が重みの外へ出て、メモリ、skill、プロトコル、harnessの基盤へと移っていくという見方である。*
- **[SoK: Agentic Skills -- Beyond Tool Use in LLM Agents](https://arxiv.org/abs/2602.20867)** (Jiang et al., arXiv 2026) - *Agenticなskillを、再利用して呼び出せる手続きとして体系化し、skillと単発のツール呼び出しとの境界を引く。*
- **[From Storage to Experience: A Survey on the Evolution of LLM Agent Memory Mechanisms](https://arxiv.org/abs/2605.06716)** (Luo et al., arXiv 2026) - *エージェントのメモリを、保存からreflection、そして経験へと進む三段階の進化として整理する。その原動力は一貫性、動的な変化、継続学習である。* [[code](https://github.com/FeishuLuo/Evolving-LLM-Agent-Memory-Survey)]
- **[LLM agents security duality: a comprehensive survey of self-security and empowered cybersecurity](https://arxiv.org/abs/2606.28450)** (Xu et al., arXiv 2026) - *LLMエージェントに対するセキュリティ上の脅威と緩和策を、脅威の発生源にもとづく分類体系でまとめて整理したサーベイ。あわせて、エージェントの能力をサイバー攻撃と防御のライフサイクル全体に対応づける枠組みも示す。*
- **[Agentic Environment Engineering for Large Language Models: A Survey of Environment Modeling, Synthesis, Evaluation, and Application](https://arxiv.org/abs/2606.12191)** (Li et al., arXiv 2026) - *LLMベースのエージェントのための環境研究を、モデリング、合成、評価、応用というエンジニアリングのライフサイクルに沿って整理したサーベイ。環境を八つの属性で分類する方法も提案する。*
- **[Toward Efficient Agents: Memory, Tool learning, and Planning](https://arxiv.org/abs/2601.14192)** (Yang et al., arXiv 2026) - *三つの構成要素（メモリ、ツール学習、計画）にわたってLLMエージェントのシステムの効率を見直したサーベイで、効果とコストの関係をPareto frontierとして捉えている。*
- **[Agentic Artificial Intelligence (AI): Architectures, Taxonomies, and Evaluation of Large Language Model Agents](https://arxiv.org/abs/2601.12560)** (Arunkumar V et al., arXiv 2026) - *LLMエージェントのために、六つの構成要素（知覚、脳、計画、行動、ツール利用、協調）からなる統一的な分類体系を提案するサーベイ。アーキテクチャ、動作環境、評価の実践を概観し、最後に、hallucinationから生じる行動、無限ループ、prompt injectionといった未解決の課題を挙げる。*
- **[A Survey on Long-Term Memory Security in LLM Agents: Attacks, Defenses, and Governance Across the Memory Lifecycle](https://arxiv.org/abs/2604.16548)** (Lin et al., arXiv 2026) - *LLMエージェントのlong-term memoryを狙うセキュリティ上の脅威を扱う。攻撃、防御、ガバナンスを、メモリのライフサイクルの六つの段階と四つのセキュリティ目標に沿って整理し、「Verifiable Memory Governance」という枠組みを提唱する。*
- **[Uncertainty Quantification in LLM Agents: Foundations, Emerging Challenges, and Opportunities](https://arxiv.org/abs/2602.05073)** (Oh et al., arXiv 2026) - *不確実性の定量化は単一ターンのQAを離れ、対話的なエージェントを対象にすべきだと論じる。一般的な定式化に加えて、エージェントに固有の四つの課題として、推定量の選び方、異質なエンティティ、不確実性の動的な変化、きめ細かなベンチマークの不在を挙げる。*
- **[Multi-Agent Debate Strategies: Survey, Taxonomy, and Challenges](https://arxiv.org/abs/2607.26212)** (Motger et al., arXiv 2026) - *マルチエージェントの討論を扱った研究 141 本を見直すと、分野は静的でfully connectedなトポロジーと投票の組み合わせに、いつの間にか落ち着いていた。対照比較で選ばれたのではなく、慣習として採用されたものである。*
- **[Beyond the Leaderboard: A Synthesis of Tool-Use, Planning, and Reasoning Failures in Large Language Model Agents](https://arxiv.org/abs/2607.05775)** (Albayaydh et al., arXiv 2026) - *19 のベンチマークにまたがる評価論文 27 本を統合し、失敗を六つのクラスタにまとめた。失敗はタスクが長くなるほど非線形に積み重なり、scaffoldを足しても信頼性が確実に上がるわけではない。*
- **[How Agents Ask for Permission: User Permissions for AI Agents, from Interfaces to Enforcement](https://arxiv.org/abs/2607.13718)** (Michael et al., arXiv 2026) - *エージェントの権限に関する提案 21 件を五つの商用エージェントと照らし合わせる。ユーザー単位のポリシーがどう指定され、ユーザーの入力からどう導かれ、実行時にどう強制されるか、そしてどこに穴が残っているかを分類する。*
- **[Blockchain Empowered Trustworthy Agent Networks: Foundations, Taxonomy, and Future Directions](https://arxiv.org/abs/2608.04626)** (Zhu et al., arXiv 2026) - *1980 年から 2026 年まで、古典的なマルチエージェントシステムからオープンなエージェントネットワークへの道のりを概観する。所有者の異なるエージェント同士が取引を始めると信頼の問題はネットワークの水準に移り、単一エージェントの安全機構ではそこに手が届かないと論じる。*
- **[Software Engineering for and with GUI Agent](https://arxiv.org/abs/2608.09278)** (Yu et al., arXiv 2026) - *2018 年 1 月から 2026 年 4 月までのGUIエージェントの論文 336 本を見直した。アーキテクチャは「知覚、推論、行動」のモジュール式ループに収束しつつあるが、回復、人へのescalation、安全性の強制、監査可能性は発展途上のままである。評価もいまだにタスクの成否が中心で、プロトコルをまたいだ比較が難しい。*
- **[Agent Safety Should Be a Runtime Contract](https://arxiv.org/abs/2608.11274)** (Ng et al., arXiv 2026) - *エージェントの安全性をharnessに置き、実行時の契約として扱うべきだとするポジションペーパー。契約には予防の面（sandbox、権限ゲート、モニター）と証拠の面（テスト実行、ログの取得、ファイルのdiff）がある。根拠は、記録に残るインシデント 52 件、公開されたエージェントシステム 12 個のtrajectoryスキーマの監査、そしてNeurIPS、ICML、ICLRの 2023-2025 年の論文 28,560 本すべてを対象にしたタイトル単位の監査である。この監査では、学習時を扱う論文とデプロイ時を扱う論文の数に、全体で 8-12 倍の偏りがあった。*
- **[Information Retrieval Misses the Mark for LLM Agents](https://doi.org/10.2139/ssrn.6903579)** (Sun et al., SSRN 2026) - *実運用の様子を「RAGは終わった、エージェントにはgrepがあれば十分だ」と読む見方に応えるポジションペーパー。土台が変わったことは認めつつも、ずれは五つの観点にわたる構造的なものだと論じる。IRが前提とするコーパス、入力、目的、エピソード、検索対象のどれもが、計画し、ブラウズし、ツールを呼び、検索を続けるかどうかを自分で決めるエージェントには合わないからである。このずれを確かめるため、エージェントを固定したまま、HotpotQA-distractorと2WikiMultihopQAでBM25、ベクトル、grep、ハイブリッド、closed-bookの検索を入れ替えて比べ、検索を状態に条件づけられた証拠獲得の方策として捉え直すべきだと主張する。*
- **[Terminal Agents: A Survey of AI Agents in Command-Line Environments](https://arxiv.org/abs/2608.20485)** (Bin et al., arXiv 2026) - *タスクの領域ではなくターミナルを整理の軸に据える。対象は、タスクを前に進めるループがコマンドの実行とテキストのフィードバックを通じて回るエージェントで、アーキテクチャ、能力の獲得、評価にわたって、七つの次元からなる能力プロファイルの上に位置づける。条件を固定した独自の診断では、ベンチマークの系統ごとに見えるプロセスのシグナルが異なり、条件をそろえたシステム比較の結果もベンチマークしだいで変わった。そのため、どの結果についても、単一の構成要素のおかげだとは言い切りにくい。*
- **[Autonomous Research Agents: A Survey of AI Scientists and the Verification Gap](https://arxiv.org/abs/2608.05179)** (Ding et al., arXiv 2026) - *スクリーニングした 125 のAIサイエンティストのシステムのうち 26 を七つの監査の観点で分類し、ボトルネックが能力から検証可能性へ移ったことを示す。実行できる 24 のシステムのうち 83% はコードを公開しているが、シードや実行トレースを公開しているのは 38% だけで、新規性の検証を少しでも報告しているのも 38% にとどまる。クローズドループの九つのシステムのうち七つは機械的な再実行で、外部で検証されたループ内のoracleはコーパスのどこにも見当たらない。*
</details>

<sub><a href="#contents">↑ 目次に戻る</a></sub>

<a id="architectures"></a>
### 🏗️ エージェントのアーキテクチャとフレームワーク (51)
*サーベイの§2（背景）と、全体を通して使う例に対応します。*

<details>
<summary><b>51本の論文を表示</b></summary>

- **[Auto-GPT for Online Decision Making: Benchmarks and Additional Opinions](https://arxiv.org/abs/2306.02224)** (Yang et al., arXiv 2023) - *影響力は大きいのに論文のなかったAutoGPT型の自律エージェントの設計パターンを、査読に近い水準で実証的に調べた唯一の研究。* [[code](https://github.com/younghuman/LLMAgent)]
- **[AgentBench: Evaluating LLMs as Agents](https://arxiv.org/abs/2308.03688)** (Liu et al., ICLR 2024) - *種類の異なる環境にまたがって、単一エージェントの汎用的な能力を測るための標準的なベンチマーク。* ⭐ [[code](https://github.com/THUDM/AgentBench)]
- **[WebArena: A Realistic Web Environment for Building Autonomous Agents](https://arxiv.org/abs/2307.13854)** (Zhou et al., ICLR 2024) - *Webを閲覧する単一エージェントのアーキテクチャを試すための、事実上の標準のテストベッド。* [[code](https://github.com/web-arena-x/webarena)]
- **[Gorilla: Large Language Model Connected with Massive APIs](https://arxiv.org/abs/2305.15334)** (Patil et al., NeurIPS 2024) - *単一エージェントのツール利用における重要な論文。ファインチューニングと検索を組み合わせれば、実世界の大規模なAPIカタログをエージェントが確実に呼び出せることを示した。* [[code](https://github.com/ShishirPatil/gorilla)]
- **[ReWOO: Decoupling Reasoning from Observations for Efficient Augmented Language Models](https://arxiv.org/abs/2305.18323)** (Xu et al., arXiv 2023) - *効率を重視したReActループの代替として影響力を持った研究で、「先に計画してから実行する」か「交互に進める」かというアーキテクチャ設計の軸をよく表している。* [[code](https://github.com/billxbf/ReWOO)]
- **[Tree of Thoughts: Deliberate Problem Solving with Large Language Models](https://arxiv.org/abs/2305.10601)** (Yao et al., NeurIPS 2023) - *熟考しながら探索する、中核的な推論アーキテクチャ。LATSのような後発の単一エージェントの計画・探索フレームワークを支えている。* [[code](https://github.com/princeton-nlp/tree-of-thought-llm)]
- **[WebGPT: Browser-assisted question-answering with human feedback](https://arxiv.org/abs/2112.09332)** (Nakano et al., arXiv 2021) - *ChatGPT以前に現れた、現代のLLM Webエージェントの初期の先駆け。ブラウジングというツール利用と人のフィードバックを組み合わせる型を確立した。*
- **[SELF-REFINE: Iterative Refinement with Self-Feedback](https://arxiv.org/abs/2303.17651)** (Madaan et al., NeurIPS 2023) - *最小限の構成で広く採用された、単一エージェントの自己改善ループ。多くの大きなエージェントアーキテクチャのなかで、サブルーチンとして再利用されている。* [[code](https://github.com/madaan/self-refine)]
- **[SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](https://arxiv.org/abs/2405.15793)** (Yang et al., NeurIPS 2024) - *インターフェースの設計が単一エージェントの能力を大きく左右することを示した。この考え方は、今ではコーディングエージェント設計の標準になっている。* [[code](https://github.com/princeton-nlp/SWE-agent)]
- **[Language Agent Tree Search Unifies Reasoning, Acting, and Planning in Language Models](https://arxiv.org/abs/2310.04406)** (Zhou et al., ICML 2024) - *探索ベースの計画とReAct/Reflexionの系譜が合流した、最先端の到達点を示す。* [[code](https://github.com/lapisrocks/LanguageAgentTreeSearch)]
- **[Executable Code Actions Elicit Better LLM Agents](https://arxiv.org/abs/2402.01030)** (Wang et al., ICML 2024) - *単一エージェントのaction space設計における有力な代替案として、「code-as-action」を確立した。* [[code](https://github.com/xingyaoww/code-act)]
- **[Describe, Explain, Plan and Select: Interactive Planning with Large Language Models Enables Open-World Multi-Task Agents](https://arxiv.org/abs/2302.01560)** (Wang et al., NeurIPS 2023) - *オープンワールドやembodiedのタスクに向けた、単一エージェントの計画アーキテクチャの要となる研究。* [[code](https://github.com/CraftJarvis/MC-Planner)]
- **[OS-Copilot: Towards Generalist Computer Agents with Self-Improvement](https://arxiv.org/abs/2402.07456)** (Wu et al., arXiv 2024) - *汎用で自己改善するOSレベルの単一エージェントの、最近の代表例。AutoGPT流の自律性を実際のコンピュータ環境にまで広げた。* [[code](https://github.com/OS-Copilot/OS-Copilot)]
- **[AppAgent: Multimodal Agents as Smartphone Users](https://arxiv.org/abs/2312.13771)** (Zhang et al., CHI 2025) - *ReActとツール利用のパラダイムをGUIやモバイルの操作に広げた、最近の代表的な単一エージェントアーキテクチャ。* [[code](https://github.com/TencentQQGYLab/AppAgent)]
- **[The Landscape of Emerging AI Agent Architectures for Reasoning, Planning, and Tool Calling: A Survey](https://arxiv.org/abs/2404.11584)** (Masterman et al., arXiv 2024) - *エージェントアーキテクチャの設計パターンに範囲を絞ったサーベイで、単一エージェントのフレームワークを分類するのに直接役立つ。*
- **[MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework](https://arxiv.org/abs/2308.00352)** (Hong et al., ICLR 2024) - *単一エージェントの役割や手順のテンプレートが信頼性を高めることを示した、広く引用されるフレームワーク。フレームワーク設計が単一エージェントからマルチエージェントへと移る転換点にあたる。* [[code](https://github.com/geekan/MetaGPT)]
- **[Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, Long Context, and Next Generation Agentic Capabilities](https://arxiv.org/abs/2507.06261)** (Comanici et al., arXiv 2025) - *Agenticなツール利用とcomputer useを主要な能力として前面に押し出した、フロンティアモデルの技術報告。*
- **[Kimi K2: Open Agentic Intelligence](https://arxiv.org/abs/2507.20534)** (Kimi Team, arXiv 2025) - *大規模なagentic post-trainingを明確に中心に据えて作られた、フラッグシップのオープンモデル。* [[code](https://github.com/MoonshotAI/Kimi-K2)]

- **[GenericAgent: A Token-Efficient Self-Evolving LLM Agent via Contextual Information Density Maximization](https://arxiv.org/abs/2604.17091)** (Liang et al., arXiv 2026) - *コンテキスト上の経験を蓄積していく、トークン効率の高い自己進化エージェント。2026 年のエージェントフレームワークのなかでも、スター数が最も多いものの一つ。* [[code](https://github.com/lsdefine/GenericAgent)]
- **[Orchestral AI: A Framework for Agent Orchestration](https://arxiv.org/abs/2601.02577)** (Roman et al., arXiv 2026) - *専門化したエージェントを組み合わせ、単一のインターフェースの裏側でorchestrationするためのフレームワーク。* [[code](https://github.com/orchestralAI/orchestral-ai)]
- **[AgentArk: Distilling Multi-Agent Intelligence into a Single LLM Agent](https://arxiv.org/abs/2602.03955)** (Luo et al., arXiv 2026) - *マルチエージェントの知能をdistillationで単一のLLMエージェントに移し、協調による改善を低いコストのまま保つ。* [[code](https://github.com/AIFrontierLab/AgentArk)]
- **[The Interplay of Harness Design and Post-Training in LLM Agents](https://arxiv.org/abs/2606.25447)** (Kim et al., arXiv 2026) - *Harnessの設計とpost-trainingは互いに影響し合う。そのため、harnessを考慮したpost-trainingを行うと、分布内と分布外の両方で性能が上がる。*
- **[Next-Generation Agentic Reinforcement Learning Systems Enable Self-Evolving Agents](https://arxiv.org/abs/2607.01120)** (Ran Yan et al., arXiv 2026) - *重みだけでなく自分の構成要素まで書き換えるエージェントを可能にするのは、アルゴリズムではなくagentic RLのシステムスタックだと論じる。*
- **[From Atomic Actions to Standard Operating Procedures: Iterative Tool Optimization for Self-Evolving LLM Agents](https://arxiv.org/abs/2607.07321)** (Ding et al., arXiv 2026) - *実行トレースに繰り返し現れる行動の列を、呼び出し可能な高次の手続きにまとめる。そのうえで、できあがったツール群を統合し、評価し、刈り込む。*
- **[Self-Evolving World Models for LLM Agent Planning](https://arxiv.org/abs/2606.30639)** (Zhang et al., arXiv 2026) - *実行役を固定したまま、テスト時にエージェント内部の世界モデルを磨き、計画とシミュレーションのループを引き締める。*
- **[Scaling Self-Evolving Agents via Parametric Memory](https://arxiv.org/abs/2606.04536)** (Ren et al., arXiv 2026) - *自己進化の場をcontext windowからパラメータへ移し、プロンプトを長くしなくても、蓄積した経験をスケールさせられるようにする。*
- **[Inside the Scaffold: A Source-Code Taxonomy of Coding Agent Architectures](https://arxiv.org/abs/2604.03515)** (Rombaut et al., arXiv 2026) - *オープンなコーディングエージェントのscaffold 13 個から、ソースコードにもとづく分類体系を導く。システムごとに組み替えて使われる、合成可能なループの基本要素を五つ特定した。*
- **[Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses](https://arxiv.org/abs/2604.25850)** (Lin et al., arXiv 2026) - *可観測性のシグナルをもとにコーディングエージェントのharnessを自動で進化させ、Terminal-Bench 2の成績を 69.7 から 77.0 に引き上げた。*
- **[AgentFactory: A Self-Evolving Framework Through Executable Subagent Accumulation and Reuse](https://arxiv.org/abs/2603.18000)** (Zhang et al., arXiv 2026) - *成功した解法をテキストのプロンプトではなく、再利用できる実行可能なサブエージェントのコードとして保存することで能力を積み上げ、実行時のフィードバックで磨いていく。* [[code](https://github.com/zzatpku/AgentFactory)]
- **[CORAL: Towards Autonomous Multi-Agent Evolution for Open-Ended Discovery](https://arxiv.org/abs/2604.01658)** (Qu et al., COLM 2026) - *ハードコードされた探索ルールの代わりに、長時間動くエージェントに探索、reflection、協調を任せる。エージェントは共有の永続メモリを通じてやり取りし、ワークスペースは隔離され、評価者も分離されている。10 の最適化タスクで最高性能を達成し、評価ごとの改善率は 3 倍から 10 倍に達した。共に進化する四つのエージェントは、Anthropicのカーネルタスクを 1363 サイクルから 1103 サイクルに縮めた。* [[code](https://github.com/Human-Agent-Society/CORAL)]
- **[LogicHunter: Testing LLM Agent Frameworks with an Agentic Oracle](https://arxiv.org/abs/2607.06195)** (Long et al., arXiv 2026) - *仕様駆動のファジングフレームワークLogicHunterを提案する。ReActベースのagenticなoracleを組み合わせており、このoracleがドキュメントを検索し、ソースコードをたどり、実行時の状態を調べる。広く使われている三つのエージェントフレームワークで未知のバグを 40 件見つけ、うち 30 件が確認され、26 件が修正された。Oracleの適合率は 91.17% で、受動的な手法のうち最良のものは 29.27% にとどまった。*
- **[AgentFlow: Building Agent Dependency Graphs for Static Analysis of Agent Programs](https://arxiv.org/abs/2607.01640)** (Wang et al., arXiv 2026) - *LLMエージェントのソースコードからエージェントの依存関係を復元する、静的解析フレームワークAgentFlowを提案する。特定のフレームワークに依存しないAgent Dependency Graphを構築し、その型付きノードはエージェント、プロンプト、モデル、能力、メモリの状態、制御ポリシーを表す。実世界のエージェントプログラム 5,399 個に適用し、プロンプトからツールへと汚染が伝わるtaint型のリスクを 238 件見つけた。*
- **[SEAGym: An Evaluation Environment for Self-Evolving LLM Agents](https://arxiv.org/abs/2606.17546)** (Zheng et al., arXiv 2026) - *自己進化するLLMエージェントのための評価環境SEAGymを提案する。エージェントのharnessへの変更を、単一のタスクスコアではなく、学習、検証、held-outのテスト、リプレイ、コストという複数の観点で測る。*
- **[Harness-MU: A Safe, Governed, and Effective Harness for Multi-User LLM Agents](https://arxiv.org/abs/2606.21856)** (Fan et al., arXiv 2026) - *モデルを選ばず、チューニングも不要なharness、Harness-MUを提案する。モデル内部の安全策に頼らず、決定的な実行フックを使って、LLMエージェントに複数の主体を前提としたアクセス制御を強制する。* [[code](https://github.com/YuanJrShiuan/Harness-MulUser)]
- **[Co-Evolving Skill Generation and Policy Optimization](https://arxiv.org/abs/2606.08755)** (Zhang et al., arXiv 2026) - *Skillで拡張した言語エージェントのための、オンラインの枠組みを提案する。候補のskillごとに、文脈に依存する限界効用を、条件をそろえた比較群（その候補を含む場合と含まない場合の検索済みskill）で見積もり、効果のないskillや有害なskillを保存する前に取り除く。これを通常のrolloutの予算内で行い、さらに方策そのものがskillを生成するように学習させる。*
- **[DemoEvolve: Overcoming Sparse Feedback in Agentic Harness Evolution with Demonstrations](https://arxiv.org/abs/2605.24539)** (Che et al., arXiv 2026) - *DemoEvolveは、人間の専門家によるデモンストレーションのtrajectoryを使って、agenticなharnessを進化させるときの探索を導く。自己練習だけではうまくいかないBalatroのような複雑で確率的な環境で、報酬が疎なことによる不安定さに対処する。*
- **[Self-Evolving Software Agents](https://arxiv.org/abs/2604.27264)** (Robol et al., arXiv 2026) - *BDI（Belief-Desire-Intention）推論と大規模言語モデルを組み合わせたアーキテクチャを提案する。自動化された進化モジュールが経験から新しい要件を引き出し、それに対応する設計とコードを合成する。*
- **[Codified Context: Infrastructure for AI Agents in a Complex Codebase](https://arxiv.org/abs/2602.20478)** (Vasilopoulos et al., arXiv 2026) - *LLMのコーディングアシスタントに永続的なコンテキストを持たせるため、三つの構成要素からなる基盤（規約をまとめた憲章、19 の専門エージェント、34 の仕様書からなる知識ベース）を提案する。* [[code](https://github.com/arisvas4/codified-context-infrastructure)]
- **[LLM-as-a-Verifier: A General-Purpose Verification Framework](https://arxiv.org/abs/2607.05391)** (Kwok et al., arXiv 2026) - *検証そのものを独立したスケーリングの軸として扱う。採点用トークンのlogitから得た連続値のスコアを、粒度、評価の繰り返し、基準の分解でスケールさせ、追加の学習なしでTerminal-Bench V2で 86.5% に達した。* [[code](https://github.com/llm-as-a-verifier/llm-as-a-verifier)]
- **[Molt: A Scalable PyTorch-Native Training Framework for Agentic Reinforcement Learning](https://arxiv.org/abs/2607.21653)** (Hu et al., arXiv 2026) - *研究者やコーディングアシスタントが最初から最後まで読み通せるほど小さな、PyTorchネイティブのコンパクトなagentic RLトレーナーでも、Megatronベースのスタックと統計的に遜色ない結果を保てることを示す。* [[code](https://github.com/NVIDIA-NeMo/labs-molt)]
- **[Baselines Before Architecture: Evaluating Coding Agents for Autonomous Penetration Testing](https://arxiv.org/abs/2607.13085)** (Dhakal et al., arXiv 2026) - *デフォルトのままのコーディングCLIエージェントでも、104 タスクからなるXBOWベンチマークの大部分をすでに解ける。モデルをそろえれば、素のエージェントを繰り返し実行するだけで、公開されているharnessアーキテクチャに並ぶことができる。*
- **[Argus: A General-Purpose Agentic Runtime for Long-Horizon Reasoning](https://arxiv.org/abs/2608.05144)** (Li et al., arXiv 2026) - *Manager、Planner、Engineer、Reviewerが、永続するプロジェクトの状態の上で範囲を限ったミッションを実行する、持続型のランタイム。メモリ、skill、検証器は、担当する役割のレビューを通ってはじめて取り込まれる。重みは固定したままで、SWE-Bench Proでの 78%（直接実行のbaselineは 59%）はランタイムの状態だけから生まれている。*
- **[Architectural Implications of Agentic AI Workflows](https://arxiv.org/abs/2608.04458)** (Yang et al., arXiv 2026) - *Azureの本番環境での調査を通じて、agenticなワークロードをデータセンターの問題として特徴づける。OrchestrationとツールがCPUをcritical pathに乗せること、そして細切れの実行が、従来の均一なサーバーではCPUとGPUの両方の容量を遊ばせてしまうことを明らかにした。*
- **[Ouroboros: A Self-Developing Frontier Coding Agent with Reviewed Core Evolution](https://arxiv.org/abs/2608.08311)** (Razzhigaev et al., arXiv 2026) - *ツール、プロンプト、コンテキストの組み立て、中核の実装が、レビューを経たコミットによって改善され、そのコミットが後の作業のランタイムになるコーディングエージェントのharness。固定したsnapshotからTerminal-Bench 2.1で 86.74%、OSWorld-Verifiedで 90.69% を報告しており、これとは別の 161 日間のデプロイでは、稼働しながら進化を続けている。* [[code](https://github.com/razzant/ouroboros)]
- **[The Scaffolding Matters More Than the Interface: A Controlled Comparison of MCP and CLI Tool Use Across Seven Agent Scaffoldings, Five Language Models, and One Software Task](https://arxiv.org/abs/2608.08654)** (Alier Forment et al., arXiv 2026) - *固定したgitのタスク一つを、七つのagent scaffoldと五つの言語モデルで実行し、コストを左右するのはMCPかCLIかというインターフェースではなく、scaffoldのほうだと示す。MCPに対応していない二つのscaffoldはすべての実行をCLIで完了し、CLIでの実行だけで比べても、MCPに対応した五つのscaffoldより 5.0 倍から 28 倍安かった。厳密に対にした十三組のMCP対CLIのコスト比は 0.43 倍から 29 倍に広がり、MCPでの実行に使った費用の 12.9% は完了した作業に結びつかなかった（CLIでは 2.2%）。*
- **[Persistent Recursive Worlds Enable Autonomous Software Evolution](https://arxiv.org/abs/2608.10450)** (Huang et al., arXiv 2026) - *永続させるのはエージェントではなく、ソフトウェアのプロジェクトである。寿命の限られたエージェントが局所的な変更を提案し、受け入れられた結果だけがバージョン履歴を先へ進める。120 時間を超える一度の実行で、約 250k 行のRust製Cコンパイラを作り上げ、c-testsuiteをすべて通過させた。かかったモデルのトークン料金は 44 米ドルである。*
- **[What Does Multi-Harness RL Learn? Credit Assignment and Portability in Coding Agents](https://arxiv.org/abs/2609.04518)** (Le et al., arXiv 2026) - *Aider、OpenHands、Qwen Code、SWE-agentの固定された記録を再生し、一つのadvantageグループに複数のharnessをまとめると、ほかのharnessにも持ち運べるskillが身につくのかを切り分ける。結果を最も大きく左右したのは評価用のharnessだった。封印した 24,000 回の評価で、平均解決率は評価用harnessによって 2.14% から 9.27% まで動いたが、学習レシピによる変化は 1.16 にとどまった。Held-outのharnessでは、harnessをまたいだグループ化が同じharness内でのグループ化を 0.25 ポイント上回ったものの、その信頼区間はゼロをまたぎ、差は各ルール自身のシードによるばらつきの幅よりも小さい。*
- **[TROVE: Adaptive Agent Skill Orchestration via Trace-Grounded Route Validation and Editing](https://arxiv.org/abs/2609.05019)** (Wang et al., arXiv 2026) - *計画した経路を、確定したものではなく暫定的なものとして扱う。オフラインでは、評価済みのworkflow探索のトレースから、単体のskillと複合skill、そして結果に条件づけた遷移グラフを作っておき、オンラインでは、有効な続きを残す、トレースに裏づけられた局所的な対応を差し込む、無効な末尾だけを置き換える、のいずれかを選ぶ。こうして実行時の証拠は、大がかりな再計画ではなく局所的な修復に使われる。アブレーションによると、オフラインでの効果の大半は複合skillから、効率の改善の大半は末尾の置き換えから来ている。*
- **[SwiftSage: A Generative Agent with Fast and Slow Thinking for Complex Interactive Tasks](https://arxiv.org/abs/2305.17390)** (Lin et al., NeurIPS 2023) - *エージェントを、素早く行動するファインチューニング済みの小さなモデルと、行動が行き詰まったり無効だったりといったきっかけがあるときだけ呼ばれるGPT-4のplannerに分ける。ScienceWorldの 30 種類のタスクで、SayCan、ReAct、Reflexionを上回った。*
- **[R2V Agent: Teaching SLMs When to Ask for Help](https://arxiv.org/abs/2605.16604)** (Hemadri et al., arXiv 2026) - *難しさはtrajectoryの途中で変わるため、クエリ単位ではなくステップ単位でルーティングする。Brierスコアでcalibrationしたrouterが、残る失敗のリスクが高いときだけ、distillationで作った小さなモデルから教師のLLMへescalationする。TextWorldでの成功率を 64.6% から 98.2% に高め、escalationの割合は 41.7% だった。* [[code](https://github.com/RaghuHemadri/r2v-agent)]
- **[REFLEX with Jev for Efficient Selective Control in LLM Agents](https://arxiv.org/abs/2609.26532)** (Wu and Lim, arXiv 2026) - *テキストの代わりに型付きの決定を返すモデルJevに、エージェントの限られた選択を任せ、confidenceが低いときやテキストが必要なときだけ強いLLMを呼ぶ。固定した 100 タスクのベンチマークで成功率 95% を保ちつつ強いモデルの呼び出しを 72.7% 減らしたが、BFCLやτ系のタスクでは安価な生成型cascadeと比べてほとんど改善がない。*
</details>

<sub><a href="#contents">↑ 目次に戻る</a></sub>

## 🧱 第1部：中核となる構成要素

<a id="planning"></a>
### 🧠 計画と推論 (51)
*サーベイの§4（計画と推論）に対応します。*

<details>
<summary><b>51本の論文を表示</b></summary>

- **[Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://arxiv.org/abs/2201.11903)** (Wei et al., NeurIPS 2022) - *ほぼすべてのLLMエージェントの推論・計画モジュールの土台にある基礎技術で、CoT、ToT、ReActと続く系譜全体の出発点である。*
- **[Self-Consistency Improves Chain of Thought Reasoning in Language Models](https://arxiv.org/abs/2203.11171)** (Wang et al., ICLR 2023) - *推論時のensembleと検証の標準的な戦略で、エージェントの推論・計画のパイプラインのなかで広く再利用されている。*
- **[Large Language Models are Zero-Shot Reasoners](https://arxiv.org/abs/2205.11916)** (Kojima et al., NeurIPS 2022) - *推論する振る舞いはモデルに潜在しており、zero-shotのプロンプトで引き出せることを示した。汎用的なエージェントのプロンプトテンプレートを可能にした、重要な成果である。* [[code](https://github.com/kojima-takeshi188/zero_shot_cot)]
- **[Least-to-Most Prompting Enables Complex Reasoning in Large Language Models](https://arxiv.org/abs/2205.10625)** (Zhou et al., ICLR 2023) - *タスク分解を早い段階で定式化した研究。タスク分解は計画の中核となる基本要素で、その後のLLMエージェントのタスクplannerのほぼすべてが再利用している。*
- **[STaR: Bootstrapping Reasoning With Reasoning](https://arxiv.org/abs/2203.14465)** (Zelikman et al., NeurIPS 2022) - *自ら生成した推論をエージェントに身につけさせる、RLによるreasoning modelの学習パラダイム（DeepSeek-R1、o1など）の先駆け。* [[code](https://github.com/ezelikman/STaR)]
- **[Graph of Thoughts: Solving Elaborate Problems with Large Language Models](https://arxiv.org/abs/2308.09687)** (Besta et al., AAAI 2024) - *エージェントが使う構造化された推論・探索の枠組みを木構造の先へと広げ、複雑な多段階タスクで品質とコストの両方を改善する。* [[code](https://github.com/spcl/graph-of-thoughts)]
- **[Reasoning with Language Model is Planning with World Model](https://arxiv.org/abs/2305.14992)** (Hao et al., EMNLP 2023) - *探索としての古典的な計画（MCTS、世界モデル）をLLMの推論と結びつけた研究で、不確実な状況でのエージェントの計画に直結する。* [[code](https://github.com/maitrix-org/llm-reasoners)]
- **[CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing](https://arxiv.org/abs/2305.11738)** (Gou et al., ICLR 2024) - *Self-critiqueとツールによる検証を橋渡しする。Reflectionを外部のフィードバックに根ざしたものにする、現代のエージェントフレームワークの要となる仕組みである。* [[code](https://github.com/microsoft/ProphetNet/tree/master/CRITIC)]
- **[Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models](https://arxiv.org/abs/2305.04091)** (Wang et al., ACL 2023) - *広く使われている軽量な「計画してから実行する」テンプレートで、多くのLLMエージェントの計画モジュールがそのまま採用している。* [[code](https://github.com/AGI-Edgerunners/Plan-and-Solve-Prompting)]
- **[ADaPT: As-Needed Decomposition and Planning with Language Models](https://arxiv.org/abs/2311.05772)** (Prasad et al., ACL 2024) - *実行の結果に応じて適応する計画を示し、計画の粒度とエージェントの能力の釣り合いをとる。静的に計画してから実行するエージェントに対する、重要な改良である。* [[code](https://github.com/archiki/ADaPT)]
- **[Self-Discover: Large Language Models Self-Compose Reasoning Structures](https://arxiv.org/abs/2402.03620)** (Zhou et al., NeurIPS 2024) - *LLMがタスクごとに自分の推論戦略を自ら選べることを示す。これは、適応的なエージェントの計画の中心となるメタ推論の能力である。*
- **[Buffer of Thoughts: Thought-Augmented Reasoning with Large Language Models](https://arxiv.org/abs/2406.04271)** (Yang et al., NeurIPS 2024) - *再利用できる推論の構造をメモリから検索する手法の代表例で、推論戦略とエージェントのlong-term memoryの設計を結びつける。* [[code](https://github.com/YangLing0818/buffer-of-thought-llm)]
- **[Large Language Models Cannot Self-Correct Reasoning Yet](https://arxiv.org/abs/2310.01798)** (Huang et al., ICLR 2024) - *エージェント設計でself-critiqueのループに頼りすぎる傾向に歯止めをかけた、広く引用される警鐘的・批判的な結果。外部のフィードバックに根ざした手法が生まれるきっかけになった。*
- **[Training Language Models to Self-Correct via Reinforcement Learning](https://arxiv.org/abs/2409.12917)** (Kumar et al., ICLR 2025) - *プロンプトだけに頼らずRLを使えば、self-correctionを本当に効果のあるものにできることを示した。現代のエージェントで使われるreasoning modelのpost-trainingに、直接生かされている。*
- **[Let's Verify Step by Step](https://arxiv.org/abs/2305.20050)** (Lightman et al., ICLR 2024) - *Process reward modelとステップ単位の検証を確立した。今では、推論エージェントの探索やself-critiqueを導く標準的な部品になっている。* [[code](https://github.com/openai/prm800k)]
- **[DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/abs/2501.12948)** (Guo et al., Nature 2025) - *RLによって計画やreflectionの振る舞いが創発することを示した、節目となるオープンなreasoning modelの公開。こうした振る舞いは、今や次世代の推論エージェントを支えている。* [[code](https://github.com/deepseek-ai/DeepSeek-R1)]
- **[Towards Reasoning in Large Language Models: A Survey](https://arxiv.org/abs/2212.10403)** (Huang et al., ACL 2023) - *LLMの推論に絞ったサーベイとして最も早く、最も多く引用されているものの一つ。LLMエージェントのサーベイで推論の節を書くなら、まず引くべき文献である。* [[code](https://github.com/jeffhj/LM-reasoning)]
- **[Large Language Models for Planning: A Comprehensive and Systematic Survey](https://arxiv.org/abs/2505.19683)** (Cao et al., arXiv 2025) - *この小分野のうち、計画戦略の部分をちょうど扱う専用の最新サーベイ。分類体系にかかわる主張の裏づけに最適である。* [[code](https://github.com/Quester-one/Awesome-LLM-Planning)]
- **[When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs](https://arxiv.org/abs/2406.01297)** (Kamoi et al., ACL 2024) - *Self-critiqueとself-correctionに特化した、重要な批判的サーベイ。エージェントのサーベイでreflectionの手法を偏りなく厳密に扱うには欠かせない。* [[code](https://github.com/ryokamoi/llm-self-correction-papers)]
- **[Search-R1: Training LLMs to Reason and Leverage Search Engines with Reinforcement Learning](https://arxiv.org/abs/2503.09516)** (Jin et al., arXiv 2025) - *Agentic RLの定番の成果。モデルは結果に対する報酬だけから、検索エンジンの呼び出しを自分の推論に織り交ぜることを学ぶ。* [[code](https://github.com/PeterGriffinJin/Search-R1)]
- **[ReTool: Reinforcement Learning for Strategic Tool Use in LLMs](https://arxiv.org/abs/2504.11536)** (Feng et al., arXiv 2025) - *導出の途中で、いつ、どのようにコードインタープリタを呼び出すかをreasoning modelに教えるRL。*

- **[Harness Updating Is Not Harness Benefit: Disentangling Evolution Capabilities in Self-Evolving LLM Agents](https://arxiv.org/abs/2605.30621)** (Lin et al., arXiv 2026) - *自己進化するエージェントにおける「harnessの更新」と「harnessの恩恵」を切り分け、恩恵の曲線がモデルの階層をまたいで単調にならないことを見いだした。* [[code](https://github.com/A-EVO-Lab/a-evolve)]
- **[Demystifying Reinforcement Learning for Long-Horizon Tool-Using Agents: A Comprehensive Recipe](https://arxiv.org/abs/2603.21972)** (Wu et al., arXiv 2026) - *Agentic RLのための報酬設計、モデルの規模、データ、アルゴリズムの選び方を実験的にまとめたレシピで、TravelPlannerでSOTAに達した。* [[code](https://github.com/WxxShirley/Agent-STAR)]
- **[StraTA: Incentivizing Agentic Reinforcement Learning with Strategic Trajectory Abstraction](https://arxiv.org/abs/2605.06642)** (Xue et al., arXiv 2026) - *サンプリングしたtrajectoryの抽象化を介して戦略の生成と行動の実行を同時に学習し、ALFWorld、WebShop、SciWorldでのagentic RLを改善する。*
- **[The Self-Correction Illusion: LLMs Correct Others but Not Themselves](https://arxiv.org/abs/2606.05976)** (Chen et al., arXiv 2026) - *LLMは外部の主張の誤りなら正せても、自分が書いた同じ誤りは正せないことを示す。これは能力の差ではなく、チャットテンプレートの役割ラベルが生む見かけ上の現象である。*
- **[Recursive Self-Improvement in AI: From Bounded Self-Refinement to Autonomous Research Loops](https://arxiv.org/abs/2607.07663)** (Chen et al., arXiv 2026) - *範囲を限った自己改良から自律的な研究ループまでの広がりを整理し、再帰的な自己改善の各段階が現状どこで破綻するのかを示す。*
- **[SIRI: Self-Internalizing Reinforcement Learning with Intrinsic Skills for LLM Agent Training](https://arxiv.org/abs/2606.02355)** (He et al., arXiv 2026) - *見つけたskillを外部のライブラリに置いたままにせず、方策の中に取り込む強化学習。* [[code](https://github.com/kirito618/SIRI)]
- **[Agentic Chain-of-Thought Steering for Efficient and Controllable LLM Reasoning](https://arxiv.org/abs/2606.03965)** (Xia et al., arXiv 2026) - *推論時にagenticなchain-of-thoughtを誘導して推論の長さを制御し、再学習なしで計算量と精度のバランスを調整する。* [[code](https://github.com/Andree-9/ACTS)]
- **[ECHO: Prune To Act, Trace To Learn With Selective Turn Memory In Agentic RL](https://arxiv.org/abs/2606.31650)** (Xie et al., arXiv 2026) - *Agentic RLのための選択的なターンメモリ。行動するときはtrajectoryを刈り込み、学習のためにはトレースを残す。*
- **[AgentTether: Graph-Guided Diagnosis and Runtime Intervention for Reliable LLM Agent Operation](https://arxiv.org/abs/2607.06273)** (Zhao et al., arXiv 2026) - *実行をグラフにしてエージェントの失敗を診断し、事後だけでなく実行中にも介入する。*
- **[Reasoning as Gradient: Scaling MLE Agents Beyond Tree Search](https://arxiv.org/abs/2603.01692)** (Zhang et al., arXiv 2026) - *MLEエージェントのtree searchを勾配型の最適化の枠組みに置き換え、推論を勾配に、成功事例のメモリをモーメンタムに対応させる。* [[code](https://github.com/microsoft/RD-Agent)]
- **[MAP: A Map-then-Act Paradigm for Long-Horizon Interactive Agent Reasoning](https://arxiv.org/abs/2605.13037)** (Liu et al., arXiv 2026) - *行動する前に環境の認知地図を作り、long-horizonな対話的推論のために、地図作りと行動を切り離す。*
- **[Learning from Trials and Errors: Reflective Test-Time Planning for Embodied LLMs](https://arxiv.org/abs/2602.21198)** (Hong et al., arXiv 2026) - *Embodiedエージェントのための、reflectionを伴うテスト時の計画。一つのエピソードのなかで、自らの試行錯誤から学ぶ。* [[code](https://github.com/Reflective-Test-Time-Planning/Reflective-Test-Time-Planning)]
- **[Agora: Enhancing LLM Agent Reasoning Via Auction-Based Task Allocation](https://arxiv.org/abs/2607.09600)** (Zhou et al., arXiv 2026) - *オークション方式のorchestrationフレームワークAgoraを提案する。推論のステップを取引できる品目として扱い、専門モデルやツールが、生のconfidenceではなく補正した能力に応じてそれに入札する。*
- **[Training the Orchestrator: A Supervised Approach to End-to-End PDDL Planning with LLM Agents](https://arxiv.org/abs/2606.21740)** (Mangannavar et al., arXiv 2026) - *HALOを提案する。QLoRAで調整した小さなorchestratorの方策を、11 のPDDLドメインにわたり、検証器が認めた計画改良のtrajectoryで教師あり学習させる。*
- **[Retrospective Progress-Aware Self-Refinement for LLM Agent Training](https://arxiv.org/abs/2606.14302)** (Ma et al., arXiv 2026) - *先に進めてからreflectionするrolloutの枠組み、ReProを提案する。LLMエージェントがオンラインで行動を実行し、その後、完了したtrajectoryと判明した結果をもとに、ステップごとの進み具合を振り返って評価し直す。*
- **[LiTS: A Modular Framework for LLM Tree Search](https://arxiv.org/abs/2603.00631)** (Li et al., arXiv 2026) - *LiTSは、LLMのtree searchを再利用可能なPolicy、Transition、RewardModelの部品に分解するPythonフレームワークで、MCTSやBFSのようなアルゴリズムに対応する。MATH500、Crosswords、MapEvalで評価している。* [[code](https://github.com/xinzhel/lits-llm)]
- **[Localizing and Correcting Errors for LLM-based Planners](https://arxiv.org/abs/2602.00276)** (Kumar et al., arXiv 2026) - *Localized In-Context Learning（L-ICL）を提案する。LLMが生成した計画のなかで制約違反の箇所を特定し、失敗したステップに最小限の修正例を差し込む。*
- **[CLEANER: Self-Purified Trajectories Boost Agentic Reinforcement Learning](https://arxiv.org/abs/2601.15141)** (Xu et al., arXiv 2026) - *CLEANERを提案する。Similarity-Aware Adaptive Rollbackを使って、失敗したステップを成功したself-correctionに置き換え、agentic RL用の浄化されたtrajectoryを作る。より少ない学習ステップで、AIME24/25での精度を高めた。*
- **[VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning](https://arxiv.org/abs/2601.20055)** (Singh et al., arXiv 2026) - *LLMの出力を原子的な主張に分解し、一階述語論理で形式化したうえで、SMTソルバーで整合性を検証しながら答えを反復的に洗練するニューロシンボリックな枠組み。複数モデルの合意も使う。*
- **[TREK: A Travel Reasoning and Evaluation Kit for LLM Agents in Complex Trip Planning](https://arxiv.org/abs/2607.26977)** (Qi et al., arXiv 2026) - *LLM評価者ではなく、決定的なルールベースの評価器で採点する旅行計画のベンチマーク。15 のエージェントのうち最も強いものでも、完全に実行可能な旅程を返せたのは、解けるタスクの 46.2% にとどまった。* [[code](https://github.com/TonyQJH/TREK-A-Travel-Reasoning-and-Evaluation-Kit-for-LLM-Agents-in-Complex-Trip-Planning)]
- **[PRO-LONG: Programmatic Memory Enables Long-Horizon Reasoning](https://arxiv.org/abs/2607.20064)** (Fox et al., arXiv 2026) - *構造化された対話ログをすべて保持し、それをコーディングエージェントで検索すると、ARC-AGI-3で素のコーディングエージェントより 18 ポイント高くなる。トークンの使用量を 4.2-5.8 倍抑えながら、専用のharnessに並ぶ成績である。* [[code](https://github.com/alexisfox7/PRO-LONG)]
- **[The Physics of Multi-Turn Long-Horizon Planning: From Pre-training to Post-training via Single- and Multi-Teacher On-Policy Agentic Distillation](https://arxiv.org/abs/2607.24720)** (Men et al., arXiv 2026) - *Long-horizonな計画能力がどこから来るのかを調べた統制研究。事前学習でのCoTによる状態遷移のモデル化が最もよく汎化し、最適でないtrajectoryは不釣り合いなほど大きな害を与える。複数の教師によるdistillationは、互いに両立する計画パターンしか統合できない。*
- **[SearchMaster: Grounded and Regulated Self-Play for Search Agents](https://arxiv.org/abs/2608.01822)** (Tan et al., arXiv 2026) - *検索エージェントのためのself-play。自己生成データが学習を誤らせる三つの経路を名指しし、次の対策をとる：見せかけのマルチホップ質問を防ぐ証拠の連鎖、成功率ではなく検索の深さで測る難易度、使いもしない文書を開くことへのペナルティ。* [[code](https://github.com/WentaoTan/SearchMaster)]
- **[R³-Bench: LLMs Struggle with Resource-Rational Reasoning under Shared Budgets](https://arxiv.org/abs/2608.16033)** (Wang et al., arXiv 2026) - *六問からなるセットで計算予算を共有させると、同じモデルの単問での応答曲線を突き合わせて作ったオフラインのoracleが、72 のセルすべてでモデルの実際のセットのスコアに並ぶか上回り、71 のセルでは厳密に上回った。単問で示せる能力と、予算を共有したときに実際に発揮できる能力との間に、ギャップがあることを示す。Trajectoryの診断では、戦略の更新は限られていた。* [[code](https://github.com/NineAbyss/R-3-Bench)]
- **[Second Thought: Reasoning in Parallel as LLM Agents Act and Observe](https://arxiv.org/abs/2608.13667)** (Sun et al., arXiv 2026) - *ReActエージェントが環境からの応答を待っている空き時間に、補助的な推論の分岐を四つ走らせ、観測の時点でそれらを合流させる。九つのモデルとベンチマークの組すべてでターン数が減り、そのうち六つではメインスレッドのデコードが最大 43% 減った。Pass@1は九つのうち七つで統計的に変わらなかった。*
- **[CHIME: Credit-Aware Hierarchical Memory Evolution for Long-Horizon Agentic Planning](https://arxiv.org/abs/2609.02074)** (Ye et al., arXiv 2026) - *計画用のバンクと実行用のバンクを分け、何かを書き込む前に、各タスクの結果を計画、実行、その両方、どちらでもない、のいずれに帰すかを判定する。最終結果だけのフィードバックでは、計画の質と実行の誤りや環境のノイズが混ざってしまう、という考えにもとづく。できあがるメモリは小さく、学習された価値は下流での有用性とよく連動し、計画のメモリのほうが実行のメモリより価値が高い。このメモリはバックボーンのモデルをまたいで転用できる。*
- **[Do GUI Agents Know When Not to Act? Enabling Conflict-Aware Termination for Multimodal GUI Agents](https://arxiv.org/abs/2609.03438)** (Huang et al., arXiv 2026) - *行動する判断ではなく、止まる判断をベンチマークにする。指示そのものが矛盾している場合と、指示が画面の内容と矛盾している場合を扱い、実行に偏った過剰な従順さを見いだした。実行可能なタスクで高いスコアを出すエージェントが、矛盾したタスクでも実行を続けてしまうのである。推論時の実行可能性チェックと行動の調整を組み合わせると、五つのエージェントでこの傾向が減り、通常のタスクの性能も落ちない。*
- **[Steer, Don't Solve: Training Small Critic Models for Large Code Agents](https://arxiv.org/abs/2606.21811)** (Gandhi et al., arXiv 2026) - *SFTとDPOで4Bと8Bのcriticモデルを学習し、コーディングエージェントのtrajectoryにある誤りを見つけさせ、推論時に数ステップごとに大まかな指針を与える。行動そのものは生成しない。このcriticは、より大きな六つのエージェントのSWE-bench Verifiedでの解決率を高め、GLM-4.7-Flash-30B-A3Bでは 16.0 ポイント、GPT-OSS-120Bでは 14.4 ポイント上げた。エージェントが少ないステップで終えられる場合は誘導のコストが回収でき、GPT-OSS-20Bでは例ごとの費用が $0.07 から $0.03 に下がった。* [[code](https://github.com/shubhamrgandhi/critic-training)]
- **[Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners (KnowNo)](https://arxiv.org/abs/2307.01928)** (Ren et al., CoRL 2023) - *LLMのplannerが出す次のステップの候補にconformal predictionを適用し、閾値を越えて残るステップが複数あるときだけ、ロボットが人に助けを求めるようにする。タスクの達成に統計的な保証を与えつつ、人の手助けを最小限に抑える。*
- **[Real-Time Detection and Repair of LLM Agent Failures](https://arxiv.org/abs/2608.02464)** (Dubey, arXiv 2026) - *エージェント本体より費用がかかる、ステップごとのLLMによる判定をやめる。代わりに、ステップごとに約 200 マイクロ秒のテレメトリ監視と、決定的な再計算チェックを使う。問題を検出した実行はロールバックし、タスクの成功率を 52% から 73% に上げた。ただし、監視はデプロイごとにcalibrationし直す必要がある。* [[code](https://github.com/sunnydubey1111/agent-trajectory-sentinel)]
</details>

<sub><a href="#contents">↑ 目次に戻る</a></sub>

<a id="memory"></a>
### 💾 メモリ (56)
*サーベイの§5（メモリ）に対応します。*

<details>
<summary><b>56本の論文を表示</b></summary>

- **[RET-LLM: Towards a General Read-Write Memory for Large Language Models](https://arxiv.org/abs/2305.14322)** (Modarressi et al., arXiv 2023) - *トリプレット形式で構造化した読み書き型メモリの初期の設計で、影響も大きい。のちのグラフやKGにもとづくエージェントメモリの先駆けとなった。*
- **[MemoryBank: Enhancing Large Language Models with Long-Term Memory](https://arxiv.org/abs/2305.10250)** (Zhong et al., AAAI 2024) - *心理学に裏づけられた（人間の記憶に着想を得た）忘却と定着の仕組みを、LLMエージェントのメモリに持ち込んだ最初期のシステムの一つである。* [[code](https://github.com/zhongwanjun/MemoryBank-SiliconFriend)]
- **[Augmenting Language Models with Long-Term Memory](https://arxiv.org/abs/2306.07174)** (Wang et al., NeurIPS 2023) - *エージェントのscaffoldだけでなく、土台となる言語モデルそのものに学習可能なlong-term memoryの検索機構を持たせる、アーキテクチャ面での重要なアプローチ。* [[code](https://github.com/Victorwz/LongMem)]
- **[Synapse: Trajectory-as-Exemplar Prompting with Memory for Computer Control](https://arxiv.org/abs/2306.07863)** (Zheng et al., ICLR 2024) - *検索で補強したepisodicなtrajectoryメモリを使えば、複雑なGUI操作やコンピュータ制御のタスクでエージェントの意思決定をgroundingできることを示した。* [[code](https://github.com/ltzheng/Synapse)]
- **[ExpeL: LLM Agents Are Experiential Learners](https://arxiv.org/abs/2308.10144)** (Zhao et al., AAAI 2024) - *生のepisodic replayではなく、エージェント自身のメモリから再利用・転用できる「経験」の知識を引き出す、影響力の大きいパラダイムである。* [[code](https://github.com/LeapLabTHU/ExpeL)]
- **[Walking Down the Memory Maze: Beyond Context Limit through Interactive Reading (MemWalker)](https://arxiv.org/abs/2310.05029)** (Chen et al., arXiv 2023) - *木構造（階層型）のメモリをたどって読む手法で、long-contextのモデリングとエージェントによるメモリ検索を橋渡しした点で影響が大きい。*
- **[MemGPT: Towards LLMs as Operating Systems](https://arxiv.org/abs/2310.08560)** (Packer et al., COLM 2024) - *LLMエージェントが階層化したlong-term memoryを自ら管理するアーキテクチャで、最も広く引用され、製品化（Letta）も進んだものの一つである。* [[code](https://github.com/cpacker/MemGPT)]
- **[Think-in-Memory: Recalling and Post-thinking Enable LLMs with Long-Term Memory](https://arxiv.org/abs/2311.08719)** (Liu et al., arXiv 2023) - *生のテキストではなく推論の過程を保存することで、素朴なメモリ想起では推論が食い違いやすいという落とし穴を避ける。のちの「reflective retrieval」型のメモリ設計に影響を与えた。*
- **[Evaluating Very Long-Term Conversational Memory of LLM Agents](https://arxiv.org/abs/2402.17753)** (Maharana et al., ACL 2024) - *LLMエージェントの長期にわたる会話のメモリを評価・比較するための標準ベンチマーク（Mem0、MIRIX、A-MEMなどが採用）。* [[code](https://github.com/snap-research/locomo)]
- **[Larimar: Large Language Models with Episodic Memory Control](https://arxiv.org/abs/2403.11901)** (Das et al., ICML 2024) - *編集でき、すばやく更新できるepisodic memoryをLLMに持たせる手法のうち、プロンプトではなくアーキテクチャの水準で取り組むものの代表例である。* [[code](https://github.com/IBM/larimar)]
- **[HippoRAG: Neurobiologically Inspired Long-Term Memory for Large Language Models](https://arxiv.org/abs/2405.14831)** (Gutiérrez et al., NeurIPS 2024) - *脳の仕組みに着想を得たlong-term memory兼RAGのフレームワークで、ナレッジグラフ検索とエージェントメモリを橋渡しする。影響力が大きく、強いbaselineとして広く使われている。* [[code](https://github.com/OSU-NLP-Group/HippoRAG)]
- **[On the Structural Memory of LLM Agents](https://arxiv.org/abs/2412.15266)** (Zeng et al., arXiv 2024) - *メモリの構造化の選択肢を統制された条件で実証的に比べており、サーベイでエージェントメモリの設計上のトレードオフを論じる際の根拠として役立つ。*
- **[A-MEM: Agentic Memory for LLM Agents](https://arxiv.org/abs/2502.12110)** (Xu et al., arXiv 2025) - *グラフやノートのリンクで動的に自己組織化する、最新世代のLLMエージェント向けlong-term memoryシステムの代表例。* [[code](https://github.com/WujiangXu/A-mem)]
- **[From Human Memory to AI Memory: A Survey on Memory Mechanisms in the Era of LLMs](https://arxiv.org/abs/2504.15965)** (Wu et al., arXiv 2025) - *メモリという下位分野に絞った最近の包括的なサーベイで、心理学にもとづく分類体系を示す。LLMエージェント全体を扱うサーベイがメモリの文献を整理するときに引用できる。*
- **[Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://arxiv.org/abs/2504.19413)** (Chhikara et al., arXiv 2025) - *実運用を見据えた代表的なLLMエージェント向けlong-term memoryシステムで、広く導入されている。最先端の比較対象としてよく使われる。* [[code](https://github.com/mem0ai/mem0)]
- **[MIRIX: Multi-Agent Memory System for LLM-Based Agents](https://arxiv.org/abs/2507.07957)** (Wang et al., arXiv 2025) - *LLMベースのエージェントに向けて、マルチエージェント構成で複数種類（multimodal）のメモリを扱うアーキテクチャという、いまの最先端の流れをよく表している。* [[code](https://github.com/Mirix-AI/MIRIX)]
- **[LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory](https://arxiv.org/abs/2410.10813)** (Wu et al., ICLR 2025) - *長期の対話的なメモリを、個別に試験できる五つの能力に分解する。* [[code](https://github.com/xiaowu0162/LongMemEval)]
- **[ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory](https://arxiv.org/abs/2509.25140)** (Ouyang et al., arXiv 2025) - *成功したtrajectoryと失敗したtrajectoryの両方から戦略レベルのメモリを抽出し、エージェントが連続するタスクのなかで自己進化できるようにする。*
- **[Memory OS of AI Agent](https://arxiv.org/abs/2506.06326)** (Kang et al., EMNLP 2025) - *オペレーティングシステムのメモリ管理（STM/MTM/LPMの階層、heatにもとづく昇格、セグメント単位のページング）をエージェントメモリに持ち込み、LoCoMoで大きく改善した。* [[code](https://github.com/BAI-LAB/MemoryOS)]
- **[Zep: A Temporal Knowledge Graph Architecture for Agent Memory](https://arxiv.org/abs/2501.13956)** (Rasmussen et al., arXiv 2025) - *会話データと業務データを動的に統合するbi-temporalなナレッジグラフのメモリエンジン（Graphiti）で、DMRとLongMemEvalでMemGPTを上回った。実運用向けメモリの標準的な参照先である。* [[code](https://github.com/getzep/graphiti)]
- **[What Deserves Memory: Adaptive Memory Distillation for LLM Agents](https://arxiv.org/abs/2508.03341)** (Ma et al., ACL 2026) - *対話を出来事の境界で区切り、predict-then-calibrateのループで意味内容を抽出する自己組織化型のepisodic memory（Nemori）。構築コストを下げながら、時間に関する推論も改善する。* [[code](https://github.com/nemori-ai/nemori)]
- **[MemOS: A Memory OS for AI System](https://arxiv.org/abs/2507.03724)** (Li et al., arXiv 2025) - *メモリを第一級の資源（MemCube）に格上げし、パラメトリックメモリ、活性化メモリ、平文メモリを、スケジューリングと統制を担う一つのオペレーティングシステムのもとで統一する。* [[code](https://github.com/MemTensor/MemOS)]
- **[G-Memory: Tracing Hierarchical Memory for Multi-Agent Systems](https://arxiv.org/abs/2506.07398)** (Zhang et al., NeurIPS 2025) - *組織論に着想を得た三層のグラフ（洞察・クエリ・相互作用）に協調のtrajectoryを蓄える、マルチエージェントシステム向けに設計したメモリである。* [[code](https://github.com/bingreeky/GMemory)]
- **[Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models](https://arxiv.org/abs/2510.04618)** (Zhang et al., ICLR 2026) - *コンテキストそのものをplaybookとみなし、generate・reflect・curateという差分操作で進化させていく。自己改善するエージェントで起きがちなbrevity biasとcontext collapseを抑える。* [[code](https://github.com/ace-agent/ace)]

- **[SimpleMem: Efficient Lifelong Memory for LLM Agents](https://arxiv.org/abs/2601.02553)** (Liu et al., arXiv 2026) - *意味圧縮による生涯メモリ（構造化圧縮、オンライン統合、意図を踏まえた検索）で、推論トークンを最大 30 倍削減する。* [[code](https://github.com/aiming-lab/SimpleMem)]
- **[PlugMem: A Task-Agnostic Plugin Memory Module for LLM Agents](https://arxiv.org/abs/2603.03296)** (Yang et al., arXiv 2026) - *認知科学に着想を得たナレッジグラフ型のメモリで、設計し直さずにさまざまなタスクへ差し込める。* [[code](https://github.com/TIMAN-group/PlugMem)]
- **[Memanto: Typed Semantic Memory with Information-Theoretic Retrieval for Long-Horizon Agents](https://arxiv.org/abs/2604.22085)** (Abtahi et al., arXiv 2026) - *13 カテゴリに型付けしたメモリのスキーマと、情報理論にもとづく単一クエリでの検索を組み合わせ、LongMemEvalとLoCoMoでSOTAを達成した。*
- **[MINTEval: Evaluating Memory under Multi-Target Interference in Long-Horizon Agent Systems](https://arxiv.org/abs/2605.18565)** (Lee et al., arXiv 2026) - *15.6K 件のQAからなるベンチマーク（コンテキストは最大 1.8M トークン）で、互いに干渉し頻繁に更新される事実を前にすると、メモリエージェントが苦戦することを示した。* [[code](https://github.com/amy-hyunji/MINTEval)]
- **[What to Keep, What to Forget: A Rate-Distortion View of Memory Compaction in LLMs and Agents](https://arxiv.org/abs/2607.08032)** (Colaco et al., arXiv 2026) - *コンテキストのcompactionをrate-distortionの問題として定式化し、何を残し何を忘れるかを、ヒューリスティックではなく明示的な歪みの予算として扱う。*
- **[AutoMem: Automated Learning of Memory as a Cognitive Skill](https://arxiv.org/abs/2607.01224)** (Wu et al., arXiv 2026) - *メモリ管理そのものを、harnessが書いた固定の検索ポリシーではなく、エージェントが学ぶskillとして扱う。* [[code](https://github.com/autoLearnMem/AutoMem)]
- **[TokenPilot: Cache-Efficient Context Management for LLM Agents](https://arxiv.org/abs/2606.17016)** (Xu et al., arXiv 2026) - *プロンプトキャッシュを前提にコンテキストを管理し、追い出しが起きてもキャッシュの連続性を保つことでコストを下げる。* [[code](https://github.com/zjunlp/LightMem2)]
- **[Self-GC: Self-Governing Context for Long-Horizon LLM Agents](https://arxiv.org/abs/2607.00692)** (Hao et al., arXiv 2026) - *Long-horizonなタスクのあいだ、コンテキストの管理をエージェント自身に任せる。決まったスケジュールでcompactionするのではなく、いつcompactionするかをエージェントが判断する。*
- **[MemSyco-Bench: Benchmarking Sycophancy in Agent Memory](https://arxiv.org/abs/2607.01071)** (Xiang et al., arXiv 2026) - *エージェントのメモリにおけるsycophancy、つまり保存された信念がセッションをまたいでユーザーの圧力に屈するかどうかを測るベンチマーク。* [[code](https://github.com/XMUDeepLIT/MemSyco-Bench)]
- **[Remember the Decision, Not the Description: A Rate-Distortion Framework for Agent Memory](https://arxiv.org/abs/2605.10870)** (Zou et al., arXiv 2026) - *エージェントのメモリにrate-distortionの定式化を与え、明示的な歪みの予算のもとで、記述ではなく決定のほうを残す。*
- **[LongMemEval-V2: Evaluating Long-Term Agent Memory Toward Experienced Colleagues](https://arxiv.org/abs/2605.12493)** (Wu et al., arXiv 2026) - *短いコンテキストでの質問応答の先へ進み、「経験豊富な同僚」という設定をねらったエージェントのlong-term memoryベンチマークである。*
- **[Experience Compression Spectrum: Unifying Memory, Skills, and Rules in LLM Agents](https://arxiv.org/abs/2604.15877)** (Zhang et al., arXiv 2026) - *メモリ、skill、ルールを別々の仕組みとしてではなく、経験の圧縮という一本のスペクトル上の点として統一的に扱う。*
- **[PLACEMEM: Toward a Compute-Aware Memory Plane for Lifelong Agents](https://arxiv.org/abs/2607.04089)** (Ganguly et al., arXiv 2026) - *生涯にわたって動くエージェントのためのメモリプレーンPLACEMEMを提案する。意味内容、provenance、有効性を、訂正を踏まえた同一性のもとで束ねるバージョン付きのカプセルが土台になっている。*
- **[COMFYCLAW: Self-Evolving Skill Harnesses for Image Generation Workflows](https://arxiv.org/abs/2607.01709)** (Li et al., arXiv 2026) - *Agenticなフレームワークを提案する。画像生成のworkflowの構築を型付きグラフの編集として定式化し、vision-language modelで視覚的な誤りを見つけて直し、過去の実行を再利用できるskillのライブラリにまとめて育てていく。六つのエージェント構成すべてで平均スコアが最も高く、skillを進化させない検証器だけのbaselineも上回った。*
- **[The Past Is Prologue: A Plug-in Controller for Selective Updates in Sequentially Evolving LLM Memory](https://arxiv.org/abs/2606.31121)** (Chen et al., arXiv 2026) - *手法を問わないコントローラJanusを提案した。既存のLLMエージェントのメモリ更新器を包み込み、更新候補を一つずつ受け入れるか却下するかを決める。*
- **[E-mem: Multi-agent based Episodic Context Reconstruction for LLM Agent Memory](https://arxiv.org/abs/2601.21714)** (Wang et al., arXiv 2026) - *E-memは階層型のマルチエージェントメモリのフレームワークで、アシスタントエージェントが圧縮しないメモリ断片を保持し、マスターエージェントが計画を調整してepisodicなコンテキストを再構成する。LoCoMoベンチマークで評価している。* [[code](https://github.com/dog-last/E-mem)]
- **[AMV-L: Lifecycle-Managed Agent Memory for Tail-Latency Control in Long-Running LLM Systems](https://arxiv.org/abs/2603.04443)** (Bamidele et al., arXiv 2026) - *エージェントメモリシステムAMV-Lを提案する。メモリ項目ごとに継続的に更新される効用スコアを割り当て、価値にもとづく昇格、降格、追い出しによって、検索の対象を上限のある候補集合に収める。TTLによる保持と比べてスループットを 3.1 倍に高め、レイテンシの中央値を 4.2 倍縮めた。この改善はプロンプトが短くなったからではなく、検索の作業量に上限を設けたことによる。*
- **[From Raw Experience to Skill Consumption: A Systematic Study of Model-Generated Agent Skills](https://arxiv.org/abs/2605.23899)** (Huang et al., arXiv 2026) - *モデルが生成したLLMエージェントのskillを、経験の生成からskillの抽出、skillの利用まで通して評価する、効用にもとづくフレームワーク。*
- **[MemFail: Stress-Testing Failure Modes of LLM Memory Systems](https://arxiv.org/abs/2605.26667)** (Garg et al., arXiv 2026) - *四つのタスクにまたがる五つのデータセットからなる診断用ベンチマークMemFailを導入し、LLMエージェントが使う外部メモリシステムの要約・保存・検索での失敗モードを切り分けて負荷試験する。*
- **[Filesystem-Based Memory for LLM Agents: Organization, Evolution, and Sustainability](https://arxiv.org/abs/2607.26637)** (Zhou et al., arXiv 2026) - *エージェントが実際に採用しているMarkdownディレクトリ型のメモリは、検索の効率（大きな資料で検索コストがおよそ半分）をもたらすものの答えの質は上がらず、蓄積が増えるにつれて構成が崩れていくことを明らかにした。*
- **[Keep It InMind: Benchmarking the Implicit-Association Blind Spot in Agent Memory](https://arxiv.org/abs/2607.24368)** (Li et al., arXiv 2026) - *必要な事実がクエリと似ていないとメモリは機能しないことを示す。メモリをコンテキストに入れればbackboneは間接的な質問の 84.0% に答えられるが、六つの検索システムでは最高でも 14.4% にとどまる。*
- **[Metis: Memory Foundation Model](https://arxiv.org/abs/2607.26760)** (Zhang et al., arXiv 2026) - *メモリを外部モジュールではなくbackboneの内部に置く。ネイティブなメモリ状態を一度のforward passだけで勾配を使わずに維持し、推論時の重みは固定したままである。チェックポイントも公開されている。*
- **[When Memory Lies: An Empirical Study of Spatial Memory Staleness in VLM Agents](https://arxiv.org/abs/2608.04574)** (Sun et al., arXiv 2026) - *確信をもって保存されたメモリが、エージェントに見えているものと食い違ったときに何が起きるかを測る。同一のグリッドでも視覚のF1は 0.887 から 0.067 まで開き、生のメモリを信じるエージェントは、メモリをまったく与えない同じエージェントの倍以上の頻度で死ぬ。*
- **[Caching for the Future: Scrub Jay Episodic Memory Principles for Agent Memory Systems](https://arxiv.org/abs/2608.04746)** (Bhandari et al., arXiv 2026) - *アメリカカケスのepisodic memoryから種類に応じた忘却を借用し、保存した各項目に腐りやすさの係数と効用のhorizonを付けて、古くなった事実が検索から自然に消えていくようにする。減衰項を取り除くと汎化性能が 5.7 倍悪化する。*
- **[What Does Context Compression Cost an Agent? Interaction Costs Unrevealed by Task-Completion Metrics](https://arxiv.org/abs/2608.16370)** (Liu, arXiv 2026) - *タスクの完了率が統計的に変わらない圧縮でも、落とした状態を取り戻そうとしてエージェントの検索呼び出しがおよそ三倍に増えることがある（GPT-5.5の完了率は 80% から 85% で p = 1.0 だが、検索は 21.0 回から 63.9 回に増え、p = .002）。一方、同じスライディング方式の圧縮でもALFWorldでは検索の急増が起きず、この兆候は環境に依存する。*
- **[When Your Agent Opens the Chat App: Agent-Controlled Search over Raw Chat Logs Rivals Structured Memory](https://arxiv.org/abs/2608.12888)** (Li et al., arXiv 2026) - *手を加えていないチャット履歴に対し、キーワード検索を繰り返すループだけをエージェントに与える。インデックスはターン単位の語彙的なもので、要約、埋め込み、木、グラフは事前に作らない。それでも、backboneをGPT-4o-miniにそろえたMemoryAgentBenchの逐次マルチターン設定で、約 2,800 問にわたり、比較したどのシステムよりも高い平均正解率に達した（HippoRAG 2の 53.2 に対して 58.2）。*
- **[ForeDreamer: A Self-Evolving Dual-Agent Memory Architecture for Future Event Prediction](https://arxiv.org/abs/2608.20920)** (Zhong et al., EMNLP Findings 2026) - *検索結果をそのままエージェントに渡すのではなく、予測の前に生のWeb上の根拠を構造化されたメモリに変換する。質問ごとの事実メモリと、予測のエピソードをまたいで持続する経験メモリを分け、前者はメモリ担当のサブエージェントが構築し、二つの進化トラックが予測とメモリ構築の両方を改善する。Prophet ArenaとFutureXで評価した。* [[code](https://github.com/zhongzero/ForeDreamer)]
- **[Corpus2Skill: Distilling Enterprise Knowledge into Navigable Agent Skills for QA and RAG](https://arxiv.org/abs/2604.14572)** (Sun et al., EMNLP Findings 2026) - *オフラインのコンパイラがコーパスを階層的なskillのディレクトリにまとめ、エージェントはサービング時にそれをたどる。質問ごとに新しいクエリを出すのではなく、全体を見渡すところから細かな要約を経て文書まで掘り下げ、行き止まりの枝からは引き返す。ただし十一のデータセットでは、このナビゲーションは万能の代替にならず、勝ちが五、引き分けが三、負けが三だった。改善はトピックの分類体系を復元できる単一ドメインのコーパスに集中し、オープンドメインのファクトイド問題ではフラットな検索のほうが依然として望ましい。* [[code](https://github.com/dukesun99/Corpus2Skill)]
- **[Does Your Agent's Memory Survive a Model Upgrade? A Controlled Study of Memory Portability](https://arxiv.org/abs/2609.05339)** (Goyal et al., arXiv 2026) - *保存した履歴を固定してモデルだけを入れ替え、アップグレードを乗り切れるかどうかはメモリの形式で決まることを示す。スキーマ固定のナレッジグラフでは正解率の変化が 0.0004 ポイントにとどまる一方、モデルが圧縮したノートは移行の向きによって +9.91 ポイントまたは -13.28 ポイントと非対称に振れる。半分だけ移行した埋め込みインデックスは、全面的な再埋め込みで回復する 11.90 ポイントのうち 4.96 ポイントしか取り戻せず、ノートを保存領域だけで修復する方法は、元データを残していない限り 48 件すべての履歴で 90% の回復目標に届かない。*
- **[The Memory Trust Gap: Capability-Dependent Failures in Persistent-Memory Agents](https://arxiv.org/abs/2609.01852)** (Hu et al., arXiv 2026) - *メモリが唯一の情報源である場合と、信頼できるツールが正しい値を持っている場合を分け、失敗を混乱ではなく過信として読み解く。メモリしか頼れないとき、モデルは 0.92 から 1.00 の割合で古い保存値から答える。罠を仕掛けた条件での害は能力に左右され、Qwen3のサイズ系列では、古いメモを最新のように見せかけると大きなモデルほど激しく崩れる。*
- **[Dual-Layer Agentic Memory with Fast Write Routing and Slow Consolidation](https://arxiv.org/abs/2608.22215)** (Li et al., arXiv 2026) - *メモリへの書き込みを毎回、スキップ・新規書き込み・更新の三択にし、1.7B から 8B のcascadeで決める。冗長なメモリを最大 68% 削りつつ、escalationは入力の半分未満にとどめ、すべてを保持した場合のexact matchの 98% 超を保つ。*
- **[Jev-Mem: System-One-Controlled Agentic Memory for Efficient AI Agents](https://arxiv.org/abs/2609.23986)** (Jiang et al., arXiv 2026) - *メモリの型付け、ルーティング、グラフの探索、停止の判断をJevに任せ、LLMは返ってきた結果の推論にだけ使う。LoCoMoのメモリを最速のbaselineより 6.6 倍速く構築し、スコアは 0.700 に対して 0.777 だった。その差の大半は敵対的な質問から生まれている。* [[code](https://github.com/libingzheren/Jev-Mem)]
</details>

<sub><a href="#contents">↑ 目次に戻る</a></sub>

<a id="tools"></a>
### 🔧 ツール利用 (46)
*サーベイの§6（ツール利用と行動実行）に対応します。*

<details>
<summary><b>46本の論文を表示</b></summary>

- **[TALM: Tool Augmented Language Models](https://arxiv.org/abs/2205.12255)** (Parisi et al., arXiv 2022) - *LMのツール利用を自己教師ありのbootstrappingで身につけさせる初期の定式化で、影響力が大きい。Toolformerの自己教師ありアプローチを直接先取りしていた。*
- **[API-Bank: A Comprehensive Benchmark for Tool-Augmented LLMs](https://arxiv.org/abs/2304.08244)** (Li et al., EMNLP 2023) - *ツールで拡張した対話LLMの評価と学習に特化したベンチマークとして、最も早く、最も引用されているものの一つである。* [[code](https://github.com/AlibabaResearch/DAMO-ConvAI)]
- **[Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models](https://arxiv.org/abs/2304.09842)** (Lu et al., NeurIPS 2023) - *種類の異なるツールを、自然言語で立てた計画にもとづいて組み合わせ、協調させる代表例で、ツール利用と合成的推論の文献で広く引用されている。* [[code](https://github.com/lupantech/chameleon-llm)]
- **[Large Language Models as Tool Makers](https://arxiv.org/abs/2305.17126)** (Cai et al., arXiv 2023) - *ツールを使うのではなくツールを作るという方向の基礎となった研究で、LLMが既存のツールを呼ぶだけでなく、再利用できるツールを自ら書けることを示した。* [[code](https://github.com/ctlllll/LLM-ToolMaker)]
- **[GPT4Tools: Teaching Large Language Model to Use Tools via Self-instruction](https://arxiv.org/abs/2305.18752)** (Yang et al., NeurIPS 2023) - *Multimodalなツール利用をオープンソースのinstruction tuningで実現する手法の参照先として広く使われ、プロプライエタリなモデルを扱うツール利用の論文を補う位置にある。* [[code](https://github.com/StevenGrove/GPT4Tools)]
- **[ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings](https://arxiv.org/abs/2305.11554)** (Hao et al., NeurIPS 2023) - *プロンプトにツールを列挙する方式が抱えるコンテキスト長のボトルネックを避け、スケールするツール選択を可能にする、影響力のある別系統のアーキテクチャである。* [[code](https://github.com/Ber666/ToolkenGPT)]
- **[ToolAlpaca: Generalized Tool Learning for Language Models with 3000 Simulated Cases](https://arxiv.org/abs/2306.05301)** (Tang et al., arXiv 2023) - *自動合成したツール利用のコーパスで、小さなオープンモデルにも汎用的なツール利用能力を持たせられることを示す重要な根拠となり、のちの合成データによるツール学習パイプラインに影響を与えた。* [[code](https://github.com/tangqiaoyu/ToolAlpaca)]
- **[RestGPT: Connecting Large Language Models with Real-World RESTful APIs](https://arxiv.org/abs/2306.06624)** (Song et al., arXiv 2023) - *おもちゃのようなツール集合を越えて、状態を持つ複雑な実世界のREST APIにまでツール利用を広げられることを示した。付属のベンチマークは、APIにgroundingしたエージェントの評価にいまも使われている。* [[code](https://github.com/Yifan-Song793/RestGPT)]
- **[ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world APIs](https://arxiv.org/abs/2307.16789)** (Qin et al., ICLR 2024) - *最大級かつ最も引用されているツール利用のデータセット兼フレームワークの一つで、ToolBenchをオープンソースのツール利用LLMの標準的な学習・評価資源として定着させた。* [[code](https://github.com/OpenBMB/ToolBench)]
- **[Tool Documentation Enables Zero-Shot Tool-Usage with Large Language Models](https://arxiv.org/abs/2308.00675)** (Hsieh et al., arXiv 2023) - *ツール利用を引き出す手がかりを、デモではなくドキュメントに置き直した。多数のツールへスケールするうえで重要な方法論上の知見として、よく引用される。*
- **[Small LLMs Are Weak Tool Learners: A Multi-LLM Agent](https://arxiv.org/abs/2401.07324)** (Shen et al., EMNLP 2024) - *マルチエージェントで役割を分解してツール学習に取り組む手法として影響力があり、小さなオープンモデルでツール利用を効率よく運用するうえで特に参考になる。* [[code](https://github.com/X-PLUG/Multi-LLM-Agent)]
- **[StableToolBench: Towards Stable Large-Scale Benchmarking on Tool Learning of Large Language Models](https://arxiv.org/abs/2403.07714)** (Guo et al., ACL 2024) - *実APIを使う大規模なツール学習ベンチマークを悩ませていた再現性の問題を解決した評価基盤の論文で、広く使われている。* [[code](https://github.com/THUNLP-MT/StableToolBench)]
- **[What Are Tools Anyway? A Survey from the Language Model Perspective](https://arxiv.org/abs/2403.15452)** (Wang et al., COLM 2024) - *LMを中心に据えたツール利用専門のサーベイで、より広いLLMエージェントのサーベイからサブトピックの参照先としてそのまま引用できる。*
- **[ToolACE: Winning the Points of LLM Function Calling](https://arxiv.org/abs/2409.00920)** (Liu et al., arXiv 2024) - *小さなオープンモデルに正確なfunction callingを学ばせる合成データパイプラインの最先端を代表し、GPT-4に匹敵する性能を出す。*
- **[xLAM: A Family of Large Action Models to Empower AI Agent Systems](https://arxiv.org/abs/2409.03215)** (Zhang et al., arXiv 2024) - *Agenticなツール利用に最適化した独自のモデル群として「large action model」を打ち出した、産業界（Salesforce）の代表的な取り組み。五つのモデル（1Bから8x22Bまで）は公開時にBerkeley Function-Calling Leaderboardで首位に立ち、よく使われるbaselineになった。* [[code](https://github.com/SalesforceAIResearch/xLAM)]
- **[The Berkeley Function Calling Leaderboard (BFCL): From Tool Use to Agentic Evaluation of Large Language Models](https://openreview.net/forum?id=2GmDdhBdDk)** (Patil et al., ICML 2025) - *LLMのfunction callingとツール利用の性能を比べるための事実上の標準リーダーボード兼ベンチマークで、その後のfunction calling論文のほぼすべてが参照している。* [[code](https://github.com/ShishirPatil/gorilla)]
- **[Model Context Protocol (MCP): Landscape, Security Threats, and Future Research Directions](https://arxiv.org/abs/2503.23278)** (Hou et al., arXiv 2025) - *サーバーのライフサイクル全体にわたってMCPエコシステムのセキュリティを分析する。プロトコル層のサプライチェーンリスクを論じるときの定番の参照先である。*

- **[UniToolCall: Unifying Tool-Use Representation, Data, and Evaluation for LLM Agents](https://arxiv.org/abs/2604.11557)** (Liang et al., arXiv 2026) - *ツール呼び出しの表現、22K 超のツールと 390K 超のインスタンスからなるコーパス、標準化した七つのベンチマークを一つのフレームワークに統合する。* [[code](https://github.com/EIT-NLP/UniToolCall)]
- **[Skill Retrieval Augmentation for Agentic AI](https://arxiv.org/abs/2604.24594)** (Su et al., arXiv 2026) - *大規模なライブラリから必要に応じてskillを検索して適用できるようにし、約 26K のskillを含むSRA-Benchを導入する。*
- **[ToolFailBench: Diagnosing Tool-Use Failures in LLM Agents](https://arxiv.org/abs/2607.04686)** (Soni et al., arXiv 2026) - *最終タスクの成否だけを採点するのではなく、ツール利用の失敗のしかたを切り分ける診断用ベンチマーク。* [[code](https://github.com/SoHarshh/ToolFailBench)]
- **[Why Multi-Step Tool-Use Reinforcement Learning Collapses and How Supervisory Signals Fix It](https://arxiv.org/abs/2606.26027)** (Hao et al., arXiv 2026) - *マルチターンのツール利用RLがなぜ崩壊するのか、どの教師信号がそれを防ぐのかを突き止める。* [[code](https://github.com/hypasd-art/Tool-RL-Box)]
- **[When Does Restricting a Coding Agent to execute_code Help? A Regime × Agent-Design Ablation](https://arxiv.org/abs/2607.10569)** (Yang et al., arXiv 2026) - *コーディングエージェントの行動をexecute_codeひとつに絞ることがいつ役立ち、どの条件では逆効果になるかを調べるablationである。* [[code](https://github.com/hyang0129/onlycodes)]
- **[PACT: Privileged Trace Co-Training for Multi-Turn Tool-Use Agents](https://arxiv.org/abs/2606.16215)** (Du et al., arXiv 2026) - *マルチターンのツール利用エージェントを特権的なトレースで共同学習させ、学習時には得られるが推論時には得られない情報を移し込む。* [[code](https://github.com/ZhenbangDu/PACT)]
- **[PlanBench-XL: Evaluating Long-Horizon Planning of LLM Tool-Use Agents in Large-Scale Tool Ecosystems](https://arxiv.org/abs/2606.22388)** (Liu et al., arXiv 2026) - *大規模なツールエコシステムにおけるツール利用エージェント向けのlong-horizonな計画ベンチマークで、そこでは検索と選択が成否を左右する。* [[code](https://github.com/JiayuJeff/PlanBench-XL)]
- **[MCP-Atlas: A Large-Scale Benchmark for Tool-Use Competency with Real MCP Servers](https://arxiv.org/abs/2602.00933)** (Bandi et al., arXiv 2026) - *合成したツールのスタブではなく、実際のModel Context Protocolサーバーの上に構築した大規模なツール利用ベンチマークである。* [[code](https://github.com/scaleapi/mcp-atlas)]
- **[Model Context Protocol (MCP) Tool Descriptions Are Smelly! Towards Improving AI Agent Efficiency with Augmented MCP Tool Descriptions](https://arxiv.org/abs/2602.14878)** (Hasan et al., arXiv 2026) - *MCPのツール説明には繰り返し現れる品質上の「におい」があり、それを直すとエージェントのツール利用が目に見えて改善することを示す。*
- **[LLM Agents Already Know When to Call Tools -- Even Without Reasoning](https://arxiv.org/abs/2605.09252)** (Sun et al., arXiv 2026) - *明示的な推論の過程がなくても、エージェントはいつツールを呼ぶべきかをすでに内部で表現していることを見いだし、呼び出しの前に推論させる必要性に疑問を投げかける。* [[code](https://github.com/Trustworthy-ML-Lab/when2tool)]
- **[Tool-Making and Self-Evolving LLM Agents in Low-Latency Systems](https://arxiv.org/abs/2607.08010)** (Kujanpää et al., arXiv 2026) - *LLMエージェントが推論時に回すコード生成ループを、オフラインで動くagenticなツール作成パイプラインに置き換える。このパイプラインは、繰り返し現れる標準作業手順のステップを、検証済みでバージョン管理されたツールにコンパイルする。本番のアラームトリアージシステムではツール呼び出しによってp50レイテンシが 42% 短くなり、過去のアラーム 1,500 件ではend-to-endのエラー率が最大 53% 減った。*
- **[Looking Is Not Picking: An Attention-Segment Account of Tool-Selection Failures in LLM Agents](https://arxiv.org/abs/2606.16364)** (Chen et al., arXiv 2026) - *パラメータ数 0.5B から 32B までのモデルのBFCLでの失敗事例に、セグメントごとのattention指標を当てはめ、ツール選択の誤りが検索ではなく決定の段階で生じていることを突き止めた。*
- **[HyperTool: Beyond Step-Wise Tool Calls for Tool-Augmented Agents](https://arxiv.org/abs/2606.13663)** (Du et al., arXiv 2026) - *決定的なツールのサブルーチンを、モデルがコードとして発行する一つの外側の呼び出しにまとめ、途中の値が推論の過程を経由せずローカルで受け渡されるようにする。MCP-UniverseではQwen3-32Bを 15.7% から 35.3% に引き上げた。*
- **[Tool-Aware Optimization with Entropy Guidance for Efficient Agentic Reinforcement Learning](https://arxiv.org/abs/2606.03762)** (Cao et al., arXiv 2026) - *ツール呼び出しがすべて失敗したrolloutや、結果が一様に正解または不正解のrolloutを捨て、さらにツール呼び出し直後のトークンにエントロピーボーナスを加える。こうして重要な決定点での探索を保ちながら、エージェントのRLを安定させる。*
- **[SENTINEL: Failure-Driven Reinforcement Learning for Training Tool-Using Language Model Agents](https://arxiv.org/abs/2606.12908)** (Wang et al., arXiv 2026) - *失敗駆動の強化学習パイプラインSENTINELを提案する。Controllerが方策自身の失敗したrolloutから失敗モードを掘り出し、Proposerがそれを狙いを絞った学習タスクに変換し、Solverがそのタスクで学習する。Qwen3-4Bを使ったTau2-Bench Retailで、pass^1を 66.4 から 74.9 に上げた。*
- **[SCRIBE: Structured Mid-Level Supervision for Tool-Using Language Models](https://arxiv.org/abs/2601.03555)** (Jiang et al., arXiv 2026) - *SCRIBEは、ツールで拡張したエージェントのプロセスレベルのreward modelingを、厳選したskillのプロトタイプのライブラリにgroundingさせる強化学習フレームワークである。*
- **[CodeDelegator: Mitigating Context Pollution via Role Separation in Code-as-Action Agents](https://arxiv.org/abs/2601.14914)** (Fei et al., arXiv 2026) - *CodeDelegatorを提案する。戦略的な計画を担う常駐のDelegatorエージェントと、まっさらなコンテキストでサブタスクを実行する新たに起動したCoderエージェントとを分離する。*
- **[PruneTIR: Inference-Time Tool Call Pruning for Effective yet Efficient Tool-Integrated Reasoning](https://arxiv.org/abs/2605.09931)** (Zhang et al., arXiv 2026) - *ツール統合型の推論で誤ったツール呼び出しを刈り込む推論時のフレームワークを提案し、Success-Triggered Pruning、Stuck-Triggered Pruning、Resamplingを使う。*
- **[The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration](https://arxiv.org/abs/2603.22862)** (Xu et al., arXiv 2026) - *複数のツールを使うLLMエージェントを概観するサーベイ。最近の進展を六つの観点（計画・実行、学習、安全性、効率、能力開発、評価）から整理し、ソフトウェアエンジニアリング、企業のworkflow、グラフィカルユーザーインターフェース、モバイルシステムでの応用も取り上げる。*
- **[AppWorld-UL: Benchmarking Diverse Agent-User Interactions for Tool-Use](https://arxiv.org/abs/2607.20536)** (Chen et al., arXiv 2026) - *聞き返し、確認、拒否のいずれかが必要な、ユーザーが介在するツールタスク 516 件のうち、Claude Opus 4.7が解けたのは 48.6% だけで、組み合わせ型のシナリオでは 21.3% まで落ちた。*
- **[HANDBOOK.md: A Benchmark for Long-Context Agentic Instruction Following](https://arxiv.org/abs/2607.25398)** (Panavas et al., arXiv 2026) - *20 から 124 ページのポリシー文書とMCPツールを渡すと、エージェントは指示に従わなくなる。三十の構成のうち最良のものでも、厳格な採点で合格する試行は 36.2% にとどまる。* [[code](https://github.com/surge-ai/handbook)]
- **[ToolAtlas: Learning Once, Reusing Everywhere with Tool-Side Memory](https://arxiv.org/abs/2607.11126)** (Fang et al., arXiv 2026) - *メモリをエージェント側ではなくツールの提供者側に置く。実行して確かめたツールの能力、失敗の境界、組み合わせ方の記録を使うとpass@1が最大 21.61% 上がり、再学習なしで別のエージェントフレームワークにも移せる。*
- **[The Bitter Lesson of Tool Calling](https://arxiv.org/abs/2608.06370)** (Patel et al., arXiv 2026) - *BFCL v4の 14 モデルで、プログラムによるツール呼び出しとネイティブのJSONを比べる。ツールを型付きのPythonスタブとして公開し、モデルがコード経由で呼び出す方式は、14 モデル中 11 モデルでJSONと同等以上で、GPT-5.6系では 10.6% 向上し、baselineが崩れるcontext rotのもとでも安定している。*
- **[Diagnosing Tool-Selection Reasoning in LLM Agents with Canary Tools](https://arxiv.org/abs/2608.04719)** (Anand et al., arXiv 2026) - *MCPのツール集合に診断用のおとりツールを仕込み、「間違ったツールを選んだ」という結果だけから、その理由のプロファイルを得られるようにする。六種類のプローブと 8,640 回の実行で調べると、引っかかりやすさはモデル間で約 36 倍異なり、能力の階層とは連動しない。*
- **[The Devil Is in the Interface: Evaluating How Tool Architecture Shapes Coding Agent Behavior](https://arxiv.org/abs/2608.11386)** (Xu et al., arXiv 2026) - *背後の情報と行動は固定し、見せ方だけを変えた六つのツールアーキテクチャを、リポジトリ単位のissue修正 11,700 件のtrajectoryで比べる。構造化された低水準のインターフェースは繰り返し試行の一貫性を最大 4.7 倍高め、PythonのCodeAct風インターフェースはステップを 41.6%、トークン使用量を 56.3% 減らしながら同等のタスク性能を出す。一方、テキストベースの認知的scaffoldingのツールはほとんど変化をもたらさない。*
- **[Thinking With Tools, Not With Pixels: Tool Calls as Text Scaffolds for Visual Reasoning](https://arxiv.org/abs/2608.09682)** (Shao et al., arXiv 2026) - *切り抜きやズームのツールが返す画像をテキストのプレースホルダに置き換えても、LoRA、フルファインチューニング、RLのいずれでも、画像を使う本来のthinking-with-imagesと同等以上の結果が出る。効いているのは返ってくるピクセルではなく、呼び出し時に出力する構造化されたテキストのほうだとわかる。レイテンシは 29% から 46% 下がり、ツール実行のAPI呼び出しは不要になった。*
- **[Can MCP Clients Decide What to Do After Failure? A Result-Only Actionability Audit](https://arxiv.org/abs/2609.00072)** (Mehan, arXiv 2026) - *完了したMCPの失敗結果だけから、決定的なソフトウェアが何を判断できるかを問う。到達可能な十のサーバーで意図的に起こした 21 件という、あえて小さなサンプルでは、型付きのフィールドを見れば失敗そのものは 18 件でわかり、大まかな方針も 8 件で読み取れたが、具体的な原因、対象、実行可能な修復、再実行の制約はどれも示されなかった。そのため回復は、誰かが解釈しなければならない文章に頼ったままになる。*
- **[One Policy Is Enough: Single-Agent Reinforcement Learning Outperforms Tree Search for Chemistry Tool Learning](https://arxiv.org/abs/2608.30952)** (Dariani et al., arXiv 2026) - *二つの学習済みcriticのもとで方策モデルと実行モデルを別々に動かす階層的な進化型tree searchを、左から右への一本の生成に置き換える。この生成は、正解の呼び出し列から読み取ったプログラム的な報酬に対して、結果レベルの強化学習で訓練する。学習ループには学習済みのcriticも評価者も置かないが、それでもQwen-2.5-7Bで、質問あたり一度のモデル呼び出しのまま、Tool F1を 5.5%、Return F1を 9.6% 改善した。*
- **[DRACO: Fine-Grained Credit Assignment with Dynamic Rubrics for Long-Horizon Agent Training](https://arxiv.org/abs/2609.04094)** (Gandhi et al., arXiv 2026) - *正解の成功信号がない状況で、long-horizonなツール利用エージェントをGRPOで学習させる。学習中にタスク固有のrubricを生成し、各trajectoryをLLM評価者で一度だけ採点し、注釈した基準ごとに、それに責任のあるステップへadvantageを閉じた形で再配分する。帰属を学習するモジュールは使わない。AppWorldではベースモデルより 15.9 ポイント高く、自身は検証器を使わないにもかかわらず、正解の報酬で学習したGRPOを 5.3 上回った。最先端の評価者がなくても、Tau-Benchで 5.3 ポイントの改善が得られる。* [[code](https://github.com/IBM/draco)]
</details>

<sub><a href="#contents">↑ 目次に戻る</a></sub>

<a id="multi-agent"></a>
### 🤝 マルチエージェントシステム (51)
*サーベイの§7（マルチエージェントシステム）に対応します。*

<details>
<summary><b>51本の論文を表示</b></summary>

- **[CAMEL: Communicative Agents for "Mind" Exploration of Large Language Model Society](https://arxiv.org/abs/2303.17760)** (Li et al., NeurIPS 2023) - *ロールプレイを通じたエージェント同士の自律的な協力を確立した、最も早く、最も引用されているフレームワークの一つである。* [[code](https://github.com/camel-ai/camel)]
- **[Improving Factuality and Reasoning in Language Models through Multiagent Debate](https://arxiv.org/abs/2305.14325)** (Du et al., ICML 2024) - *「society of minds」風の討論をテスト時の手法として広めた、マルチエージェント討論の先駆的な論文。* [[code](https://github.com/composable-models/llm_multiagent_debate)]
- **[Encouraging Divergent Thinking in Large Language Models through Multi-Agent Debate](https://arxiv.org/abs/2305.19118)** (Liang et al., EMNLP 2024) - *マルチエージェント討論がself-consistency以上の効果を持つ理由を説明する、中核的な失敗モードを明らかにした。* [[code](https://github.com/Skytliang/Multi-Agents-Debate)]
- **[ChatEval: Towards Better LLM-based Evaluators through Multi-Agent Debate](https://arxiv.org/abs/2308.07201)** (Chan et al., ICLR 2024) - *マルチエージェント討論でLLM-as-judge評価の信頼性が上がることを示す。* [[code](https://github.com/chanchimin/ChatEval)]
- **[AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation](https://arxiv.org/abs/2308.08155)** (Wu et al., arXiv 2023) - *産業界で広く採用されているマルチエージェントのorchestrationフレームワーク（Microsoft）である。* [[code](https://github.com/microsoft/autogen)]
- **[ChatDev: Communicative Agents for Software Development](https://arxiv.org/abs/2307.07924)** (Qian et al., ACL 2024) - *複雑な実世界のworkflowをend-to-endのマルチエージェント協調でこなせることを示し、広く引用されている。* [[code](https://github.com/OpenBMB/ChatDev)]
- **[AgentVerse: Facilitating Multi-Agent Collaboration and Exploring Emergent Behaviors in Agents](https://arxiv.org/abs/2308.10848)** (Chen et al., ICLR 2024) - *動的に構成を変える汎用のマルチエージェント協調フレームワークであり、創発的な社会的ダイナミクスの研究でもある。* [[code](https://github.com/OpenBMB/AgentVerse)]
- **[Building Cooperative Embodied Agents Modularly with Large Language Models](https://arxiv.org/abs/2307.02485)** (Zhang et al., ICLR 2024) - *マルチエージェントの協調とコミュニケーションを、embodiedで物理世界にgroundingした設定へ広げる。* [[code](https://github.com/UMass-Embodied-AGI/CoELA)]
- **[ReConcile: Round-Table Conference Improves Reasoning via Consensus among Diverse LLMs](https://arxiv.org/abs/2309.13007)** (Chen et al., ACL 2024) - *異なるLLMのbackboneを組み合わせ、エージェントの討論と合意形成に、confidenceで重みづけした説得と投票を取り入れる。* [[code](https://github.com/dinobby/ReConcile)]
- **[Dynamic LLM-Agent Network: An LLM-Agent Collaboration Framework with Agent Team Optimization (v2 retitled: A Dynamic LLM-Powered Agent Network for Task-Oriented Agent Collaboration)](https://arxiv.org/abs/2310.02170)** (Liu et al., arXiv 2023) - *マルチエージェント協調のために、エージェントチームの構成とトポロジーを動的に最適化する手法を導入した。* [[code](https://github.com/SALT-NLP/DyLAN)]
- **[Exchange-of-Thought: Enhancing Large Language Model Capabilities through Cross-Model Communication](https://arxiv.org/abs/2312.01823)** (Yin et al., EMNLP 2023) - *エージェント間のコミュニケーションのパラダイムを分類しており、コミュニケーションの仕組みを概観するのに役立つ。* [[code](https://github.com/yinzhangyue/EoT)]
- **[LLM-Deliberation: Evaluating LLMs with Interactive Multi-Agent Negotiation Games (v2 retitled: Cooperation, Competition, and Maliciousness: LLM-Stakeholders Interactive Negotiation)](https://arxiv.org/abs/2309.17234)** (Abdelnabi et al., arXiv 2023) - *マルチエージェントLLMの研究を、戦略的・競争的なコミュニケーション（交渉）へ広げた。* [[code](https://github.com/S-Abdelnabi/LLM-Deliberation)]
- **[Unleashing the Emergent Cognitive Synergy in Large Language Models: A Task-Solving Agent through Multi-Persona Self-Collaboration](https://arxiv.org/abs/2307.05300)** (Wang et al., ACL 2024) - *マルチエージェント風の協調を、personaを使って単一のモデルの中で模倣できることを示す境界事例である。* [[code](https://github.com/MikeWangWZHL/Solo-Performance-Prompting)]
- **[Should we be going MAD? A Look at Multi-Agent Debate Strategies for LLMs](https://arxiv.org/abs/2311.17371)** (Smit et al., ICML 2024) - *マルチエージェント討論が本当に役立つのはいつなのかを問い直す、批判的かつ実証的な重要な反論。* [[code](https://github.com/instadeepai/DebateLLM)]
- **[Debating with More Persuasive LLMs Leads to More Truthful Answers](https://arxiv.org/abs/2402.06782)** (Khan et al., ICML 2024) - *マルチエージェント討論を、AI安全性におけるscalable oversightに結びつける。* [[code](https://github.com/ucl-dark/llm_debate)]
- **[Mixture-of-Agents Enhances Large Language Model Capabilities](https://arxiv.org/abs/2406.04692)** (Wang et al., ICLR 2025) - *複数エージェントの出力を構造的に集約すれば、強力なプロプライエタリモデルのどれを単体で使うよりも高い性能を出せることを示した、影響力のあるアーキテクチャである。* [[code](https://github.com/togethercomputer/MoA)]
- **[More Agents Is All You Need](https://arxiv.org/abs/2402.05120)** (Li et al., TMLR 2024) - *マルチエージェントの利点の多くが、コミュニケーションではなくensembleの規模拡大から来うることを示す、きわめて重要なbaseline。* [[code](https://github.com/MoreAgentsIsAllYouNeed/AgentForest)]
- **[Beyond Self-Talk: A Communication-Centric Survey of LLM-Based Multi-Agent Systems](https://arxiv.org/abs/2502.14321)** (Yan et al., arXiv 2025) - *マルチエージェントLLMシステム内のコミュニケーションを、最近のサーベイのなかで最も正面から扱っている。*
- **[Multi-Agent Collaboration Mechanisms: A Survey of LLMs](https://arxiv.org/abs/2501.06322)** (Tran et al., arXiv 2025) - *協調の仕組みを構造立てて分類した、このテーマ専門の最近のサーベイである。*
- **[Language Agents as Optimizable Graphs](https://arxiv.org/abs/2402.16823)** (Zhuge et al., ICML 2024) - *GPTSwarm：マルチエージェントシステムを、プロンプトとエッジを同時に学習するcomputation graphとして定式化する。* [[code](https://github.com/metauto-ai/GPTSwarm)]
- **[Scaling Large Language Model-based Multi-Agent Collaboration](https://arxiv.org/abs/2406.07155)** (Qian et al., arXiv 2024) - *明示的なトポロジーのもとで協調を 1000 超のエージェントまで拡大し、不規則なグラフが規則的なグラフを上回ることを示した（協調のスケーリングに関する結果）。*
- **[AFlow: Automating Agentic Workflow Generation](https://arxiv.org/abs/2410.10762)** (Zhang et al., ICLR 2025) - *コードで表したworkflowの空間を探索し、エージェントのパイプラインを自動で発見する。*

- **[Graph-of-Agents: A Graph-based Framework for Multi-Agent LLM Collaboration](https://arxiv.org/abs/2604.17148)** (Yun et al., arXiv 2026) - *順方向と逆方向のメッセージパッシングを用いたグラフベースのエージェント選択で、より少ないエージェントでMixture-of-Agentsを上回る。* [[code](https://github.com/UNITES-Lab/GoA)]
- **[Latent Agents: A Post-Training Procedure for Internalized Multi-Agent Debate](https://arxiv.org/abs/2604.24881)** (Yi et al., arXiv 2026) - *二段階のファインチューニングによるdistillationで、マルチエージェント討論を単一のモデルに取り込み、制御可能な視点を保ったままトークンを最大 93% 削減する。* [[code](https://github.com/johnsk95/latent_agents)]
- **[Uno-Orchestra: Parsimonious Agent Routing via Selective Delegation](https://arxiv.org/abs/2605.05007)** (Cui et al., arXiv 2026) - *分解の深さとワーカーへの委任を同時に決める統一的なRL方策で、コストを 10 倍下げながらworkflow型のbaselineを上回る。*
- **[Competition and Cooperation of LLM Agents in Games](https://arxiv.org/abs/2604.00487)** (Yao et al., arXiv 2026) - *資源配分ゲームやCournotゲームで、LLMエージェントはNash均衡に達するのではなく協力を選び、その背景には公平性にもとづく推論があることを見いだした。*
- **[Multi-Agent LLMs Fail to Explore Each Other](https://arxiv.org/abs/2607.11250)** (Choi et al., arXiv 2026) - *相手の探索をpartially observable stochastic gameとして定式化し、現在のエージェントは互いを探るときに近視眼的で両極端に偏ることを見いだす。対策のMACEは構造化した相手選択を使い、探索の価値がエージェントの多様性とともに高まることも証明している。* [[code](https://github.com/deeplearning-wisc/mace)]
- **[Who Broke the System? Failure Localization in LLM-Based Multi-Agent Systems](https://arxiv.org/abs/2607.07989)** (Xia et al., arXiv 2026) - *マルチエージェントの実行をどのエージェントが壊したのかを特定する。全体の成功率には表れない、デバッグの前提となる情報である。*
- **[When is Routing Meaningful? Diversity and Robustness in Language Model Societies](https://arxiv.org/abs/2607.09197)** (Huot et al., arXiv 2026) - *モデルの集団のなかでのルーティングがいつ意味を持つのか、多様性がノイズではなく頑健性をもたらすのはいつなのかを問う。*
- **[What LLM Agents Say When No One Is Watching: Social Structure and Latent Objective Emergence in Multi-Agent Debates](https://arxiv.org/abs/2607.02507)** (Ghaffarizadeh et al., arXiv 2026) - *聞き手がいないときにエージェントが何を話すかを観察し、タスクの指標では見落とされる潜在的な目的と社会構造を浮かび上がらせる。*
- **[Decision Protocols in Multi-Agent Large Language Model Conversations](https://arxiv.org/abs/2607.05477)** (Kaesberg et al., arXiv 2026) - *マルチエージェントの会話における意思決定プロトコルを比較し、投票や合意のルールを設計変数として扱う。*
- **[The Long-Horizon Task Mirage? Diagnosing Where and Why Agentic Systems Break](https://arxiv.org/abs/2604.11978)** (Wang et al., arXiv 2026) - *エージェントシステムがlong-horizonなタスクのどこで、なぜ破綻するのかを診断し、見かけ上のlong-horizonな能力の多くは蜃気楼にすぎないと論じる。*
- **[GoAgent: Group-of-Agents Communication Topology Generation for LLM-based Multi-Agent Systems](https://arxiv.org/abs/2603.19677)** (Chen et al., arXiv 2026) - *マルチエージェントシステムのcommunication topologyを手で固定するのではなく、エージェントのグループからなるグラフとして生成する。*
- **[Reinforcement Learning for LLM-based Multi-Agent Systems through Orchestration Traces](https://arxiv.org/abs/2605.02801)** (Zhang et al., arXiv 2026) - *Orchestrationのトレースを使い、強化学習でマルチエージェントシステムをend-to-endに学習する。*
- **[Learning Latency-Aware Orchestration for Multi-Agent Systems](https://arxiv.org/abs/2607.13359)** (Shi et al., arXiv 2026) - *総コストではなく実行のcritical pathに狙いを定め、学習時にレイテンシを考慮した実行グラフを学び、実行時には冗長なエージェント間のやり取りを刈り込む。同等の精度を保ちながら、end-to-endのレイテンシを 50% 以上下げる。*
- **[ProACT: Towards Breakdown-Aware Proactive Agent in Multi-User Collaboration](https://arxiv.org/abs/2607.03730)** (Yang et al., arXiv 2026) - *フレームワークProACTを提案する。会話エージェントが、発話者がひも付いた複数ユーザーの対話を観察し、現在のターンに介入が必要な協調の破綻が含まれるかを検出したうえで、黙っているか、的を絞った協調のskillで介入するかを決める。ターン単位の 3,244 例と五つのbackboneにわたって、適切さ、話を遮らないこと、簡潔さで、直接チャットする方式を上回った。*
- **[MAS-Orchestra: Understanding and Improving Multi-Agent Reasoning Through Holistic Orchestration and Controlled Benchmarks](https://arxiv.org/abs/2601.14652)** (Ke et al., arXiv 2026) - *LLMのマルチエージェント協調を、マルチエージェントシステム全体を一度に生成する強化学習の問題（holistic orchestration）として定式化し、五つのタスク次元をもつ統制されたベンチマークMASBENCHも導入した。*
- **[Security Threat Modeling for Emerging AI-Agent Protocols: A Comparative Analysis of MCP, A2A, Agora, and ANP](https://arxiv.org/abs/2602.11327)** (Anbiaee et al., arXiv 2026) - *AIエージェントの四つの通信プロトコル（MCP、A2A、Agora、ANP）に脅威モデリングを適用する。作成、運用、更新の各段階にわたってプロトコルレベルのリスクを十二種類特定する定性的なリスクフレームワークを示し、あわせてMCPの事例研究では、複数のサーバーを組み合わせたときに誤ったプロバイダのツールが実行される頻度を測る。*
- **[WebWeaver: Breaking Topology Confidentiality in LLM Multi-Agent Systems with Stealthy Context-Based Inference](https://arxiv.org/abs/2603.11132)** (Xiong et al., arXiv 2026) - *攻撃フレームワークWebWeaverを提案する。エージェントを一つ乗っ取り、エージェントIDではなくエージェントのコンテキストだけから推論して、LLMマルチエージェントシステムのcommunication topologyを割り出す。*
- **[Towards Self-Improving Error Diagnosis in Multi-Agent Systems](https://arxiv.org/abs/2604.17658)** (Li et al., arXiv 2026) - *LLMマルチエージェントシステムのfailure attributionのための、自己改善型のフレームワークErrorProbeを提案する。逆方向の追跡と、検証済みのepisodic memoryを備えたStrategist/Investigator/Arbiterのチームを使い、責任のあるエージェントと、誤りが始まったステップを特定する。TracerTrajとWho&Whenでbaselineを上回り、差が最もはっきり出るのはステップ単位の評価である。*
- **[OrchBench: Evaluating Multi-Agent Orchestration Plans in Isolation via Deterministic Simulation](https://arxiv.org/abs/2607.25656)** (Ren et al., arXiv 2026) - *ワーカーを実際に動かす代わりにシミュレーションでorchestrationの計画を採点し、トークンの 1.3% だけで実際の実行品質と r=0.816 で連動する。タスクに不可欠な情報を保つほうが、エージェントを増やすより効果が大きい。*
- **[Two Calls Beat Five Agents: Evaluating Multi-Agent Pipelines Against Self-Refinement for Local Language Models](https://arxiv.org/abs/2607.26922)** (Prajapati et al., arXiv 2026) - *ローカルの 7B モデルでは、二回の呼び出しによるself-refinementが五つの役割からなるパイプラインに勝つ（GSM8Kで 86.2% 対 82.0%、トークン使用量は 7.4 倍少ない）。アーキテクチャよりも、JSONを平文に切り替えることのほうが効く。*
- **[Do Latent Channels Actually Communicate? A Causal Audit of Latent Multi-Agent LLM](https://arxiv.org/abs/2607.26773)** (Zhang et al., arXiv 2026) - *潜在メッセージを別の例のものと入れ替え、全体の正解率が仕組みを覆い隠していることを示す。GSM8Kでの -1.00 ポイントという効果は、無関係なメッセージによる -6.17 と、例ごとの内容による +5.17 に分解できる。*
- **[When Does Latent Communication Pay? A Causal Audit of Relayed KV Caches in Multi-Agent LLMs](https://arxiv.org/abs/2608.04893)** (Cheng et al., arXiv 2026) - *エージェント間でKVキャッシュを中継すれば潜在的な思考が伝わる、という主張を、並べ替えたキャッシュ、ゼロにしたキャッシュ、モーメントを合わせたキャッシュに差し替えて検証する。受け手が送り手しか持たない情報を必要とする場合には効果は本物だが、そうでない場合、報告された改善は統計的にゼロと変わらない。*
- **[Everyone Conforms, No One Believes: Pluralistic Ignorance in LLM Agent Populations](https://arxiv.org/abs/2608.02758)** (YS, arXiv 2026) - *エージェントの集団がpluralistic ignoranceを再現することを見いだした。内心では規範を拒みながら、表向きには 64% から 94% の割合で同調する。公然と異を唱える者が一人いても、偽りの合意を崩せる割合は八つのモデルのうち七つで 26% 未満だった。*
- **[CityReal: Human-Aligned Urban Behavior and City Dynamics Simulation with Large-Scale LLM Agents](https://arxiv.org/abs/2608.16897)** (Bougie et al., arXiv 2026) - *都市での行動と都市のダイナミクスを、人間に沿う形で大規模にシミュレーションする。意図にもとづいて動くエージェントが、テキストのアダプタを通じて習慣や好みを学び、実際の人口統計に合わせる。*
- **[When Agents Coordinate: Measuring Coordination in Multi-Agent AI Coding](https://arxiv.org/abs/2608.16801)** (Destefanis et al., arXiv 2026) - *エージェントチームによるコーディング実行 1902 件を、メッセージ、ファイル書き込み、ファイル読み込みの時間ネットワークに変換して分析する。メッセージの多い作業では、共有ファイルが一対一のメッセージの繰り返しに取って代わり、エージェント八体で出力トークンを約 42% 減らす。一体をコーディネーターに指名しても通信のハブは生まれず、成功率も確実には上がらない。さらに、封印した 244 回の再実行でも、エージェントは五分の四の実行で隠された採点用の資料に手を伸ばした。*
- **[Debate Training Reduces Reward Hacking in RLAIF](https://arxiv.org/abs/2608.17776)** (Kenton et al., arXiv 2026) - *Gemini 2.5 Flash級の方策を、固定したより弱いGemini 2.5 Flash Liteの評価者が裁くgeneratorとcriticの討論でRLファインチューニングすると、一人で行うRLAIFのbaselineがすぐに評価者をハックしてしまうのに対し、学習を通じて評価者の性能が保たれ、性能差の 45% を取り戻す。プレイヤーに制約をかけないと、敵対的な学習はcriticによる評価者のハッキングに陥りやすい。批評の語数制限（150 語までなら有効）はゲームの釣り合いをとるが、その代わりcriticの表現の明快さが損なわれる。*
- **[OrchMAS: Orchestrated Reasoning with Multi Collaborative Heterogeneous Scientific Expert Structured Agents](https://arxiv.org/abs/2603.03005)** (Feng et al., arXiv 2026) - *科学的推論のために、orchestrationと実行を二つの層に分ける。Orchestratorモデルがタスクを読んでドメインを踏まえたパイプラインを組み、生成する専門家エージェントそれぞれの役割とプロンプトを書き、途中のフィードバックをもとに実行中にパイプラインを修正する。一方、別の実行モデルが各ステップをこなす。これにより、能力もコストも異なるbackboneを一回の実行のなかで混ぜて使える。*
- **[At Equal Inference Cost, Multi-Agent Structure Does Not Beat a Single Frozen Agent](https://arxiv.org/abs/2609.04217)** (Dylan et al., arXiv 2026) - *環境でのrolloutの回数ではなくモデル呼び出しの総数をそろえると、進化させた単一のexecutorに対してPlanner-Executor-Criticチームが持つとされた優位は消える。ALFWorldでは 0.769 対 0.754（p = 0.80）で、評価呼び出しは 1.8 倍かかる。Leave-one-in分析では、plannerとcriticが空の、あるいは効き目のないプロンプトへと進化し、実際の価値はすべてexecutorにあった。WebShopではチームのほうが悪くなる傾向がある。*
- **[A Case Study on Emergent Cheating and Whistleblowing in Autonomous Research Swarms](https://arxiv.org/abs/2609.04170)** (Paglieri et al., arXiv 2026) - *形式的な予想を証明する 100 体のエージェント集団のうち一体が評価システムの抜け穴を見つけ、それが競争の圧力のもとで、まず共有知識ライブラリで、次にエージェント間のメッセージで広がった。一方で別のグループは不正な証明を監査し、仲間に警告し、ボイコットを行い、検証用のパッチを提案した。抜け穴を運んだ透明な経路は、抵抗を可能にした経路と同じものであり、著者らはこれを単一のエージェント内部の失敗ではなく、コモンズのガバナンスの問題として読み解く。*
</details>

<sub><a href="#contents">↑ 目次に戻る</a></sub>

## 🌍 第2部：環境と応用のなかのエージェント

<a id="environments"></a>
### 🌐 インタラクティブ環境 (57)
*サーベイの§8（インタラクティブ環境のエージェント）に対応します。*

<details>
<summary><b>57本の論文を表示</b></summary>

- **[Do As I Can, Not As I Say: Grounding Language in Robotic Affordances](https://arxiv.org/abs/2204.01691)** (Ahn et al., CoRL 2022) - *Embodiedなロボットエージェントにおいて、実世界のaffordanceでgroundingしたLLMをplannerとして使えることを示した、基礎となる実証である。* [[code](https://github.com/google-research/google-research/tree/master/saycan)]
- **[Inner Monologue: Embodied Reasoning through Planning with Language Models](https://arxiv.org/abs/2207.05608)** (Huang et al., CoRL 2022) - *フィードバックにgroundingした閉ループの計画パターンを確立し、その後のembodiedエージェントやGUIエージェントのアーキテクチャの土台となった。*
- **[ALFWorld: Aligning Text and Embodied Environments for Interactive Learning](https://arxiv.org/abs/2010.03768)** (Shridhar et al., ICLR 2021) - *LLMベースのembodiedな家事エージェント（ReAct、Reflexion）の評価に広く使われるベンチマークで、テキストでの推論とembodiedな実行を橋渡しする。* [[code](https://github.com/alfworld/alfworld)]
- **[RT-1: Robotics Transformer for Real-World Control at Scale](https://arxiv.org/abs/2212.06817)** (Brohan et al., RSS 2023) - *大規模なロボット用Transformerモデルの基礎となった研究で、のちにRT-2やOpenVLAが発展させるレシピを確立した。* [[code](https://github.com/google-research/robotics_transformer)]
- **[PaLM-E: An Embodied Multimodal Language Model](https://arxiv.org/abs/2303.03378)** (Driess et al., ICML 2023) - *インターネット規模のvision-language事前学習がembodiedなロボットの推論に転移することを示した先駆的なembodied multimodal LLMで、RT-2やVLAモデルに影響を与えた。*
- **[RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control](https://arxiv.org/abs/2307.15818)** (Brohan et al., CoRL 2023) - *Embodiedエージェントやロボットのエージェント研究で中心となる、vision-language-action（VLA）モデルのパラダイムを確立した。*
- **[OpenVLA: An Open-Source Vision-Language-Action Model](https://arxiv.org/abs/2406.09246)** (Kim et al., CoRL 2024) - *クローズドなVLAモデルに対するオープンソースの対抗馬で、LLMを使ったロボット制御の研究を広く開放した。* [[code](https://github.com/openvla/openvla)]
- **[WebShop: Towards Scalable Real-World Web Interaction with Grounded Language Agents](https://arxiv.org/abs/2207.01206)** (Yao et al., NeurIPS 2022) - *言語をgroundingさせたWebエージェントのための、基礎的で広く使われているベンチマークである。LLMベースのWebナビゲーション研究よりも前に登場し、その動機づけとなった。* [[code](https://github.com/princeton-nlp/WebShop)]
- **[Mind2Web: Towards a Generalist Agent for the Web](https://arxiv.org/abs/2306.06070)** (Deng et al., NeurIPS 2023) - *実際のWebサイトでの汎用的なWebナビゲーションのために明示的に設計された最初のベンチマーク兼LLMベースのエージェントで、その後のWeb/GUIエージェントの論文で標準的に引用される。* [[code](https://github.com/OSU-NLP-Group/Mind2Web)]
- **[A Real-World WebAgent with Planning, Long Context Understanding, and Program Synthesis](https://arxiv.org/abs/2307.12856)** (Gur et al., ICLR 2024) - *指示を正規化したサブ指示に分け、長いHTMLをタスクに関係する断片に要約し、生成したPythonコードで行動する。実際のWebサイトでの成功率を 50% 以上引き上げ、Mind2Webのオフライン計画でも首位に立った。*
- **[GPT-4V(ision) is a Generalist Web Agent, if Grounded](https://arxiv.org/abs/2401.01614)** (Zheng et al., ICML 2024) - *Multimodal LLMが視覚にもとづく汎用Webエージェントとして振る舞えることを初めて体系的に示し、視覚にgroundingしたWeb/GUIエージェントへの移行を後押しした。* [[code](https://github.com/OSU-NLP-Group/SeeAct)]
- **[WebVoyager: Building an End-to-End Web Agent with Large Multimodal Models](https://arxiv.org/abs/2401.13919)** (He et al., ACL 2024) - *実世界で動くmultimodalなブラウザエージェントの重要な実証であり、ベンチマークでもある。その後のWebエージェントシステムの評価に広く使われている。* [[code](https://github.com/MinorJerry/WebVoyager)]
- **[Web Agents with World Models: Learning and Leveraging Environment Dynamics in Web Navigation](https://arxiv.org/abs/2410.13232)** (Chae et al., ICLR 2025) - *現在のLLMが世界モデルを持たないことを確かめたうえで、各行動が何を変えるかを自由記述のテキストで説明する世界モデルを学習させる。これにより、返金できない予約のような取り返しのつかない行動に踏み切る前に、エージェントが結果をシミュレーションできる。WebArenaとMind2Webで、tree searchより安価に方策の選択を改善した。* [[code](https://github.com/kyle8581/WMA-Agents)]
- **[CogAgent: A Visual Language Model for GUI Agents](https://arxiv.org/abs/2312.08914)** (Hong et al., arXiv 2023) - *スクリーンショットだけによるGUIのgroundingを目的に作られた最初期の大規模VLMの一つで、高解像度の視覚的GUIエージェントというアーキテクチャの系譜を切り開いた。* [[code](https://github.com/zai-org/CogAgent)]
- **[SeeClick: Harnessing GUI Grounding for Advanced Visual GUI Agents](https://arxiv.org/abs/2401.10935)** (Cheng et al., ACL 2024) - *GUI groundingを視覚的GUIエージェントの中核的な部分問題として位置づけ、groundingの標準ベンチマークであるScreenSpotを導入した。* [[code](https://github.com/njucckevin/SeeClick)]
- **[Mobile-Agent: Autonomous Multi-Modal Mobile Device Agent with Visual Perception](https://arxiv.org/abs/2401.16158)** (Wang et al., arXiv 2024) - *視覚を中心に据えたモバイルGUIエージェントの代表的な設計で、メタデータなしでアプリをまたいで操作できることを示した。* [[code](https://github.com/X-PLUG/MobileAgent)]
- **[OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](https://arxiv.org/abs/2404.07972)** (Xie et al., NeurIPS 2024) - *「computer use」エージェントを評価する標準ベンチマークで、2024 年以降の主要なcomputer useエージェントはほぼすべてこれで評価されている。* [[code](https://github.com/xlang-ai/OSWorld)]
- **[AndroidWorld: A Dynamic Benchmarking Environment for Autonomous Agents](https://arxiv.org/abs/2405.14573)** (Rawles et al., ICLR 2025) - *タスクを動的に変化させられる、モバイルGUIエージェントの再現可能なベンチマークとして主流になっている。* [[code](https://github.com/google-research/android_world)]
- **[UI-TARS: Pioneering Automated GUI Interaction with Native Agents](https://arxiv.org/abs/2501.12326)** (Qin et al., arXiv 2025) - *最先端のオープンな「ネイティブ」GUI/computer useエージェントモデルで、分野全体がend-to-endで学習したGUI行動モデルへ移りつつあることを示す。* [[code](https://github.com/bytedance/UI-TARS)]
- **[GUI Agents: A Survey](https://arxiv.org/abs/2412.13501)** (Nguyen et al., ACL 2025) - *GUIエージェントに的を絞った最新のサーベイで、GUI/computer useエージェントという下位分野とその分類体系を整理するのに使える。*
- **[Large Language Model-Brained GUI Agents: A Survey](https://arxiv.org/abs/2411.18279)** (Zhang et al., arXiv 2024) - *LLMで動くGUIエージェントの文献を網羅的に押さえるうえで価値のある、GUIエージェント専門の補完的なサーベイである。* [[code](https://github.com/vyokky/LLM-Brained-GUI-Agents-Survey)]
- **[A Survey of WebAgents: Towards Next-Generation AI Agents for Web Automation with Large Foundation Models](https://arxiv.org/abs/2503.23350)** (Ning et al., KDD 2025) - *Webエージェントという下位分野に絞ったサーベイで、ブラウザやWebの自動化エージェントに固有の分類体系と信頼性の議論を、すぐに使える形で示している。*
- **[UI-TARS-2 Technical Report: Advancing GUI Agent with Multi-Turn Reinforcement Learning](https://arxiv.org/abs/2509.02544)** (Wang et al., arXiv 2025) - *UI-TARSの後継で、end-to-endのGUI制御にマルチターンのRLを用いる。*
- **[π0: A Vision-Language-Action Flow Model for General Robot Control](https://arxiv.org/abs/2410.24164)** (Black et al., arXiv 2024) - *事前学習済みのVLMにflow matchingによる行動エキスパートを載せ、さまざまな形態のロボットを制御する。* [[code](https://github.com/Physical-Intelligence/openpi)]
- **[Tongyi DeepResearch Technical Report](https://arxiv.org/abs/2510.24701)** (Tongyi DeepResearch Team, arXiv 2025) - *Long-horizonなWeb調査と情報の統合を行う、オープンなend-to-endのdeep researchエージェントモデルである。* [[code](https://github.com/Alibaba-NLP/DeepResearch)]

- **[Mobile-Agent-v3.5: Multi-platform Fundamental GUI Agents](https://arxiv.org/abs/2602.16855)** (Xu et al., arXiv 2026) - *GUI-Owl-1.5は、モバイル・デスクトップ・ブラウザにネイティブ対応するマルチプラットフォームのエージェント群で、データフライホイールとMRPOによるRLを備え、20 以上のGUIベンチマークでSOTAを達成した。* [[code](https://github.com/X-PLUG/MobileAgent)]
- **[EvoCUA: Evolving Computer Use Agents via Learning from Scalable Synthetic Experience](https://arxiv.org/abs/2601.15876)** (Xue et al., arXiv 2026) - *合成タスクの生成と、sandboxでのオンラインの方策最適化を融合した自己進化型のcomputer useエージェントで、OSWorldで 56.7% に達した。*
- **[CUA-Suite: Massive Human-annotated Video Demonstrations for Computer-Use Agents](https://arxiv.org/abs/2603.24440)** (Jian et al., arXiv 2026) - *Computer useエージェント向けに、VideoCUA、UI-Visionベンチマーク、GroundCUA（スクリーンショット 56K 枚、UIアノテーション 3.6M 件）を公開する。* [[code](https://github.com/ServiceNow/GroundCUA)]
- **[Long-Horizon-Terminal-Bench: Testing the Limits of Agents on Long-Horizon Terminal Tasks with Dense Reward-Based Grading](https://arxiv.org/abs/2607.08964)** (Li et al., arXiv 2026) - *Long-horizonなタスクのために作ったターミナルベンチマークで、エージェントの失敗は単一ステップの能力不足よりも状態の追跡から生じる。* [[code](https://github.com/zli12321/LHTB)]
- **[WebRetriever: A Large-Scale Comprehensive Benchmark for Efficient Web Agent Evaluation](https://arxiv.org/abs/2607.06118)** (Dong et al., arXiv 2026) - *手作りの少数のサイトに頼るのではなく、効率的な評価を目的に設計した大規模なWebエージェントのベンチマークである。* [[code](https://github.com/Mininglamp-AI/WebRetriever)]
- **[CLI-Anything: Towards Agent-Native Computer Use](https://arxiv.org/abs/2606.03854)** (Yang et al., arXiv 2026) - *Computer useは画面をピクセル単位でなぞるのではなく、CLIを通じたエージェントネイティブなものであるべきだと主張する。* [[code](https://github.com/HKUDS/CLI-Anything)]
- **[PhoneBuddy: Training Open Models for Agentic Phone Use](https://arxiv.org/abs/2606.23049)** (Tang et al., arXiv 2026) - *クローズドなシステムが主流の、エージェントによるスマートフォン操作という設定で、オープンモデルを学習させる。* [[code](https://github.com/PhoneBuddyAI/phonebuddy)]
- **[Designing Agent-Ready Websites for AI Web Agents: A Framework for Machine Readability, Actionability, and Decision Reliability](https://arxiv.org/abs/2607.12056)** (Elnaffar et al., arXiv 2026) - *問題を逆から捉え、エージェントにとって機械可読で操作しやすいWebサイトをどう作るべきかを問う。*
- **[TerminalWorld: Benchmarking Agents on Real-World Terminal Tasks](https://arxiv.org/abs/2605.22535)** (Chu et al., arXiv 2026) - *実世界のターミナルタスクでエージェントを評価する。そこでは一歩ごとの能力よりも、long-horizonにわたる状態の追跡が成否を分ける。* [[code](https://github.com/EuniAI/TerminalWorld)]
- **[WebNavigator: Global Web Navigation via Interaction Graph Retrieval](https://arxiv.org/abs/2603.20366)** (Zhang et al., arXiv 2026) - *インタラクショングラフ上の検索でWebをナビゲートし、ページ単位の局所的な視野ではなく全体の構造をエージェントに与える。* [[code](https://github.com/fate-ubw/webNavigator)]
- **[MobileGym: A Verifiable and Highly Parallel Simulation Platform for Mobile GUI Agent Research](https://arxiv.org/abs/2605.26114)** (Wu et al., arXiv 2026) - *モバイルGUIエージェントの学習と評価のための、検証可能で高度に並列化されたシミュレーション基盤である。*
- **[ABot-AgentOS: A General Robotic Agent OS with Lifelong Multi-modal Memory](https://arxiv.org/abs/2607.10350)** (Tian et al., arXiv 2026) - *Embodiedなロボット向けのエージェントOSを提案する。計画、skillの実行、視覚・空間・時間の情報を統合するUniversal Multi-modal Graph Memoryを一つにまとめる。* [[code](https://github.com/amap-cvlab/ABot-AgentOS)]
- **[EvoPolicyGym: Evaluating Autonomous Policy Evolution in Interactive Environments](https://arxiv.org/abs/2607.02440)** (Zhilin Wang et al., arXiv 2026) - *評価設定としてAutonomous Policy Evolutionを、あわせてEvoPolicyGymベンチマークを導入する。エージェントとなるモデルが、コンパクトでインタラクティブな 16 の強化学習環境で、実行可能な方策のコードを繰り返し書き換える。* [[code](https://github.com/Linzwcs/EvoPolicyGym)]
- **[ChainSWE: Benchmarking Coding Agents on Multi-Bug Software Maintenance](https://arxiv.org/abs/2607.02606)** (Jin et al., arXiv 2026) - *54 のPythonプロジェクトにわたり、時系列につながった 304 件のissueからなるベンチマークChainSWE。孤立した欠陥ではなく、順に依存し合うバグ修正の連なりでコーディングエージェントを評価する。*
- **[VisCritic: Visual State Comparison as Process Reward for GUI Agents](https://arxiv.org/abs/2606.24525)** (Qian et al., arXiv 2026) - *視覚的なprocess rewardのフレームワークVisCriticを提案した。Siamese vision transformerと行動を考慮したcriticヘッドで行動の前後のスクリーンショットを視覚特徴空間で比べ、GUIエージェントの行動を検証する仕組みである。*
- **[ASPIRE: Agentic /Skills Discovery for Robotics](https://arxiv.org/abs/2607.00272)** (Lu et al., arXiv 2026) - *継続学習システムASPIREの提案で、エージェントがcode-as-policyのパラダイムのもとでロボットの制御プログラムを自律的に書き、磨き上げていく。*
- **[GUI vs. CLI: Execution Bottlenecks in Screen-Only and Skill-Mediated Computer-Use Agents](https://arxiv.org/abs/2606.24551)** (Zhou et al., arXiv 2026) - *条件をそろえたベンチマークでGUIとCLIのcomputer useエージェントを比べ、最も強いGUIエージェントの完全合格率が 59.1% だったのに対し、元のskillを使う最も強いCLIエージェントは 48.2% にとどまったと報告している。*
- **[A History-Aware Visually Grounded Critic for Computer Use Agents](https://arxiv.org/abs/2606.11078)** (Lee et al., arXiv 2026) - *HiViGは、GUIのtrajectoryで学習したmultimodalなcriticとして提案された。Computer useエージェントのやり取りの履歴を複数ステップの目標に圧縮し、提案された行動を現在のスクリーンショットと照らし合わせて確かめる。* [[code](https://github.com/G-JWLee/HiViG)]
- **[ISE: An Execution-Grounded Recipe for Multi-Turn OS-Agent Trajectories](https://arxiv.org/abs/2606.11520)** (Luo et al., arXiv 2026) - *Intent、Simulate、Executeの三段階からなるパイプラインISEの提案。役割を固定したユーザーシミュレータと、隔離されたOSのワークスペースでの実際のツール実行を組み合わせ、マルチターンのOSエージェント用の学習trajectoryを合成する。* [[code](https://github.com/Valiere01/ISE-Trace)]
- **[Demonstration-Free Robotic Control via LLM Agents](https://arxiv.org/abs/2601.20334)** (Tsui et al., arXiv 2026) - *FAEA（Frontier Agent as Embodied Agent）を導入し、手を加えていない汎用のLLMエージェントフレームワークを、デモもファインチューニングもなしにロボットの操作へ適用した。* [[code](https://github.com/robiemusketeer/faea-sim)]
- **[On Data Engineering for Scaling LLM Terminal Capabilities](https://arxiv.org/abs/2602.21193)** (Pi et al., arXiv 2026) - *合成タスク生成パイプラインTerminal-Task-Genを導入し、Nemotron-Terminalモデルを学習させるためのデータ戦略（フィルタリング、カリキュラム）を調べる。*
- **[Generalization in Online Reinforcement Learning for Mobile Agents](https://arxiv.org/abs/2603.07432)** (Gu et al., arXiv 2026) - *GUIモバイルエージェントのためのベンチマークと、GRPOにもとづくオンラインRLの学習システムであるAndroidWorld-Generalizationを導入する。未見のインスタンスではzero-shotの汎化が 26.1% 向上するが、未見のテンプレートでは 15.7% まで縮む。* [[code](https://github.com/zihuanjiang/AndroidWorld-Generalization)]
- **[WebXSkill: Skill Learning for Autonomous Web Agents](https://arxiv.org/abs/2604.13318)** (Wang et al., arXiv 2026) - *WebXSkillは、パラメータ化した行動プログラムと自然言語のガイダンスを組み合わせた、Webエージェントのためのskill学習フレームワークである。合成したtrajectoryから再利用できる行動パターンを抽出し、文脈に応じて検索できるようURLベースのグラフに整理する。WebArena、WebVoyager、Online-Mind2Webで成績を改善した。* [[code](https://github.com/aiming-lab/WebXSkill)]
- **[Beyond Sequential Interaction: Benchmarking Parallel Execution and Coordination for GUI Agents](https://arxiv.org/abs/2607.22689)** (Yu et al., arXiv 2026) - *並列GUIエージェントのための初のベンチマーク。Long-horizonなデスクトップタスクを、別々のマシン上で同時に動くワーカーに分けると、最良の逐次baselineを 12.9 ポイント上回り、ステップ数とトークン数はおよそ半分で済む。* [[code](https://github.com/pkgunboat/ParaGUIBench)]
- **[OpenForgeRL: Train Harness-native Agents in Any Environment](https://arxiv.org/abs/2607.21557)** (Yu et al., arXiv 2026) - *エージェントを、実際に導入される推論用のharness（Claude Code、Codex、OpenClaw）の中でend-to-endに学習させ、harnessによっては他よりはるかに学習しにくいものがあることを見いだした。*
- **[StateAct: Program State, before Pixels, for Long-Horizon Computer-Use Agents](https://arxiv.org/abs/2607.22798)** (Yang et al., arXiv 2026) - *Computer useエージェントをスクリーンショットではなくプログラムの状態にgroundingさせると、OSWorld 2.0でClaude Opus 4.8の成績が 20.6% から 26.9% に上がり、タスクあたりのコストは約九分の一になる。*
- **[StepReflect: Structured UI Transition Reflection for Mobile GUI Agents](https://arxiv.org/abs/2608.05587)** (Guo et al., arXiv 2026) - *ステップごとのGUIのreflectionを、自由形式のmultimodalな推論ではなく、明示的な遷移仕様にもとづく構造化予測として扱う。8B のモデルがAndroidWorldで遷移の正解率 82.16% に達し、同じ入力を与えたzero-shotのGPT-5.2を 11.83 ポイント上回った。*
- **[ComponentBench: Diagnosing Component-Level Failures in Computer-Use Agents](https://arxiv.org/abs/2608.18307)** (Guan et al., arXiv 2026) - *97 種類の標準的なUIコンポーネントからなるオントロジーの上に、プログラムで検証できる 2,910 件のタスクを用意し、computer useエージェントをコンポーネント単位で評価する。共通のharnessひとつのなかで観測とaction spaceだけを変えても、同じモデルのタスク成功率が 30% 以上動き、GPT-5 miniはaccessibility treeの観測では 83.1% だったのが、座標だけのピクセル操作では 48.9% に落ちる。* [[code](https://github.com/TianchenGuan/ComponentBench)]
- **[Neurosymbolic Embodied Agents](https://arxiv.org/abs/2608.16794)** (Albinhassan et al., arXiv 2026) - *家事タスクを、タスクに向けた視覚的探索と、Monte Carlo tree searchを伴うPDDL制約付きデコーディングに分解する。これにより 4B から 27B のオープンモデルがVirtualHomeとALFWorldの両方で成功率 90% を超える。ALFWorldでは制約か探索の一方だけだと解けるタスクは三分の一未満だが、両者を組み合わせると 95% を超える。残る失敗は計画の生成ではなく状態の取得に集中している。*
- **[CUA-Universe: A Scalable and Dynamic Environment for Hybrid GUI+CLI Agents](https://arxiv.org/abs/2609.05374)** (Shi et al., arXiv 2026) - *同じアプリケーションの状態に、画面とコマンドラインのどちらからでも到達できる環境を構築する。実在する 16 のデスクトップアプリケーションを、発見、ラップ、生成のいずれかで得たコマンドの窓口を備えた再現可能な仮想マシンに作り替え、そこで集めたtrajectoryで学習すると、9B のモデルは非効率なクリックや壊れやすいスクリプトから、安く済むほうのインターフェースを使う方向へ変わる。OSWorldで成功率が 16.8 ポイント上がり、ステップは 57%、トークンは 44% 減った。*
- **[Discriminative World Models for Web Agents](https://arxiv.org/abs/2609.02885)** (Li et al., arXiv 2026) - *教師ありの次状態予測で学習した世界モデルは、rankerがそれを使う段になると、間違ったものを最適化していると論じる。ランキングに必要なのは、もっともらしく見えるだけの状態ではなく、候補となる行動どうしを区別できる予測状態だからである。そこで代わりに、分岐するWebArenaのtrajectoryの上で予測状態のマッチングを学習する。各決定点には、代わりの行動と、それぞれが生み出す状態が並べて付いている。*
- **[Routing Is Least Learnable Where It Is Most Valuable: Bounds on Representation Routing for Web Agents](https://arxiv.org/abs/2608.06171)** (Wei et al., arXiv 2026) - *Webエージェントの六つの観測モードを切り替える五つのルーティング方針（confidenceによるcascadeを含む）のどれも、うまく選んだ固定モード一つに頑健には勝てない。Routerがラベルを得られるのはエージェントが成功したときだけだからである。同じモードを再実行するだけでも、結果の 12% から 14% が変わる。*
</details>

<sub><a href="#contents">↑ 目次に戻る</a></sub>

<a id="applications"></a>
### 🚀 応用分野 (54)
*サーベイの§10（応用分野）に対応します。*

<details>
<summary><b>54本の論文を表示</b></summary>

- **[AutoCodeRover: Autonomous Program Improvement](https://arxiv.org/abs/2404.05427)** (Zhang et al., arXiv 2024) - *構造化されたコード検索に基づく、低コストな自律型プログラム修復エージェントの最初期の一つ。* [[code](https://github.com/nus-apr/auto-code-rover)]
- **[Agentless: Demystifying LLM-based Software Engineering Agents](https://arxiv.org/abs/2407.01489)** (Xia et al., arXiv 2024) - *エージェントを使わない単純なパイプラインでも複雑なエージェントに匹敵しうることを示した、主流の見方に対する影響力のある反論。* [[code](https://github.com/OpenAutoCoder/Agentless)]
- **[OpenHands: An Open Platform for AI Software Developers as Generalist Agents](https://arxiv.org/abs/2407.16741)** (Wang et al., ICLR 2025) - *その後の応用的なコーディングエージェント研究の多くが土台とする、代表的なオープンコミュニティプラットフォーム。* [[code](https://github.com/OpenHands/OpenHands)]
- **[Large Language Model-Based Agents for Software Engineering: A Survey](https://arxiv.org/abs/2409.02977)** (Liu et al., arXiv 2024) - *コーディング／SWEエージェントの研究を位置づけるのに必要な分類体系を与える、この分野専門のサーベイ。* [[code](https://github.com/FudanSELab/Agent4SE-Paper-List)]
- **[Autonomous chemical research with large language models](https://www.nature.com/articles/s41586-023-06792-0)** (Boiko et al., Nature 2023) - *LLMエージェントが物理世界で自律的に科学実験を行えることを示した、最初期かつ最もよく引用される事例の一つ。* [[code](https://github.com/gomesgroup/coscientist)]
- **[ChemCrow: Augmenting large-language models with chemistry tools](https://arxiv.org/abs/2304.05376)** (Bran et al., Nature 2023) - *化学分野でツールを組み込んだLLMエージェントの基礎となる論文。* [[code](https://github.com/ur-whitelab/chemcrow-public)]
- **[The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery](https://arxiv.org/abs/2408.06292)** (Lu et al., arXiv 2024) - *科学論文のライフサイクル全体を完全に自動化しようとした、広く知られる象徴的な試み。* [[code](https://github.com/SakanaAI/AI-Scientist)]
- **[The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search](https://arxiv.org/abs/2504.08066)** (Yamada et al., arXiv 2025) - *自律的に科学的発見を行うエージェントにとって、具体的で検証可能な節目となる成果。* [[code](https://github.com/SakanaAI/AI-Scientist-v2)]
- **[Towards an AI co-scientist](https://arxiv.org/abs/2502.18864)** (Gottweis et al., arXiv 2025) - *科学の仮説生成を担う、産業界（Google）の主要な応用エージェントシステム。*
- **[AlphaEvolve: A coding agent for scientific and algorithmic discovery](https://arxiv.org/abs/2506.13131)** (Novikov et al., arXiv 2025) - *LLMエージェントが検証可能な数学／アルゴリズム上の新発見を本当に成し遂げたことを示す、節目となる実証。*
- **[Kosmos: An AI Scientist for Autonomous Discovery](https://arxiv.org/abs/2511.02824)** (Mitchener et al., arXiv 2025) - *現時点で最も高性能で、最も厳密に評価された「AI scientist」エージェントの一つ。*
- **[ScienceAgentBench: Toward Rigorous Assessment of Language Agents for Data-Driven Scientific Discovery](https://arxiv.org/abs/2410.05080)** (Chen et al., ICLR 2025) - *現在のLLMエージェントと、end-to-endな科学的発見の自動化とのあいだの差を定量化する、専門家が検証した厳密なベンチマーク。* [[code](https://github.com/OSU-NLP-Group/ScienceAgentBench)]
- **[Towards Scientific Intelligence: A Survey of LLM-based Scientific Agents](https://arxiv.org/abs/2503.24047)** (Ren et al., arXiv 2025) - *科学的発見エージェントの文献を整理する土台となる、この分野専門のサーベイ。*
- **[A Survey of LLM-based Agents in Medicine: How far are we from Baymax?](https://arxiv.org/abs/2502.11211)** (Wang et al., ACL 2025) - *医療分野のLLMエージェントを扱う、中心的な専門サーベイ。*
- **[MDAgents: An Adaptive Collaboration of LLMs for Medical Decision-Making](https://arxiv.org/abs/2404.15155)** (Kim et al., NeurIPS 2024) - *医療推論の複雑さに合わせてマルチエージェントのorchestrationを適応的に変える、広く引用されている例。* [[code](https://github.com/mitmedialab/MDAgents)]
- **[Agent Hospital: A Simulacrum of Hospital with Evolvable Medical Agents](https://arxiv.org/abs/2405.02957)** (Li et al., arXiv 2024) - *エージェント同士のシミュレーションを通じて医療の専門知識を身につける、独自の応用エージェントのパラダイム。*
- **[Towards Conversational Diagnostic AI](https://arxiv.org/abs/2401.05654)** (Tu et al., arXiv 2024) - *模擬診断対話でLLMエージェントが医師に匹敵するか上回ることを示した、厳密に評価されたGoogleの象徴的なシステム。*
- **[Large Language Model Agent in Financial Trading: A Survey](https://arxiv.org/abs/2408.06361)** (Ding et al., arXiv 2024) - *応用LLMエージェントのうち、金融分野の研究の足場として欠かせない専門のサーベイ。*
- **[FinMem: A Performance-Enhanced LLM Trading Agent with Layered Memory and Character Design](https://arxiv.org/abs/2311.13743)** (Yu et al., AAAI 2023) - *早い時期のLLMトレーディングエージェントで、人間の認知に着想を得た階層型のメモリ設計を導入し、広く参照されている。* [[code](https://github.com/pipiku915/FinMem-LLM-StockTrading)]
- **[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://arxiv.org/abs/2412.20138)** (Xiao et al., arXiv 2024) - *複数の役割を分担するマルチエージェント構成の、最近人気の金融システム。参照アーキテクチャとして広く使われている。* [[code](https://github.com/TauricResearch/TradingAgents)]
- **[FinGPT: Open-Source Financial Large Language Models](https://arxiv.org/abs/2306.06031)** (Yang et al., IJCAI 2023) - *最もよく引用されるオープンソースの金融LLM／エージェントの取り組みの一つで、多くの下流の金融エージェントシステムを支えるベースモデル基盤を提供する。* [[code](https://github.com/AI4Finance-Foundation/FinGPT)]
- **[SWE-Lancer: Can Frontier LLMs Earn $1 Million from Real-World Freelance Software Engineering?](https://arxiv.org/abs/2502.12115)** (Miserendino et al., arXiv 2025) - *コーディングエージェントの能力を、実際のフリーランス案件の報酬額（ドル）で測る。フロンティアモデルは、提示された報酬の大半を獲得できない。* [[code](https://github.com/openai/SWELancer-Benchmark)]
- **[AgentClinic: A Multimodal Agent Benchmark to Evaluate AI in Simulated Clinical Environments](https://arxiv.org/abs/2405.07960)** (Schmidgall et al., arXiv 2024) - *医師と患者のエージェント間のやり取りを対象に、臨床現場を模擬したmultimodalなベンチマーク。*
- **[OptimAI: Optimization from Natural Language Using LLM-Powered AI Agents](https://arxiv.org/abs/2504.16918)** (Thind et al., arXiv 2025) - *自然言語で書かれた最適化問題を、formulator、planner、coder、criticからなるパイプラインで実行可能なソルバーのコードに変換する。計画の選択にはUCBを使う。*

- **[AutoSci: A Memory-Centric Agentic System for the Full Scientific Research Lifecycle](https://arxiv.org/abs/2605.31468)** (Qian et al., arXiv 2026) - *メモリを中心に据えたエージェントシステムで、科学研究のループ全体を自動化する。* [[code](https://github.com/skyllwt/AutoSci)]
- **[SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents](https://arxiv.org/abs/2601.16746)** (Wang et al., arXiv 2026) - *長いリポジトリのコンテキストでもコーディングエージェントの効果を保つ、自己適応型のコンテキスト刈り込み。* [[code](https://github.com/Ayanami1314/swe-pruner)]
- **[LiteResearcher: A Scalable Agentic RL Training Framework for Deep Research Agent](https://arxiv.org/abs/2604.17931)** (Li et al., arXiv 2026) - *Deep researchエージェントのための、スケーラブルなagentic RL学習フレームワーク。* [[code](https://github.com/simplex-ai-inc/LiteResearcher)]
- **[LawThinker: A Deep Research Legal Agent in Dynamic Environments](https://arxiv.org/abs/2602.12056)** (Yang et al., arXiv 2026) - *動的な法務環境で動作する、deep researchの法務エージェント。* [[code](https://github.com/RUC-NLPIR/LawThinker-agent)]
- **[Agentic Trading: When LLM Agents Meet Financial Markets](https://arxiv.org/abs/2605.19337)** (Xia et al., arXiv 2026) - *金融市場で行動するLLMエージェントと、それが生み出す取引のダイナミクスを調べる。*
- **[Rethinking Scientific Discovery in the Agentic Era](https://arxiv.org/abs/2607.03863)** (Zheng et al., arXiv 2026) - *科学的発見をエージェントが担うようになったとき、何が変わり、何が変わらないのかを論じるポジションペーパー。*
- **[Deep Research in Physical Sciences: A Multi-Agent Framework and Comprehensive Benchmark](https://arxiv.org/abs/2606.18648)** (Jiang et al., arXiv 2026) - *物理科学を対象とした、マルチエージェントのdeep researchフレームワークとベンチマーク。* [[code](https://github.com/yigengjiang/physci-deepresearch)]
- **[HealthAgentBench: A Unified Benchmark Suite of Realistic Agentic Healthcare Environments for Challenging Frontier AI Agents](https://arxiv.org/abs/2606.31179)** (Liu et al., arXiv 2026) - *静的な臨床質問応答ではなく、エージェントが動く現実的な医療環境を集めたベンチマーク群。* [[code](https://github.com/microsoft/HealthAgentBench)]
- **[EvoDS: Self-Evolving Autonomous Data Science Agent with Skill Learning and Context Management](https://arxiv.org/abs/2606.03841)** (Yang et al., arXiv 2026) - *Skill学習とコンテキスト管理を組み合わせた、自己進化するデータサイエンスエージェント。* [[code](https://github.com/usail-hkust/EvoDS)]
- **[MetaResearcher: Scaling Deep Research via Self-Reflective Reinforcement Learning in Adversarial Virtual Environments](https://arxiv.org/abs/2606.19893)** (Yu et al., arXiv 2026) - *敵対的な条件のもとで、self-reflectionを取り入れた強化学習によってdeep researchのループを学習する。*
- **[Can Deep Research Agents Retrieve and Organize? Evaluating the Synthesis Gap with Expert Taxonomies](https://arxiv.org/abs/2601.12369)** (Zhang et al., arXiv 2026) - *Deep researchエージェントの統合のギャップを評価する。証拠を検索するだけでなく、検索した証拠を整理できるかを、専門家が作った参照と照らし合わせて測る。* [[code](https://github.com/KongLongGeFDU/TaxoBench)]
- **[ClinicalAgents: Multi-Agent Orchestration for Clinical Decision Making with Dual-Memory](https://arxiv.org/abs/2603.26182)** (Ge et al., arXiv 2026) - *二重のメモリ設計を備えた、臨床での意思決定のためのマルチエージェントorchestration。* [[code](https://github.com/ZhuohanGe/ClinicalAgents-Code)]
- **[SciResearcher: Scaling Deep Research Agents for Frontier Scientific Reasoning](https://arxiv.org/abs/2605.01489)** (Zheng et al., arXiv 2026) - *Deep researchエージェントを、最先端の科学的推論タスクに向けてスケールさせる。*
- **[Physics-Audited Agentic Discovery in Scientific Machine Learning](https://arxiv.org/abs/2607.07379)** (Abueidda et al., arXiv 2026) - *エージェントが見つけた代理モデルを、誤差だけに頼らず、機械的に検査できる物理的要件で選ぶ。これにより、誤差が同等のbaselineが荷重履歴の未来の部分に反応し、因果性のチェックに落ちる事例を見つけた。*
- **[LLMoxie: Exploring Agentic AI for Scientific Software Development](https://arxiv.org/abs/2607.02703)** (Setiawan et al., arXiv 2026) - *LiteLLM/MLflowによるガバナンスのコントロールプレーンと、オープンソースのPlugin-Agent-Skillエコシステムを備えた組織向け三層構成のagentic AIプラットフォーム、LLMoxieを二十か月にわたって運用した経験を報告する。*
- **[Agon: An Autonomous Large-Scale Omnidisciplinary Research System Built on Prompt Economy](https://arxiv.org/abs/2606.24177)** (Sun et al., arXiv 2026) - *Workflowの中で確かめられることは自ら検証し、残りは人間の科学者に任せる研究用のorchestrator。人間が書いた実験コードなしで複数の分野にわたりループを 444 回まわし、ループが直せる失敗と直せない失敗を分ける失敗の分類体系も示した。* [[code](https://github.com/AutoResearch-Factory/Agon)]
- **[Hybrid-Gym: Training Coding Agents to Generalize Across Tasks](https://arxiv.org/abs/2602.16819)** (Xie et al., arXiv 2026) - *関数の位置特定や依存関係の探索といった合成の補助タスクでコーディングエージェントを学習させる。これらは実際の作業にも転移し、SWE-Bench Verifiedで +25.4%、SWT-Bench Verifiedで +7.9%、Commit-0 Liteで +5.1% の改善を得た。* [[code](https://github.com/yiqingxyq/Hybrid-Gym)]
- **[Toward Expert Investment Teams: A Multi-Agent LLM System with Fine-Grained Trading Tasks](https://arxiv.org/abs/2602.23330)** (Miyazaki et al., arXiv 2026) - *投資分析を細かな取引サブタスクに分解するマルチエージェントLLMフレームワークを提案する。日本株のデータで評価し、抽象的な指示だけを与えるbaselineよりリスク調整後リターンを改善した。*
- **[MiroEval: Benchmarking Multimodal Deep Research Agents in Process and Outcome](https://arxiv.org/abs/2603.28407)** (Ye et al., arXiv 2026) - *MiroEvalは 100 タスク（テキストのみ 70、multimodal 30）からなるベンチマークで、deep researchエージェントを統合の質、事実性、研究プロセスの観点から評価する。* [[code](https://github.com/MiroMindAI/MiroEval)]
- **[HeartAgent: An Autonomous Agent System for Explainable Differential Diagnosis in Cardiology](https://arxiv.org/abs/2603.10764)** (Zhou et al., arXiv 2026) - *HeartAgentは、独自に用意したツールと厳選したデータ資源を統合し、専門のサブエージェントを束ねて循環器領域の説明可能な鑑別診断を行う、自律型のマルチエージェントシステムである。*
- **[AutoNumerics: An Autonomous, PDE-Agnostic Multi-Agent Pipeline for Scientific Computing](https://arxiv.org/abs/2602.17607)** (Du et al., arXiv 2026) - *自然言語の問題文から古典的な数値PDEソルバーを直接組み立て、残差で検証する。ソルバーはニューラルネットにせず、中身の見える形のまま保つ。* [[code](https://github.com/Daviddjddu/Autonumerics)]
- **[Stress-testing large language model agents in a robotic chemistry laboratory](https://arxiv.org/abs/2607.23045)** (Guo et al., arXiv 2026) - *45 台のワークステーションを備えたロボット化学実験室で 4,608 回の試行を行った。専門家が実行可能と判断したエージェントのworkflowはわずか 3.3%、最良のシステムでも 28.1% にとどまり、フィードバックが再計画につながることは一度もなかった。*
- **[PatientAgentBench: A Benchmark Framework for Evaluating Patient-Facing Health AI Agents](https://arxiv.org/abs/2607.25485)** (Vatanparvar et al., arXiv 2026) - *患者と直接やり取りする医療エージェントを、ツールを使う 1,200 件の会話で評価する。モデルの差が最も大きく出るのはトリアージで（合格率 32% から 88%）、最も強いモデルでも総合で 5 点中 4.25 点にとどまる。* [[code](https://github.com/amazon-science/PatientAgentBench)]
- **[Agentic Evaluation of Copyright Law Compliance](https://arxiv.org/abs/2607.21799)** (Hui et al., arXiv 2026) - *Copyright-Benchはエージェントに商用の仕事（Webサイト、グッズ、ピッチ資料）を任せ、パブリックドメインの代替があっても著作物を選んでしまうことを示した。Open-weightモデルの違反率は、模擬的な時間的プレッシャーの下で上がる。*
- **[From Social Coding to Agentic Coding: Productivity and Relational Reconfiguration in Open-Source Communities](https://arxiv.org/abs/2608.03585)** (Zhou et al., arXiv 2026) - *実在するGitHub開発者 1,084 人のコミュニティを、コーディングエージェントの有無でシミュレーションする。完了タスクは 39.0% 増え、完了時間の中央値は 45 分から 20 分に縮んだ。一方で人と人の直接のやり取りは 32.4% から 11.6% に減り、恩恵はもともとつながりの多い人に集中した。*
- **[Vero: Can AI Agents Build Formally Verified Software Repositories?](https://arxiv.org/abs/2608.13522)** (Ye et al., arXiv 2026) - *Python、Dafny、Verus、Coqにまたがる実際のリポジトリから取った 43 個の複数モジュールのインスタンスで、リポジトリ単位の実装と、機械検証される証明の合成を同時に評価する。最も強いフロンティアのコーディングエージェント構成でも完全に解けたのは 43 個中 27 個だけで、最も難しいリポジトリでは仕様を一つも証明しきれなかった。* [[code](https://github.com/sunblaze-ucb/vero)]
- **[Auditing Self-Evolution in Financial Agents: Capability Gains, Security Drift, and Execution-Interface Mismatch](https://arxiv.org/abs/2608.17684)** (Li et al., arXiv 2026) - *自己進化する三つのエージェント設計（SkillOpt、Agent Workflow Memory、ReasoningBank）を模擬オンラインバンキングで監査し、能力と攻撃への露出がそろって高まることを示した。SkillOptは通常タスクの有用性を 0.741 から 0.837 に上げる一方、注入されたコンテンツへの露出は 0.820 から 0.943 に、全体の攻撃成功率は 0.496 から 0.530 に上がり、無許可の金融上の状態変更は 0.685 に達した。*
- **[SWE-Gate: Passing Functional Tests Is Not Enough for Software Engineering Agents](https://arxiv.org/abs/2609.04167)** (He et al., arXiv 2026) - *実際のpull requestのレビューコメントからレビュー上の制約を抽出し、75 のPythonプロジェクトにまたがる 303 のリポジトリ単位のインスタンスで、機能的な正しさとは別に採点する。機能テストを通った 644 件のパッチのうち 221 件は、レビュアーが示した制約をなお破っていた。機能だけで採点すると、エージェントが実際に届けたものを過大評価することになる。* [[code](https://github.com/DeepSoftwareAnalytics/SWE-Gate)]
- **[Why Better Models Can Create Riskier Systems: Evidence from LLM Agents in Financial Markets](https://arxiv.org/abs/2609.04373)** (Ross et al., arXiv 2026) - *学習とアーキテクチャが共通しているため、能力の高いモデルほど振る舞いが似通い、その相関した行動がどれだけ分散させても消えないリスクの下限を残す、と主張する。これをエージェントベースの市場でLLMトレーダーを使って検証した。能力が上がるほど相関は強まり、共有された推論が正確なうちはエージェントを増やすと市場全体のリスクが下がるが、エージェントが同じ誤情報の環境を共有したとたん、同じ相関が弱点に変わる。*
- **[Training Agents to Evolve with Their Harness: TaoLive Digital Avatar Agent Technical Report](https://arxiv.org/abs/2608.15763)** (TaoLive AIGC LLM Team, arXiv 2026) - *大きなモデルは編集されたSkill、hook、プロンプト、ツールのスキーマに再学習なしで適応できるが、ライブ配信が課すレイテンシの予算には収まらない。そこで、変わり続けるharnessに合わせて小さなモデルを学習させるべきだという立場を取り、学習中にharnessの状態を拡張して、モデルが固定の構成を一度も見ないようにする。Harnessを変えた質問では、ベースモデルの 75.4 に対して 94.6 を記録した。Harnessを固定した教師ありファインチューニングはベースモデル比でIFEvalを 7.7 ポイント落とすが、拡張したレシピではまったく落ちない。H20一枚でのレイテンシはP50で 3.4 秒、P95で 8.1 秒で、Taobao LiveでのA/Bテストでも良い結果が出た。*
</details>

<sub><a href="#contents">↑ 目次に戻る</a></sub>

## ⚖️ 第3部：横断的な課題

<a id="evaluation"></a>
### 📊 評価とベンチマーク (50)
*サーベイの§9（評価とベンチマーク）に対応します。*

<details>
<summary><b>50本の論文を表示</b></summary>

- **[GAIA: a benchmark for General AI Assistants](https://arxiv.org/abs/2311.12983)** (Mialon et al., ICLR 2024) - *ツールを使う汎用エージェントアシスタントの基準となるベンチマーク。フロンティアエージェントの進歩を追う、人気の公開リーダーボードの土台になっている。*
- **[SWE-bench: Can Language Models Resolve Real-World GitHub Issues?](https://arxiv.org/abs/2310.06770)** (Jimenez et al., ICLR 2024) - *コーディング／ソフトウェア工学エージェントの事実上の標準ベンチマーク。SWE-bench Verified/Lite/Live/Multimodalといった派生版を生んだ。* [[code](https://github.com/SWE-bench/SWE-bench)]
- **[MLAgentBench: Evaluating Language Agents on Machine Learning Experimentation](https://arxiv.org/abs/2310.03302)** (Huang et al., arXiv 2023) - *「AI研究エージェント」「ML工学エージェント」を評価する分野の先駆けとなったベンチマークで、MLE-benchやRE-Benchなどの前身にあたる。* [[code](https://github.com/snap-stanford/MLAgentBench)]
- **[τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains](https://arxiv.org/abs/2406.12045)** (Yao et al., arXiv 2024) - *エージェントとユーザーのやり取りと、ポリシーの遵守を評価する道を開いた。企業向け／カスタマーサービス向けエージェントの評価で標準的に参照される。* [[code](https://github.com/sierra-research/tau-bench)]
- **[AgentBoard: An Analytical Evaluation Board of Multi-turn LLM Agents](https://arxiv.org/abs/2401.13178)** (Ma et al., NeurIPS 2024) - *成功／失敗だけの粗い採点では見えない部分を補う、広く使われている統一評価ツールキット。評価方法論の枠組みを考えるうえで直接関係する。* [[code](https://github.com/hkust-nlp/AgentBoard)]
- **[SmartPlay: A Benchmark for LLMs as Intelligent Agents](https://arxiv.org/abs/2310.01557)** (Wu et al., ICLR 2024) - *能力を要素に分けて評価する方法論で、のちの細粒度なエージェント能力ベンチマークに影響を与えた。* [[code](https://github.com/microsoft/SmartPlay)]
- **[TravelPlanner: A Benchmark for Real-World Planning with Language Agents](https://arxiv.org/abs/2402.01622)** (Xie et al., ICML 2024) - *制約の多い複雑なマルチツール計画を試す、広く引用されているストレステスト。信頼できるlong-horizonな計画からエージェントがまだ遠いことを示す。* [[code](https://github.com/OSU-NLP-Group/TravelPlanner)]
- **[InterCode: Standardizing and Benchmarking Interactive Coding with Execution Feedback](https://arxiv.org/abs/2306.14898)** (Yang et al., NeurIPS 2023) - *実行フィードバックを使う対話的な評価のパラダイムを確立し、のちのコーディングエージェントやターミナルエージェントのベンチマークの基礎となった。* [[code](https://intercode-benchmark.github.io)]
- **[GTA: A Benchmark for General Tool Agents](https://arxiv.org/abs/2407.08713)** (Wang et al., NeurIPS 2024) - *以前の合成的なツール利用ベンチマークに欠けていた現実味（暗黙の意図、本物のmultimodalなコンテキスト）を補う。* [[code](https://github.com/open-compass/GTA)]
- **[Survey on Evaluation of LLM-based Agents](https://arxiv.org/abs/2503.16416)** (Yehudai et al., arXiv 2025) - *まさにこのテーマを扱うサーベイで、新しくエージェントのサーベイを書く際の評価の章にそのまま使える分類体系を示す。*
- **[Evaluation and Benchmarking of LLM Agents: A Survey](https://arxiv.org/abs/2507.21504)** (Mohammadi et al., KDD 2025) - *Yehudai et al.とは独立に作られたこの分野のサーベイで、それを補完する。分類体系の網羅性を突き合わせるのに役立つ。*
- **[τ²-Bench: Evaluating Conversational Agents in a Dual-Control Environment](https://arxiv.org/abs/2506.07982)** (Barres et al., arXiv 2025) - *τ-benchを、ユーザーとエージェントの両方が環境に働きかける設定に拡張する。* [[code](https://github.com/sierra-research/tau2-bench)]
- **[Agent-as-a-Judge: Evaluate Agents with Agents](https://arxiv.org/abs/2410.10934)** (Zhuge et al., arXiv 2024) - *エージェントによるエージェントの評価を体系化する。評価者の循環性という懸念を論じるときの参照点である。* [[code](https://github.com/metauto-ai/agent-as-a-judge)]
- **[Holistic Agent Leaderboard: The Missing Infrastructure for AI Agent Evaluation](https://arxiv.org/abs/2510.11977)** (Kapoor et al., arXiv 2025) - *エージェントを大規模に評価し直す標準化されたharnessで、精度と並べてコストも報告する。*
- **[Dr. Bench: A Multidimensional Evaluation for Deep Research Agents, from Answers to Reports](https://arxiv.org/abs/2510.02190)** (Yao et al., arXiv 2025) - *Deep researchエージェントを、回答からレポートまで、意味的な質、話題の焦点、検索の信頼性の観点で評価する。* [[code](https://github.com/EVIGBYEN/DrBench)]
- **[Terminal-Bench: Benchmarking Agents on Hard, Realistic Tasks in Command Line Interfaces](https://arxiv.org/abs/2601.11868)** (Merrill et al., arXiv 2026) - *難しく現実的なコマンドラインのタスク集。ターミナルエージェントの事実上の標準である。* [[code](https://github.com/laude-institute/terminal-bench)]

- **[Can AI Agents Answer Your Data Questions? A Benchmark for Data Agents (DataAgentBench)](https://arxiv.org/abs/2603.20576)** (Ma et al., arXiv 2026) - *種類の異なるデータベースシステムにまたがるベンチマーク。複雑なデータの質問に対し、フロンティアモデルでも正解率は 38% にとどまる。* [[code](https://github.com/ucbepic/DataAgentBench)]
- **[AgencyBench: Benchmarking the Frontiers of Autonomous Agents in 1M-Token Real-World Contexts](https://arxiv.org/abs/2601.11044)** (Li et al., arXiv 2026) - *最大 1M トークンのコンテキストで自律エージェントを試す、現実世界の 32 のlong-horizonなシナリオ。* [[code](https://github.com/GAIR-NLP/AgencyBench)]
- **[Agent-Diff: Benchmarking LLM Agents on Enterprise API Tasks via Code Execution with State-Diff-Based Evaluation](https://arxiv.org/abs/2602.11224)** (Pysklo et al., arXiv 2026) - *Sandbox内のコード実行を通じて、企業向けAPIのタスクでエージェントを評価する。成功の基準はtraceの一致ではなく、状態の差分である。* [[code](https://github.com/agent-diff-bench/agent-diff)]
- **[When Tools Fail: Benchmarking Dynamic Replanning and Anomaly Recovery in LLM Agents (ToolMaze)](https://arxiv.org/abs/2606.05806)** (Zhu et al., arXiv 2026) - *DAGに基づくベンチマークで、摂動の分類体系を使い、ツール呼び出しが失敗したときのエージェントの再計画と回復を試す。* [[code](https://github.com/Zhudongsheng75/ToolMaze)]
- **[Agent-ValueBench: A Comprehensive Benchmark for Evaluating Agent Values](https://arxiv.org/abs/2605.10365)** (Dong et al., arXiv 2026) - *エージェントの価値観を専門に扱う初のベンチマーク。28 の価値体系にわたり、実行可能な環境 394 個と、価値が衝突するタスク 4,335 件を含む。*
- **[How Many Tasks Are Enough for Agent Benchmark Decisions? A Replay Analysis of Public LLM Agent Benchmarks](https://arxiv.org/abs/2607.12338)** (Huang et al., arXiv 2026) - *ベンチマークの順位が信頼できるようになるまでに実際に何タスク必要かを、リプレイ分析で問う。* [[code](https://github.com/WilliamWJHuang/How-Many-Tasks-Are-Enough-for-Agent-Benchmark-Decisions)]
- **[Beyond Static Leaderboards: Predictive Validity for the Evaluation of LLM Agents](https://arxiv.org/abs/2606.19704)** (Patel et al., arXiv 2026) - *エージェントのリーダーボードが実運用について何かを語るには、スコアだけでなく予測的妥当性が必要だと主張する。*
- **[AgentGym2: Benchmarking Large Language Model Agents in De-Idealized Real-World Environments](https://arxiv.org/abs/2607.05174)** (Xi et al., arXiv 2026) - *理想化を取り除いた環境でエージェントを評価し、整ったベンチマークの世界と現実の世界との差を埋める。* [[code](https://github.com/hotdog-zz/Agentgym2)]
- **[Measuring Harness-Induced Belief Divergence in Multi-Step LLM Agents](https://arxiv.org/abs/2607.04528)** (Yi et al., arXiv 2026) - *Harnessだけでエージェントの信念がステップをまたいでどれだけずれるかを測り、エージェント評価に潜む交絡要因を切り分ける。* [[code](https://github.com/Hik289/Harness-induce-bias)]
- **[Rethinking the Evaluation of Harness Evolution for Agents](https://arxiv.org/abs/2607.12227)** (Wang et al., arXiv 2026) - *Harnessもモデルと同じくらい数値を動かすことを踏まえ、harnessの進化をどう評価すべきかを考え直す。* [[code](https://github.com/rethinking-harness-evolution/code)]
- **[ReliabilityBench: Evaluating LLM Agent Reliability Under Production-Like Stress Conditions](https://arxiv.org/abs/2601.06112)** (Gupta et al., arXiv 2026) - *一回きりのきれいな実行ではなく、本番に近いストレス条件でエージェントの信頼性を評価する。*
- **[AgentAtlas: Beyond Outcome Leaderboards for LLM Agents](https://arxiv.org/abs/2605.20530)** (Mazaheri et al., arXiv 2026) - *エージェント評価を結果だけのリーダーボードから一歩進め、制御がどこで崩れるかを判断ごとに診断する方向へ移す。*
- **[CUBE: A Standard for Unifying Agent Benchmarks](https://arxiv.org/abs/2603.15798)** (Lacoste et al., arXiv 2026) - *ばらばらなエージェントベンチマークを一つのインターフェースにまとめる標準を提案する。* [[code](https://github.com/The-AI-Alliance/cube-standard)]
- **[UniClawBench: A Universal Benchmark for Proactive Agents on Real-World Tasks](https://arxiv.org/abs/2607.08768)** (Chen et al., arXiv 2026) - *実際に動くDocker環境で実行する 400 タスクからなる、能力を軸に設計した二言語のベンチマークUniClawBenchを提案する。ステップごとのチェックポイントを備え、skillの利用、探索、長いコンテキストでの推論、multimodalな理解、プラットフォームをまたいだ連携にわたって、能動的なLLMエージェントを評価する。隠れた監督役のエージェントを置くことで、複数ターンのフィードバックから採点基準が漏れないようにしている。* [[code](https://github.com/HKU-MMLab/UniClawBench)]
- **[PolyWorkBench: Benchmarking LLM Agents for Cross-Lingual Long-Horizon Workflows](https://arxiv.org/abs/2607.06008)** (Li et al., arXiv 2026) - *商取引、知識労働、法務分析、ローカライズ、製造にまたがる 67 タスクのベンチマークPolyWorkBenchを提案する。多言語でlong-horizonな職場のworkflowについて、rubricにもとづく構造の採点、実行可能な状態チェック、LLM評価者を組み合わせたハイブリッドな方式でLLMエージェントを評価する。性能は言語ごとに大きくばらつき、難度の高い言語横断タスクでは急激に下がる。*
- **[EvoAgentBench: Benchmarking Agent Self-Evolution via Ability Transfer](https://arxiv.org/abs/2607.05202)** (Gao et al., arXiv 2026) - *LLMエージェントの自己進化を手続き的知識の転移として評価するベンチマークを提案する。エージェントの実行からトレースに裏づけられた「Ability」を抽出し、Webリサーチ、アルゴリズム的推論、ソフトウェアエンジニアリング、知識労働にわたる領域別のAbility Graphに整理する。精選したAbilityはモデルファミリーをまたいで安定して転移するが、どの設定でも性能が上がる自動手法は一つもない。*
- **[Act As a Real Researcher: A Suite of Benchmarks Evaluating Frontier LLMs and Agentic Harnesses in Research Lifecycle](https://arxiv.org/abs/2606.07462)** (Wang et al., arXiv 2026) - *コンテナ化されたベンチマーク群AARRI-Benchを提案し、フロンティアLLMとエージェントのharnessが、研究のライフサイクル全体にわたって研究インターンの入門レベルのタスクをこなせるかを評価する。* [[code](https://github.com/AARR-bench/AARRI-bench)]
- **[ReplicatorBench: Benchmarking LLM Agents for Replicability in Social and Behavioral Sciences](https://arxiv.org/abs/2602.11354)** (Nguyen et al., arXiv 2026) - *再現できる主張とできない主張を人手で確かめて集めたベンチマークReplicatorBenchを提案する。社会科学・行動科学の研究をLLMエージェントが再現できるかを、データの取得、実験の設計と実行、結果の解釈にわたって評価する。エージェントは実験の設計と実行はうまくこなすが、再現に必要な新しいデータの取得には苦戦する。* [[code](https://github.com/CenterForOpenScience/llm-benchmarking)]
- **[Benchmark Test-Time Scaling of General LLM Agents](https://arxiv.org/abs/2602.18998)** (Li et al., arXiv 2026) - *検索、コーディング、推論、ツール利用にわたって汎用LLMエージェントを評価する統一ベンチマークGeneral AgentBenchを提案する。逐次的なtest-time scalingも並列的なものも性能の向上につながらず、その原因は、逐次ではコンテキストの上限、並列では検証のギャップにあることを示した。また、主要な十のエージェントは、領域特化の評価から汎用の設定に移すと性能が大きく落ちる。* [[code](https://github.com/cxcscmu/General-AgentBench)]
- **[BenchGuard: Who Guards the Benchmarks? Automated Auditing of LLM Agent Benchmarks](https://arxiv.org/abs/2604.24955)** (Tu et al., arXiv 2026) - *フロンティアモデルをベンチマークそのものの点検に向ける。ScienceAgentBenchでは、タスクを解けなくしていた誤りを含め、著者が認めた問題を 12 件見つけた。BIXBenchでは専門家が指摘した問題の 83.3% と一致し、費用は 50 タスクの監査あたり 15 米ドル未満だった。*
- **[Automated Benchmark Auditing for AI Agents and Large Language Models](https://arxiv.org/abs/2605.26079)** (Wang et al., arXiv 2026) - *Agenticな監査フレームワークAuto Benchmark Audit（ABA）を提案する。九つの領域にわたる 168 のベンチマークを監査し、タスクの 25.7% 超に重大な問題（曖昧な設計、実行時の衝突、誤った正解データ）を見つけた。これらのタスクを除くとモデルの順位が入れ替わり、SWE-bench VerifiedとTerminal-Bench 2の平均スコアがそれぞれ 9.9% と 9.6% 上がる。*
- **[PerspectiveGap: A Benchmark for Multi-Agent Orchestration Prompting](https://arxiv.org/abs/2606.08878)** (Sun et al., arXiv 2026) - *Orchestration用のプロンプトを書く力を、独立した能力として切り出す。10 種類のトポロジーにわたる 110 のシナリオで、33 のモデルの平均合格率は 17.2% だった。* [[code](https://github.com/WhymustIhaveaname/PerspectiveGap)]
- **[ClawBench: Can AI Agents Complete Everyday Online Tasks?](https://arxiv.org/abs/2604.08523)** (Zhang et al., arXiv 2026) - *稼働中の本番サイト 144 か所にまたがる 153 の日常タスクにブラウザエージェントを取り組ませる。最後のリクエストは途中で止めるので、実際に購入や予約が行われることはない。試した中で最も強いモデルでも、クリアできたのは三分の一だった。* [[code](https://github.com/TIGER-AI-Lab/ClawBench)]
- **[Do Agent Benchmarks Measure Capability? Protocol Validity in the Age of Agentic AI](https://arxiv.org/abs/2607.22368)** (Shao et al., arXiv 2026) - *15 のエージェントベンチマークにわたる 2,385 件のtraceを監査し、Frontier ScienceとAutoLabのタスクの約三分の二で情報の露出やreward hackingを見つけた。これによりスコアは 0.45 から 1.00 水増しされていた。*
- **[The Hidden Footprint: Making Storage a First-Class Metric for LLM Agent Evaluation](https://arxiv.org/abs/2607.11149)** (Yu et al., arXiv 2026) - *精度が同じエージェント構成でも、ディスクに残すバイト数は 15.7 倍も違う。だから永続ストレージの使用量は、精度や再構成可能性と並べて報告すべきである。*
- **[OmegaUse-OfficeVal: Benchmarking LLM Agents on Long-Horizon Office-Suite Tasks with Economic Grounding](https://arxiv.org/abs/2607.27155)** (Zhou et al., arXiv 2026) - *Long-horizonなオフィスタスク 100 件に、それが置き換える人間の労働（平均 2.32 時間）で値段を付ける。フロンティアモデルは人よりはるかに安いが、成果物の質では大きく及ばない。* [[code](https://omegause-officeval.github.io)]
- **[AV-AIVAT: 74x Cheaper Agent Evaluation with Certified Anytime-Valid Stopping in Imperfect-Information Games](https://arxiv.org/abs/2608.06362)** (Li et al., arXiv 2026) - *分散削減と、常時監視するconfidence sequenceを組み合わせ、表明した信頼水準を損なわずに、証拠が固まった時点でエージェントの比較を打ち切れるようにする。ペアにしたポーカーのハンド 71,439 組で比べると、生の勝敗だけを使う場合は中央値で 74 倍のゲーム数が必要になる。*
- **[PATH-Bench: Path-Dependent Evaluation of Lifelong Agents](https://arxiv.org/abs/2608.01149)** (Yang et al., arXiv 2026) - *生涯学習エージェントをタスクごとではなく経験の順序に沿って評価し、前方転移、後方転移、忘却を測る。転移が強くても保持されるとは限らず、後の経験が以前の向上を打ち消しうることを示した。*
- **[Benchmarking LLM Judges for Mobile Agent Evaluation](https://arxiv.org/abs/2608.11434)** (Wang et al., arXiv 2026) - *人手で注釈を付けたモバイルエージェントのtrajectory 931 件に対して、六つのLLM-as-judge手法を試す。スクリーンショットをサンプリングするだけの単純なbaselineが専用の評価者と同等かそれ以上で、評価の質を決めるのはパイプラインではなくbackboneモデルだった。二つのバックエンドは、保守的な失敗と寛容な失敗という正反対の傾向を示した。*
- **[OmnilingualGAIA2: Evaluating the Multilingual Gap in Frontier AI Agents](https://arxiv.org/abs/2608.08775)** (Caciolai et al., arXiv 2026) - *GAIA2を五つの文字体系にまたがる十言語に広げると、pass@3で 8.8 から 18.4 ポイントの言語間の差が現れる。この差は定量的推論よりツールのorchestrationに集中し、モデルの規模を大きくしても縮まらない。誤りの原因を分析すると 55% はモデルに起因し、翻訳によるcontaminationはシナリオと言語の組の 6.4% までに収まる。*
- **[LoopArena: Benchmarking Models as Runtime Controllers for Loop Engineering](https://arxiv.org/abs/2608.28281)** (Wang et al., arXiv 2026) - *コードを書くモデルではなく、舵を取るモデルを採点する。各コーディングラウンドの後、評価対象のControllerは構造化された実行サマリーを読み、別に固定されたWorkerに、次に何をするか、何を検証するか、止めるかどうかを指示する。実行範囲とコストを引き換えにする三つの設定で評価し、完全なタスクでの厳密な成功率は最高でも 24.69% だった。Workerを一度も動かさない安価な設定でも、Controllerの順位は高価な設定とほぼ同じで、Spearman相関は 0.97 である。* [[code](https://github.com/AMAP-ML/LoopArena)]
- **[τ^τ-Bench: An Environment for End-To-End, Realistic Agent Construction](https://arxiv.org/abs/2609.04611)** (Shi et al., arXiv 2026) - *エージェントを作ること自体をタスクにする。開発者エージェントは、コードベース、本番のAPI、要件を握るクライアント、運用コストの上限を引き継ぎ、カスタマーサービスエージェントを出荷する。そのエージェントはheld-outの模擬ユーザーを相手にデプロイして採点される。53 タスクで最も強い構成でも評価シミュレーションの 23.9% しか通らず、専門家が書いた上限の 82.2% には遠い。失敗の仕方は人間にもよく見られるもので、記録を浅くしか調べず、クライアントにほとんど何も伝えず、最初に動いたアーキテクチャをそのまま出荷する。*
- **[Autonomous Evaluation and Refinement of Digital Agents](https://arxiv.org/abs/2404.06474)** (Pan et al., COLM 2024) - *コスト水準の異なる複数のエージェント評価器を作り、oracle指標との一致率は 74.4% から 92.9% だった。さらにそれらを報酬として使い、追加の教師データなしでWebArenaの最高性能を 29% 改善した。* [[code](https://github.com/Berkeley-NLP/Agent-Eval-Refine)]
- **[JEV-as-a-Judge: Accept When Confident, Escalate When Unsure](https://arxiv.org/abs/2609.26550)** (Li et al., arXiv 2026) - *テキストではなく決定を返す評価者は、通常の選好と事実性の判定で最強のLLM評価者に三ポイント差まで迫り、費用はその 0.36% で済む。一方、導出を確かめる必要がある場合や、誤った答えがうまく書かれている場合には差が広がる。Acceptかescalateかを選ぶcascadeにすると、強い評価者の精度の 99% を保てる。*
</details>

<sub><a href="#contents">↑ 目次に戻る</a></sub>

<a id="safety"></a>
### 🛡️ 安全性とアライメント (59)
*サーベイの§11（安全性・セキュリティ・信頼性）に対応します。*

<details>
<summary><b>59本の論文を表示</b></summary>

- **[Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection](https://arxiv.org/abs/2302.12173)** (Greshake et al., arXiv 2023) - *Indirect prompt injectionという脅威モデルを打ち立てた論文で、その後のLLMエージェントのセキュリティ研究のほぼすべてがこれを土台にしている。* ⭐ [[code](https://github.com/greshake/llm-security)]
- **[AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents](https://arxiv.org/abs/2406.13352)** (Debenedetti et al., NeurIPS 2024) - *Prompt injectionの攻撃と防御に対するエージェントの頑健性を測る、最も広く使われている標準的なテストベッド。* [[code](https://github.com/ethz-spylab/agentdojo)]
- **[InjecAgent: Benchmarking Indirect Prompt Injections in Tool-Integrated Large Language Model Agents](https://arxiv.org/abs/2403.02691)** (Zhan et al., ACL 2024) - *ツールを組み込んだエージェントがindirect prompt injectionにどれだけ弱いかを定量化する、標準的な参照ベンチマーク。* [[code](https://github.com/uiuc-kang-lab/InjecAgent)]
- **[WASP: Benchmarking Web Agent Security Against Prompt Injection Attacks](https://arxiv.org/abs/2504.18575)** (Evtimov et al., arXiv 2025) - *Prompt injectionの評価を、単一ステップのツール呼び出しから、複数ステップで自律的にWebを閲覧する現実的なエージェントへと広げる。* [[code](https://github.com/facebookresearch/wasp)]
- **[R-Judge: Benchmarking Safety Risk Awareness for LLM Agents](https://arxiv.org/abs/2401.10019)** (Yuan et al., EMNLP 2024) - *エージェントの安全性を監視する部品として、LLM自身のリスク認識／判断の能力を評価する、広く引用されているベンチマーク。* [[code](https://github.com/Lordog/R-Judge)]
- **[Identifying the Risks of LM Agents with an LM-Emulated Sandbox](https://arxiv.org/abs/2309.15817)** (Ruan et al., ICLR 2024) - *実際のツールにアクセスすることなく、ツールを使うエージェントのレッドチーミング／リスク発見を行う、基礎的でスケーラブルな方法論。* [[code](https://github.com/ryoungj/ToolEmu)]
- **[AgentHarm: A Benchmark for Measuring Harmfulness of LLM Agents](https://arxiv.org/abs/2410.09024)** (Andriushchenko et al., ICLR 2025) - *エージェントの悪用リスクをチャットボットのjailbreakリスクと区別する重要なベンチマークで、エージェントとしての能力が害を及ぼす可能性を増幅することを示す。* [[code](https://github.com/UKGovernmentBEIS/inspect_evals)]
- **[Evil Geniuses: Delving into the Safety of LLM-based Agents](https://arxiv.org/abs/2311.11855)** (Tian et al., arXiv 2023) - *マルチエージェントでのLLMの協調が、安全上のリスクを和らげるどころか増幅することを示した、最初期の体系的研究の一つ。* [[code](https://github.com/T1aNS1R/Evil-Geniuses)]
- **[BadAgent: Inserting and Activating Backdoor Attacks in LLM Agents](https://arxiv.org/abs/2406.03007)** (Wang et al., ACL 2024) - *エージェントのbackdoorが下流での安全性のためのファインチューニングを経ても残ることを示した先駆的な実証で、エージェントのサプライチェーンのセキュリティへの懸念を呼び起こした。* [[code](https://github.com/DPamK/BadAgent)]
- **[AgentPoison: Red-teaming LLM Agents via Poisoning Memory or Knowledge Bases](https://arxiv.org/abs/2407.12784)** (Chen et al., NeurIPS 2024) - *Memory poisoningや知識ベースへのポイズニングを、メモリで拡張されたLLMエージェントに固有の、学習を必要としない独立したattack surfaceとして確立した。* [[code](https://github.com/AI-secure/AgentPoison)]
- **[Agent Security Bench (ASB): Formalizing and Benchmarking Attacks and Defenses in LLM-based Agents](https://arxiv.org/abs/2410.02644)** (Zhang et al., arXiv 2024) - *LLMエージェントに対する多様な攻撃と防御の種類を一つの評価フレームワークにまとめた、最大規模の統一分類体系／ベンチマーク。* [[code](https://github.com/agiresearch/ASB)]
- **[TrustAgent: Towards Safe and Trustworthy LLM-based Agents](https://arxiv.org/abs/2402.01586)** (Hua et al., EMNLP 2024) - *エージェントの安全性を守る仕組みとして、constitutionに基づく計画を提案した、影響力のある初期の防御／緩和フレームワーク。* [[code](https://github.com/agiresearch/TrustAgent)]
- **[SafeAgentBench: A Benchmark for Safe Task Planning of Embodied LLM Agents](https://arxiv.org/abs/2412.13178)** (Yin et al., arXiv 2024) - *エージェントの安全性評価をデジタル／テキストの領域から物理世界のembodiedな危険にまで広げ、安全上の失敗がロボティクスにも及ぶことを示す。* [[code](https://github.com/shengyin1224/SafeAgentBench)]
- **[AI Agents That Matter](https://arxiv.org/abs/2407.01502)** (Kapoor et al., arXiv 2024) - *エージェントの能力に関する主張をこの分野がどう評価するかを見直させた、広く引用されている批判。エージェントのリスクと便益のトレードオフを信頼できる形で評価することに直接関わる。*
- **[Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training](https://arxiv.org/abs/2401.05566)** (Hubinger et al., arXiv 2024) - *現在のsafety trainingのパイプラインでは、隠れた欺瞞的な振る舞いやアライメントから外れた振る舞いを取り除けない場合があることを示した象徴的な実証で、エージェントの信頼性をめぐる懸念に直接つながる。* [[code](https://github.com/anthropics/sleeper-agents-paper)]
- **[Frontier Models are Capable of In-context Scheming](https://arxiv.org/abs/2412.04984)** (Meinke et al., arXiv 2024) - *フロンティアの自律エージェントがin-context schemingの能力を持つことを示した、初の体系的な実証的証拠。自律性にまつわるアライメントのリスクで中心となる懸念である。*
- **[Emergent Misalignment: Narrow Finetuning can Produce Broadly Misaligned LLMs](https://arxiv.org/abs/2502.17424)** (Betley et al., arXiv 2025) - *エージェントとしての能力を対象にした、一見無害で狭い範囲のファインチューニングだけで、広範で予測できない安全上の失敗が起こりうることを示した、最近の非常に影響力のある発見。* [[code](https://github.com/emergent-misalignment/emergent-misalignment)]
- **[AI Deception: A Survey of Examples, Risks, and Potential Solutions](https://arxiv.org/abs/2308.14752)** (Park et al., arXiv 2023) - *AIによる欺瞞を、実証的な裏付けのある独立したリスク区分として確立した基礎的なサーベイ。このリスクは、エージェントの信頼性とアライメントの中心にある。*
- **[AI Alignment: A Comprehensive Survey](https://arxiv.org/abs/2310.19852)** (Ji et al., arXiv 2023) - *アライメント全般を扱うサーベイの中でも特に包括的なものの一つで、エージェント固有の安全性研究が土台とする概念的な枠組み（RICE、forward/backward alignment）を示す。* [[code](https://github.com/PKU-Alignment/AlignmentSurvey)]
- **[A Survey on Trustworthy LLM Agents: Threats and Countermeasures](https://arxiv.org/abs/2503.09648)** (Yu et al., arXiv 2025) - *この分野に最も直接的に対応する最近のサーベイで、エージェント固有の安全性／セキュリティ上の脅威のほぼすべてを覆う分類体系を示す。* [[code](https://github.com/Ymm-cll/TrustAgent)]
- **[A Comprehensive Survey in LLM(-Agent) Full Stack Safety: Data, Training and Deployment](https://arxiv.org/abs/2504.15585)** (Wang et al., arXiv 2025) - *ライフサイクル全体を扱う大規模な安全性サーベイで、エージェント固有のリスクをより広いLLMの安全性パイプラインの中に位置づける。エージェントのリスクを、より大きな安全対策の一段として捉えるのに役立つ。*
- **[A Survey on Autonomy-Induced Security Risks in Large Model-Based Agents](https://arxiv.org/abs/2506.23844)** (Su et al., arXiv 2025) - *この分野の中心的な主張を正面から打ち出す。エージェント固有の新たなセキュリティリスクを生むのは、基盤となるLLMだけでなく自律性そのものだ、という主張である。*
- **[Discovering Language Model Behaviors with Model-Written Evaluations](https://arxiv.org/abs/2212.09251)** (Perez et al., arXiv 2022) - *RLHFの学習規模を、自己保存や権力追求に近い選好の表明が新たに現れることと結びつけた、初期の先駆的な実証的証拠。自律エージェントのアライメントをめぐる懸念の先がけである。* [[code](https://github.com/anthropics/evals)]
- **[Towards Understanding Sycophancy in Language Models](https://arxiv.org/abs/2310.13548)** (Sharma et al., arXiv 2023) - *Sycophancyを頑健性／アライメントの失敗モードとして調べた重要な実証研究。自律的な意思決定の中で正直な評価を下さなければならないエージェントに直接関わる。* [[code](https://github.com/meg-tong/sycophancy-eval)]
- **[Design Patterns for Securing LLM Agents against Prompt Injections](https://arxiv.org/abs/2506.08837)** (Beurer-Kellner et al., arXiv 2025) - *信頼できない入力を読んだ後にエージェントができることを制限する、アーキテクチャ上のパターン集。*
- **[OS-Harm: A Benchmark for Measuring Safety of Computer Use Agents](https://arxiv.org/abs/2506.14866)** (Kuntz et al., arXiv 2025) - *エージェントの安全性の測定を、実際のインターフェースを操作するcomputer useエージェントへ広げる。*
- **[The 2025 AI Agent Index: Documenting Technical and Safety Features of Deployed Agentic AI Systems](https://arxiv.org/abs/2602.17753)** (Staufer et al., FAccT 2026) - *実運用されている 30 のエージェントシステムを調べた実証的なインデックス。能力に比べて安全性の情報公開が遅れているという、透明性の差を記録する。*

- **[AgentDoG: A Diagnostic Guardrail Framework for AI Agent Safety and Security](https://arxiv.org/abs/2601.18491)** (Liu et al., arXiv 2026) - *エージェントのリスクの統一分類体系を土台に、二値のラベルではなく、安全でないtrajectoryの根本原因を示す診断型のguardrailを構築する。* [[code](https://github.com/AI45Lab/AgentDoG)]
- **[The Landscape of Prompt Injection Threats in LLM Agents: From Taxonomy to Analysis](https://arxiv.org/abs/2602.10453)** (Wang et al., arXiv 2026) - *LLMエージェントに対するindirect prompt injectionの脅威を分類体系として整理し、防御が手薄な部分を分析する。*
- **[ARGUS: Defending LLM Agents Against Context-Aware Prompt Injection](https://arxiv.org/abs/2605.03378)** (Weng et al., arXiv 2026) - *エージェントの判断が信頼できる証拠に基づいているかを監査するinfluence-provenanceグラフを構築し、攻撃成功率を 3.8% まで下げる。*
- **[Provably Secure Agent Guardrail](https://arxiv.org/abs/2605.29251)** (Wu et al., arXiv 2026) - *行動する前に、エージェントに意図を一階述語論理の制約として形式化させる。攻撃成功率と誤検知率はどちらもゼロだった。*
- **[AutoRISE: Agent-Driven Strategy Evolution for Red-Teaming Large Language Models](https://arxiv.org/abs/2604.22871)** (Gautam et al., arXiv 2026) - *コーディングエージェントが（プロンプトだけでなく）実行可能な攻撃戦略を進化させ、11 のモデルでjailbreak攻撃の成功率を 17 ポイント高める。*
- **[When Agents Remember Too Much: Memory Poisoning Attacks on Large Language Model Agents](https://arxiv.org/abs/2607.06595)** (Torres et al., arXiv 2026) - *エージェントへのmemory poisoning攻撃。永続する状態を汚染し、侵害がセッションを越えて残るようにする。*
- **[Agent Data Injection Attacks are Realistic Threats to AI Agents](https://arxiv.org/abs/2607.05120)** (Choi et al., arXiv 2026) - *エージェントの入力へのデータ注入が、作りものの実験設定ではなく現実的な脅威であることを示す。*
- **[AgentAbstain: Do LLM Agents Know When Not to Act?](https://arxiv.org/abs/2607.10059)** (Liu et al., arXiv 2026) - *エージェントが行動すべきでないときを分かっているかを問い、行動を控えることを第一級の安全行動として扱う。* [[code](https://github.com/AntiQuality/agentabstain)]
- **[Prismata: Confining Cross-Site Prompt Injection in Web Agents](https://arxiv.org/abs/2607.08147)** (Villa et al., arXiv 2026) - *Webエージェントに対するクロスサイトのprompt injectionを、モデルが抵抗することに期待するのではなく、境界で封じ込める。*
- **[The Balkanization of Execution-Security Research for AI Coding Agents: Isolation, Access Control, and Time-of-Check-to-Time-of-Use Vulnerabilities](https://arxiv.org/abs/2607.05743)** (Rashidi et al., arXiv 2026) - *分離、アクセス制御、それに関連する防御にまたがって断片化した、コーディングエージェントの実行時セキュリティ研究を概観する。*
- **[Supply-Chain Poisoning Attacks Against LLM Coding Agent Skill Ecosystems](https://arxiv.org/abs/2604.03081)** (Qu et al., arXiv 2026) - *コーディングエージェントがインストール元とするskillのエコシステムに対して、サプライチェーンを狙ったポイズニング攻撃が成り立つことを示す。*
- **[Overcoming the Retrieval Barrier: Indirect Prompt Injection in the Wild for LLM Systems](https://arxiv.org/abs/2601.07072)** (Chang et al., arXiv 2026) - *実環境でのindirect prompt injectionを調べ、実際のLLMシステムでは検索という障壁が想定より弱いことを示す。*
- **[PISmith: Reinforcement Learning-based Red Teaming for Prompt Injection Defenses](https://arxiv.org/abs/2603.13026)** (Yin et al., arXiv 2026) - *Prompt injectionの防御を自動でストレステストする、強化学習によるレッドチーミング。* [[code](https://github.com/albert-y1n/PISmith)]
- **[MOSAIC: Knowledge-Guided CLI Command Composition Attack in LLM Coding Agents](https://arxiv.org/abs/2607.02857)** (Wu et al., arXiv 2026) - *LLMコーディングエージェントで、個々には無害なCLIコマンドが組み合わさると生産者と消費者のあいだに危険な状態の関係が生まれるという、組み合わせレベルのattack surfaceを特定し、MOSAICを提案する。*
- **[KidnapRAG: A Black-Box Attack for Hijacking Reasoning in Agentic Retrieval-Augmented Generation Systems](https://arxiv.org/abs/2607.00422)** (Choi et al., arXiv 2026) - *役割の異なる三つの文書、Bait、Chain-Link、Mal-Insを使って、agentic RAGをブラックボックスのままポイズニングする。それぞれ最初の検索を引き寄せ、クエリの書き換えを誘い、攻撃者が操作する証拠を差し出す。プロンプトにもtraceにもパラメータにもアクセスしない。* [[code](https://github.com/chanwoochoi316/KidnapRAG)]
- **[(A)I Sees What You Don't: Exploiting New Attack Surfaces in Third-Party Mobile Agents](https://arxiv.org/abs/2607.00333)** (Zhang et al., arXiv 2026) - *VLMで動くサードパーティのモバイルエージェントに、これまで特徴づけられていなかった二つのattack surfaceを見いだす。人間と機械の見え方の違いから生じる画面知覚のsurfaceと、エージェントの実行パイプラインを横取りしたり操作したりする、悪用されたチャネルのsurfaceである。広く使われている五つのフレームワークで、七つの具体的な攻撃により、特別な権限を持たない悪意あるアプリがエージェントの行動を乗っ取り、任意のコマンド実行にまで至る。*
- **[Beware of Agentic Botnets: Scalable Untargeted Promptware Attacks via Universal and Transferable Adversarial HalluSquatting](https://arxiv.org/abs/2607.07433)** (Spira et al., arXiv 2026) - *Adversarial hallucination squattingを提案する。攻撃者は、話題のリポジトリやskillについてLLMがhallucinationで生み出すリソース識別子の分布をモデル化し、その名前を先回りして登録して敵対的なプロンプトを置く。Hallucinationで生じた識別子は、リポジトリのクローンの場面で最大 85%、skillのインストールの場面で最大 100% 現れ、モデルをまたいで転移し、本番のLLMアプリケーションでリモートコード実行につながる。*
- **[BackdoorAgent: A Unified Framework for Backdoor Attacks on LLM-based Agents](https://arxiv.org/abs/2601.04566)** (Feng et al., arXiv 2026) - *LLMエージェントのworkflow（計画、メモリ、ツール利用）に計測を仕込み、複数ステップのtrajectoryにわたってbackdoorのトリガーを注入、追跡、評価する、段階を意識したフレームワークとベンチマークを示す。* [[code](https://github.com/Yunhao-Feng/BackdoorAgent)]
- **[Defense Against Indirect Prompt Injection via Tool Result Parsing](https://arxiv.org/abs/2601.04795)** (Yu et al., arXiv 2026) - *ツールの出力を抽出して無害化する、ツール結果の解析による防御を提案する。タスクの有用性を保ったまま、LLMエージェントへのindirect prompt injectionの攻撃成功率を下げ、AgentDojoベンチマークで評価した。* [[code](https://github.com/qiang-yu/agentdojo/tree/tool-result-extract)]
- **[ICON: Indirect Prompt Injection Defense for Agents based on Inference-Time Correction](https://arxiv.org/abs/2602.20708)** (Wang et al., arXiv 2026) - *LLMエージェント向けの推論時の防御を提案する。潜在空間の分析でindirect prompt injectionを検出し、attentionの操作で無力化しつつ、タスクの有用性を保つ。*
- **[An AI Agent Execution Environment to Safeguard User Data](https://arxiv.org/abs/2604.19657)** (Stanley et al., arXiv 2026) - *AIエージェントの実行環境GAAPを提案する。情報フロー制御を使い、ユーザーの個人データをどう開示するかについてユーザーが指定した権限を、AIモデルとその提供者への開示も含めて強制する。*
- **[Protocol-Level Attacks on Agentic Commerce Platforms: A Cross-Platform Taxonomy, AIP-Bench, and Unified Defense](https://arxiv.org/abs/2607.21824)** (Louck, arXiv 2026) - *Agentic commerceのセキュリティを一段下の層で捉え直す。三つのプラットフォームにまたがる 33 のプロトコル脆弱性は、モデルに関係なく決定論的に悪用でき、そのうち三つを連鎖させるとend-to-endで決済を乗っ取れる。*
- **[IssueTrojanBench: Benchmarking AI Coding Agents Against Malicious Issue Requests](https://arxiv.org/abs/2607.20759)** (Singh et al., arXiv 2026) - *実運用中のCursor、Claude Code、Codex Desktopでは、悪意あるissueの依頼の 66.5% がすべてのguardrailをすり抜ける。実際に起きた拒否も、エージェントフレームワークではなくモデルによるものだった。*
- **[Rethinking MCP Security: A Large-Scale Study of Runtime MCP Servers and Security Scanner Reliability](https://arxiv.org/abs/2607.11086)** (Chen et al., arXiv 2026) - *実環境のMCPサーバー 64,611 個を集め（うち 37,000 個超が実行可能）、それらを監査するスキャナーが誤報ばかり出していることを示す。抽出したアラートのうち、手作業の検証を経て残ったのは半分に満たない。*
- **[Agent Against Agent: An Agentic System for Automatic Prompt Injection Red Teaming](https://arxiv.org/abs/2608.05108)** (Wang et al., arXiv 2026) - *一つの標的に合わせたRLの攻撃者ではなく、転用できるprompt injection戦略のライブラリを構築し、追加学習なしで未知のモデルに再利用する。サンプルあたり約十回のクエリで、Gemini-2.5-Proへの攻撃成功率 76.2%、AgentDojoで 86.7% を達成した。* [[code](https://github.com/Wang-Yanting/PIMiner)]
- **[LoginTrap: Uncovering Task-Agnostic Phishing-Style Indirect Prompt Injection Attacks against LLM-based Web Agents](https://arxiv.org/abs/2608.04741)** (Guo et al., arXiv 2026) - *Webエージェントを言いくるめてログインさせられることを示す。攻撃者が操作するページの内容が、認証をタスクの前提条件のように見せ、エージェントを攻撃者の管理するログインページへ誘導する。ユーザーのタスクを知らなくても、end-to-endで平均 86% の成功率に達した。*
- **[Emergent Misaligned Communication in Long-Horizon Multi-Agent LLM Commerce](https://arxiv.org/abs/2608.14825)** (Li et al., arXiv 2026) - *13 のフロンティアモデルにまたがる、一年間の自動販売機運営シミュレーション 20 回から得たエージェント間のメール 2,583 通のうち、12.6% には、意図して引き出したわけでもないのに、事実と異なる主張、操作、共謀、脅しが含まれていた。この振る舞いは相互的で（アライメントから外れた返信のオッズが 1.65 倍）、ストレスに左右され（在庫が少ないと 1.58 倍）、モデルの性能順位からは予測できない。*
- **[Governance at the Boundary: How Agent Decomposition Degrades Policy Compliance](https://arxiv.org/abs/2608.16055)** (Li et al., arXiv 2026) - *エージェントを分解すると、引き継ぎの境界で統制が効きにくくなる。KYC/AMLの 626 エピソードで、32B のopen-weightsモデルが発見したポリシー上重要な事実のうち、減衰させた割合は単一ループで 0%、固定パイプラインで 56%、orchestratorとsubagentの構成で 85% だった。同じ仕組みが、escalationの不足と過剰の両方を生む。*
- **[What's in Your Agent's Context? Context Privilege Escalation Attacks against AI Agent Harness](https://arxiv.org/abs/2609.01222)** (Li et al., arXiv 2026) - *実際のharnessがコンテキストをどう組み立てるかを体系化し、その設計から生じる二つのescalation経路を特定する。低い権限のソースから来た攻撃者の操作するコンテンツが、より高い権限のメッセージロールに入り込む経路と、そうしたコンテンツが入ってきたスコープを越えて残り続ける経路である。Claude CodeやCodexを含む 12 のharnessで実証し、その影響はリモートコード実行や、ツールやskillの呼び出しの改ざんにまで及ぶ。*
- **[BAITBENCH: Measuring Agent Reward Hacking with Optional Shortcuts Planted in ML Tasks](https://arxiv.org/abs/2608.30724)** (Prasad et al., arXiv 2026) - *三つの合成された表形式のMLタスクそれぞれに、公開スコアを押し上げる一方で隠しテストセットでは失敗し、明示されたルールには違反しない任意の近道を仕込む。七つのフロンティアエージェントの実行の 57.1% がその近道を使い、七つのうち五つは半数を超えた。プロンプトでずるをしないよう頼んでも、平均は半数を上回ったままだった。*
- **[LlamaFirewall: An open source guardrail system for building secure AI agents](https://arxiv.org/abs/2505.03574)** (Chennabasappa et al., arXiv 2025) - *小さなjailbreak分類器、注入と目標のずれを見張るchain-of-thoughtの監査器、静的コードスキャナーを重ね、エージェントを囲む実行時の最後の層とする。AgentDojoでは 86M の分類器だけで攻撃成功率が 17.6% から 7.5% に下がり、監査器を加えると 1.75% になる。* [[code](https://github.com/meta-llama/PurpleLlama/tree/main/LlamaFirewall)]
- **[Type-Safe Is Not Error-Free: A Constrained Decision Head Follows the Option Name, Not the Rubric Bound to It](https://arxiv.org/abs/2609.26758)** (Sun and Xu, arXiv 2026) - *どの選択肢名をどのrubricに結びつけるかを入れ替え、型付きの決定を返すモデルが名前のほうに従うことを示す。1,200 件のworkflow上の判断で、0/1 をno/yesに言い換えると、百件あたり 70.4 件多く答えが反転した。Jev自身にも同じ反転が見られ、その間type errorの発生率はずっと 0% のままだった。*
</details>

<sub><a href="#contents">↑ 目次に戻る</a></sub>

## 🔗 関連するAwesomeリスト

同じ分野で参考になる、ほかのリストです。

- [js-lee-AI/awesome-agent-loop-papers](https://github.com/js-lee-AI/awesome-agent-loop-papers)：**このリストの姉妹リスト**です。エージェントのループそのものへ一段掘り下げ、制御戦略、学習によって身につけたループ、skill、harness、そしてループが生む評価と安全性の問題を扱います。 ![stars](https://img.shields.io/github/stars/js-lee-AI/awesome-agent-loop-papers?style=social)
- [Hannibal046/Awesome-LLM](https://github.com/Hannibal046/Awesome-LLM)：大規模言語モデルの論文、ツール、リソースが集まる定番のハブです。 ![stars](https://img.shields.io/github/stars/Hannibal046/Awesome-LLM?style=social)
- [ysymyth/awesome-language-agents](https://github.com/ysymyth/awesome-language-agents)：言語エージェントの論文を、CoALAフレームワークに沿って整理しています。 ![stars](https://img.shields.io/github/stars/ysymyth/awesome-language-agents?style=social)
- [WooooDyy/LLM-Agent-Paper-List](https://github.com/WooooDyy/LLM-Agent-Paper-List)：*The Rise and Potential of LLM-Based Agents*（Fudan NLP）のサーベイと連動したエージェント論文リストです。 ![stars](https://img.shields.io/github/stars/WooooDyy/LLM-Agent-Paper-List?style=social)
- [luo-junyu/Awesome-Agent-Papers](https://github.com/luo-junyu/Awesome-Agent-Papers)：エージェントの構築、協調、進化を扱うサーベイの付属リストで、分類体系に沿って並んでいます。 ![stars](https://img.shields.io/github/stars/luo-junyu/Awesome-Agent-Papers?style=social)
- [e2b-dev/awesome-ai-agents](https://github.com/e2b-dev/awesome-ai-agents)：オープンソースとクローズドソースの**エージェント製品とフレームワーク**を、画像などを交えて大量に集めたディレクトリです（作る側の視点）。 ![stars](https://img.shields.io/github/stars/e2b-dev/awesome-ai-agents?style=social)
- [kyrolabs/awesome-agents](https://github.com/kyrolabs/awesome-agents)：厳選したエージェントのフレームワークとライブラリを、それぞれリアルタイムのスター数バッジ付きで紹介しています。 ![stars](https://img.shields.io/github/stars/kyrolabs/awesome-agents?style=social)

> 関連するリストを管理している方は、[PRを送って](CONTRIBUTING.md)ここに追加してください。相互リンクは大歓迎です。

<sub><a href="#contents">↑ 目次に戻る</a></sub>

## 📄 引用

サーベイはPreprints.orgで **[LLM Agents: A Survey](https://www.preprints.org/manuscript/202608.0265)** として公開しており、DOIは[`10.20944/preprints202608.0265.v1`](https://doi.org/10.20944/preprints202608.0265.v1)です。引用にはこのバージョン付きの記録を使ってください。同じ 47 ページの論文をこのリポジトリの[`paper/llm-agents-a-survey.pdf`](paper/llm-agents-a-survey.pdf)にも置いているので、GitHubを離れずに読めます。

このリストやサーベイが役に立った場合は、次の形式で引用してください。

```bibtex
@article{lee2026llmagents,
  title     = {LLM Agents: A Survey},
  author    = {Lee, Jungseob},
  year      = {2026},
  month     = {August},
  journal   = {Preprints},
  publisher = {Preprints},
  doi       = {10.20944/preprints202608.0265.v1},
  url       = {https://doi.org/10.20944/preprints202608.0265.v1}
}
```

GitHubの**Cite this repository**ボタンは[`CITATION.cff`](CITATION.cff)を読み込み、同じ記録をAPA形式またはBibTeX形式で返します。

姉妹編としてさらに掘り下げた*The Agent Loop: A Survey of Control Strategies, Skills, and Harnesses for LLM Agents*は別の記録で、DOIは[`10.2139/ssrn.7186738`](https://ssrn.com/abstract=7186738)です。実際に参照したほうを引用してください。

## 🤝 コントリビュート

エージェント研究の論文は月に千本ほどのペースで出ており、一人で追える量をはるかに超えています。このリストのために私もかなり読み込んでいますが、**優れた論文や手法を見落としているのは間違いありません**。ここに載るべき論文があれば（**ご自身の論文も含めて**）、次のどちらかの方法で力を貸してください。

- **PRを送る**：確認できるリンクと、*なぜ重要か*を一行で書いた説明を添えて、適切なセクションに追加してください。実装があれば `[code]` リンクもお願いします。
- **[issue](https://github.com/js-lee-AI/awesome-llm-agent-papers/issues)を立てる**：リンクを書いてもらえれば、すぐに目を通して対応を決めます。

誤りの指摘、より的確な説明文、まるごと新しいセクションも同じように歓迎します。項目の書式は **[CONTRIBUTING.md](CONTRIBUTING.md)** を見てください。

## 👥 コントリビューター

このリストはコミュニティの手で保守されています。論文の提案、確認、説明文の執筆に協力してくださったすべての方に感謝します。

<details>
<summary><b>13人のコントリビューターを表示</b></summary>

| | コントリビューター | 貢献内容 |
|---|---|---|
| <a href="https://github.com/shubhamrgandhi"><img src="https://github.com/shubhamrgandhi.png?size=48" width="48" height="48" alt="@shubhamrgandhi"></a> | **[@shubhamrgandhi](https://github.com/shubhamrgandhi)** | 「計画と推論」に、小さなcriticモデルで大きなコーディングエージェントを導くSteer, Don't Solve（[#16](https://github.com/js-lee-AI/awesome-llm-agent-papers/pull/16)）、「ツール利用」に、検証器なしで学習するエージェントのためのrubricベースのcredit assignmentであるDRACO（[#17](https://github.com/js-lee-AI/awesome-llm-agent-papers/pull/17)）。いずれも第一著者本人による投稿 |
| <a href="https://github.com/sunyuhan19981208"><img src="https://github.com/sunyuhan19981208.png?size=48" width="48" height="48" alt="@sunyuhan19981208"></a> | **[@sunyuhan19981208](https://github.com/sunyuhan19981208)** | 「応用分野」に、harnessが変わっても動き続けるよう小さなモデルを学習させるTaoLiveのレポート。著者の一人による投稿（[#15](https://github.com/js-lee-AI/awesome-llm-agent-papers/pull/15)） |
| <a href="https://github.com/burgerseater"><img src="https://github.com/burgerseater.png?size=48" width="48" height="48" alt="@burgerseater"></a> | **[@burgerseater](https://github.com/burgerseater)** | 「評価とベンチマーク」に、コードを書くモデルではなくコーディングエージェントを操るモデルを採点するベンチマーク、LoopArena。著者の一人による提案（[#14](https://github.com/js-lee-AI/awesome-llm-agent-papers/issues/14)） |
| <a href="https://github.com/dukesun99"><img src="https://github.com/dukesun99.png?size=48" width="48" height="48" alt="@dukesun99"></a> | **[@dukesun99](https://github.com/dukesun99)** | 「メモリ」にCorpus2Skill、「マルチエージェントシステム」にOrchMAS、「サーベイとポジションペーパー」にエージェント向けIRのポジションペーパー。投稿者は三本すべての著者の一人（[#13](https://github.com/js-lee-AI/awesome-llm-agent-papers/pull/13)） |
| <a href="https://github.com/zhongzero"><img src="https://github.com/zhongzero.png?size=48" width="48" height="48" alt="@zhongzero"></a> | **[@zhongzero](https://github.com/zhongzero)** | 「メモリ」に、予測のための、二つのエージェントからなるメモリアーキテクチャ、ForeDreamer。著者の一人による投稿（[#12](https://github.com/js-lee-AI/awesome-llm-agent-papers/pull/12)） |
| <a href="https://github.com/Nicolas99-9"><img src="https://github.com/Nicolas99-9.png?size=48" width="48" height="48" alt="@Nicolas99-9"></a> | **[@Nicolas99-9](https://github.com/Nicolas99-9)** | 「マルチエージェントシステム」に、人間の行動に沿わせた大規模な都市シミュレーション、CityReal（[#10](https://github.com/js-lee-AI/awesome-llm-agent-papers/pull/10)） |
| <a href="https://github.com/BobbyZhouZijian"><img src="https://github.com/BobbyZhouZijian.png?size=48" width="48" height="48" alt="@BobbyZhouZijian"></a> | **[@BobbyZhouZijian](https://github.com/BobbyZhouZijian)** | 「エージェントのアーキテクチャとフレームワーク」に、自律的なマルチエージェント進化フレームワーク、CORAL。著者の一人による投稿（[#9](https://github.com/js-lee-AI/awesome-llm-agent-papers/pull/9)） |
| <a href="https://github.com/razzant"><img src="https://github.com/razzant.png?size=48" width="48" height="48" alt="@razzant"></a> | **[@razzant](https://github.com/razzant)** | 「エージェントのアーキテクチャとフレームワーク」に、自らを開発し続けるコーディングエージェントのharness、Ouroboros。メンテナー本人による投稿（[#8](https://github.com/js-lee-AI/awesome-llm-agent-papers/pull/8)） |
| <a href="https://github.com/reacher-z"><img src="https://github.com/reacher-z.png?size=48" width="48" height="48" alt="@reacher-z"></a> | **[@reacher-z](https://github.com/reacher-z)** | 「評価とベンチマーク」に、deep researchエージェントの評価、Dr. Bench。著者の一人による投稿（[#7](https://github.com/js-lee-AI/awesome-llm-agent-papers/pull/7)）。同じセクションに、実際のWebで動かすブラウザエージェントのベンチマーク、ClawBench（[#3](https://github.com/js-lee-AI/awesome-llm-agent-papers/pull/3)） |
| <a href="https://github.com/JEONGSEJIN"><img src="https://github.com/JEONGSEJIN.png?size=48" width="48" height="48" alt="@JEONGSEJIN"></a> | **[@JEONGSEJIN](https://github.com/JEONGSEJIN)** | 「インタラクティブ環境」に、WebAgentと、世界モデルで強化したWebエージェント（[#6](https://github.com/js-lee-AI/awesome-llm-agent-papers/pull/6)） |
| <a href="https://github.com/jinmang2"><img src="https://github.com/jinmang2.png?size=48" width="48" height="48" alt="@jinmang2"></a> | **[@jinmang2](https://github.com/jinmang2)** | エージェントのメモリシステム 6 件：MemoryOS、Zep、Nemori、MemOS、G-Memory、ACE（[#2](https://github.com/js-lee-AI/awesome-llm-agent-papers/pull/2)） |
| <a href="https://github.com/WhymustIhaveaname"><img src="https://github.com/WhymustIhaveaname.png?size=48" width="48" height="48" alt="@WhymustIhaveaname"></a> | **[@WhymustIhaveaname](https://github.com/WhymustIhaveaname)** | 研究エージェントとorchestrationの論文 3 本：AutoNumerics、OptimAI、PerspectiveGap（[#1](https://github.com/js-lee-AI/awesome-llm-agent-papers/pull/1)）。Agonのコードリンクと、途中で切れていた九本の説明文を書き直すきっかけになった報告（[#5](https://github.com/js-lee-AI/awesome-llm-agent-papers/pull/5)） |
| <a href="https://github.com/js-lee-AI"><img src="https://github.com/js-lee-AI.png?size=48" width="48" height="48" alt="@js-lee-AI"></a> | **[@js-lee-AI](https://github.com/js-lee-AI)** | メンテナー |
</details>

<sub>この表は自動生成ではなく手で書いています。たまたま<code>git commit</code>を実行した人ではなく、実際に貢献した人の名前が載るようにするためです。コミット単位の履歴は<a href="https://github.com/js-lee-AI/awesome-llm-agent-papers/graphs/contributors">コントリビューターのグラフ</a>を見てください。</sub>

ここにアバターを載せたい方は **[CONTRIBUTING.md](CONTRIBUTING.md)** を見てください。書式の整ったPRを一本送るだけで十分です。

## 📜 ライセンス

[MIT License](LICENSE)のもとで公開しています。

## 🗓️ 更新履歴

- **2026-09-24**: 韓国語、簡体字中国語、日本語でも読めるようになりました。言語はページ上部で選べます。タイトル、著者、会議、コードへのリンクはすべての版で同じで、訳しているのは説明文と本文だけです。専門用語は英語のまま残しています。元になるのは引き続きREADME.mdで、ほかの三つの版はこれを一行ずつ追いかけます。翻訳を進めるなかで、文の途中で切れていながらチェックをすり抜けていた説明文二十二件と、筆頭著者が抜けていた項目十三件が見つかり、すべて直しました。
- **2026-09-23**: Jevの公開で見過ごせなくなったパターンを扱う論文を十二本追加しました。テキストではなく型付きの決定で答えるモデルが、評価者、router、ガード、メモリの制御役としてエージェントのループの中に入り、確信が持てないときはLLMに引き継ぐ、というパターンです。そのうち四本はJevそのものを調べたもので、うち一本は、type errorを一度も出さないまま、選択肢の裏にあるrubricではなく選択肢の名前に従ってしまう反例を示しています。残りの八本は同じ役割を扱った先行研究で、SwiftSageの速い処理と遅い処理の分担から、どのルーティングポリシーも固定の選択に勝てなかったWebエージェントの研究までを含みます。520 本から 532 本になりました。
- **2026-09-16**: コミュニティからの追加を三件マージしました。いずれも論文の著者本人からの投稿で、harnessを意識した学習を扱うTaoLiveのレポート（[@sunyuhan19981208](https://github.com/sunyuhan19981208)、[#15](https://github.com/js-lee-AI/awesome-llm-agent-papers/pull/15)）と、Steer, Don't SolveおよびDRACO（[@shubhamrgandhi](https://github.com/shubhamrgandhi)、[#16](https://github.com/js-lee-AI/awesome-llm-agent-papers/pull/16)と[#17](https://github.com/js-lee-AI/awesome-llm-agent-papers/pull/17)）です。三本とも、アブストラクトにすでにあった数値が入るよう説明文を書き直しました。TaoLiveの説明文は、harnessを固定したファインチューニングでは指示追従が 7.7 ポイント落ちるのに対し、harnessの状態を拡張すれば何も落ちない、という結果を軸にしています。517 本から 520 本になりました。
- **2026-09-16**: コントリビューターの表を、各セクションと同じように折りたたみ表示にしました。表の人数も `sync_counts.py` で正しく保つようにしています。
- **2026-09-07**: 最新論文の追加：2026 年 5 月以降に出たすべての論文から、セクションごとに二本ずつ計 +20 本を加えました。LoopArenaは、著者の一人である[@burgerseater](https://github.com/burgerseater)が[#14](https://github.com/js-lee-AI/awesome-llm-agent-papers/issues/14)で提案してくれたものです。今回は否定的な結果が多めですが、役に立つ研究はまさにそこにありました。たとえば、rolloutの数ではなく推論コストをそろえると元が取れなくなるマルチエージェント構造、モデルを更新しただけで十三ポイントも振れる、モデル自身が書いたメモリのノート（固定スキーマならほとんど動かない）、機能テストは通ったのにレビュアーならまだ差し戻す 644 件中 221 件のパッチ、そしてプロンプトでやめるよう頼んでも 57% の実行で仕込まれた近道を使うフロンティアエージェントです。497 本から 517 本になりました。
- **2026-09-03**: [@dukesun99](https://github.com/dukesun99)が、自身が著者に名を連ねる論文を三本追加してくれました（[#13](https://github.com/js-lee-AI/awesome-llm-agent-papers/pull/13)）。内訳は、「メモリ」にCorpus2Skill、「マルチエージェントシステム」にOrchMAS、「サーベイとポジションペーパー」にInformation Retrieval Misses the Mark for LLM Agentsです。最後の一本はこのリストで初めてのSSRN掲載論文ですが、CONTRIBUTINGはarXivかDOIのリンクを求めているだけで掲載先を限定していないため、規定の範囲内です。三本ともマージ前にアブストラクトから説明文を書き直し、Corpus2Skillの説明文には、十一のデータセットでの結果（うち三つではコーパスのナビゲーションのほうが負ける）を入れました。494 本から 497 本になりました。
- **2026-08-25**: 著者の一人である[@zhongzero](https://github.com/zhongzero)が、ForeDreamerを「メモリ」に追加してくれました（[#12](https://github.com/js-lee-AI/awesome-llm-agent-papers/pull/12)）。説明文の冒頭では、このシステムならではの点を述べています。検索結果をそのままエージェントに渡すのではなく、予測の前にWebの証拠を構造化されたメモリに変えるという点です。493 本から 494 本になりました。
- **2026-08-20**: 最新論文の追加：2026 年 8 月の論文から、セクションごとに二本ずつ計 +20 本を加えました。コードリンクは、論文が自身のリポジトリを明記している場合にだけ付けています。この月は否定的な結果が多く、このリストの方針にも合っています。たとえば、scaffoldingのほうが結果を左右すると分かったMCPとCLIの比較、タスク完了率は変わらないのに検索が三倍に増える圧縮、返されるツール画像が実は冗長だったという結果、そしてモデルの規模を大きくしても縮まらない多言語間の差です。473 本から 493 本になりました。
- **2026-08-20**: コミュニティからの追加を二件マージしました。Dr. Bench（[@reacher-z](https://github.com/reacher-z)、[#7](https://github.com/js-lee-AI/awesome-llm-agent-papers/pull/7)）とCityReal（[@Nicolas99-9](https://github.com/Nicolas99-9)、[#10](https://github.com/js-lee-AI/awesome-llm-agent-papers/pull/10)）です。CityRealのPRはセクションの見出しと折りたたみ部分の見出しの件数を更新していましたが、目次の行はそのままだったため、先にブランチ上で件数をそろえました。471 本から 473 本になりました。
- **2026-08-12**: コミュニティからの追加を四件マージしました。Ouroboros（[@razzant](https://github.com/razzant)、[#8](https://github.com/js-lee-AI/awesome-llm-agent-papers/pull/8)）、CORAL（[@BobbyZhouZijian](https://github.com/BobbyZhouZijian)、[#9](https://github.com/js-lee-AI/awesome-llm-agent-papers/pull/9)）、そしてWebAgentと世界モデルで強化したWebエージェント（[@JEONGSEJIN](https://github.com/JEONGSEJIN)、[#6](https://github.com/js-lee-AI/awesome-llm-agent-papers/pull/6)）です。一つ上の項目からコピーされていたコードリンクを一件削除しました。467 本から 471 本になりました。
- **2026-08-08**: 最新論文の追加：2026 年 8 月の論文 +16 本を、十のセクションすべてにわたって加えました。公式リポジトリがあるものにはリンクを付けています。451 本から 467 本になりました。
- **2026-08-08**: 以前の一括補充で、九本の説明文が文の途中で切れており、うち三本は括弧が閉じないままでした。九本すべてを各論文のアブストラクトから書き直し、Agonには[@WhymustIhaveaname](https://github.com/WhymustIhaveaname)が[#5](https://github.com/js-lee-AI/awesome-llm-agent-papers/pull/5)で教えてくれた `[code]` リンクを付けました。この問題を検出するチェッカーは `scripts/check_glosses.py` にあります。
- **2026-08-06**: サーベイをPreprints.orgで公開しました。DOIは `10.20944/preprints202608.0265.v1` です。引用ブロック、`CITATION.cff`、冒頭のリンクは、このリポジトリのPDFではなく、バージョン付きの記録を指すようにしました。
- **2026-07-31**: 最新論文の追加：2026 年 7 月の論文から、セクションごとに三本ずつ計 +30 本を加え、公式リポジトリがあるものにはリンクを付けました。421 本から 451 本になりました。
- **2026-07-26**: ClawBenchの保守に携わる[@reacher-z](https://github.com/reacher-z)が、ClawBenchを「評価とベンチマーク」に追加してくれました。420 本から 421 本になりました。
- **2026-07-25**: 初めてのコミュニティ貢献です。[@jinmang2](https://github.com/jinmang2)からエージェントのメモリシステム +6 件（MemoryOS、Zep、Nemori、MemOS、G-Memory、ACE）、[@WhymustIhaveaname](https://github.com/WhymustIhaveaname)から研究エージェントとorchestrationの論文 +3 本（AutoNumerics、OptimAI、PerspectiveGap）が届きました。マージ前に、すべてのタイトル、著者、掲載先、arXiv ID、コードリンクを確認し直しています。
- **2026-07-19**: 2026 年分の包括的な補充：確認済みの論文をさらに +78 本（2026 年 1 月から 7 月）、十のセクションすべてに追加しました。公式リポジトリが確認できたものにはリンクを付けています。
- **2026-07-19**: 2026 年 1 月から 5 月分の補充：+30 本（セクションごとに三本）を追加し、公式リポジトリがあるものにはリンクを付けました。
- **2026-07-16**: 最新論文の追加：2026 年 6 月と 7 月の論文 +50 本を、十のセクションすべてにわたって加えました。公式リポジトリがあるものにはリンクを付けています。
- **2026-07-12**: 2026 年の論文の一括追加：十のセクションすべてに +42 本を加えました。あわせて、スター数をリアルタイムで表示する **注目の10本 (2026)** セクションを新設し、関連リストにもリアルタイムのスター数バッジを付けました。211 本から 253 本になりました。
- **2026-07-09**: 文献の更新：+27 本を追加しました（agentic RL、プロトコル、deep research、フロンティアの評価と安全性）。184 本から 211 本になりました。
- **2026-07-08**: 最初の公開です。説明付きの論文 184 本を、サーベイの分類体系に沿って整理しました。
