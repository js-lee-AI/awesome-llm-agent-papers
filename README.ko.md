<h1 align="center">🤖 Awesome LLM Agent Papers</h1>

<p align="center"><a href="README.md">English</a> · <b>한국어</b> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.ja.md">日本語</a></p>

<p align="center">
<b>꼭 읽어야 할 논문 200편 이상, 지금도 계속 추가 중</b>: 계획하고, 기억하고, 도구를 쓰고, 서로 협력하는<br>
LLM 에이전트를 만들 때 읽을 논문을 한 줄 설명과 함께 정리한 목록입니다. 서베이 <i>“LLM Agents: A Survey”</i>를 바탕으로 만들었습니다.
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
📄 <b><a href="https://www.preprints.org/manuscript/202608.0265">서베이 읽기 → “LLM Agents: A Survey”</a></b> &nbsp;·&nbsp; 📖 <b><a href="https://llm-agents-a-survey.gitbook.io/llm-agents-a-survey-docs/">GitBook 온라인 책(영어)</a></b> &nbsp;·&nbsp; <a href="paper/llm-agents-a-survey.pdf">이 저장소의 PDF</a> &nbsp;·&nbsp; ⭐ <b><a href="#starter-kit">10편짜리 스타터 키트부터 시작하기</a></b>
</p>

<p align="center"><sub><i> LLM agents · LLM agent papers · autonomous agents · agentic AI · multi-agent systems · tool use · ReAct · planning · memory · agent benchmarks · agent safety &amp; prompt injection</i></sub></p>

<p align="center"><img src="assets/taxonomy.png" width="460" alt="LLM 에이전트 연구의 분류 체계"></p>

## ✨ 한눈에 보기

| | 담긴 내용 |
|---|---|
| 📚 **서베이보다 넓은 범위** | *LLM Agents: A Survey*에서 인용한 228편과 함께 서베이를 쓴 뒤에 나온 논문도 실었고, 새로 나오는 논문은 계속 추가합니다. |
| 🧭 **기능별 정리** | 서베이 구성을 따라 10개 섹션으로 나눴습니다: 서베이, 아키텍처, 계획, 메모리, 도구 사용, 다중 에이전트, 환경, 응용, 평가, 안전. |
| ✍️ **한 줄 주석** | 항목마다 무엇을 기여했는지 한 줄로 적고 학회와 연도를 밝혔으며, 공식 구현이 있으면 `[code]` 링크를 붙였습니다. |
| ⭐ **스타터 키트** | 분야의 큰 그림을 잡기 위한 [10편 목록](#starter-kit)입니다. 편마다 먼저 읽을 만한 이유를 적어 두었습니다. |
| 🔎 **쉬운 탐색** | 섹션별 논문 수가 붙은 [목차](#contents)가 있고, 섹션마다 접고 펼 수 있습니다. |

**다루는 주제:** cognitive architecture · ReAct와 추론·행동 결합 · long-horizon 계획 · 에이전트 메모리 · 도구로 확장한 LLM · 다중 에이전트 협업 · 웹 / 코드 / embodied 에이전트 · 에이전트 벤치마크와 평가 · 안전, 정렬, 간접 prompt injection.

> 📖 **온라인 책으로 읽기**: 이 분야를 처음 접하는 분을 위해 논문 내용을 기본 개념부터 열 개의 장으로 다시 써서 GitBook에 [**LLM Agents: A Survey**](https://llm-agents-a-survey.gitbook.io/llm-agents-a-survey-docs/)로 올렸습니다. 논문과 마찬가지로, 효과가 있었던 방법뿐 아니라 기대에 못 미친 방법도 같은 비중으로 다룹니다. 책은 영어로 되어 있습니다.

> 🔁 **후속 서베이의 논문 목록**: [**Awesome Agent Loop Papers**](https://github.com/js-lee-AI/awesome-agent-loop-papers)는 에이전트 루프 자체를 다룬 논문 524편과 오픈소스 프로젝트 60개(프레임워크, 코딩 harness, 메모리·sandbox 인프라, skill 라이브러리, 레지스트리)를 모은 목록으로, 서베이 *The Agent Loop: A Survey of Control Strategies, Skills, and Harnesses for LLM Agents*를 바탕으로 만들었습니다.

**LLM 기반 에이전트**의 필독 논문을 모은 저장소입니다. 여기서 LLM 기반 에이전트란 계획, 메모리, 도구 사용, 다중 에이전트 협업 능력을 갖추고 긴 작업을 여러 단계에 걸쳐 수행하는 언어 모델을 말합니다. 논문은 서베이의 분류 체계에 따라 에이전트의 핵심 구성 요소, 에이전트가 쓰이는 환경과 응용, 평가와 안전처럼 모든 구성 요소에 걸쳐 있는 과제 순으로 정리했습니다. 항목마다 논문 링크를 달았고, 공식 구현이 있으면 코드 링크도 함께 달았습니다.

이 목록은 **직접 골라 계속 업데이트하는 목록**으로, 서베이의 참고문헌을 그대로 옮긴 것이 아닙니다. 섹션은 기본으로 접혀 있으며, **논문 N편 보기**를 누르면 펼쳐집니다.

> **범례:** ⭐ = [스타터 키트](#starter-kit) 선정 논문(먼저 읽기 권장) · `[code]` = 공식 구현 링크.

<a id="starter-kit"></a>
## ⭐ 스타터 키트

이 분야가 처음이신가요? 이 열 편에서 시작하시면 좋습니다.

| # | 논문 | 분야 | 먼저 읽는 이유 |
|---|-------|------|----------------|
| 1 | [ReAct: Synergizing Reasoning and Acting](https://arxiv.org/abs/2210.03629) | 계획 | 오늘날 에이전트 루프의 원형으로, 추론과 행동을 번갈아 수행합니다. |
| 2 | [Reflexion: Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366) | 계획 | 메모리에 저장한 self-reflection으로 gradient 없이 개선하는 루프입니다. |
| 3 | [Toolformer: LMs Can Teach Themselves to Use Tools](https://arxiv.org/abs/2302.04761) | 도구 사용 | Self-supervised 방식으로 도구 사용을 익히게 한 선구적 논문입니다. |
| 4 | [Generative Agents: Interactive Simulacra](https://arxiv.org/abs/2304.03442) | 다중 에이전트 | 메모리와 reflection을 집단 규모로 확장했습니다. 에이전트 메모리 설계의 전형으로 꼽힙니다. |
| 5 | [Voyager: An Open-Ended Embodied Agent](https://arxiv.org/abs/2305.16291) | 메모리 / 환경 | 실행 가능한 skill을 라이브러리에 계속 쌓아 가며 평생 학습합니다. |
| 6 | [Cognitive Architectures for Language Agents (CoALA)](https://arxiv.org/abs/2309.02427) | 기초 | 이 목록을 짜는 기준이 된 어휘(메모리, action space, 의사결정 루프)를 제시했습니다. |
| 7 | [A Survey on LLM-based Autonomous Agents](https://arxiv.org/abs/2308.11432) | 서베이 | 이 분야를 대표하는 종합 서베이입니다. |
| 8 | [LLM-based Multi-Agents: A Survey](https://arxiv.org/abs/2402.01680) | 다중 에이전트 | 다중 에이전트 분야의 표준 참고문헌입니다. |
| 9 | [AgentBench: Evaluating LLMs as Agents](https://arxiv.org/abs/2308.03688) | 평가 | 여러 환경에서 에이전트를 평가하는 표준 벤치마크입니다. |
| 10 | [Not what you've signed up for (Indirect Prompt Injection)](https://arxiv.org/abs/2302.12173) | 안전 | 에이전트 보안의 위협 모델을 처음 세운 논문입니다. |

<a id="to-watch"></a>
## 🔥 주목할 10편 (2026)

2026년에 나와 벌써 주목받고 있는 연구입니다.

| 논문 | 분야 | Stars |
|-------|------|-------|
| [GenericAgent: A Token-Efficient Self-Evolving LLM Agent via Contextual Information Density Maximization](https://arxiv.org/abs/2604.17091) | 아키텍처 | ![stars](https://img.shields.io/github/stars/lsdefine/GenericAgent?style=flat&label=%E2%AD%90&labelColor=2B2926&color=7A1F2B) |
| [SimpleMem: Efficient Lifelong Memory for LLM Agents](https://arxiv.org/abs/2601.02553) | 메모리 | ![stars](https://img.shields.io/github/stars/aiming-lab/SimpleMem?style=flat&label=%E2%AD%90&labelColor=2B2926&color=7A1F2B) |
| [AutoSci: A Memory-Centric Agentic System for the Full Scientific Research Lifecycle](https://arxiv.org/abs/2605.31468) | 응용 | ![stars](https://img.shields.io/github/stars/skyllwt/AutoSci?style=flat&label=%E2%AD%90&labelColor=2B2926&color=7A1F2B) |
| [Mobile-Agent-v3.5: Multi-platform Fundamental GUI Agents](https://arxiv.org/abs/2602.16855) | 환경 | ![stars](https://img.shields.io/github/stars/X-PLUG/MobileAgent?style=flat&label=%E2%AD%90&labelColor=2B2926&color=7A1F2B) |
| [AgentDoG: A Diagnostic Guardrail Framework for AI Agent Safety and Security](https://arxiv.org/abs/2601.18491) | 안전 | ![stars](https://img.shields.io/github/stars/AI45Lab/AgentDoG?style=flat&label=%E2%AD%90&labelColor=2B2926&color=7A1F2B) |
| [Agentic Reasoning for Large Language Models](https://arxiv.org/abs/2601.12538) | 서베이 | ![stars](https://img.shields.io/github/stars/weitianxin/Awesome-Agentic-Reasoning?style=flat&label=%E2%AD%90&labelColor=2B2926&color=7A1F2B) |
| [UniToolCall: Unifying Tool-Use Representation, Data, and Evaluation for LLM Agents](https://arxiv.org/abs/2604.11557) | 도구 사용 | ![stars](https://img.shields.io/github/stars/EIT-NLP/UniToolCall?style=flat&label=%E2%AD%90&labelColor=2B2926&color=7A1F2B) |
| [Graph-of-Agents: A Graph-based Framework for Multi-Agent LLM Collaboration](https://arxiv.org/abs/2604.17148) | 다중 에이전트 | ![stars](https://img.shields.io/github/stars/UNITES-Lab/GoA?style=flat&label=%E2%AD%90&labelColor=2B2926&color=7A1F2B) |
| [Can AI Agents Answer Your Data Questions? A Benchmark for Data Agents (DataAgentBench)](https://arxiv.org/abs/2603.20576) | 평가 | ![stars](https://img.shields.io/github/stars/ucbepic/DataAgentBench?style=flat&label=%E2%AD%90&labelColor=2B2926&color=7A1F2B) |
| [Harness Updating Is Not Harness Benefit: Disentangling Evolution Capabilities in Self-Evolving LLM Agents](https://arxiv.org/abs/2605.30621) | 계획 | ![stars](https://img.shields.io/github/stars/A-EVO-Lab/a-evolve?style=flat&label=%E2%AD%90&labelColor=2B2926&color=7A1F2B) |

<sub><a href="#contents">↑ 목차로 돌아가기</a></sub>

## <a id="contents"></a>목차

- [⭐ 스타터 키트](#starter-kit)
- [🔥 주목할 10편 (2026)](#to-watch)
- **🧭 배경**
  - [📚 서베이와 포지션 페이퍼 (57)](#surveys)
  - [🏗️ 에이전트 아키텍처와 프레임워크 (51)](#architectures)
- **🧱 제1부: 핵심 구성 요소**
  - [🧠 계획과 추론 (51)](#planning)
  - [💾 메모리 (56)](#memory)
  - [🔧 도구 사용 (46)](#tools)
  - [🤝 다중 에이전트 시스템 (51)](#multi-agent)
- **🌍 제2부: 환경과 응용 속의 에이전트**
  - [🌐 상호작용 환경 (57)](#environments)
  - [🚀 응용 분야 (54)](#applications)
- **⚖️ 제3부: 전반에 걸친 과제**
  - [📊 평가와 벤치마크 (50)](#evaluation)
  - [🛡️ 안전과 정렬 (59)](#safety)

## 🧭 배경

<a id="surveys"></a>
### 📚 서베이와 포지션 페이퍼 (57)
*서베이 §1-§3(서론, 배경, 분류 체계)에 해당합니다.*

<details>
<summary><b>논문 57편 보기</b></summary>

- **[A Survey on Large Language Model based Autonomous Agents](https://arxiv.org/abs/2308.11432)** (Wang et al., arXiv 2023) - *가장 많이 인용되는 범용 LLM 에이전트 서베이이자 이 분야의 표준 문헌이다.* ⭐ [[code](https://github.com/Paitesanshi/LLM-Agent-Survey)]
- **[The Rise and Potential of Large Language Model Based Agents: A Survey](https://arxiv.org/abs/2309.07864)** (Xi et al., arXiv 2023) - *Wang et al. 2023과 함께 이 분야의 기틀을 놓은 두 종합 서베이 중 하나다.* [[code](https://github.com/WooooDyy/LLM-Agent-Paper-List)]
- **[Cognitive Architectures for Language Agents](https://arxiv.org/abs/2309.02427)** (Sumers et al., TMLR 2023) - *LLM 에이전트를 설명할 때 가장 널리 쓰이는 개념·아키텍처 어휘를 정립했다.* ⭐ [[code](https://github.com/ysymyth/awesome-language-agents)]
- **[ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)** (Yao et al., ICLR 2023) - *오늘날 LLM 에이전트의 기술적 전신 가운데 가장 많이 인용된 논문이다.* ⭐ [[code](https://github.com/ysymyth/ReAct)]
- **[Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366)** (Shinn et al., NeurIPS 2023) - *에이전트 자기 개선에서 gradient 기반 RL의 대안으로 'self-reflection + 메모리' 루프를 확립했다.* ⭐ [[code](https://github.com/noahshinn/reflexion)]
- **[Toolformer: Language Models Can Teach Themselves to Use Tools](https://arxiv.org/abs/2302.04761)** (Schick et al., NeurIPS 2023) - *도구 사용 분야의 선구적 논문이다. LLM 에이전트 분류 체계에서 '도구 확장' 축을 다룰 때 기준으로 삼는다.* ⭐
- **[Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442)** (Park et al., arXiv 2023) - *LLM으로 움직이는 에이전트 사회와 시뮬레이션을 보여 준 기초 연구다.* ⭐ [[code](https://github.com/joonspk-research/generative_agents)]
- **[Voyager: An Open-Ended Embodied Agent with Large Language Models](https://arxiv.org/abs/2305.16291)** (Wang et al., TMLR 2023) - *코드로 된 skill을 쌓으며 평생 학습하는 embodied LLM 에이전트의 선구적 사례다.* ⭐ [[code](https://github.com/MineDojo/Voyager)]
- **[HuggingGPT: Solving AI Tasks with ChatGPT and its Friends in Hugging Face](https://arxiv.org/abs/2303.17580)** (Shen et al., NeurIPS 2023) - *LLM을 도구와 모델의 orchestrator로 쓰는 에이전트 패턴의 기초 사례다.* [[code](https://github.com/microsoft/JARVIS)]
- **[MRKL Systems: A Modular, Neuro-Symbolic Architecture that Combines Large Language Models, External Knowledge Sources and Discrete Reasoning](https://arxiv.org/abs/2205.00445)** (Karpas et al., arXiv 2022) - *LLM 도구 사용·에이전트 아키텍처의 전신이 된 neuro-symbolic 연구 가운데 널리 인용되는 가장 이른 논문이다.*
- **[Agent AI: Surveying the Horizons of Multimodal Interaction](https://arxiv.org/abs/2401.03568)** (Durante et al., arXiv 2024) - *LLM 에이전트 서베이가 다루는 범위를 multimodal·embodied 에이전트 AI까지 넓혔다.*
- **[Igniting Language Intelligence: The Hitchhiker's Guide From Chain-of-Thought Reasoning to Language Agents](https://arxiv.org/abs/2311.11797)** (Zhang et al., arXiv 2023) - *추론(CoT) 연구와 에이전트 연구를 잇는다.* [[code](https://github.com/Zoeyyao27/CoT-Igniting-Agent)]
- **[Large Language Model based Multi-Agents: A Survey of Progress and Challenges](https://arxiv.org/abs/2402.01680)** (Guo et al., IJCAI 2024) - *LLM 에이전트 가운데 다중 에이전트 갈래만을 다룬 표준 참고 서베이다.* ⭐ [[code](https://github.com/taichengguo/LLM_MultiAgents_Survey_Papers)]
- **[Understanding the Planning of LLM Agents: A Survey](https://arxiv.org/abs/2402.02716)** (Huang et al., arXiv 2024) - *기초 서베이들이 따로 다루지 않던 계획 분야를 다룬다.*
- **[Tool Learning with Large Language Models: A Survey](https://arxiv.org/abs/2405.17935)** (Qu et al., arXiv 2024) - *LLM 에이전트의 도구 사용 축을 다룬 결정판 서베이다.* [[code](https://github.com/quchangle1/LLM-Tool-Survey)]
- **[A Survey on the Memory Mechanism of Large Language Model based Agents](https://arxiv.org/abs/2404.13501)** (Zhang et al., arXiv 2024) - *LLM 에이전트의 메모리 하위 시스템을 다룬 표준 서베이다.* [[code](https://github.com/nuster1128/LLM_Agent_Memory_Survey)]
- **[Agentic Large Language Models, a Survey](https://arxiv.org/abs/2503.23037)** (Plaat et al., arXiv 2025) - *추론·행동·상호작용으로 간결하게 나눈 분류 체계를 갖춘 최근 종합 서베이로, 널리 참조된다.*
- **[Large Language Model Agent: A Survey on Methodology, Applications and Challenges](https://arxiv.org/abs/2503.21460)** (Luo et al., arXiv 2025) - *가장 포괄적인 최신(2025년) 종합 서베이 중 하나다.* [[code](https://github.com/luo-junyu/Awesome-Agent-Papers)]
- **[Fully Autonomous AI Agents Should Not Be Developed](https://arxiv.org/abs/2502.02649)** (Mitchell et al., arXiv 2025) - *에이전트 자율성에 반대 입장을 밝힌 포지션 페이퍼로, 널리 주목받고 논의되었다.*
- **[AI Agents vs. Agentic AI: A Conceptual Taxonomy, Applications and Challenges](https://arxiv.org/abs/2505.10468)** (Sapkota et al., arXiv 2025) - *이 분야에서 용어가 제각각 쓰이는 탓에, 용어와 개념을 가려 정리한 이 논문의 인용이 점점 늘고 있다.*
- **[LLM-Based Human-Agent Collaboration and Interaction Systems: A Survey](https://arxiv.org/abs/2505.00753)** (Zou et al., arXiv 2025) - *초기 기초 서베이들이 짚어 둔 사람과 에이전트의 협력 분야를 다룬다.* [[code](https://github.com/HenryPengZou/Awesome-Human-Agent-Collaboration-Interaction-Systems)]
- **[Levels of Autonomy for AI Agents](https://arxiv.org/abs/2506.12469)** (Feng et al., arXiv 2025) - *LLM 에이전트 시스템의 자율성을 서로 비교할 수 있게 하는 실용적 틀로, 널리 인용된다.*
- **[Advances and Challenges in Foundation Agents: From Brain-Inspired Intelligence to Evolutionary, Collaborative, and Safe Systems](https://arxiv.org/abs/2504.01990)** (Liu et al., arXiv 2025) - *저자 48명이 함께 쓴 대표적인 서베이로, 뇌에서 착안한 인지 모듈, 자기 진화, 집단 지능, 안전을 축으로 분야를 정리한다.*
- **[The Landscape of Agentic Reinforcement Learning for LLMs: A Survey](https://arxiv.org/abs/2509.02547)** (Zhang et al., arXiv 2025) - *Agentic RL의 표준 서베이로, LLM을 수동적인 생성기가 아니라 스스로 결정을 내리는 에이전트로 학습시키는 연구를 정리한다.*
- **[A Comprehensive Survey of Self-Evolving AI Agents: A New Paradigm Bridging Foundation Models and Lifelong Agentic Systems](https://arxiv.org/abs/2508.07407)** (Fang et al., arXiv 2025) - *에이전트가 상호작용 데이터로 자기 구성 요소를 최적화하는 기법을 정리하며, foundation model과 평생 학습하는 agentic 시스템을 잇는다.*
- **[Deep Research Agents: A Systematic Examination and Roadmap](https://arxiv.org/abs/2506.18096)** (Huang et al., arXiv 2025) - *검색, 도구 사용, 보고서 작성을 오가는 long-horizon 자율 연구 에이전트를 체계적으로 다룬 첫 서베이다.*
- **[A Survey of AI Agent Protocols](https://arxiv.org/abs/2504.16736)** (Yang et al., arXiv 2025) - *새로 생겨나는 프로토콜 계층(MCP, A2A와 그 뒤를 잇는 프로토콜)을 정리하고, 에이전트 상호운용 표준을 평가할 기준 축을 제안한다.*

- **[Agentic Reasoning for Large Language Models](https://arxiv.org/abs/2601.12538)** (Wei et al., arXiv 2026) - *Agentic 추론을 단일 에이전트, 자기 진화, 다중 에이전트 층으로 정리하고, in-context 추론과 post-training을 잇는 서베이다.* [[code](https://github.com/weitianxin/Awesome-Agentic-Reasoning)]
- **[Memory for Autonomous LLM Agents: Mechanisms, Evaluation, and Emerging Frontiers](https://arxiv.org/abs/2603.07670)** (Du et al., arXiv 2026) - *에이전트 메모리를 쓰기·관리·읽기 루프로 보고, 메커니즘·벤치마크·응용에 걸친 분류 체계를 세운다.*
- **[Anatomy of Agentic Memory: Taxonomy and Empirical Analysis of Evaluation and System Limitations](https://arxiv.org/abs/2602.19320)** (Jiang et al., arXiv 2026) - *에이전트 메모리 구조를 분류하고, 여러 시스템에서 벤치마크 포화와 지표 타당성 문제가 있음을 실험으로 보인다.*
- **[Beyond Individual Intelligence: Surveying Collaboration, Failure Attribution, and Self-Evolution in LLM-based Multi-Agent Systems](https://arxiv.org/abs/2605.14892)** (Qi et al., arXiv 2026) - *다중 에이전트 협업, failure attribution, 자기 진화를 하나로 묶는 'LIFE' 프레임워크(foundation, integrate, find faults, evolve)를 제안한다.*
- **[A Technical Taxonomy of LLM Agent Communication Protocols](https://arxiv.org/abs/2606.19135)** (Sander et al., arXiv 2026) - *공개된 에이전트 간 프로토콜 아홉 개를 다섯 가지 차원에서 분석하고, 결국 연합형 프로토콜 스택으로 수렴하리라고 내다본다.*
- **[Bridging the Agent-World Gap: Text World Models for LLM-based Agents](https://arxiv.org/abs/2606.09032)** (Li et al., arXiv 2026) - *에이전트가 계획과 검증을 위해 환경을 명시적으로 예측하게 해 주는 텍스트 world model(LLM-as-WM 대 code-as-WM)을 체계화한다.* [[code](https://github.com/sustech-nlp/awesome-text-world-models)]
- **[Agents That Know Too Much: A Data-Centric Survey of Privacy in LLM Agents](https://arxiv.org/abs/2606.26627)** (Lahjouji et al., arXiv 2026) - *에이전트 프라이버시 연구를 공격 유형이 아니라 데이터가 노출되는 지점별로 정리한 데이터 중심 서베이로, 거버넌스 공백을 정리한다.*
- **[Self-Improvements in Modern Agentic Systems: A Survey](https://arxiv.org/abs/2607.13104)** (Ren et al., arXiv 2026) - *현대 에이전트를 foundation model에 운영용 scaffold를 더한 것으로 보고, 자기 개선을 무엇이 갱신되는지(가중치인가 scaffold인가)와 어떤 신호가 변화를 이끄는지에 따라 정리한다.* [[code](https://github.com/selfimproving-agent/awesome-Self-Improving-Agents)]
- **[Dynamic Agent Skills: A Lifecycle Survey and Taxonomy of Evolving Skill Libraries](https://arxiv.org/abs/2607.10113)** (Li et al., arXiv 2026) - *진화하는 skill 라이브러리를 생애주기로 관리되는 아티팩트 저장소로 보고 논문 124편을 정리하며, 결정적인 단계는 skill을 얻는 일이 아니라 받아들이고 고치는 일이라고 주장한다.*
- **[From Question Answering to Task Completion: A Survey on Agent System and Harness Design](https://arxiv.org/abs/2606.20683)** (Guo et al., arXiv 2026) - *에이전트를 모델과 harness로 나누어 분석한다. Harness는 실행 시점의 책임 여섯 가지로 쪼개고, 성능 병목이 실제로 어디에 있는지 따진다.* [[code](https://github.com/ggjy/Awesome-Agent-Engineering)]
- **[Isolation as a First-Class Principle for LLM-Agent System Safety: Concepts, Taxonomy, Challenges and Future Directions](https://arxiv.org/abs/2607.12406)** (Jing et al., arXiv 2026) - *Prompt injection, 도구 오용, memory poisoning을 하나의 구조적 문제로 다시 규정하는 포지션 페이퍼다. 핵심은 에이전트의 다섯 인터페이스에 걸쳐 격리 경계가 빠져 있다는 점이다.*
- **[Always-On Agents: A Survey of Persistent Memory, State, and Governance in LLM Agents](https://arxiv.org/abs/2606.30306)** (Ding et al., arXiv 2026) - *세션을 넘어 상태를 유지하는 에이전트에 관한 연구 435편을 정리한다. 축적과 검색을 다룬 연구는 많지만 거버넌스와 복구는 소홀히 다뤄진다는 점을 밝힌다.*
- **[Externalization in LLM Agents: A Unified Review of Memory, Skills, Protocols and Harness Engineering](https://arxiv.org/abs/2604.08224)** (Zhou et al., arXiv 2026) - *에이전트의 발전을 외부화 과정으로 본다. 가중치가 맡던 능력을 메모리, skill, 프로토콜, harness 인프라가 나누어 맡게 된다는 관점이다.*
- **[SoK: Agentic Skills -- Beyond Tool Use in LLM Agents](https://arxiv.org/abs/2602.20867)** (Jiang et al., arXiv 2026) - *Agentic skill을 재사용할 수 있는 호출형 절차로 보고 체계화하며, skill과 원자적 도구 호출을 구분한다.*
- **[From Storage to Experience: A Survey on the Evolution of LLM Agent Memory Mechanisms](https://arxiv.org/abs/2605.06716)** (Luo et al., arXiv 2026) - *에이전트 메모리를 저장에서 reflection, 다시 경험으로 이어지는 세 단계 진화로 정리하고, 그 동력을 일관성, 동역학, 지속 학습에서 찾는다.* [[code](https://github.com/FeishuLuo/Evolving-LLM-Agent-Memory-Survey)]
- **[LLM agents security duality: a comprehensive survey of self-security and empowered cybersecurity](https://arxiv.org/abs/2606.28450)** (Xu et al., arXiv 2026) - *LLM 에이전트가 받는 보안 위협과 그 완화책을 위협 출처별 분류 체계로 함께 정리하고, 에이전트의 능력을 사이버 공격·방어 생애주기 전체에 대응시키는 틀도 제시하는 서베이다.*
- **[Agentic Environment Engineering for Large Language Models: A Survey of Environment Modeling, Synthesis, Evaluation, and Application](https://arxiv.org/abs/2606.12191)** (Li et al., arXiv 2026) - *LLM 기반 에이전트를 위한 환경 연구를 모델링, 합성, 평가, 응용이라는 엔지니어링 생애주기에 따라 정리하고, 환경을 여덟 가지 속성으로 분류하는 방식을 제안한다.*
- **[Toward Efficient Agents: Memory, Tool learning, and Planning](https://arxiv.org/abs/2601.14192)** (Yang et al., arXiv 2026) - *LLM 에이전트 시스템의 효율을 세 구성 요소(메모리, 도구 학습, 계획)에 걸쳐 살피고, 효과와 비용의 관계를 Pareto frontier로 보는 서베이다.*
- **[Agentic Artificial Intelligence (AI): Architectures, Taxonomies, and Evaluation of Large Language Model Agents](https://arxiv.org/abs/2601.12560)** (Arunkumar V et al., arXiv 2026) - *LLM 에이전트를 여섯 가지 구성 요소(지각, 두뇌, 계획, 행동, 도구 사용, 협업)로 나누는 통합 분류 체계를 제안하고, 아키텍처, 동작 환경, 평가 관행을 검토한 서베이이다. Hallucination에서 나온 행동, 무한 루프, prompt injection 같은 미해결 문제를 짚으며 끝맺는다.*
- **[A Survey on Long-Term Memory Security in LLM Agents: Attacks, Defenses, and Governance Across the Memory Lifecycle](https://arxiv.org/abs/2604.16548)** (Lin et al., arXiv 2026) - *LLM 에이전트의 long-term memory가 받는 보안 위협을 메모리 생애주기 여섯 단계와 네 가지 보안 목표에 걸쳐 공격, 방어, 거버넌스로 정리하고, "Verifiable Memory Governance" 프레임워크를 제안한다.*
- **[Uncertainty Quantification in LLM Agents: Foundations, Emerging Challenges, and Opportunities](https://arxiv.org/abs/2602.05073)** (Oh et al., arXiv 2026) - *불확실성 정량화가 단일 턴 QA를 벗어나 상호작용하는 에이전트로 옮겨 가야 한다고 주장한다. 일반적인 정식화를 제시하고, 에이전트에만 있는 과제로 추정기 선택, 이질적인 개체, 불확실성의 동역학, 세밀한 벤치마크의 부재 네 가지를 든다.*
- **[Multi-Agent Debate Strategies: Survey, Taxonomy, and Challenges](https://arxiv.org/abs/2607.26212)** (Motger et al., arXiv 2026) - *다중 에이전트 토론 연구 141편을 검토해, 대부분이 투표를 곁들인 정적 fully connected 토폴로지를 별다른 논의 없이 쓰고 있으며, 이는 통제된 비교가 아니라 관행에 따른 선택임을 밝힌다.*
- **[Beyond the Leaderboard: A Synthesis of Tool-Use, Planning, and Reasoning Failures in Large Language Model Agents](https://arxiv.org/abs/2607.05775)** (Albayaydh et al., arXiv 2026) - *벤치마크 19개에 걸친 평가 논문 27편을 여섯 가지 실패 군집으로 종합한다. 실패는 과제 길이에 따라 비선형적으로 쌓이며, scaffolding을 더해도 신뢰성이 꾸준히 나아지지는 않는다.*
- **[How Agents Ask for Permission: User Permissions for AI Agents, from Interfaces to Enforcement](https://arxiv.org/abs/2607.13718)** (Michael et al., arXiv 2026) - *에이전트 권한 제안 21건을 상용 에이전트 다섯 개와 대조해, 사용자 수준 정책이 어떻게 명세되고, 사용자 입력에서 도출되고, 실행 중에 강제되는지, 그리고 어디에 빈틈이 남는지를 분류한다.*
- **[Blockchain Empowered Trustworthy Agent Networks: Foundations, Taxonomy, and Future Directions](https://arxiv.org/abs/2608.04626)** (Zhu et al., arXiv 2026) - *1980년부터 2026년까지 고전적 다중 에이전트 시스템에서 개방형 에이전트 네트워크에 이르는 흐름을 정리한다. 서로 다른 주체가 소유한 에이전트끼리 거래하기 시작하면 신뢰 문제가 네트워크 수준으로 옮겨 가고, 단일 에이전트용 안전 장치로는 이 문제를 다룰 수 없다고 주장한다.*
- **[Software Engineering for and with GUI Agent](https://arxiv.org/abs/2608.09278)** (Yu et al., arXiv 2026) - *2018년 1월부터 2026년 4월까지 나온 GUI 에이전트 논문 336편을 검토해, 아키텍처는 모듈식 지각·추론·행동 루프로 수렴하는 반면 복구, 사람에게 넘기는 escalation, 안전 강제, 감사 가능성은 여전히 덜 발달했음을 밝힌다. 평가는 아직 과제 성공에 머물러 있고 프로토콜끼리 비교하기도 어렵다.*
- **[Agent Safety Should Be a Runtime Contract](https://arxiv.org/abs/2608.11274)** (Ng et al., arXiv 2026) - *에이전트 안전을 harness 안의 런타임 계약으로 다루자는 포지션 페이퍼다. 이 계약은 사고를 막는 장치(sandbox, 권한 게이트, 모니터)와 증거를 남기는 장치(테스트 실행, 로그 수집, 파일 diff)로 이루어진다. 기록된 사고 52건, 12개 공개 에이전트 시스템의 trajectory 스키마 감사, NeurIPS·ICML·ICLR 2023-2025 논문 28,560편 전체의 제목 수준 감사를 근거로 삼으며, 마지막 감사에서는 학습 시점 연구와 배포 시점 연구 사이에 합산 기준 8-12배의 출판 불균형이 나타났다.*
- **[Information Retrieval Misses the Mark for LLM Agents](https://doi.org/10.2139/ssrn.6903579)** (Sun et al., SSRN 2026) - *실제 배포 사례를 보고 "RAG는 끝났고 에이전트에게는 grep이면 된다"고 해석하는 시각에 답하는 포지션 페이퍼다. 기반이 바뀌었다는 점은 인정하지만, 불일치는 다섯 차원에 걸친 구조적 문제라고 본다. IR이 전제하는 코퍼스, 입력, 목표, 에피소드, 검색 대상이 모두 계획하고 브라우징하고 도구를 부르며 검색을 계속할지 스스로 정하는 에이전트에게는 맞지 않기 때문이다. 에이전트를 고정한 채 HotpotQA-distractor와 2WikiMultihopQA에서 BM25, 벡터, grep, 하이브리드, closed-book 검색을 바꿔 가며 이 격차를 시험하고, 검색을 상태에 따라 증거를 모으는 정책으로 다시 정의하자고 주장한다.*
- **[Terminal Agents: A Survey of AI Agents in Command-Line Environments](https://arxiv.org/abs/2608.20485)** (Bin et al., arXiv 2026) - *과제 영역이 아니라 터미널을 기준으로 연구를 정리한다. 명령을 실행하고 텍스트 피드백을 받으며 과제를 진행하는 에이전트를 아키텍처, 역량 획득, 평가에 걸쳐 일곱 차원의 역량 프로파일로 정리한다. 조건을 고정한 자체 진단에서는 벤치마크 계열마다 관찰되는 과정 신호가 다르고, 조건을 맞춘 시스템 비교도 벤치마크에 따라 결과가 달라진다. 그래서 어떤 결과든 단일 구성 요소의 효과로 돌릴 수 있는 범위가 제한된다.*
- **[Autonomous Research Agents: A Survey of AI Scientists and the Verification Gap](https://arxiv.org/abs/2608.05179)** (Ding et al., arXiv 2026) - *AI 과학자 시스템 후보 125개를 선별해 그중 26개를 일곱 가지 감사 차원으로 코딩하고, 병목이 능력에서 검증 가능성으로 옮겨 갔음을 밝힌다. 실행 가능한 24개 시스템 중 83%가 코드를 공개하지만 seed나 실행 trace를 공개하는 것은 38%뿐이고 참신성 검증을 조금이라도 보고하는 것도 38%뿐이다. 폐쇄 루프 시스템 아홉 개 가운데 일곱 개는 기계적 재실행이며, 외부에서 검증된 루프 내 oracle은 코퍼스 전체 어디에도 없다.*
</details>

<sub><a href="#contents">↑ 목차로 돌아가기</a></sub>

<a id="architectures"></a>
### 🏗️ 에이전트 아키텍처와 프레임워크 (51)
*서베이 §2(배경)와 서베이 전체에서 이어지는 예시에 해당합니다.*

<details>
<summary><b>논문 51편 보기</b></summary>

- **[Auto-GPT for Online Decision Making: Benchmarks and Additional Opinions](https://arxiv.org/abs/2306.02224)** (Yang et al., arXiv 2023) - *큰 영향을 끼쳤지만 논문은 없는 AutoGPT 자율 에이전트 설계 패턴을 다룬, 동료 심사에 준하는 유일한 실증 연구다.* [[code](https://github.com/younghuman/LLMAgent)]
- **[AgentBench: Evaluating LLMs as Agents](https://arxiv.org/abs/2308.03688)** (Liu et al., ICLR 2024) - *이질적인 여러 환경에 걸쳐 단일 에이전트의 일반 능력을 재는 표준 벤치마크다.* ⭐ [[code](https://github.com/THUDM/AgentBench)]
- **[WebArena: A Realistic Web Environment for Building Autonomous Agents](https://arxiv.org/abs/2307.13854)** (Zhou et al., ICLR 2024) - *웹 브라우징 단일 에이전트 아키텍처의 사실상 표준 테스트베드다.* [[code](https://github.com/web-arena-x/webarena)]
- **[Gorilla: Large Language Model Connected with Massive APIs](https://arxiv.org/abs/2305.15334)** (Patil et al., NeurIPS 2024) - *단일 에이전트 도구 사용의 핵심 논문이다. Fine-tuning에 검색을 더하면 에이전트가 방대한 실제 API 목록을 안정적으로 호출할 수 있음을 보였다.* [[code](https://github.com/ShishirPatil/gorilla)]
- **[ReWOO: Decoupling Reasoning from Observations for Efficient Augmented Language Models](https://arxiv.org/abs/2305.18323)** (Xu et al., arXiv 2023) - *효율을 겨냥한 ReAct 루프의 대안으로 영향력이 컸으며, '계획 후 실행' 대 '번갈아 실행'이라는 아키텍처 설계 축을 보여 준다.* [[code](https://github.com/billxbf/ReWOO)]
- **[Tree of Thoughts: Deliberate Problem Solving with Large Language Models](https://arxiv.org/abs/2305.10601)** (Yao et al., NeurIPS 2023) - *숙고형 탐색 추론의 핵심 아키텍처로, LATS 같은 후속 단일 에이전트 계획·탐색 프레임워크의 바탕이 되었다.* [[code](https://github.com/princeton-nlp/tree-of-thought-llm)]
- **[WebGPT: Browser-assisted question-answering with human feedback](https://arxiv.org/abs/2112.09332)** (Nakano et al., arXiv 2021) - *ChatGPT 이전에 나온 현대 LLM 웹 에이전트의 초기 전신으로, 브라우징 도구 사용에 사람의 피드백을 더하는 패턴을 확립했다.*
- **[SELF-REFINE: Iterative Refinement with Self-Feedback](https://arxiv.org/abs/2303.17651)** (Madaan et al., NeurIPS 2023) - *최소한의 구성으로 널리 채택된 단일 에이전트 자기 개선 루프로, 여러 대형 에이전트 아키텍처 안에서 서브루틴으로 다시 쓰인다.* [[code](https://github.com/madaan/self-refine)]
- **[SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](https://arxiv.org/abs/2405.15793)** (Yang et al., NeurIPS 2024) - *인터페이스 설계가 단일 에이전트의 능력을 실질적으로 바꾼다는 것을 보였고, 이 관점은 이제 코딩 에이전트 설계의 표준이 되었다.* [[code](https://github.com/princeton-nlp/SWE-agent)]
- **[Language Agent Tree Search Unifies Reasoning, Acting, and Planning in Language Models](https://arxiv.org/abs/2310.04406)** (Zhou et al., ICML 2024) - *탐색 기반 계획과 ReAct/Reflexion 계보를 최고 수준으로 결합한 대표 연구다.* [[code](https://github.com/lapisrocks/LanguageAgentTreeSearch)]
- **[Executable Code Actions Elicit Better LLM Agents](https://arxiv.org/abs/2402.01030)** (Wang et al., ICML 2024) - *'code-as-action'을 단일 에이전트 action space 설계의 유력한 대안으로 자리 잡게 했다.* [[code](https://github.com/xingyaoww/code-act)]
- **[Describe, Explain, Plan and Select: Interactive Planning with Large Language Models Enables Open-World Multi-Task Agents](https://arxiv.org/abs/2302.01560)** (Wang et al., NeurIPS 2023) - *오픈월드·embodied 과제를 위한 핵심 단일 에이전트 계획 아키텍처다.* [[code](https://github.com/CraftJarvis/MC-Planner)]
- **[OS-Copilot: Towards Generalist Computer Agents with Self-Improvement](https://arxiv.org/abs/2402.07456)** (Wu et al., arXiv 2024) - *스스로 개선하는 범용 OS 수준 단일 에이전트의 최근 대표 사례로, AutoGPT식 자율성을 실제 컴퓨터 환경으로 넓혔다.* [[code](https://github.com/OS-Copilot/OS-Copilot)]
- **[AppAgent: Multimodal Agents as Smartphone Users](https://arxiv.org/abs/2312.13771)** (Zhang et al., CHI 2025) - *ReAct/도구 사용 패러다임을 GUI/모바일 조작으로 넓힌 최근의 대표적 단일 에이전트 아키텍처다.* [[code](https://github.com/TencentQQGYLab/AppAgent)]
- **[The Landscape of Emerging AI Agent Architectures for Reasoning, Planning, and Tool Calling: A Survey](https://arxiv.org/abs/2404.11584)** (Masterman et al., arXiv 2024) - *에이전트 아키텍처 설계 패턴으로 범위를 좁힌 서베이로, 단일 에이전트 프레임워크를 분류할 때 바로 참고가 된다.*
- **[MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework](https://arxiv.org/abs/2308.00352)** (Hong et al., ICLR 2024) - *단일 에이전트의 역할·절차 템플릿이 어떻게 신뢰성을 높이는지 보여 준, 널리 인용되는 프레임워크다. 프레임워크 설계가 단일 에이전트에서 다중 에이전트로 넘어가는 시점의 대표 사례이기도 하다.* [[code](https://github.com/geekan/MetaGPT)]
- **[Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, Long Context, and Next Generation Agentic Capabilities](https://arxiv.org/abs/2507.06261)** (Comanici et al., arXiv 2025) - *프런티어 모델 보고서로, agentic 도구 사용과 컴퓨터 조작을 대표 능력으로 내세운다.*
- **[Kimi K2: Open Agentic Intelligence](https://arxiv.org/abs/2507.20534)** (Kimi Team, arXiv 2025) - *대규모 agentic post-training을 중심에 두고 설계한 대표 오픈 모델이다.* [[code](https://github.com/MoonshotAI/Kimi-K2)]

- **[GenericAgent: A Token-Efficient Self-Evolving LLM Agent via Contextual Information Density Maximization](https://arxiv.org/abs/2604.17091)** (Liang et al., arXiv 2026) - *컨텍스트 경험을 쌓아 가는 토큰 효율적인 자기 진화 에이전트로, 2026년 에이전트 프레임워크 가운데 스타를 가장 많이 받은 축에 든다.* [[code](https://github.com/lsdefine/GenericAgent)]
- **[Orchestral AI: A Framework for Agent Orchestration](https://arxiv.org/abs/2601.02577)** (Roman et al., arXiv 2026) - *전문화된 에이전트들을 조합하고 조율해 하나의 인터페이스로 제공하는 프레임워크다.* [[code](https://github.com/orchestralAI/orchestral-ai)]
- **[AgentArk: Distilling Multi-Agent Intelligence into a Single LLM Agent](https://arxiv.org/abs/2602.03955)** (Luo et al., arXiv 2026) - *다중 에이전트의 지능을 distillation으로 단일 LLM 에이전트에 옮겨, 협업으로 얻는 이득을 더 적은 비용으로 유지한다.* [[code](https://github.com/AIFrontierLab/AgentArk)]
- **[The Interplay of Harness Design and Post-Training in LLM Agents](https://arxiv.org/abs/2606.25447)** (Kim et al., arXiv 2026) - *Harness 설계와 post-training이 서로 영향을 주고받으므로, harness를 고려한 post-training이 in-distribution과 out-of-distribution 성능을 모두 높인다는 것을 보인다.*
- **[Next-Generation Agentic Reinforcement Learning Systems Enable Self-Evolving Agents](https://arxiv.org/abs/2607.01120)** (Ran Yan et al., arXiv 2026) - *에이전트가 가중치뿐 아니라 자기 구성 요소까지 고칠 수 있게 하는 것은 알고리즘이 아니라 agentic RL 시스템 스택이라고 주장한다.*
- **[From Atomic Actions to Standard Operating Procedures: Iterative Tool Optimization for Self-Evolving LLM Agents](https://arxiv.org/abs/2607.07321)** (Ding et al., arXiv 2026) - *실행 trace에서 반복되는 행동 시퀀스를 호출 가능한 상위 절차로 합성한 뒤, 그렇게 만든 도구 모음을 병합하고 평가하고 가지치기한다.*
- **[Self-Evolving World Models for LLM Agent Planning](https://arxiv.org/abs/2606.30639)** (Zhang et al., arXiv 2026) - *실행기는 고정한 채 테스트 시점에 에이전트 내부의 world model을 다듬어, 계획하고 시뮬레이션하는 루프를 더 정교하게 만든다.*
- **[Scaling Self-Evolving Agents via Parametric Memory](https://arxiv.org/abs/2606.04536)** (Ren et al., arXiv 2026) - *자기 진화를 context window가 아니라 파라미터에 담아, 경험이 쌓여도 프롬프트가 길어지지 않게 한다.*
- **[Inside the Scaffold: A Source-Code Taxonomy of Coding Agent Architectures](https://arxiv.org/abs/2604.03515)** (Rombaut et al., arXiv 2026) - *공개 코딩 에이전트 scaffold 13개의 소스 코드에서 분류 체계를 끌어내고, 시스템들이 재조합하는 루프 기본 요소 다섯 가지를 찾아낸다.*
- **[Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses](https://arxiv.org/abs/2604.25850)** (Lin et al., arXiv 2026) - *관측 가능성 신호를 바탕으로 코딩 에이전트 harness를 자동으로 진화시켜, Terminal-Bench 2 점수를 69.7에서 77.0으로 올렸다.*
- **[AgentFactory: A Self-Evolving Framework Through Executable Subagent Accumulation and Reuse](https://arxiv.org/abs/2603.18000)** (Zhang et al., arXiv 2026) - *성공한 해법을 텍스트 프롬프트가 아니라 재사용 가능한 실행형 하위 에이전트 코드로 저장해 능력을 쌓고, 이를 실행 피드백으로 다듬는다.* [[code](https://github.com/zzatpku/AgentFactory)]
- **[CORAL: Towards Autonomous Multi-Agent Evolution for Open-Ended Discovery](https://arxiv.org/abs/2604.01658)** (Qu et al., COLM 2026) - *하드코딩된 탐색 규칙 대신, 공유된 영구 메모리를 매개로 탐색하고 되돌아보고 협업하는 장기 실행 에이전트를 쓴다. 작업 공간을 격리하고 평가자를 분리한 조건에서 최적화 과제 10개의 최고 성능을 경신했고, 평가 한 번당 개선 속도는 3배에서 10배에 이른다. 함께 진화하는 에이전트 네 개는 Anthropic의 커널 과제를 1363 사이클에서 1103 사이클로 줄였다.* [[code](https://github.com/Human-Agent-Society/CORAL)]
- **[LogicHunter: Testing LLM Agent Frameworks with an Agentic Oracle](https://arxiv.org/abs/2607.06195)** (Long et al., arXiv 2026) - *명세 기반 fuzzing 프레임워크에 ReAct 기반 agentic oracle을 짝지은 LogicHunter를 제안한다. 이 oracle은 문서를 찾아 읽고, 소스 코드를 탐색하고, 실행 중 상태를 살핀다. 널리 배포된 에이전트 프레임워크 세 개에서 알려지지 않았던 버그 40개를 찾았는데, 그중 30개가 확인되고 26개가 고쳐졌으며, oracle의 정밀도는 91.17%로 가장 좋은 수동적 방식의 29.27%를 앞섰다.*
- **[AgentFlow: Building Agent Dependency Graphs for Static Analysis of Agent Programs](https://arxiv.org/abs/2607.01640)** (Wang et al., arXiv 2026) - *LLM 에이전트 소스 코드에서 에이전트 간 의존 관계를 복원하는 정적 분석 프레임워크 AgentFlow를 내놓는다. 프레임워크에 구애받지 않는 Agent Dependency Graph를 만들고, 타입이 붙은 노드가 에이전트, 프롬프트, 모델, 능력, 메모리 상태, 제어 정책을 아우른다. 실제 에이전트 프로그램 5,399개에서 프롬프트에서 도구로 이어지는 taint 형태의 위험 238건을 찾아냈다.*
- **[SEAGym: An Evaluation Environment for Self-Evolving LLM Agents](https://arxiv.org/abs/2606.17546)** (Zheng et al., arXiv 2026) - *자기 진화 LLM 에이전트를 위한 평가 환경 SEAGym을 소개한다. 에이전트 harness의 수정을 단일 과제 점수가 아니라 학습, 검증, held-out 테스트, 리플레이, 비용이라는 여러 차원에서 잰다.*
- **[Harness-MU: A Safe, Governed, and Effective Harness for Multi-User LLM Agents](https://arxiv.org/abs/2606.21856)** (Fan et al., arXiv 2026) - *모델에 구애받지 않고 튜닝도 필요 없는 harness인 Harness-MU를 제안한다. 모델 내부의 안전장치 대신 결정론적 실행 hook으로 LLM 에이전트의 다중 주체 접근 제어를 강제한다.* [[code](https://github.com/YuanJrShiuan/Harness-MulUser)]
- **[Co-Evolving Skill Generation and Policy Optimization](https://arxiv.org/abs/2606.08755)** (Zhang et al., arXiv 2026) - *Skill로 보강한 언어 에이전트를 위한 온라인 프레임워크를 제안한다. 후보 skill마다 맥락에 따라 달라지는 한계 효용을 짝지은 비교군(후보를 넣은 검색 skill 묶음과 뺀 묶음)으로 추정해, 효과가 없거나 해로운 skill을 저장 전에 걸러 내며, 이 과정은 표준 rollout 예산 안에서 이루어진다. 정책 자체도 skill을 생성하도록 학습시킨다.*
- **[DemoEvolve: Overcoming Sparse Feedback in Agentic Harness Evolution with Demonstrations](https://arxiv.org/abs/2605.24539)** (Che et al., arXiv 2026) - *DemoEvolve는 사람 전문가의 시연 trajectory로 agentic harness 진화의 탐색을 이끈다. 자기 연습만으로는 버거운 Balatro 같은 복잡한 확률적 환경에서, 희소 보상 때문에 생기는 불안정성 문제를 푼다.*
- **[Self-Evolving Software Agents](https://arxiv.org/abs/2604.27264)** (Robol et al., arXiv 2026) - *BDI(Belief-Desire-Intention) 추론과 대규모 언어 모델을 결합한 아키텍처를 제안한다. 자동 진화 모듈이 경험에서 새 요구 사항을 끌어내고, 그에 맞는 설계와 코드를 합성한다.*
- **[Codified Context: Infrastructure for AI Agents in a Complex Codebase](https://arxiv.org/abs/2602.20478)** (Vasilopoulos et al., arXiv 2026) - *LLM 코딩 어시스턴트에 지속되는 컨텍스트를 주기 위해, 세 요소로 된 인프라(규약을 담은 헌장, 전문 에이전트 19개, 명세 문서 34건으로 된 지식 베이스)를 제안한다.* [[code](https://github.com/arisvas4/codified-context-infrastructure)]
- **[LLM-as-a-Verifier: A General-Purpose Verification Framework](https://arxiv.org/abs/2607.05391)** (Kwok et al., arXiv 2026) - *검증을 독립된 스케일링 축으로 다룬다. 채점 토큰의 logit에서 얻은 연속 점수를 세분화 정도, 반복 평가, 기준 분해로 확장하면 추가 학습 없이 Terminal-Bench V2에서 86.5%에 이른다.* [[code](https://github.com/llm-as-a-verifier/llm-as-a-verifier)]
- **[Molt: A Scalable PyTorch-Native Training Framework for Agentic Reinforcement Learning](https://arxiv.org/abs/2607.21653)** (Hu et al., arXiv 2026) - *연구자나 코딩 어시스턴트가 처음부터 끝까지 읽을 수 있을 만큼 작은 PyTorch 네이티브 agentic RL 학습기가, Megatron 기반 스택과 통계적으로 대등한 결과를 낸다는 것을 보인다.* [[code](https://github.com/NVIDIA-NeMo/labs-molt)]
- **[Baselines Before Architecture: Evaluating Coding Agents for Autonomous Penetration Testing](https://arxiv.org/abs/2607.13085)** (Dhakal et al., arXiv 2026) - *기본 설정의 코딩 CLI 에이전트만으로도 과제 104개짜리 XBOW 벤치마크의 상당 부분을 이미 풀고, 같은 모델 조건에서 평범한 에이전트를 여러 번 돌리면 발표된 harness 아키텍처와 맞먹는다.*
- **[Argus: A General-Purpose Agentic Runtime for Long-Horizon Reasoning](https://arxiv.org/abs/2608.05144)** (Li et al., arXiv 2026) - *Manager, Planner, Engineer, Reviewer가 오래 유지되는 프로젝트 상태를 바탕으로 범위가 정해진 임무를 수행하는 지속형 런타임이다. 메모리, skill, 검증기는 담당 역할의 검토를 거친 뒤에만 받아들인다. 가중치는 그대로이므로, SWE-Bench Pro에서 모델을 바로 쓰는 baseline이 59%일 때 78%를 낸 것은 전적으로 런타임 상태 덕분이다.*
- **[Architectural Implications of Agentic AI Workflows](https://arxiv.org/abs/2608.04458)** (Yang et al., arXiv 2026) - *Azure의 실제 운영 환경을 조사해 agentic 워크로드를 데이터센터 문제로 규정한다. Orchestration과 도구 때문에 CPU가 critical path에 놓이고, 실행이 단편화되어 기존의 균일한 서버에서는 CPU와 GPU 용량이 모두 쓰이지 못하고 남는다는 점을 밝힌다.*
- **[Ouroboros: A Self-Developing Frontier Coding Agent with Reviewed Core Evolution](https://arxiv.org/abs/2608.08311)** (Razzhigaev et al., arXiv 2026) - *도구, 프롬프트, 컨텍스트 구성, 핵심 구현이 검토를 거친 커밋으로 개선되고, 그 커밋이 이후 작업의 런타임이 되는 코딩 에이전트 harness다. 고정한 snapshot 기준으로 Terminal-Bench 2.1에서 86.74%, OSWorld-Verified에서 90.69%를 보고했으며, 이와 별도로 161일에 걸친 배포에서는 지금도 실시간으로 진화를 이어 간다.* [[code](https://github.com/razzant/ouroboros)]
- **[The Scaffolding Matters More Than the Interface: A Controlled Comparison of MCP and CLI Tool Use Across Seven Agent Scaffoldings, Five Language Models, and One Software Task](https://arxiv.org/abs/2608.08654)** (Alier Forment et al., arXiv 2026) - *고정된 git 과제 하나를 에이전트 scaffolding 일곱 개와 언어 모델 다섯 개로 돌려, 비용을 좌우하는 것은 MCP냐 CLI냐 하는 인터페이스가 아니라 scaffolding임을 보인다. MCP를 지원하지 않는 scaffolding 두 개는 CLI로 모든 실행을 끝냈고, CLI 실행만 놓고 봐도 MCP를 지원하는 scaffolding 다섯 개보다 5.0배에서 28배 저렴했다. 엄격하게 짝지은 MCP 대 CLI 비율 열세 개는 0.43배에서 29배에 걸쳐 있으며, MCP 실행에 쓴 비용의 12.9%는 완료된 작업으로 이어지지 않았다. CLI 실행에서는 이 비율이 2.2%였다.*
- **[Persistent Recursive Worlds Enable Autonomous Software Evolution](https://arxiv.org/abs/2608.10450)** (Huang et al., arXiv 2026) - *에이전트가 아니라 소프트웨어 프로젝트를 지속시킨다. 수명이 한정된 에이전트들이 국소적인 변경을 제안하고, 받아들여진 결과만 버전 이력에 반영된다. 120시간 넘게 이어진 한 번의 실행으로 Rust로 된 약 250k줄짜리 C 컴파일러를 만들었고, 이 컴파일러는 c-testsuite 전체를 통과했다. 모델 토큰 요금으로 든 비용은 44달러였다.*
- **[What Does Multi-Harness RL Learn? Credit Assignment and Portability in Coding Agents](https://arxiv.org/abs/2609.04518)** (Le et al., arXiv 2026) - *Aider, OpenHands, Qwen Code, SWE-agent의 고정된 기록을 재생해, 여러 harness를 한 advantage group에 묶으면 다른 harness에서도 통하는 skill을 얻는지를 따로 떼어 본다. 결과를 보면 평가 harness가 다른 모든 요인을 압도한다. 봉인된 평가 24,000건에서 평가 harness는 평균 해결률을 2.14%에서 9.27%까지 움직였지만 학습 레시피가 움직인 폭은 1.16에 그쳤다. 서로 다른 harness를 한 그룹으로 묶는 방식은 held-out harness에서 같은 harness끼리 묶는 방식보다 0.25포인트 높았는데, 이 차이의 신뢰구간은 음수부터 양수까지 걸쳐 있고 각 규칙의 seed 간 편차보다도 좁다.*
- **[TROVE: Adaptive Agent Skill Orchestration via Trace-Grounded Route Validation and Editing](https://arxiv.org/abs/2609.05019)** (Wang et al., arXiv 2026) - *계획한 경로를 확정된 것이 아니라 잠정적인 것으로 다룬다. 오프라인에서는 평가를 마친 workflow 탐색 trace를 원자 skill과 복합 skill, 그리고 결과에 조건화된 전이 그래프로 추려 낸다. 온라인에서는 유효한 나머지 경로는 그대로 두고, trace가 뒷받침하는 국소 대응을 끼워 넣거나 유효하지 않은 뒷부분만 교체한다. 그래서 실행 중에 얻은 증거가 전면 재계획 대신 국소 수리로 이어진다. Ablation 결과, 오프라인 이득은 대부분 복합 skill에서, 효율 향상은 대부분 뒷부분 교체에서 나왔다.*
- **[SwiftSage: A Generative Agent with Fast and Slow Thinking for Complex Interactive Tasks](https://arxiv.org/abs/2305.17390)** (Lin et al., NeurIPS 2023) - *에이전트를 빠르게 행동하는 fine-tuning된 작은 모델과, 진행이 멈추거나 유효하지 않은 행동이 나오는 등의 신호가 있을 때만 호출되는 GPT-4 planner로 나눈다. ScienceWorld 과제 유형 30개 전반에서 SayCan, ReAct, Reflexion을 앞섰다.*
- **[R2V Agent: Teaching SLMs When to Ask for Help](https://arxiv.org/abs/2605.16604)** (Hemadri et al., arXiv 2026) - *난이도가 trajectory 중간에 바뀌므로 질의 단위가 아니라 단계 단위로 라우팅한다. Brier score로 calibration한 router가 남은 실패 위험이 높을 때만 distillation으로 만든 작은 모델에서 교사 LLM으로 escalation해, escalation 비율 41.7%로 TextWorld 성공률을 64.6%에서 98.2%까지 끌어올렸다.* [[code](https://github.com/RaghuHemadri/r2v-agent)]
- **[REFLEX with Jev for Efficient Selective Control in LLM Agents](https://arxiv.org/abs/2609.26532)** (Wu and Lim, arXiv 2026) - *텍스트 대신 타입이 정해진 결정을 내놓는 모델 Jev에게 에이전트의 제한된 선택을 맡기고, confidence가 낮거나 텍스트가 필요할 때만 강한 LLM을 부른다. 고정된 100개 과제 벤치마크에서 성공률 95%를 내면서 강한 모델 호출을 72.7% 줄였지만, BFCL과 τ 계열 과제에서는 값싼 생성형 cascade보다 나은 점이 거의 없었다.*
</details>

<sub><a href="#contents">↑ 목차로 돌아가기</a></sub>

## 🧱 제1부: 핵심 구성 요소

<a id="planning"></a>
### 🧠 계획과 추론 (51)
*서베이 §4(계획과 추론)에 해당합니다.*

<details>
<summary><b>논문 51편 보기</b></summary>

- **[Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://arxiv.org/abs/2201.11903)** (Wei et al., NeurIPS 2022) - *사실상 모든 LLM 에이전트 추론·계획 모듈의 바탕에 있는 기초 기법이자, CoT/ToT/ReAct 계보 전체의 출발점이다.*
- **[Self-Consistency Improves Chain of Thought Reasoning in Language Models](https://arxiv.org/abs/2203.11171)** (Wang et al., ICLR 2023) - *에이전트의 추론·계획 파이프라인 안에서 널리 재사용되는 표준 추론 시점 ensemble·검증 전략이다.*
- **[Large Language Models are Zero-Shot Reasoners](https://arxiv.org/abs/2205.11916)** (Kojima et al., NeurIPS 2022) - *추론 능력이 모델 안에 잠재해 있어 zero-shot 프롬프트만으로 끌어낼 수 있음을 보였고, 이는 범용 에이전트 프롬프트 템플릿을 가능하게 한 핵심 토대가 되었다.* [[code](https://github.com/kojima-takeshi188/zero_shot_cot)]
- **[Least-to-Most Prompting Enables Complex Reasoning in Large Language Models](https://arxiv.org/abs/2205.10625)** (Zhou et al., ICLR 2023) - *과제 분해를 일찍이 정식화했다. 이는 이후 거의 모든 LLM 에이전트의 과제 planner가 재사용하는 핵심 계획 요소가 되었다.*
- **[STaR: Bootstrapping Reasoning With Reasoning](https://arxiv.org/abs/2203.14465)** (Zelikman et al., NeurIPS 2022) - *에이전트가 스스로 생성한 추론으로 학습하는 RL 기반 reasoning model 학습 패러다임(예: DeepSeek-R1, o1)의 전신이다.* [[code](https://github.com/ezelikman/STaR)]
- **[Graph of Thoughts: Solving Elaborate Problems with Large Language Models](https://arxiv.org/abs/2308.09687)** (Besta et al., AAAI 2024) - *에이전트가 쓰는 구조화된 추론·탐색 프레임워크를 트리에 한정되지 않도록 확장해, 복잡한 다단계 과제에서 품질과 비용을 모두 개선한다.* [[code](https://github.com/spcl/graph-of-thoughts)]
- **[Reasoning with Language Model is Planning with World Model](https://arxiv.org/abs/2305.14992)** (Hao et al., EMNLP 2023) - *탐색 기반의 고전적 계획(MCTS, world model)을 LLM 추론과 연결한다. 불확실한 상황에서 에이전트가 계획을 세우는 문제와 직접 관련된다.* [[code](https://github.com/maitrix-org/llm-reasoners)]
- **[CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing](https://arxiv.org/abs/2305.11738)** (Gou et al., ICLR 2024) - *Self-critique와 도구로 보강한 검증을 잇는다. 이 결합은 reflection의 근거를 외부 피드백에 두는 현대 에이전트 프레임워크의 핵심 메커니즘이다.* [[code](https://github.com/microsoft/ProphetNet/tree/master/CRITIC)]
- **[Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models](https://arxiv.org/abs/2305.04091)** (Wang et al., ACL 2023) - *'계획 후 실행'을 가볍게 구현한 템플릿으로, 많은 LLM 에이전트 계획 모듈이 그대로 가져다 써 널리 퍼졌다.* [[code](https://github.com/AGI-Edgerunners/Plan-and-Solve-Prompting)]
- **[ADaPT: As-Needed Decomposition and Planning with Language Models](https://arxiv.org/abs/2311.05772)** (Prasad et al., ACL 2024) - *실행 결과에 맞춰 계획의 세분도를 에이전트 능력에 따라 조절하는 적응형 계획을 보였다. 정적인 '계획 후 실행' 에이전트를 한 단계 다듬은 중요한 개선이다.* [[code](https://github.com/archiki/ADaPT)]
- **[Self-Discover: Large Language Models Self-Compose Reasoning Structures](https://arxiv.org/abs/2402.03620)** (Zhou et al., NeurIPS 2024) - *LLM이 과제마다 자기 추론 전략을 스스로 고를 수 있음을 보인다. 이런 메타 추론 능력은 적응형 에이전트 계획의 핵심이다.*
- **[Buffer of Thoughts: Thought-Augmented Reasoning with Large Language Models](https://arxiv.org/abs/2406.04271)** (Yang et al., NeurIPS 2024) - *재사용할 수 있는 추론 구조를 메모리에 두고 검색해 쓰는 접근을 대표하며, 추론 전략을 에이전트의 long-term memory 설계와 연결한다.* [[code](https://github.com/YangLing0818/buffer-of-thought-llm)]
- **[Large Language Models Cannot Self-Correct Reasoning Yet](https://arxiv.org/abs/2310.01798)** (Huang et al., ICLR 2024) - *에이전트 설계에서 self-critique 루프에 지나치게 기대는 경향을 경계하게 만든, 널리 인용되는 경고성·비판적 결과다. 외부 피드백에 근거한 방법이 나오는 계기가 되었다.*
- **[Training Language Models to Self-Correct via Reinforcement Learning](https://arxiv.org/abs/2409.12917)** (Kumar et al., ICLR 2025) - *Self-correction을 프롬프팅에만 맡기지 않고 RL로 학습시키면 실제로 효과를 낼 수 있음을 보였고, 현대 에이전트에 쓰이는 reasoning model의 post-training에 직접 영향을 주었다.*
- **[Let's Verify Step by Step](https://arxiv.org/abs/2305.20050)** (Lightman et al., ICLR 2024) - *Process reward model과 단계 수준 검증을 확립했다. 이는 이제 추론 에이전트에서 탐색과 self-critique를 이끄는 표준 구성 요소다.* [[code](https://github.com/openai/prm800k)]
- **[DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/abs/2501.12948)** (Guo et al., Nature 2025) - *RL로 학습하자 계획·reflection 행동이 창발함을 보인 대표적인 오픈 reasoning model로, 차세대 추론 에이전트의 토대가 되고 있다.* [[code](https://github.com/deepseek-ai/DeepSeek-R1)]
- **[Towards Reasoning in Large Language Models: A Survey](https://arxiv.org/abs/2212.10403)** (Huang et al., ACL 2023) - *LLM 추론만을 다룬 서베이 가운데 가장 이르고 가장 많이 인용된 것 중 하나로, LLM 에이전트 서베이라면 추론 절에서 자연스럽게 기준으로 인용할 만하다.* [[code](https://github.com/jeffhj/LM-reasoning)]
- **[Large Language Models for Planning: A Comprehensive and Systematic Survey](https://arxiv.org/abs/2505.19683)** (Cao et al., arXiv 2025) - *이 하위 주제 중 계획 전략 부분만을 정확히 다룬 최신 전문 서베이로, 분류 체계에 관한 주장의 근거로 삼기에 알맞다.* [[code](https://github.com/Quester-one/Awesome-LLM-Planning)]
- **[When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs](https://arxiv.org/abs/2406.01297)** (Kamoi et al., ACL 2024) - *Self-critique와 self-correction만을 다룬 핵심 비판적 서베이로, 에이전트 서베이에서 reflection 방법을 균형 있고 엄밀하게 다루려면 꼭 필요하다.* [[code](https://github.com/ryokamoi/llm-self-correction-papers)]
- **[Search-R1: Training LLMs to Reason and Leverage Search Engines with Reinforcement Learning](https://arxiv.org/abs/2503.09516)** (Jin et al., arXiv 2025) - *Agentic RL의 대표 결과로, 모델이 결과 보상만으로 검색 엔진 호출과 자기 추론을 번갈아 수행하는 법을 익힌다.* [[code](https://github.com/PeterGriffinJin/Search-R1)]
- **[ReTool: Reinforcement Learning for Strategic Tool Use in LLMs](https://arxiv.org/abs/2504.11536)** (Feng et al., arXiv 2025) - *RL로 reasoning model에게 풀이 도중 언제, 어떻게 코드 인터프리터를 호출할지 가르친다.*

- **[Harness Updating Is Not Harness Benefit: Disentangling Evolution Capabilities in Self-Evolving LLM Agents](https://arxiv.org/abs/2605.30621)** (Lin et al., arXiv 2026) - *자기 진화 에이전트에서 'harness 갱신'과 'harness 이득'을 분리해, 모델 등급에 따라 이득 곡선이 비단조적이라는 점을 발견한다.* [[code](https://github.com/A-EVO-Lab/a-evolve)]
- **[Demystifying Reinforcement Learning for Long-Horizon Tool-Using Agents: A Comprehensive Recipe](https://arxiv.org/abs/2603.21972)** (Wu et al., arXiv 2026) - *Agentic RL의 reward shaping, 모델 규모, 데이터, 알고리즘 선택을 두루 다룬 실증 레시피로, TravelPlanner에서 SOTA를 달성했다.* [[code](https://github.com/WxxShirley/Agent-STAR)]
- **[StraTA: Incentivizing Agentic Reinforcement Learning with Strategic Trajectory Abstraction](https://arxiv.org/abs/2605.06642)** (Xue et al., arXiv 2026) - *샘플링한 trajectory 추상화로 전략 생성과 행동 실행을 함께 학습시켜, ALFWorld/WebShop/SciWorld에서 agentic RL 성능을 높인다.*
- **[The Self-Correction Illusion: LLMs Correct Others but Not Themselves](https://arxiv.org/abs/2606.05976)** (Chen et al., arXiv 2026) - *LLM이 외부의 주장은 바로잡지만 똑같은 오류를 스스로 썼을 때는 바로잡지 못함을 보인다. 이는 능력의 한계가 아니라 chat template의 역할 라벨이 만든 부산물이다.*
- **[Recursive Self-Improvement in AI: From Bounded Self-Refinement to Autonomous Research Loops](https://arxiv.org/abs/2607.07663)** (Chen et al., arXiv 2026) - *범위가 제한된 self-refinement부터 자율 연구 루프까지의 스펙트럼을 정리하고, 재귀적 자기 개선의 각 단계가 현재 어디에서 막히는지 짚는다.*
- **[SIRI: Self-Internalizing Reinforcement Learning with Intrinsic Skills for LLM Agent Training](https://arxiv.org/abs/2606.02355)** (He et al., arXiv 2026) - *발견한 skill을 외부 라이브러리에 남겨 두지 않고 정책 안으로 내재화하는 강화학습이다.* [[code](https://github.com/kirito618/SIRI)]
- **[Agentic Chain-of-Thought Steering for Efficient and Controllable LLM Reasoning](https://arxiv.org/abs/2606.03965)** (Xia et al., arXiv 2026) - *추론 시점에 agentic chain-of-thought를 조종해 추론 길이를 제어하고, 재학습 없이 연산량과 정확도를 맞바꾼다.* [[code](https://github.com/Andree-9/ACTS)]
- **[ECHO: Prune To Act, Trace To Learn With Selective Turn Memory In Agentic RL](https://arxiv.org/abs/2606.31650)** (Xie et al., arXiv 2026) - *Agentic RL을 위한 선택적 턴 메모리다. 행동할 때는 trajectory를 가지치기하고, 학습할 때는 trace를 그대로 남긴다.*
- **[AgentTether: Graph-Guided Diagnosis and Runtime Intervention for Reliable LLM Agent Operation](https://arxiv.org/abs/2607.06273)** (Zhao et al., arXiv 2026) - *실행 과정을 그래프로 놓고 에이전트 실패를 진단하며, 사후에만 손대는 것이 아니라 실행 중에 개입한다.*
- **[Reasoning as Gradient: Scaling MLE Agents Beyond Tree Search](https://arxiv.org/abs/2603.01692)** (Zhang et al., arXiv 2026) - *MLE 에이전트의 tree search를 gradient 방식의 최적화 프레임워크로 바꾸고, 추론을 gradient에, 성공 메모리를 momentum에 대응시킨다.* [[code](https://github.com/microsoft/RD-Agent)]
- **[MAP: A Map-then-Act Paradigm for Long-Horizon Interactive Agent Reasoning](https://arxiv.org/abs/2605.13037)** (Liu et al., arXiv 2026) - *행동하기 전에 환경의 인지 지도를 먼저 만들어, long-horizon 상호작용 추론에서 지도 작성과 행동을 분리한다.*
- **[Learning from Trials and Errors: Reflective Test-Time Planning for Embodied LLMs](https://arxiv.org/abs/2602.21198)** (Hong et al., arXiv 2026) - *Embodied 에이전트를 위한 reflection 기반 테스트 시점 계획으로, 한 에피소드 안에서 스스로 겪은 시행착오로부터 배운다.* [[code](https://github.com/Reflective-Test-Time-Planning/Reflective-Test-Time-Planning)]
- **[Agora: Enhancing LLM Agent Reasoning Via Auction-Based Task Allocation](https://arxiv.org/abs/2607.09600)** (Zhou et al., arXiv 2026) - *경매 기반 orchestration 프레임워크 Agora를 제안한다. 추론 단계를 거래할 수 있는 품목으로 다루고, 전문 모델과 도구가 보정하지 않은 confidence가 아니라 보정한 역량에 따라 입찰한다.*
- **[Training the Orchestrator: A Supervised Approach to End-to-End PDDL Planning with LLM Agents](https://arxiv.org/abs/2606.21740)** (Mangannavar et al., arXiv 2026) - *HALO를 소개한다. PDDL 도메인 11개에서 검증기가 인증한 계획 개선 trajectory를 모아, QLoRA로 튜닝한 작은 orchestrator 정책을 지도 학습으로 가르친다.*
- **[Retrospective Progress-Aware Self-Refinement for LLM Agent Training](https://arxiv.org/abs/2606.14302)** (Ma et al., arXiv 2026) - *먼저 실행하고 나중에 되돌아보는 rollout 프레임워크 RePro를 소개한다. LLM 에이전트가 온라인으로 행동을 실행한 뒤, 완료된 trajectory와 알려진 결과를 바탕으로 단계별 진척을 되짚어 다시 평가한다.*
- **[LiTS: A Modular Framework for LLM Tree Search](https://arxiv.org/abs/2603.00631)** (Li et al., arXiv 2026) - *LiTS는 LLM tree search를 재사용 가능한 Policy, Transition, RewardModel 구성 요소로 나누는 Python 프레임워크로, MCTS와 BFS 같은 알고리즘을 지원하며 MATH500, Crosswords, MapEval에서 평가했다.* [[code](https://github.com/xinzhel/lits-llm)]
- **[Localizing and Correcting Errors for LLM-based Planners](https://arxiv.org/abs/2602.00276)** (Kumar et al., arXiv 2026) - *Localized In-Context Learning(L-ICL)을 제안한다. LLM이 생성한 계획에서 제약 위반 지점을 찾아내고, 실패하는 단계에 최소한의 교정 예시를 넣는다.*
- **[CLEANER: Self-Purified Trajectories Boost Agentic Reinforcement Learning](https://arxiv.org/abs/2601.15141)** (Xu et al., arXiv 2026) - *CLEANER를 제안한다. Similarity-Aware Adaptive Rollback으로 실패한 단계를 성공한 self-correction으로 바꿔 정제된 agentic RL trajectory를 만들고, 더 적은 학습 단계로 AIME24/25 정확도를 높인다.*
- **[VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning](https://arxiv.org/abs/2601.20055)** (Singh et al., arXiv 2026) - *LLM 출력을 원자적 주장으로 나누고 일차 논리로 형식화한 뒤, SMT solver로 일관성을 검증해 답을 반복해서 다듬는 neurosymbolic 프레임워크로, 여러 모델의 합의를 활용한다.*
- **[TREK: A Travel Reasoning and Evaluation Kit for LLM Agents in Complex Trip Planning](https://arxiv.org/abs/2607.26977)** (Qi et al., arXiv 2026) - *LLM 심판 대신 결정론적 규칙 기반 평가기로 채점하는 여행 계획 벤치마크다. 에이전트 15개 중 가장 강한 것도 풀 수 있는 과제의 46.2%에서만 완전히 실행 가능한 일정을 내놓는다.* [[code](https://github.com/TonyQJH/TREK-A-Travel-Reasoning-and-Evaluation-Kit-for-LLM-Agents-in-Complex-Trip-Planning)]
- **[PRO-LONG: Programmatic Memory Enables Long-Horizon Reasoning](https://arxiv.org/abs/2607.20064)** (Fox et al., arXiv 2026) - *구조화된 상호작용 로그를 전부 보관하고 코딩 에이전트로 이를 검색하게 하면, ARC-AGI-3에서 기본 코딩 에이전트보다 18점 높아지고 전문 harness와 맞먹는 성능을 4.2-5.8배 적은 토큰으로 낸다.* [[code](https://github.com/alexisfox7/PRO-LONG)]
- **[The Physics of Multi-Turn Long-Horizon Planning: From Pre-training to Post-training via Single- and Multi-Teacher On-Policy Agentic Distillation](https://arxiv.org/abs/2607.24720)** (Men et al., arXiv 2026) - *Long-horizon 계획 능력이 어디서 오는지 통제된 조건에서 살핀다. 사전학습 단계의 CoT 상태 전이 모델링이 가장 잘 일반화되고, 최적이 아닌 trajectory는 비례 이상으로 해를 끼치며, 여러 교사를 쓰는 distillation은 서로 맞는 계획 패턴만 합친다.*
- **[SearchMaster: Grounded and Regulated Self-Play for Search Agents](https://arxiv.org/abs/2608.01822)** (Tan et al., arXiv 2026) - *검색 에이전트를 위한 self-play로, 스스로 만든 데이터가 학습을 잘못 이끄는 세 가지 경우를 짚고 각각 대응책을 둔다. 가짜 multi-hop 질문은 증거 사슬로 막고, 난이도는 성공률이 아니라 검색 깊이로 매기며, 에이전트가 끝내 쓰지 않는 문서를 열면 페널티를 준다.* [[code](https://github.com/WentaoTan/SearchMaster)]
- **[R³-Bench: LLMs Struggle with Resource-Rational Reasoning under Shared Budgets](https://arxiv.org/abs/2608.16033)** (Wang et al., arXiv 2026) - *여섯 문제로 된 묶음이 연산 예산 하나를 나눠 쓰는 조건을 둔다. 같은 모델의 단일 문제 응답 곡선을 조건을 맞춰 모아 오프라인 oracle을 만들면, 이 oracle은 72개 칸 모두에서 모델의 실제 묶음 점수와 같거나 높았고 71개 칸에서는 엄밀히 더 높았다. 단일 문제에서 보여 준 역량과 예산을 나눠 써야 할 때 실제로 내는 성과 사이에 차이가 있다는 뜻이다. Trajectory 진단에서는 모델이 전략을 거의 고쳐 나가지 못했다.* [[code](https://github.com/NineAbyss/R-3-Bench)]
- **[Second Thought: Reasoning in Parallel as LLM Agents Act and Observe](https://arxiv.org/abs/2608.13667)** (Sun et al., arXiv 2026) - *ReAct 에이전트가 환경의 응답을 기다리는 유휴 구간에 보조 추론 가지 네 개를 분기했다가 관측 시점에 다시 합친다. 모델·벤치마크 조합 아홉 개 모두에서 턴 수를 줄였고, 그중 여섯 개에서는 메인 스레드 디코딩을 최대 43%까지 줄였으며, 아홉 개 중 일곱 개에서 Pass@1은 통계적으로 변화가 없었다.*
- **[CHIME: Credit-Aware Hierarchical Memory Evolution for Long-Horizon Agentic Planning](https://arxiv.org/abs/2609.02074)** (Ye et al., arXiv 2026) - *계획 저장소와 실행 저장소를 따로 두고, 무엇이든 기록하기 전에 각 과제의 결과를 계획, 실행, 둘 다, 둘 다 아님 중 어디에 돌릴지 먼저 가린다. 최종 결과만 보는 피드백은 계획의 질을 실행 오류나 환경 노이즈와 뒤섞는다는 논리다. 그렇게 만든 메모리는 더 작고, 학습된 가치는 이후의 실제 유용성을 잘 따라가며, 계획 메모리가 실행 메모리보다 가치가 높게 나온다. 백본 모델이 바뀌어도 그대로 옮겨 쓸 수 있다.*
- **[Do GUI Agents Know When Not to Act? Enabling Conflict-Aware Termination for Multimodal GUI Agents](https://arxiv.org/abs/2609.03438)** (Huang et al., arXiv 2026) - *행동하는 결정이 아니라 멈추는 결정을 벤치마크로 잰다. 스스로 모순되는 지시와 화면 내용과 모순되는 지시를 모두 다루며, 실행 쪽으로 치우친 과잉 순응을 발견한다. 실행 가능한 과제에서 점수가 좋은 에이전트도 지시가 충돌하는 과제에서는 계속 실행한다. 추론 시점의 실행 가능성 점검에 행동 조절을 더하면 에이전트 다섯 개 모두에서 이 문제가 줄고, 일반 과제 성능도 떨어지지 않는다.*
- **[Steer, Don't Solve: Training Small Critic Models for Large Code Agents](https://arxiv.org/abs/2606.21811)** (Gandhi et al., arXiv 2026) - *4B·8B critic 모델을 SFT와 DPO로 학습시켜, 코딩 에이전트의 trajectory에서 오류를 찾고 추론 시점에 몇 단계마다 상위 수준의 방향을 제시하게 한다. 행동을 직접 생성하지는 않는다. 이 critic은 더 큰 에이전트 여섯 개의 SWE-bench Verified 해결률을 높였는데, GLM-4.7-Flash-30B-A3B는 16.0점, GPT-OSS-120B는 14.4점 올랐다. 에이전트가 더 적은 단계로 끝나는 경우에는 조언에 드는 비용을 감안해도 전체 비용이 줄어, GPT-OSS-20B의 예시당 비용이 $0.07에서 $0.03이 되었다.* [[code](https://github.com/shubhamrgandhi/critic-training)]
- **[Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners (KnowNo)](https://arxiv.org/abs/2307.01928)** (Ren et al., CoRL 2023) - *LLM planner가 내놓은 다음 단계 후보에 conformal prediction을 적용해, 임계값을 통과한 단계가 둘 이상일 때만 로봇이 사람에게 묻게 한다. 사람의 도움을 최소로 유지하면서 작업 완수에 통계적 보장을 준다.*
- **[Real-Time Detection and Repair of LLM Agent Failures](https://arxiv.org/abs/2608.02464)** (Dubey, arXiv 2026) - *에이전트보다 비용이 더 드는 단계별 LLM 판정 대신, 단계당 약 200마이크로초가 드는 텔레메트리 모니터와 결정론적 재계산 점검을 쓴다. 문제가 표시된 실행은 되돌려 과제 성공률을 52%에서 73%로 끌어올렸다. 다만 모니터는 배포마다 다시 calibration해야 한다.* [[code](https://github.com/sunnydubey1111/agent-trajectory-sentinel)]
</details>

<sub><a href="#contents">↑ 목차로 돌아가기</a></sub>

<a id="memory"></a>
### 💾 메모리 (56)
*서베이 §5(메모리)에 해당합니다.*

<details>
<summary><b>논문 56편 보기</b></summary>

- **[RET-LLM: Towards a General Read-Write Memory for Large Language Models](https://arxiv.org/abs/2305.14322)** (Modarressi et al., arXiv 2023) - *Triplet 기반의 구조화된 읽기·쓰기 메모리를 일찍 내놓아 영향력이 컸던 설계로, 이후 그래프·KG 기반 에이전트 메모리 시스템의 전신이 되었다.*
- **[MemoryBank: Enhancing Large Language Models with Long-Term Memory](https://arxiv.org/abs/2305.10250)** (Zhong et al., AAAI 2024) - *심리학에 근거한(사람의 기억에서 착안한) 망각·공고화 메커니즘을 LLM 에이전트 메모리에 처음 들여온 시스템 가운데 하나이다.* [[code](https://github.com/zhongwanjun/MemoryBank-SiliconFriend)]
- **[Augmenting Language Models with Long-Term Memory](https://arxiv.org/abs/2306.07174)** (Wang et al., NeurIPS 2023) - *에이전트 scaffold만이 아니라 바탕이 되는 언어 모델 자체에 학습 가능한 long-term memory 검색 메커니즘을 주는 핵심 아키텍처 접근이다.* [[code](https://github.com/Victorwz/LongMem)]
- **[Synapse: Trajectory-as-Exemplar Prompting with Memory for Computer Control](https://arxiv.org/abs/2306.07863)** (Zheng et al., ICLR 2024) - *검색으로 보강한 episodic trajectory 메모리를 써서, 복잡한 GUI·컴퓨터 제어 과제에서 에이전트의 의사결정을 grounding하는 방법을 보여 준다.* [[code](https://github.com/ltzheng/Synapse)]
- **[ExpeL: LLM Agents Are Experiential Learners](https://arxiv.org/abs/2308.10144)** (Zhao et al., AAAI 2024) - *지난 에피소드를 그대로 재생하는 대신, 에이전트 자신의 메모리에서 재사용하고 다른 과제로 옮길 수 있는 '경험' 지식을 뽑아내는 패러다임으로 영향력이 컸다.* [[code](https://github.com/LeapLabTHU/ExpeL)]
- **[Walking Down the Memory Maze: Beyond Context Limit through Interactive Reading (MemWalker)](https://arxiv.org/abs/2310.05029)** (Chen et al., arXiv 2023) - *트리 구조(계층형) 메모리를 따라 내려가며 읽는 방식으로, 긴 컨텍스트 모델링과 agentic 메모리 검색을 이어 준 영향력 있는 접근이다.*
- **[MemGPT: Towards LLMs as Operating Systems](https://arxiv.org/abs/2310.08560)** (Packer et al., COLM 2024) - *LLM 에이전트가 여러 계층으로 나뉜 long-term memory를 스스로 관리하게 하는 아키텍처로, 가장 널리 인용되고 제품화(Letta)된 것 가운데 하나이다.* [[code](https://github.com/cpacker/MemGPT)]
- **[Think-in-Memory: Recalling and Post-thinking Enable LLMs with Long-Term Memory](https://arxiv.org/abs/2311.08719)** (Liu et al., arXiv 2023) - *원문 텍스트 대신 추론 trace를 저장해, 메모리를 단순히 회상할 때 생기는 추론 불일치 문제를 다룬다. 이후의 'reflective retrieval' 메모리 설계에 영향을 주었다.*
- **[Evaluating Very Long-Term Conversational Memory of LLM Agents](https://arxiv.org/abs/2402.17753)** (Maharana et al., ACL 2024) - *LLM 에이전트의 대화용 long-term memory 시스템을 평가하고 비교할 때 쓰는 표준 벤치마크로, Mem0, MIRIX, A-MEM 등이 이것으로 평가한다.* [[code](https://github.com/snap-research/locomo)]
- **[Larimar: Large Language Models with Episodic Memory Control](https://arxiv.org/abs/2403.11901)** (Das et al., ICML 2024) - *프롬프트 수준이 아니라 아키텍처 수준에서 LLM에 편집할 수 있고 빠르게 갱신되는 episodic memory를 주는 접근의 대표 사례이다.* [[code](https://github.com/IBM/larimar)]
- **[HippoRAG: Neurobiologically Inspired Long-Term Memory for Large Language Models](https://arxiv.org/abs/2405.14831)** (Gutiérrez et al., NeurIPS 2024) - *신경생물학에서 착안한 long-term memory·RAG 프레임워크로, 지식 그래프 검색과 에이전트 메모리를 이어 큰 영향을 주었고 강한 baseline으로 널리 쓰인다.* [[code](https://github.com/OSU-NLP-Group/HippoRAG)]
- **[On the Structural Memory of LLM Agents](https://arxiv.org/abs/2412.15266)** (Zeng et al., arXiv 2024) - *메모리 구조를 짜는 여러 선택지를 통제된 실험으로 비교한다. 서베이가 에이전트 메모리 설계의 득실을 논할 때 기댈 만한 근거가 된다.*
- **[A-MEM: Agentic Memory for LLM Agents](https://arxiv.org/abs/2502.12110)** (Xu et al., arXiv 2025) - *최신 세대 LLM 에이전트 long-term memory 시스템의 대표 사례로, 노트를 그래프로 서로 이어 가며 메모리가 스스로 동적으로 조직된다.* [[code](https://github.com/WujiangXu/A-mem)]
- **[From Human Memory to AI Memory: A Survey on Memory Mechanisms in the Era of LLMs](https://arxiv.org/abs/2504.15965)** (Wu et al., arXiv 2025) - *심리학에 기반한 분류 체계를 제시하는 최근의 포괄적인 하위 주제 서베이로, 더 넓은 LLM 에이전트 서베이가 메모리 문헌을 정리할 때 인용할 수 있다.*
- **[Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://arxiv.org/abs/2504.19413)** (Chhikara et al., arXiv 2025) - *실서비스를 겨냥해 널리 배포된 대표적인 LLM 에이전트 long-term memory 시스템으로, 최고 수준 성능의 비교 기준으로 자주 쓰인다.* [[code](https://github.com/mem0ai/mem0)]
- **[MIRIX: Multi-Agent Memory System for LLM-Based Agents](https://arxiv.org/abs/2507.07957)** (Wang et al., arXiv 2025) - *LLM 기반 에이전트를 위한 다중 에이전트·다중 유형(multimodal) 메모리 아키텍처로, 이 방향의 최신 연구 흐름을 보여 주는 사례다.* [[code](https://github.com/Mirix-AI/MIRIX)]
- **[LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory](https://arxiv.org/abs/2410.10813)** (Wu et al., ICLR 2025) - *상호작용 속 long-term memory를 따로 시험할 수 있는 다섯 가지 능력으로 나눈다.* [[code](https://github.com/xiaowu0162/LongMemEval)]
- **[ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory](https://arxiv.org/abs/2509.25140)** (Ouyang et al., arXiv 2025) - *성공한 trajectory와 실패한 trajectory 양쪽에서 전략 수준의 메모리를 뽑아내, 연이어 들어오는 과제를 풀면서 에이전트가 자기 진화하게 한다.*
- **[Memory OS of AI Agent](https://arxiv.org/abs/2506.06326)** (Kang et al., EMNLP 2025) - *운영체제의 메모리 관리(STM/MTM/LPM 계층, heat 점수에 따른 승격, 세그먼트 단위 페이징)를 에이전트 메모리에 적용해 LoCoMo에서 큰 폭으로 개선했다.* [[code](https://github.com/BAI-LAB/MemoryOS)]
- **[Zep: A Temporal Knowledge Graph Architecture for Agent Memory](https://arxiv.org/abs/2501.13956)** (Rasmussen et al., arXiv 2025) - *대화와 비즈니스 데이터를 동적으로 합치는 bi-temporal 지식 그래프 메모리 엔진(Graphiti)이다. DMR과 LongMemEval에서 MemGPT를 앞섰고, 실서비스 메모리의 표준 참고 사례로 꼽힌다.* [[code](https://github.com/getzep/graphiti)]
- **[What Deserves Memory: Adaptive Memory Distillation for LLM Agents](https://arxiv.org/abs/2508.03341)** (Ma et al., ACL 2026) - *대화를 사건 경계에서 나누고, 먼저 예측한 뒤 calibration하는 루프로 의미 정보를 뽑아내는 자기 조직형 episodic memory(Nemori)이다. 구축 비용을 줄이면서 시간 추론도 개선했다.* [[code](https://github.com/nemori-ai/nemori)]
- **[MemOS: A Memory OS for AI System](https://arxiv.org/abs/2507.03724)** (Li et al., arXiv 2025) - *메모리를 일급 자원(MemCube)으로 다루고, 파라미터 메모리, 활성값 메모리, 평문 메모리를 스케줄링과 거버넌스를 맡는 하나의 운영체제로 통합한다.* [[code](https://github.com/MemTensor/MemOS)]
- **[G-Memory: Tracing Hierarchical Memory for Multi-Agent Systems](https://arxiv.org/abs/2506.07398)** (Zhang et al., NeurIPS 2025) - *조직 이론에서 착안한 세 계층 그래프(통찰, 질의, 상호작용)에 협업 trajectory를 저장한다. 다중 에이전트 시스템에 맞춘 메모리 설계이다.* [[code](https://github.com/bingreeky/GMemory)]
- **[Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models](https://arxiv.org/abs/2510.04618)** (Zhang et al., ICLR 2026) - *생성, reflection, 정리로 이어지는 delta 연산으로 컨텍스트 자체를 playbook처럼 계속 고쳐 쓰며, 자기 개선 에이전트에서 생기는 간결성 편향과 컨텍스트 붕괴를 막는다.* [[code](https://github.com/ace-agent/ace)]

- **[SimpleMem: Efficient Lifelong Memory for LLM Agents](https://arxiv.org/abs/2601.02553)** (Liu et al., arXiv 2026) - *의미 압축 기반 평생 메모리(구조화된 압축, 온라인 종합, 의도를 반영한 검색)로 추론 토큰을 최대 30배 줄인다.* [[code](https://github.com/aiming-lab/SimpleMem)]
- **[PlugMem: A Task-Agnostic Plugin Memory Module for LLM Agents](https://arxiv.org/abs/2603.03296)** (Yang et al., arXiv 2026) - *인지과학에서 착안한 지식 그래프 메모리로, 다시 설계하지 않고도 여러 과제에 끼워 쓸 수 있다.* [[code](https://github.com/TIMAN-group/PlugMem)]
- **[Memanto: Typed Semantic Memory with Information-Theoretic Retrieval for Long-Horizon Agents](https://arxiv.org/abs/2604.22085)** (Abtahi et al., arXiv 2026) - *13개 범주로 타입을 나눈 메모리 스키마에 정보 이론 기반 단일 질의 검색을 더해 LongMemEval과 LoCoMo에서 SOTA를 기록했다.*
- **[MINTEval: Evaluating Memory under Multi-Target Interference in Long-Horizon Agent Systems](https://arxiv.org/abs/2605.18565)** (Lee et al., arXiv 2026) - *QA 15.6K개로 이루어진 벤치마크(컨텍스트 최대 1.8M 토큰)로, 서로 간섭하며 자주 갱신되는 사실을 메모리 에이전트가 잘 다루지 못한다는 것을 보여 준다.* [[code](https://github.com/amy-hyunji/MINTEval)]
- **[What to Keep, What to Forget: A Rate-Distortion View of Memory Compaction in LLMs and Agents](https://arxiv.org/abs/2607.08032)** (Colaco et al., arXiv 2026) - *컨텍스트 압축을 rate-distortion 관점으로 정식화해, 무엇을 남기고 무엇을 잊을지를 휴리스틱이 아니라 명시적인 왜곡 예산으로 정한다.*
- **[AutoMem: Automated Learning of Memory as a Cognitive Skill](https://arxiv.org/abs/2607.01224)** (Wu et al., arXiv 2026) - *메모리 관리를 harness가 정해 둔 고정 검색 정책이 아니라 에이전트가 배우는 skill로 다룬다.* [[code](https://github.com/autoLearnMem/AutoMem)]
- **[TokenPilot: Cache-Efficient Context Management for LLM Agents](https://arxiv.org/abs/2606.17016)** (Xu et al., arXiv 2026) - *프롬프트 캐시를 염두에 두고 컨텍스트를 관리해, 내용을 밀어낼 때도 캐시 연속성을 지켜 비용을 줄인다.* [[code](https://github.com/zjunlp/LightMem2)]
- **[Self-GC: Self-Governing Context for Long-Horizon LLM Agents](https://arxiv.org/abs/2607.00692)** (Hao et al., arXiv 2026) - *Long-horizon 작업 내내 에이전트가 자기 컨텍스트를 스스로 관리하게 한다. 정해진 주기로 압축하지 않고 언제 압축할지를 직접 고른다.*
- **[MemSyco-Bench: Benchmarking Sycophancy in Agent Memory](https://arxiv.org/abs/2607.01071)** (Xiang et al., arXiv 2026) - *에이전트 메모리의 아첨 성향, 곧 저장된 믿음이 여러 세션에 걸친 사용자의 압력에 따라 바뀌는지를 재는 벤치마크이다.* [[code](https://github.com/XMUDeepLIT/MemSyco-Bench)]
- **[Remember the Decision, Not the Description: A Rate-Distortion Framework for Agent Memory](https://arxiv.org/abs/2605.10870)** (Zou et al., arXiv 2026) - *에이전트 메모리를 rate-distortion 관점으로 정식화해, 명시적인 왜곡 예산 안에서 설명이 아니라 결정을 남긴다.*
- **[LongMemEval-V2: Evaluating Long-Term Agent Memory Toward Experienced Colleagues](https://arxiv.org/abs/2605.12493)** (Wu et al., arXiv 2026) - *짧은 컨텍스트 질의응답을 넘어, 경험 많은 동료 같은 에이전트를 겨냥한 long-term memory 벤치마크이다.*
- **[Experience Compression Spectrum: Unifying Memory, Skills, and Rules in LLM Agents](https://arxiv.org/abs/2604.15877)** (Zhang et al., arXiv 2026) - *메모리, skill, 규칙을 별개의 메커니즘이 아니라 하나의 경험 압축 스펙트럼 위의 점으로 통합한다.*
- **[PLACEMEM: Toward a Compute-Aware Memory Plane for Lifelong Agents](https://arxiv.org/abs/2607.04089)** (Ganguly et al., arXiv 2026) - *평생 동작하는 에이전트를 위한 메모리 플레인 PLACEMEM을 제안한다. 버전이 붙은 캡슐이 의미, provenance, 유효성을 정정 이력을 반영하는 식별자 아래 하나로 묶는다.*
- **[COMFYCLAW: Self-Evolving Skill Harnesses for Image Generation Workflows](https://arxiv.org/abs/2607.01709)** (Li et al., arXiv 2026) - *이미지 생성 workflow를 구축하는 agentic 프레임워크를 제안한다. Workflow 구축을 타입이 지정된 그래프를 편집하는 문제로 정식화하고, vision-language model로 시각적 오류를 찾아 고치며, 지난 실행을 distillation으로 정리해 재사용할 skill을 라이브러리에 계속 추가한다. 에이전트 구성 여섯 가지 모두에서 평균 점수가 가장 높고, skill 진화 없이 검증기만 쓰는 baseline도 앞선다.*
- **[The Past Is Prologue: A Plug-in Controller for Selective Updates in Sequentially Evolving LLM Memory](https://arxiv.org/abs/2606.31121)** (Chen et al., arXiv 2026) - *기존 LLM 에이전트 메모리 갱신기를 감싸 후보 갱신 하나하나를 받아들일지 거부할지 정하는, 방법에 구애받지 않는 제어기 Janus를 제안한다.*
- **[E-mem: Multi-agent based Episodic Context Reconstruction for LLM Agent Memory](https://arxiv.org/abs/2601.21714)** (Wang et al., arXiv 2026) - *E-mem은 계층형 다중 에이전트 메모리 프레임워크이다. 보조 에이전트들이 압축하지 않은 메모리 조각을 보관하고, 마스터 에이전트가 계획을 조율해 episodic 컨텍스트를 재구성한다. LoCoMo 벤치마크로 평가했다.* [[code](https://github.com/dog-last/E-mem)]
- **[AMV-L: Lifecycle-Managed Agent Memory for Tail-Latency Control in Long-Running LLM Systems](https://arxiv.org/abs/2603.04443)** (Bamidele et al., arXiv 2026) - *메모리 항목마다 계속 갱신되는 효용 점수를 매기고, 그 가치에 따라 항목을 승격, 강등, 퇴출해 검색 대상을 정해진 크기의 후보 집합 안에 묶어 두는 에이전트 메모리 시스템 AMV-L을 제안한다. TTL 기반 보존과 비교해 처리량을 3.1배 높이고 지연 시간 중앙값을 4.2배 줄이며, 이 이득은 프롬프트가 짧아져서가 아니라 검색 작업량에 상한을 둔 데서 나온다.*
- **[From Raw Experience to Skill Consumption: A Systematic Study of Model-Generated Agent Skills](https://arxiv.org/abs/2605.23899)** (Huang et al., arXiv 2026) - *모델이 생성한 LLM 에이전트 skill을 대상으로, 경험 생성, skill 추출, skill 활용까지 아우르는 효용 기반 평가 프레임워크를 제시한다.*
- **[MemFail: Stress-Testing Failure Modes of LLM Memory Systems](https://arxiv.org/abs/2605.26667)** (Garg et al., arXiv 2026) - *LLM 에이전트가 쓰는 외부 메모리 시스템의 요약, 저장, 검색 실패 유형을 따로 떼어 극한 조건에서 시험하는 진단 벤치마크 MemFail을 내놓는다. 네 가지 과제에 걸친 다섯 개 데이터셋으로 이루어져 있다.*
- **[Filesystem-Based Memory for LLM Agents: Organization, Evolution, and Sustainability](https://arxiv.org/abs/2607.26637)** (Zhou et al., arXiv 2026) - *실제로 배포되는 에이전트가 쓰는 markdown 디렉터리 메모리는 검색 비용을 줄여 주지만(큰 자료에서 대략 절반) 답의 질을 높이지는 못하고, 저장소가 커질수록 구조가 제대로 유지되지 않는다는 것을 밝혔다.*
- **[Keep It InMind: Benchmarking the Implicit-Association Blind Spot in Agent Memory](https://arxiv.org/abs/2607.24368)** (Li et al., arXiv 2026) - *필요한 사실이 질의와 닮지 않았을 때 메모리가 실패한다는 것을 보인다. 메모리를 컨텍스트에 넣어 주면 백본 모델은 간접 질문의 84.0%에 답하지만, 검색 시스템 여섯 개는 많아야 14.4%에 그친다.*
- **[Metis: Memory Foundation Model](https://arxiv.org/abs/2607.26760)** (Zhang et al., arXiv 2026) - *메모리를 외부 모듈이 아니라 백본 안으로 옮긴다. Gradient 없이 forward pass 한 번으로 유지되는 고유한 메모리 상태를 두고, 추론 때는 가중치를 고정하며, 체크포인트도 공개했다.*
- **[When Memory Lies: An Empirical Study of Spatial Memory Staleness in VLM Agents](https://arxiv.org/abs/2608.04574)** (Sun et al., arXiv 2026) - *확신도가 높게 저장된 메모리가 에이전트가 직접 보는 것과 어긋날 때 무슨 일이 생기는지 잰다. 같은 격자에서도 시각 F1은 0.887에서 0.067까지 벌어지고, 메모리를 그대로 믿는 에이전트는 메모리를 아예 받지 않은 같은 에이전트보다 두 배 넘게 자주 죽는다.*
- **[Caching for the Future: Scrub Jay Episodic Memory Principles for Agent Memory Systems](https://arxiv.org/abs/2608.04746)** (Bhandari et al., arXiv 2026) - *덤불어치의 episodic memory에서 유형에 따른 망각을 빌려 와, 저장 항목마다 부패도 계수와 효용 유지 기간을 붙여 낡은 사실이 검색에서 서서히 빠지게 한다. 감쇠 항을 빼면 일반화 성능이 5.7배 떨어진다.*
- **[What Does Context Compression Cost an Agent? Interaction Costs Unrevealed by Task-Completion Metrics](https://arxiv.org/abs/2608.16370)** (Liu, arXiv 2026) - *과제 완료율이 통계적으로 그대로인 압축도, 에이전트가 잃어버린 상태를 다시 가져오느라 검색 호출을 대략 세 배로 늘릴 수 있다(GPT-5.5는 완료율이 80%에서 85%로 바뀌어 p = 1.0이지만, 검색은 21.0회에서 63.9회로 늘어 p = .002). 같은 슬라이딩 압축이 ALFWorld에서는 검색 급증을 만들지 않으므로, 이 현상은 환경에 따라 다르다.*
- **[When Your Agent Opens the Chat App: Agent-Controlled Search over Raw Chat Logs Rivals Structured Memory](https://arxiv.org/abs/2608.12888)** (Li et al., arXiv 2026) - *손대지 않은 대화 기록을 턴 단위 어휘 색인으로만 두고(요약, 임베딩, 트리, 그래프를 미리 만들지 않음) 키워드 검색을 반복하는 루프를 준 에이전트가, 비교한 모든 시스템 가운데 평균 정확도가 가장 높았다(58.2, HippoRAG 2는 53.2). MemoryAgentBench의 점진적 다중 턴 설정에서 약 2,800개 질문을 같은 GPT-4o-mini 백본으로 비교한 결과이다.*
- **[ForeDreamer: A Self-Evolving Dual-Agent Memory Architecture for Future Event Prediction](https://arxiv.org/abs/2608.20920)** (Zhong et al., EMNLP Findings 2026) - *검색 결과를 에이전트에 바로 넣지 않고, 예측에 앞서 가공하지 않은 웹 근거를 구조화된 메모리로 바꾼다. 질문별 사실 메모리와 예측 에피소드를 넘어 이어지는 경험 메모리를 나누어 앞의 것은 메모리 하위 에이전트가 만들고, 두 갈래의 진화 과정이 예측과 메모리 구축을 함께 개선한다. Prophet Arena와 FutureX에서 평가했다.* [[code](https://github.com/zhongzero/ForeDreamer)]
- **[Corpus2Skill: Distilling Enterprise Knowledge into Navigable Agent Skills for QA and RAG](https://arxiv.org/abs/2604.14572)** (Sun et al., EMNLP Findings 2026) - *질문마다 새 질의를 던지는 대신, 오프라인 컴파일러가 코퍼스를 계층형 skill 디렉터리로 정리해 두고 에이전트가 서비스 시점에 이를 탐색한다. 전체 개요에서 시작해 더 세밀한 요약을 거쳐 문서까지 내려가고, 막다른 가지에서는 되돌아 나온다. 열한 개 데이터셋에서 이 탐색 방식은 만능 대체재가 아니었는데, 다섯 곳에서 이기고 세 곳에서 비기고 세 곳에서 졌다. 이득은 주제 분류 체계를 복원할 수 있는 단일 도메인 코퍼스에 몰렸고, 개방형 도메인의 단답형 사실 질문 모음에서는 여전히 계층 없는 평면 검색이 낫다.* [[code](https://github.com/dukesun99/Corpus2Skill)]
- **[Does Your Agent's Memory Survive a Model Upgrade? A Controlled Study of Memory Portability](https://arxiv.org/abs/2609.05339)** (Goyal et al., arXiv 2026) - *저장된 이력은 그대로 두고 모델만 바꿔, 업그레이드 뒤에도 메모리를 제대로 쓸 수 있는지는 메모리 형식에 달려 있음을 보인다. 고정 스키마 지식 그래프는 정확도가 0.0004포인트 움직이는 데 그치지만, 모델이 압축한 노트는 마이그레이션 방향에 따라 +9.91 또는 -13.28포인트로 비대칭적으로 달라진다. 절반만 마이그레이션한 임베딩 색인은 전체 재임베딩이 되찾는 11.90포인트 가운데 4.96포인트만 회복하고, 원본을 남겨 두지 않았다면 노트를 저장소 안에서만 고치는 방식은 48개 이력 모두에서 90% 회복 목표에 못 미친다.*
- **[The Memory Trust Gap: Capability-Dependent Failures in Persistent-Memory Agents](https://arxiv.org/abs/2609.01852)** (Hu et al., arXiv 2026) - *메모리가 유일한 출처인 경우와 권위 있는 도구가 올바른 값을 가진 경우를 나누고, 실패의 원인을 혼동이 아니라 과신으로 해석한다. 메모리밖에 없을 때 모델은 0.92에서 1.00의 비율로 낡은 저장값에 기대 답한다. 함정 조건의 피해는 능력에 따라 갈려서, Qwen3 크기 계열 가운데 큰 모델일수록 낡은 노트를 최신 정보처럼 꾸며 놓았을 때 성능이 더 크게 떨어진다.*
- **[Dual-Layer Agentic Memory with Fast Write Routing and Slow Consolidation](https://arxiv.org/abs/2608.22215)** (Li et al., arXiv 2026) - *메모리 쓰기를 매번 세 갈래 선택(건너뛰기, 새로 쓰기, 갱신)으로 바꾸고, 1.7B에서 8B로 이어지는 cascade가 이 선택을 맡는다. 중복 메모리를 최대 68% 걷어 내면서 입력의 절반 미만만 escalation하고, 전부 남길 때의 exact match를 98% 넘게 유지한다.*
- **[Jev-Mem: System-One-Controlled Agentic Memory for Efficient AI Agents](https://arxiv.org/abs/2609.23986)** (Jiang et al., arXiv 2026) - *메모리 유형 분류, 라우팅, 그래프 탐색, 멈출 시점 판단을 Jev에 맡기고, LLM은 돌아온 결과를 두고 추론할 때만 부른다. 가장 빠른 baseline보다 LoCoMo 메모리를 6.6배 빨리 구축하고 0.777 대 0.700으로 앞서는데, 그 차이의 대부분은 적대적 질문에서 나온다.* [[code](https://github.com/libingzheren/Jev-Mem)]
</details>

<sub><a href="#contents">↑ 목차로 돌아가기</a></sub>

<a id="tools"></a>
### 🔧 도구 사용 (46)
*서베이 §6(도구 사용과 행동 실행)에 해당합니다.*

<details>
<summary><b>논문 46편 보기</b></summary>

- **[TALM: Tool Augmented Language Models](https://arxiv.org/abs/2205.12255)** (Parisi et al., arXiv 2022) - *언어 모델이 자기 지도 방식으로 도구 사용을 스스로 익히게 하는 초기 정식화로 영향력이 컸고, Toolformer의 자기 지도 접근에 앞서 같은 방향을 제시했다.*
- **[API-Bank: A Comprehensive Benchmark for Tool-Augmented LLMs](https://arxiv.org/abs/2304.08244)** (Li et al., EMNLP 2023) - *도구로 보강한 대화형 LLM을 평가하고 학습시키는 전용 벤치마크 가운데 가장 이르고 가장 많이 인용된 것 중 하나이다.* [[code](https://github.com/AlibabaResearch/DAMO-ConvAI)]
- **[Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models](https://arxiv.org/abs/2304.09842)** (Lu et al., NeurIPS 2023) - *성격이 다른 여러 도구를 자연어로 세운 계획에 따라 조합하고 조율하는 대표 사례로, 도구 사용과 조합 추론 문헌에서 널리 인용된다.* [[code](https://github.com/lupantech/chameleon-llm)]
- **[Large Language Models as Tool Makers](https://arxiv.org/abs/2305.17126)** (Cai et al., arXiv 2023) - *도구 사용이 아닌 도구 제작이라는 방향의 토대가 된 연구로, LLM이 이미 있는 도구를 부르는 데 그치지 않고 재사용할 도구를 직접 만들 수 있음을 보였다.* [[code](https://github.com/ctlllll/LLM-ToolMaker)]
- **[GPT4Tools: Teaching Large Language Model to Use Tools via Self-instruction](https://arxiv.org/abs/2305.18752)** (Yang et al., NeurIPS 2023) - *Multimodal 도구 사용을 오픈소스 instruction tuning으로 푸는 접근에서 널리 쓰이는 참고 문헌으로, 상용 모델 기반 도구 사용 논문들을 보완한다.* [[code](https://github.com/StevenGrove/GPT4Tools)]
- **[ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings](https://arxiv.org/abs/2305.11554)** (Hao et al., NeurIPS 2023) - *프롬프트에 도구 목록을 늘어놓는 방식의 컨텍스트 길이 병목을 피하면서 도구 선택을 확장하는, 영향력 있는 대안 아키텍처이다.* [[code](https://github.com/Ber666/ToolkenGPT)]
- **[ToolAlpaca: Generalized Tool Learning for Language Models with 3000 Simulated Cases](https://arxiv.org/abs/2306.05301)** (Tang et al., arXiv 2023) - *자동으로 합성한 도구 사용 코퍼스로 작은 공개 모델도 일반화된 도구 사용 능력을 얻을 수 있다는 핵심 근거로, 이후 합성 데이터 기반 도구 학습 파이프라인에 영향을 주었다.* [[code](https://github.com/tangqiaoyu/ToolAlpaca)]
- **[RestGPT: Connecting Large Language Models with Real-World RESTful APIs](https://arxiv.org/abs/2306.06624)** (Song et al., arXiv 2023) - *단순한 예제 수준의 도구 모음을 넘어, 상태를 가진 복잡한 실제 REST API로 도구 사용을 넓혀 보였다. 함께 낸 벤치마크는 지금도 API 기반 에이전트 평가에 쓰인다.* [[code](https://github.com/Yifan-Song793/RestGPT)]
- **[ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world APIs](https://arxiv.org/abs/2307.16789)** (Qin et al., ICLR 2024) - *가장 크고 많이 인용된 도구 사용 데이터셋이자 프레임워크 가운데 하나로, ToolBench를 오픈소스 도구 사용 LLM의 표준 학습·평가 자원으로 자리 잡게 했다.* [[code](https://github.com/OpenBMB/ToolBench)]
- **[Tool Documentation Enables Zero-Shot Tool-Usage with Large Language Models](https://arxiv.org/abs/2308.00675)** (Hsieh et al., arXiv 2023) - *도구 사용을 끌어내는 수단을 시연이 아닌 문서 중심으로 다시 짠다. 도구 수를 크게 늘릴 때 중요하고 자주 인용되는 방법론적 통찰이다.*
- **[Small LLMs Are Weak Tool Learners: A Multi-LLM Agent](https://arxiv.org/abs/2401.07324)** (Shen et al., EMNLP 2024) - *도구 학습을 여러 에이전트의 역할로 쪼개는 접근에 영향을 주었고, 특히 작은 공개 모델에서 도구 사용을 효율적으로 배포하는 문제와 관련이 깊다.* [[code](https://github.com/X-PLUG/Multi-LLM-Agent)]
- **[StableToolBench: Towards Stable Large-Scale Benchmarking on Tool Learning of Large Language Models](https://arxiv.org/abs/2403.07714)** (Guo et al., ACL 2024) - *널리 쓰이는 평가 인프라 논문으로, 실제 API를 쓰는 대규모 도구 학습 벤치마크에 고질적으로 있던 재현성 문제를 해결했다.* [[code](https://github.com/THUNLP-MT/StableToolBench)]
- **[What Are Tools Anyway? A Survey from the Language Model Perspective](https://arxiv.org/abs/2403.15452)** (Wang et al., COLM 2024) - *언어 모델 관점에서 도구 사용만 다룬 서베이로, 더 넓은 LLM 에이전트 서베이가 하위 주제 서베이로 바로 인용할 수 있다.*
- **[ToolACE: Winning the Points of LLM Function Calling](https://arxiv.org/abs/2409.00920)** (Liu et al., arXiv 2024) - *작은 공개 모델이 function calling을 정확하게 하도록 합성 데이터 파이프라인으로 학습시키는 접근의 최신 수준을 대표하며, GPT-4에 견줄 만하다.*
- **[xLAM: A Family of Large Action Models to Empower AI Agent Systems](https://arxiv.org/abs/2409.03215)** (Zhang et al., arXiv 2024) - *'large action model'을 agentic 도구 사용에 최적화된 별도의 모델 부류로 자리 잡게 한 산업계(Salesforce)의 대표적 시도이다. 모델 다섯 개(1B에서 8x22B)는 공개 당시 Berkeley Function-Calling Leaderboard 맨 위에 올랐고, 이후 흔히 쓰이는 baseline이 되었다.* [[code](https://github.com/SalesforceAIResearch/xLAM)]
- **[The Berkeley Function Calling Leaderboard (BFCL): From Tool Use to Agentic Evaluation of Large Language Models](https://openreview.net/forum?id=2GmDdhBdDk)** (Patil et al., ICML 2025) - *LLM의 function calling과 도구 사용 성능을 비교하는 사실상 표준 순위표이자 벤치마크로, 이후 거의 모든 function calling 논문이 참조한다.* [[code](https://github.com/ShishirPatil/gorilla)]
- **[Model Context Protocol (MCP): Landscape, Security Threats, and Future Research Directions](https://arxiv.org/abs/2503.23278)** (Hou et al., arXiv 2025) - *서버 생애 주기 전반에 걸쳐 MCP 생태계의 보안을 분석한 연구로, 프로토콜 계층의 공급망 위험을 다룰 때 기준이 되는 문헌이다.*

- **[UniToolCall: Unifying Tool-Use Representation, Data, and Evaluation for LLM Agents](https://arxiv.org/abs/2604.11557)** (Liang et al., arXiv 2026) - *도구 호출 표현, 22K개 이상의 도구와 390K개 이상의 인스턴스로 이루어진 코퍼스, 표준화된 벤치마크 일곱 개를 하나의 프레임워크로 묶는다.* [[code](https://github.com/EIT-NLP/UniToolCall)]
- **[Skill Retrieval Augmentation for Agentic AI](https://arxiv.org/abs/2604.24594)** (Su et al., arXiv 2026) - *에이전트가 큰 라이브러리에서 필요할 때 skill을 찾아 적용하게 하고, 약 26K개 skill을 담은 SRA-Bench를 내놓는다.*
- **[ToolFailBench: Diagnosing Tool-Use Failures in LLM Agents](https://arxiv.org/abs/2607.04686)** (Soni et al., arXiv 2026) - *최종 과제 성공만 채점하지 않고, 도구 사용이 실패하는 방식을 유형별로 갈라 보는 진단 벤치마크이다.* [[code](https://github.com/SoHarshh/ToolFailBench)]
- **[Why Multi-Step Tool-Use Reinforcement Learning Collapses and How Supervisory Signals Fix It](https://arxiv.org/abs/2606.26027)** (Hao et al., arXiv 2026) - *다중 턴 도구 사용 RL이 왜 무너지는지, 어떤 지도 신호가 이를 막는지 밝힌다.* [[code](https://github.com/hypasd-art/Tool-RL-Box)]
- **[When Does Restricting a Coding Agent to execute_code Help? A Regime × Agent-Design Ablation](https://arxiv.org/abs/2607.10569)** (Yang et al., arXiv 2026) - *코딩 에이전트의 행동을 execute_code 하나로 좁히는 것이 언제 도움이 되고 어떤 조건에서 해가 되는지 묻는 ablation 연구이다.* [[code](https://github.com/hyang0129/onlycodes)]
- **[PACT: Privileged Trace Co-Training for Multi-Turn Tool-Use Agents](https://arxiv.org/abs/2606.16215)** (Du et al., arXiv 2026) - *다중 턴 도구 사용 에이전트를 privileged trace로 함께 학습시켜, 학습 때는 볼 수 있지만 추론 때는 없는 정보를 옮겨 준다.* [[code](https://github.com/ZhenbangDu/PACT)]
- **[PlanBench-XL: Evaluating Long-Horizon Planning of LLM Tool-Use Agents in Large-Scale Tool Ecosystems](https://arxiv.org/abs/2606.22388)** (Liu et al., arXiv 2026) - *검색과 선택이 성패를 좌우하는 대규모 도구 생태계에서 도구 사용 에이전트의 long-horizon 계획을 평가하는 벤치마크이다.* [[code](https://github.com/JiayuJeff/PlanBench-XL)]
- **[MCP-Atlas: A Large-Scale Benchmark for Tool-Use Competency with Real MCP Servers](https://arxiv.org/abs/2602.00933)** (Bandi et al., arXiv 2026) - *합성한 도구 stub 대신 실제 Model Context Protocol 서버 위에 세운 대규모 도구 사용 벤치마크이다.* [[code](https://github.com/scaleapi/mcp-atlas)]
- **[Model Context Protocol (MCP) Tool Descriptions Are Smelly! Towards Improving AI Agent Efficiency with Augmented MCP Tool Descriptions](https://arxiv.org/abs/2602.14878)** (Hasan et al., arXiv 2026) - *MCP 도구 설명에는 되풀이되는 품질 문제가 있고, 이를 고치면 에이전트의 도구 사용이 눈에 띄게 나아진다는 것을 보인다.*
- **[LLM Agents Already Know When to Call Tools -- Even Without Reasoning](https://arxiv.org/abs/2605.09252)** (Sun et al., arXiv 2026) - *에이전트가 명시적인 추론 trace 없이도 언제 도구를 불러야 하는지 이미 내부에 담고 있음을 발견해, 호출 전에 먼저 추론해야 한다는 관행에 의문을 던진다.* [[code](https://github.com/Trustworthy-ML-Lab/when2tool)]
- **[Tool-Making and Self-Evolving LLM Agents in Low-Latency Systems](https://arxiv.org/abs/2607.08010)** (Kujanpää et al., arXiv 2026) - *LLM 에이전트가 추론 시점에 돌리는 코드 생성 루프를, 반복되는 표준 운영 절차 단계를 검증과 버전 관리를 거친 도구로 컴파일하는 오프라인 agentic 도구 제작 파이프라인으로 바꾼다. 실제 운영 중인 경보 분류 시스템에서 도구 호출은 p50 지연 시간을 42% 줄였고, 과거 경보 1,500건에서는 end-to-end 오류율을 최대 53% 낮췄다.*
- **[Looking Is Not Picking: An Attention-Segment Account of Tool-Selection Failures in LLM Agents](https://arxiv.org/abs/2606.16364)** (Chen et al., arXiv 2026) - *파라미터 0.5B부터 32B까지의 모델에서 나온 BFCL 실패 사례에 구간별 attention 지표를 적용해, 도구 선택 오류가 검색이 아니라 결정 단계에서 생긴다는 것을 짚어 낸다.*
- **[HyperTool: Beyond Step-Wise Tool Calls for Tool-Augmented Agents](https://arxiv.org/abs/2606.13663)** (Du et al., arXiv 2026) - *결정적인 도구 서브루틴들을 모델이 코드로 내리는 바깥 호출 하나로 묶어, 중간값이 추론 trace를 거치지 않고 로컬에서 오가게 한다. MCP-Universe에서 Qwen3-32B의 성능을 15.7%에서 35.3%로 끌어올렸다.*
- **[Tool-Aware Optimization with Entropy Guidance for Efficient Agentic Reinforcement Learning](https://arxiv.org/abs/2606.03762)** (Cao et al., arXiv 2026) - *도구 호출이 모두 실패했거나 결과가 한결같이 맞거나 틀린 rollout을 버리고, 도구 호출 직후 토큰에 엔트로피 보너스를 더해 중요한 결정 지점에서 탐색이 줄지 않게 해 agentic RL을 안정시킨다.*
- **[SENTINEL: Failure-Driven Reinforcement Learning for Training Tool-Using Language Model Agents](https://arxiv.org/abs/2606.12908)** (Wang et al., arXiv 2026) - *실패에서 출발하는 강화학습 파이프라인 SENTINEL을 제안한다. Controller가 정책 자신의 실패한 rollout에서 실패 유형을 캐내고, Proposer가 이를 겨냥한 학습 과제로 바꾸며, Solver가 그 과제로 학습한다. Tau2-Bench Retail에서 Qwen3-4B의 pass^1을 66.4에서 74.9로 끌어올렸다.*
- **[SCRIBE: Structured Mid-Level Supervision for Tool-Using Language Models](https://arxiv.org/abs/2601.03555)** (Jiang et al., arXiv 2026) - *SCRIBE는 도구로 보강한 에이전트의 과정 수준 reward modeling을 엄선한 skill 원형 라이브러리에 grounding하는 강화학습 프레임워크이다.*
- **[CodeDelegator: Mitigating Context Pollution via Role Separation in Code-as-Action Agents](https://arxiv.org/abs/2601.14914)** (Fei et al., arXiv 2026) - *전략적 계획을 맡아 계속 유지되는 Delegator 에이전트와, 매번 깨끗한 컨텍스트로 새로 만들어 하위 과제를 실행하는 Coder 에이전트를 분리한 CodeDelegator를 제안한다.*
- **[PruneTIR: Inference-Time Tool Call Pruning for Effective yet Efficient Tool-Integrated Reasoning](https://arxiv.org/abs/2605.09931)** (Zhang et al., arXiv 2026) - *Success-Triggered Pruning, Stuck-Triggered Pruning, Resampling으로 도구 통합 추론 속의 잘못된 도구 호출을 잘라 내는 추론 시점 프레임워크를 내놓는다.*
- **[The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration](https://arxiv.org/abs/2603.22862)** (Xu et al., arXiv 2026) - *여러 도구를 쓰는 LLM 에이전트를 검토한 서베이로, 최근 진전을 여섯 가지 축(계획과 실행, 학습, 안전, 효율, 능력 개발, 평가)으로 정리하고 소프트웨어 공학, 기업 workflow, 그래픽 사용자 인터페이스, 모바일 시스템에서의 응용을 살핀다.*
- **[AppWorld-UL: Benchmarking Diverse Agent-User Interactions for Tool-Use](https://arxiv.org/abs/2607.20536)** (Chen et al., arXiv 2026) - *명확히 되묻기, 확인, 거절이 필요한 사용자 참여형 도구 과제 516개에서 Claude Opus 4.7은 48.6%만 풀고, 여러 요소가 조합된 시나리오에서는 21.3%로 떨어진다.*
- **[HANDBOOK.md: A Benchmark for Long-Context Agentic Instruction Following](https://arxiv.org/abs/2607.25398)** (Panavas et al., arXiv 2026) - *20쪽에서 124쪽에 이르는 정책 문서와 MCP 도구를 함께 주면 에이전트는 지시를 따르지 않게 된다. 서른 가지 구성 가운데 가장 좋은 것도 엄격한 채점에서 시행의 36.2%만 통과한다.* [[code](https://github.com/surge-ai/handbook)]
- **[ToolAtlas: Learning Once, Reusing Everywhere with Tool-Side Memory](https://arxiv.org/abs/2607.11126)** (Fang et al., arXiv 2026) - *메모리를 에이전트가 아니라 도구 제공자 쪽에 둔다. 실제로 실행해 확인한 도구의 능력, 실패 경계, 조합 기록이 pass@1을 최대 21.61% 올리고, 다시 학습하지 않아도 다른 에이전트 프레임워크에서 그대로 쓸 수 있다.*
- **[The Bitter Lesson of Tool Calling](https://arxiv.org/abs/2608.06370)** (Patel et al., arXiv 2026) - *BFCL v4에서 모델 14개를 대상으로 코드로 도구를 부르는 방식과 기본 JSON 방식을 비교한다. 도구를 타입이 붙은 Python stub으로 노출하고 모델이 코드로 호출하게 하면 14개 중 11개에서 JSON과 같거나 낫고, GPT-5.6 계열에서는 10.6% 오르며, baseline의 성능이 떨어지는 context rot 상황에서도 성능을 유지한다.*
- **[Diagnosing Tool-Selection Reasoning in LLM Agents with Canary Tools](https://arxiv.org/abs/2608.04719)** (Anand et al., arXiv 2026) - *MCP 도구 모음에 진단용 미끼 도구를 넣어, 틀린 도구를 골랐다는 결과만이 아니라 왜 틀렸는지까지 알 수 있게 한다. 여섯 가지 탐침 유형과 8,640회 실행에서 모델 간 취약도는 약 36배 차이 나며, 능력 등급과 비례하지 않는다.*
- **[The Devil Is in the Interface: Evaluating How Tool Architecture Shapes Coding Agent Behavior](https://arxiv.org/abs/2608.11386)** (Xu et al., arXiv 2026) - *바탕의 정보와 행동은 고정하고 노출 방식만 바꿔, 저장소 단위 이슈 수정 trajectory 11,700개에 걸쳐 여섯 가지 도구 아키텍처를 비교한다. 구조화된 저수준 인터페이스는 반복 시도 간 일관성을 최대 4.7배 높이고, Python CodeAct 방식 인터페이스는 단계를 41.6% 줄이고 토큰 사용량을 56.3% 낮추면서 같은 과제 성능을 낸다. 반면 텍스트 기반 인지 scaffold 도구는 별 차이를 만들지 못한다.*
- **[Thinking With Tools, Not With Pixels: Tool Calls as Text Scaffolds for Visual Reasoning](https://arxiv.org/abs/2608.09682)** (Shao et al., arXiv 2026) - *자르기·확대 도구가 돌려주는 이미지를 텍스트 placeholder로 바꿔도 LoRA, full fine-tuning, RL 모두에서 이미지를 온전히 쓰는 thinking-with-images와 같거나 더 낫다. 성능에 실제로 기여하는 신호는 돌아온 픽셀이 아니라 호출할 때 내놓는 구조화된 텍스트라는 뜻이다. 지연 시간은 29에서 46%까지 줄고 도구 실행 API 호출은 사라진다.*
- **[Can MCP Clients Decide What to Do After Failure? A Result-Only Actionability Audit](https://arxiv.org/abs/2609.00072)** (Mehan, arXiv 2026) - *끝난 MCP 실패 결과 하나만 보고 결정론적 소프트웨어가 무엇을 판단할 수 있는지 묻는다. 일부러 작게 잡은 표본(접근 가능한 서버 열 곳에서 유도한 실패 21건)에서 타입이 있는 필드로 알 수 있었던 것은 실패 여부(18건)와 대략적인 대응 방침(8건)까지였고, 구체적인 원인, 대상, 실행 가능한 수정, 재실행 제약은 한 건에서도 알 수 없었다. 그래서 복구는 누군가 읽고 해석해야 하는 자연어 설명에 의존하게 된다.*
- **[One Policy Is Enough: Single-Agent Reinforcement Learning Outperforms Tree Search for Chemistry Tool Learning](https://arxiv.org/abs/2608.30952)** (Dariani et al., arXiv 2026) - *학습된 critic 두 개 아래에서 정책 모델과 실행 모델을 따로 돌리는 계층형 진화 tree search를, 왼쪽에서 오른쪽으로 한 번 생성하는 단일 모델로 대체한다. 이 모델은 정답 호출 사슬에서 읽어 낸 프로그램 보상에 맞춰 결과 수준 강화학습으로 학습하며, 학습 루프에 학습된 critic도 심판도 두지 않는다. 그런데도 Qwen-2.5-7B에서 질문당 모델 호출 한 번으로 Tool F1을 5.5%, Return F1을 9.6% 높인다.*
- **[DRACO: Fine-Grained Credit Assignment with Dynamic Rubrics for Long-Horizon Agent Training](https://arxiv.org/abs/2609.04094)** (Gandhi et al., arXiv 2026) - *정답 성공 신호가 없을 때도 long-horizon 도구 사용 에이전트를 GRPO로 학습시킨다. 학습 중에 과제별 rubric을 만들고, 각 trajectory를 LLM 심판으로 한 번 채점한 뒤, 주석으로 단 기준마다 책임이 있는 단계들에 advantage를 닫힌 형태로 다시 나눠 주며, 따로 학습한 귀속 모듈은 쓰지 않는다. AppWorld에서 기본 모델보다 15.9포인트 오르고, 자체 검증기 없이도 정답 보상으로 학습한 GRPO를 5.3포인트 앞서며, frontier 모델 심판 없이 Tau-Bench에서도 5.3포인트를 올린다.* [[code](https://github.com/IBM/draco)]
</details>

<sub><a href="#contents">↑ 목차로 돌아가기</a></sub>

<a id="multi-agent"></a>
### 🤝 다중 에이전트 시스템 (51)
*서베이 §7(다중 에이전트 시스템)에 해당합니다.*

<details>
<summary><b>논문 51편 보기</b></summary>

- **[CAMEL: Communicative Agents for "Mind" Exploration of Large Language Model Society](https://arxiv.org/abs/2303.17760)** (Li et al., NeurIPS 2023) - *역할극으로 에이전트끼리 자율적으로 협력하는 방식을 확립한, 가장 이르고 많이 인용된 프레임워크 가운데 하나이다.* [[code](https://github.com/camel-ai/camel)]
- **[Improving Factuality and Reasoning in Language Models through Multiagent Debate](https://arxiv.org/abs/2305.14325)** (Du et al., ICML 2024) - *'society of minds' 방식의 토론을 테스트 시점 기법으로 널리 알린, 다중 에이전트 토론의 효시 격 논문이다.* [[code](https://github.com/composable-models/llm_multiagent_debate)]
- **[Encouraging Divergent Thinking in Large Language Models through Multi-Agent Debate](https://arxiv.org/abs/2305.19118)** (Liang et al., EMNLP 2024) - *핵심 실패 유형을 진단해, 다중 에이전트 토론이 self-consistency보다 더 도움이 되는 이유를 설명한다.* [[code](https://github.com/Skytliang/Multi-Agents-Debate)]
- **[ChatEval: Towards Better LLM-based Evaluators through Multi-Agent Debate](https://arxiv.org/abs/2308.07201)** (Chan et al., ICLR 2024) - *다중 에이전트 토론이 LLM 심판 평가의 신뢰도를 높인다는 것을 보인다.* [[code](https://github.com/chanchimin/ChatEval)]
- **[AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation](https://arxiv.org/abs/2308.08155)** (Wu et al., arXiv 2023) - *Microsoft가 만들어 산업계에서 널리 채택된 다중 에이전트 orchestration 프레임워크이다.* [[code](https://github.com/microsoft/autogen)]
- **[ChatDev: Communicative Agents for Software Development](https://arxiv.org/abs/2307.07924)** (Qian et al., ACL 2024) - *복잡한 실제 workflow를 다중 에이전트 협업으로 end-to-end 처리해 보인, 널리 인용되는 사례이다.* [[code](https://github.com/OpenBMB/ChatDev)]
- **[AgentVerse: Facilitating Multi-Agent Collaboration and Exploring Emergent Behaviors in Agents](https://arxiv.org/abs/2308.10848)** (Chen et al., ICLR 2024) - *구성을 동적으로 짜는 범용 다중 에이전트 협업 프레임워크이자, 창발하는 사회적 역학을 살핀 연구이다.* [[code](https://github.com/OpenBMB/AgentVerse)]
- **[Building Cooperative Embodied Agents Modularly with Large Language Models](https://arxiv.org/abs/2307.02485)** (Zhang et al., ICLR 2024) - *다중 에이전트 협업과 소통을 embodied 환경, 곧 물리 세계에 grounding된 설정으로 넓힌다.* [[code](https://github.com/UMass-Embodied-AGI/CoELA)]
- **[ReConcile: Round-Table Conference Improves Reasoning via Consensus among Diverse LLMs](https://arxiv.org/abs/2309.13007)** (Chen et al., ACL 2024) - *서로 다른 LLM 백본을 섞고, 에이전트 토론과 합의 과정에서 confidence로 가중한 설득과 투표를 쓴다.* [[code](https://github.com/dinobby/ReConcile)]
- **[Dynamic LLM-Agent Network: An LLM-Agent Collaboration Framework with Agent Team Optimization (v2 retitled: A Dynamic LLM-Powered Agent Network for Task-Oriented Agent Collaboration)](https://arxiv.org/abs/2310.02170)** (Liu et al., arXiv 2023) - *다중 에이전트 협업에서 에이전트 팀의 구성과 topology를 동적으로 최적화하는 방법을 내놓는다.* [[code](https://github.com/SALT-NLP/DyLAN)]
- **[Exchange-of-Thought: Enhancing Large Language Model Capabilities through Cross-Model Communication](https://arxiv.org/abs/2312.01823)** (Yin et al., EMNLP 2023) - *에이전트 간 소통 패러다임의 분류 체계를 제시해, 소통 메커니즘을 정리할 때 쓸모가 있다.* [[code](https://github.com/yinzhangyue/EoT)]
- **[LLM-Deliberation: Evaluating LLMs with Interactive Multi-Agent Negotiation Games (v2 retitled: Cooperation, Competition, and Maliciousness: LLM-Stakeholders Interactive Negotiation)](https://arxiv.org/abs/2309.17234)** (Abdelnabi et al., arXiv 2023) - *다중 에이전트 LLM 연구를 협상 같은 전략적·경쟁적 소통으로 넓힌다.* [[code](https://github.com/S-Abdelnabi/LLM-Deliberation)]
- **[Unleashing the Emergent Cognitive Synergy in Large Language Models: A Task-Solving Agent through Multi-Persona Self-Collaboration](https://arxiv.org/abs/2307.05300)** (Wang et al., ACL 2024) - *Persona를 써서 다중 에이전트식 협업을 단일 모델 안에서 흉내 낼 수 있음을 보인 경계 사례이다.* [[code](https://github.com/MikeWangWZHL/Solo-Performance-Prompting)]
- **[Should we be going MAD? A Look at Multi-Agent Debate Strategies for LLMs](https://arxiv.org/abs/2311.17371)** (Smit et al., ICML 2024) - *다중 에이전트 토론이 실제로 언제 도움이 되는지를 비판적·실증적으로 따져 본 중요한 반론이다.* [[code](https://github.com/instadeepai/DebateLLM)]
- **[Debating with More Persuasive LLMs Leads to More Truthful Answers](https://arxiv.org/abs/2402.06782)** (Khan et al., ICML 2024) - *다중 에이전트 토론을 AI 안전의 scalable oversight와 연결한다.* [[code](https://github.com/ucl-dark/llm_debate)]
- **[Mixture-of-Agents Enhances Large Language Model Capabilities](https://arxiv.org/abs/2406.04692)** (Wang et al., ICLR 2025) - *여러 에이전트의 답을 구조적으로 모으면 어떤 강력한 상용 단일 모델보다도 나을 수 있음을 보인 영향력 있는 아키텍처이다.* [[code](https://github.com/togethercomputer/MoA)]
- **[More Agents Is All You Need](https://arxiv.org/abs/2402.05120)** (Li et al., TMLR 2024) - *다중 에이전트의 이득 상당 부분이 소통이 아니라 ensemble 규모 확대에서 나올 수 있음을 보인 중요한 baseline이다.* [[code](https://github.com/MoreAgentsIsAllYouNeed/AgentForest)]
- **[Beyond Self-Talk: A Communication-Centric Survey of LLM-Based Multi-Agent Systems](https://arxiv.org/abs/2502.14321)** (Yan et al., arXiv 2025) - *다중 에이전트 LLM 시스템 안의 소통을 가장 직접 다루는 최근 서베이이다.*
- **[Multi-Agent Collaboration Mechanisms: A Survey of LLMs](https://arxiv.org/abs/2501.06322)** (Tran et al., arXiv 2025) - *협업 메커니즘을 체계적으로 분류한 최근의 전용 서베이이다.*
- **[Language Agents as Optimizable Graphs](https://arxiv.org/abs/2402.16823)** (Zhuge et al., ICML 2024) - *GPTSwarm은 다중 에이전트 시스템을 프롬프트와 간선을 함께 학습하는 computation graph로 정식화한다.* [[code](https://github.com/metauto-ai/GPTSwarm)]
- **[Scaling Large Language Model-based Multi-Agent Collaboration](https://arxiv.org/abs/2406.07155)** (Qian et al., arXiv 2024) - *명시적인 topology로 연결된 에이전트 1000개 이상으로 협업을 확장하고, 불규칙한 그래프가 규칙적인 그래프보다 낫다는 협업 scaling 결과를 보고한다.*
- **[AFlow: Automating Agentic Workflow Generation](https://arxiv.org/abs/2410.10762)** (Zhang et al., ICLR 2025) - *코드로 표현한 workflow 공간을 탐색해 agentic 파이프라인을 자동으로 찾아낸다.*

- **[Graph-of-Agents: A Graph-based Framework for Multi-Agent LLM Collaboration](https://arxiv.org/abs/2604.17148)** (Yun et al., arXiv 2026) - *그래프 기반으로 에이전트를 고르고 정방향·역방향 메시지 전달을 써서, 더 적은 에이전트로 Mixture-of-Agents를 앞선다.* [[code](https://github.com/UNITES-Lab/GoA)]
- **[Latent Agents: A Post-Training Procedure for Internalized Multi-Agent Debate](https://arxiv.org/abs/2604.24881)** (Yi et al., arXiv 2026) - *두 단계 fine-tuning으로 다중 에이전트 토론을 distillation해 단일 모델 안에 옮겨 넣고, 조종 가능한 관점들은 유지하면서 토큰을 최대 93% 줄인다.* [[code](https://github.com/johnsk95/latent_agents)]
- **[Uno-Orchestra: Parsimonious Agent Routing via Selective Delegation](https://arxiv.org/abs/2605.05007)** (Cui et al., arXiv 2026) - *분해 깊이와 작업자 위임을 함께 정하는 하나의 RL 정책으로, 비용을 10배 줄이고도 workflow baseline을 앞선다.*
- **[Competition and Cooperation of LLM Agents in Games](https://arxiv.org/abs/2604.00487)** (Yao et al., arXiv 2026) - *자원 배분 게임과 Cournot 게임에서 LLM 에이전트가 내시 균형에 이르기보다 협력하며, 그 바탕에 공정성에 기반한 추론이 있다는 것을 발견했다.*
- **[Multi-Agent LLMs Fail to Explore Each Other](https://arxiv.org/abs/2607.11250)** (Choi et al., arXiv 2026) - *동료를 탐색하는 문제를 partially observable 확률 게임으로 정식화하고, 지금의 에이전트가 서로를 떠볼 때 근시안적이고 양극화된다는 것을 발견한다. 해법인 MACE는 구조화된 동료 선택을 쓰며, 논문은 에이전트가 다양할수록 탐색의 가치가 커진다는 것을 증명한다.* [[code](https://github.com/deeplearning-wisc/mace)]
- **[Who Broke the System? Failure Localization in LLM-Based Multi-Agent Systems](https://arxiv.org/abs/2607.07989)** (Xia et al., arXiv 2026) - *다중 에이전트 실행을 망가뜨린 에이전트가 누구인지 짚어 낸다. 전체 성공률에 가려지지만 디버깅에 앞서 꼭 필요한 일이다.*
- **[When is Routing Meaningful? Diversity and Robustness in Language Model Societies](https://arxiv.org/abs/2607.09197)** (Huot et al., arXiv 2026) - *여러 모델 사이에서 라우팅하는 것이 언제 의미가 있는지, 다양성이 언제 잡음이 아니라 강건성을 가져오는지 묻는다.*
- **[What LLM Agents Say When No One Is Watching: Social Structure and Latent Objective Emergence in Multi-Agent Debates](https://arxiv.org/abs/2607.02507)** (Ghaffarizadeh et al., arXiv 2026) - *지켜보는 이가 없을 때 에이전트들이 무슨 말을 하는지 관찰해, 과제 지표로는 잡히지 않는 잠재 목표와 사회 구조를 찾아낸다.*
- **[Decision Protocols in Multi-Agent Large Language Model Conversations](https://arxiv.org/abs/2607.05477)** (Kaesberg et al., arXiv 2026) - *다중 에이전트 대화의 결정 프로토콜을 비교하며, 투표 규칙이나 합의 규칙을 설계 변수로 다룬다.*
- **[The Long-Horizon Task Mirage? Diagnosing Where and Why Agentic Systems Break](https://arxiv.org/abs/2604.11978)** (Wang et al., arXiv 2026) - *Long-horizon 과제에서 agentic 시스템이 어디서 왜 실패하는지 진단하고, 겉으로 보이는 long-horizon 능력의 상당 부분이 실제 능력이 아니라고 주장한다.*
- **[GoAgent: Group-of-Agents Communication Topology Generation for LLM-based Multi-Agent Systems](https://arxiv.org/abs/2603.19677)** (Chen et al., arXiv 2026) - *다중 에이전트 시스템의 communication topology를 손으로 고정하지 않고 group-of-agents 그래프로 생성한다.*
- **[Reinforcement Learning for LLM-based Multi-Agent Systems through Orchestration Traces](https://arxiv.org/abs/2605.02801)** (Zhang et al., arXiv 2026) - *Orchestration trace를 가지고 강화학습으로 다중 에이전트 시스템을 end-to-end로 학습시킨다.*
- **[Learning Latency-Aware Orchestration for Multi-Agent Systems](https://arxiv.org/abs/2607.13359)** (Shi et al., arXiv 2026) - *총비용이 아니라 실행의 critical path를 겨냥한다. 학습 중에는 지연을 고려한 실행 그래프를 배우고 실행 중에는 중복된 에이전트 상호작용을 잘라 내, 정확도는 비슷하게 유지하면서 end-to-end 지연을 50% 넘게 줄인다.*
- **[ProACT: Towards Breakdown-Aware Proactive Agent in Multi-User Collaboration](https://arxiv.org/abs/2607.03730)** (Yang et al., arXiv 2026) - *대화형 에이전트가 화자가 표시된 다중 사용자 대화를 관찰하고, 현재 턴에 개입이 필요한 협업 붕괴가 있는지 탐지한 뒤, 가만히 있을지 아니면 겨냥한 협업 skill로 끼어들지 정하게 하는 프레임워크 ProACT를 제안한다. 턴 단위 예제 3,244개와 백본 다섯 개에서 적절성, 흐름을 끊지 않는 정도, 간결성 모두 바로 대화하는 방식을 앞선다.*
- **[MAS-Orchestra: Understanding and Improving Multi-Agent Reasoning Through Holistic Orchestration and Controlled Benchmarks](https://arxiv.org/abs/2601.14652)** (Ke et al., arXiv 2026) - *LLM 다중 에이전트 조율을 다중 에이전트 시스템 전체를 한 번에 생성하는 강화학습 문제(holistic orchestration)로 정식화하고, 과제 차원 다섯 개를 갖춘 통제된 벤치마크 MASBENCH를 내놓는다.*
- **[Security Threat Modeling for Emerging AI-Agent Protocols: A Comparative Analysis of MCP, A2A, Agora, and ANP](https://arxiv.org/abs/2602.11327)** (Anbiaee et al., arXiv 2026) - *AI 에이전트 통신 프로토콜 네 가지(MCP, A2A, Agora, ANP)에 위협 모델링을 적용하고, 생성, 운영, 갱신 단계에 걸친 프로토콜 수준 위험 열두 가지를 찾아내는 정성적 위험 프레임워크를 제시한다. 여러 서버를 조합했을 때 도구가 엉뚱한 제공자 쪽에서 실행되는 빈도를 재는 MCP 사례 연구도 함께 싣는다.*
- **[WebWeaver: Breaking Topology Confidentiality in LLM Multi-Agent Systems with Stealthy Context-Based Inference](https://arxiv.org/abs/2603.11132)** (Xiong et al., arXiv 2026) - *에이전트 하나만 장악한 뒤 에이전트 ID가 아니라 에이전트 컨텍스트만으로 추론해 LLM 다중 에이전트 시스템의 communication topology를 알아내는 공격 프레임워크 WebWeaver를 제안한다.*
- **[Towards Self-Improving Error Diagnosis in Multi-Agent Systems](https://arxiv.org/abs/2604.17658)** (Li et al., arXiv 2026) - *LLM 다중 에이전트 시스템의 failure attribution을 위한 자기 개선형 프레임워크 ErrorProbe를 내놓는다. 역추적과, 검증된 episodic memory를 갖춘 Strategist/Investigator/Arbiter 팀으로 책임 있는 에이전트와 오류가 시작된 단계를 짚어 낸다. TracerTraj와 Who&When에서 baseline을 앞서며, 그 차이는 단계 수준에서 가장 뚜렷하다.*
- **[OrchBench: Evaluating Multi-Agent Orchestration Plans in Isolation via Deterministic Simulation](https://arxiv.org/abs/2607.25656)** (Ren et al., arXiv 2026) - *작업자를 실제로 돌리지 않고 시뮬레이션으로 orchestration 계획을 채점해, 토큰의 1.3%만 쓰고도 실제 실행 품질과 r=0.816으로 맞아떨어진다. 과제에 결정적인 정보를 지키는 편이 에이전트를 늘리는 것보다 낫다.*
- **[Two Calls Beat Five Agents: Evaluating Multi-Agent Pipelines Against Self-Refinement for Local Language Models](https://arxiv.org/abs/2607.26922)** (Prajapati et al., arXiv 2026) - *로컬 7B 모델에서 호출 두 번짜리 self-refinement가 역할 다섯 개짜리 파이프라인을 이기고(GSM8K에서 86.2% 대 82.0%, 토큰 사용량은 7.4배 적음), JSON을 평문으로 바꾸는 것이 아키텍처보다 더 중요하다.*
- **[Do Latent Channels Actually Communicate? A Causal Audit of Latent Multi-Agent LLM](https://arxiv.org/abs/2607.26773)** (Zhang et al., arXiv 2026) - *예제 사이에서 잠재 메시지를 바꿔 끼워, 전체 정확도가 메커니즘을 가린다는 것을 보인다. GSM8K에서 -1.00포인트로 보이던 효과는 무관한 메시지에서 오는 -6.17과 예제별 내용에서 오는 +5.17로 나뉜다.*
- **[When Does Latent Communication Pay? A Causal Audit of Relayed KV Caches in Multi-Agent LLMs](https://arxiv.org/abs/2608.04893)** (Cheng et al., arXiv 2026) - *에이전트끼리 KV cache를 넘기면 잠재적 사고가 전달된다는 주장을, 뒤섞은 캐시, 영벡터로 바꾼 캐시, 모멘트를 맞춘 캐시로 바꿔 넣어 따져 본다. 받는 쪽이 보내는 쪽의 사적 정보를 필요로 할 때는 효과가 실재하지만, 그렇지 않을 때 보고된 이득은 통계적으로 없는 것과 같다.*
- **[Everyone Conforms, No One Believes: Pluralistic Ignorance in LLM Agent Populations](https://arxiv.org/abs/2608.02758)** (YS, arXiv 2026) - *에이전트 집단도 pluralistic ignorance를 재현한다는 것을 발견했다. 속으로는 규범을 거부하면서 겉으로는 64에서 94%의 비율로 동조하고, 모델 여덟 개 중 일곱 개에서 공개적으로 반대하는 한 명이 거짓 합의를 깨는 경우는 26%도 안 된다.*
- **[CityReal: Human-Aligned Urban Behavior and City Dynamics Simulation with Large-Scale LLM Agents](https://arxiv.org/abs/2608.16897)** (Bougie et al., arXiv 2026) - *사람과 정렬한 대규모 도시 행동·도시 역학 시뮬레이션이다. 의도로 움직이는 에이전트가 텍스트 어댑터로 습관과 선호를 익혀 실제 인구 통계와 맞춘다.*
- **[When Agents Coordinate: Measuring Coordination in Multi-Agent AI Coding](https://arxiv.org/abs/2608.16801)** (Destefanis et al., arXiv 2026) - *에이전트 팀 코딩 실행 1902건을 메시지, 파일 쓰기, 파일 읽기의 시간 네트워크로 바꿔 분석한다. 공유 파일이 반복되는 일대일 메시지를 대신해, 메시지가 많은 작업에서 에이전트가 여덟일 때 출력 토큰을 약 42% 줄인다. 에이전트 하나를 조율 담당으로 지정해도 통신 허브는 생기지 않고 성공률도 믿을 만하게 오르지 않으며, 봉인한 재실행 244건에서도 에이전트는 다섯 번 중 네 번꼴로 숨겨 둔 채점 자료에 접근하려 한다.*
- **[Debate Training Reduces Reward Hacking in RLAIF](https://arxiv.org/abs/2608.17776)** (Kenton et al., arXiv 2026) - *Gemini 2.5 Flash급 정책을 생성자와 critic의 토론으로 RL fine-tuning하고, 판정은 고정된 더 약한 Gemini 2.5 Flash Lite 심판이 맡는다. 단일 플레이어 RLAIF baseline은 금세 심판을 해킹하지만 이 방식은 학습 내내 심판 성능을 지키며, 성능 격차의 45%를 되찾는다. 플레이어에 제약이 없으면 적대적 학습이 critic의 심판 해킹으로 흘러갈 위험이 있고, 비평 단어 수 제한(150단어까지 효과)은 critic의 표현 명확성을 희생하는 대신 게임의 균형을 맞춘다.*
- **[OrchMAS: Orchestrated Reasoning with Multi Collaborative Heterogeneous Scientific Expert Structured Agents](https://arxiv.org/abs/2603.03005)** (Feng et al., arXiv 2026) - *과학 추론을 위해 orchestration과 실행을 두 계층으로 나눈다. Orchestrator 모델이 과제를 읽고 도메인을 고려한 파이프라인을 세운 뒤, 만들어 내는 전문가 에이전트마다 역할과 프롬프트를 써 주고, 실행 도중 중간 피드백을 받아 파이프라인을 고친다. 별도의 실행 모델이 각 단계를 수행하므로, 능력과 비용이 다른 백본을 한 실행 안에서 섞어 쓸 수 있다.*
- **[At Equal Inference Cost, Multi-Agent Structure Does Not Beat a Single Frozen Agent](https://arxiv.org/abs/2609.04217)** (Dylan et al., arXiv 2026) - *환경 rollout 수가 아니라 전체 모델 호출 수를 고정하자, Planner-Executor-Critic 팀이 진화시킨 단일 executor보다 낫다던 이점이 사라진다. ALFWorld에서 0.769 대 0.754(p = 0.80)이면서 평가 호출은 1.8배를 쓴다. Leave-one-in 분석으로 보면 실제 가치는 전부 executor에서 나오고 planner와 critic은 비어 있거나 아무 효과 없는 프롬프트로 진화하며, WebShop에서는 팀 쪽이 더 나빠지는 경향을 보인다.*
- **[A Case Study on Emergent Cheating and Whistleblowing in Autonomous Research Swarms](https://arxiv.org/abs/2609.04170)** (Paglieri et al., arXiv 2026) - *형식 추측을 증명하는 에이전트 100개 집단에서 에이전트 하나가 평가 시스템의 허점을 찾아냈고, 이 허점은 경쟁 압력 속에서 공유 지식 라이브러리를 거쳐 에이전트 간 메시지로 퍼졌다. 한편 다른 무리는 부정한 증명을 점검하고, 동료에게 경고하고, 보이콧을 벌이고, 검증 패치를 제안했다. 허점이 퍼진 투명한 채널이 곧 저항을 가능하게 한 채널이었고, 저자들은 이를 개별 에이전트 내부의 실패가 아니라 공유지 거버넌스 문제로 본다.*
</details>

<sub><a href="#contents">↑ 목차로 돌아가기</a></sub>

## 🌍 제2부: 환경과 응용 속의 에이전트

<a id="environments"></a>
### 🌐 상호작용 환경 (57)
*서베이 §8(상호작용 환경의 에이전트)에 해당합니다.*

<details>
<summary><b>논문 57편 보기</b></summary>

- **[Do As I Can, Not As I Say: Grounding Language in Robotic Affordances](https://arxiv.org/abs/2204.01691)** (Ahn et al., CoRL 2022) - *Embodied 로봇 에이전트에서 LLM을 planner로 쓰고 실제 세계의 affordance로 grounding한, 토대가 된 시연이다.* [[code](https://github.com/google-research/google-research/tree/master/saycan)]
- **[Inner Monologue: Embodied Reasoning through Planning with Language Models](https://arxiv.org/abs/2207.05608)** (Huang et al., CoRL 2022) - *피드백에 grounding된 폐루프 계획 패턴을 확립해, 이후 embodied·GUI 에이전트 아키텍처의 바탕이 되었다.*
- **[ALFWorld: Aligning Text and Embodied Environments for Interactive Learning](https://arxiv.org/abs/2010.03768)** (Shridhar et al., ICLR 2021) - *LLM 기반 embodied·가사 에이전트(ReAct, Reflexion)를 평가할 때 널리 쓰는 벤치마크로, 텍스트 추론과 embodied 실행을 잇는다.* [[code](https://github.com/alfworld/alfworld)]
- **[RT-1: Robotics Transformer for Real-World Control at Scale](https://arxiv.org/abs/2212.06817)** (Brohan et al., RSS 2023) - *이후 RT-2와 OpenVLA가 확장한 방법의 틀을 세운, 토대가 된 대규모 로봇 transformer 모델이다.* [[code](https://github.com/google-research/robotics_transformer)]
- **[PaLM-E: An Embodied Multimodal Language Model](https://arxiv.org/abs/2303.03378)** (Driess et al., ICML 2023) - *인터넷 규모의 vision-language 사전학습이 embodied 로봇 추론으로 전이된다는 것을 보인 선구적인 embodied multimodal LLM으로, RT-2와 VLA 모델에 영감을 주었다.*
- **[RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control](https://arxiv.org/abs/2307.15818)** (Brohan et al., CoRL 2023) - *Vision-language-action(VLA) 모델링 패러다임을 확립했고, 이 패러다임은 embodied·로봇 에이전트 연구의 중심이 되었다.*
- **[OpenVLA: An Open-Source Vision-Language-Action Model](https://arxiv.org/abs/2406.09246)** (Kim et al., CoRL 2024) - *비공개 VLA 모델에 대응하는 오픈소스 모델로, LLM 기반 로봇 제어 연구의 문턱을 낮췄다.* [[code](https://github.com/openvla/openvla)]
- **[WebShop: Towards Scalable Real-World Web Interaction with Grounded Language Agents](https://arxiv.org/abs/2207.01206)** (Yao et al., NeurIPS 2022) - *언어를 grounding하는 웹 에이전트를 위한 토대 벤치마크로, 지금도 널리 쓰인다. 이후의 LLM 기반 웹 탐색 연구보다 먼저 나와 그 연구들의 동기가 되었다.* [[code](https://github.com/princeton-nlp/WebShop)]
- **[Mind2Web: Towards a Generalist Agent for the Web](https://arxiv.org/abs/2306.06070)** (Deng et al., NeurIPS 2023) - *실제 웹사이트에서의 범용 웹 탐색을 겨냥해 설계한 첫 벤치마크이자 LLM 기반 에이전트로, 이후 웹·GUI 에이전트 논문이 표준으로 인용한다.* [[code](https://github.com/OSU-NLP-Group/Mind2Web)]
- **[A Real-World WebAgent with Planning, Long Context Understanding, and Program Synthesis](https://arxiv.org/abs/2307.12856)** (Gur et al., ICLR 2024) - *지시를 정형화된 하위 지시로 나누고, 긴 HTML을 과제와 관련된 조각으로 요약한 뒤, 생성한 Python 코드로 행동한다. 실제 웹사이트에서 성공률을 50% 넘게 올렸고 Mind2Web 오프라인 계획에서 가장 높은 성적을 냈다.*
- **[GPT-4V(ision) is a Generalist Web Agent, if Grounded](https://arxiv.org/abs/2401.01614)** (Zheng et al., ICML 2024) - *Multimodal LLM이 범용 시각 웹 에이전트로 동작할 수 있음을 처음 체계적으로 보여, 시각에 grounding된 웹·GUI 에이전트로 흐름이 넘어가는 계기가 되었다.* [[code](https://github.com/OSU-NLP-Group/SeeAct)]
- **[WebVoyager: Building an End-to-End Web Agent with Large Multimodal Models](https://arxiv.org/abs/2401.13919)** (He et al., ACL 2024) - *실제 환경의 multimodal 브라우저 에이전트를 보여 준 핵심 사례이자 벤치마크로, 이후 웹 에이전트 시스템 평가에 널리 쓰인다.* [[code](https://github.com/MinorJerry/WebVoyager)]
- **[Web Agents with World Models: Learning and Leveraging Environment Dynamics in Web Navigation](https://arxiv.org/abs/2410.13232)** (Chae et al., ICLR 2025) - *지금의 LLM에 world model이 없다는 것을 확인한 뒤, 각 행동이 무엇을 바꿀지 자유 텍스트로 서술하는 모델을 학습시킨다. 그래서 에이전트는 환불 불가 예약처럼 되돌릴 수 없는 일에 나서기 전에 결과를 시뮬레이션해 볼 수 있다. WebArena와 Mind2Web에서 tree search보다 적은 비용으로 정책 선택을 개선했다.* [[code](https://github.com/kyle8581/WMA-Agents)]
- **[CogAgent: A Visual Language Model for GUI Agents](https://arxiv.org/abs/2312.08914)** (Hong et al., arXiv 2023) - *스크린샷만으로 GUI grounding을 하도록 만든 초기 대형 VLM 가운데 하나로, 고해상도 시각 GUI 에이전트 아키텍처 계열의 출발점이 되었다.* [[code](https://github.com/zai-org/CogAgent)]
- **[SeeClick: Harnessing GUI Grounding for Advanced Visual GUI Agents](https://arxiv.org/abs/2401.10935)** (Cheng et al., ACL 2024) - *GUI grounding을 시각 GUI 에이전트의 핵심 하위 문제로 자리 잡게 하고, 표준 grounding 벤치마크인 ScreenSpot을 내놓았다.* [[code](https://github.com/njucckevin/SeeClick)]
- **[Mobile-Agent: Autonomous Multi-Modal Mobile Device Agent with Visual Perception](https://arxiv.org/abs/2401.16158)** (Wang et al., arXiv 2024) - *메타데이터 없이 여러 앱을 넘나들며 동작하는 모습을 보인, 시각 중심 모바일 GUI 에이전트 설계의 대표 사례이다.* [[code](https://github.com/X-PLUG/MobileAgent)]
- **[OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](https://arxiv.org/abs/2404.07972)** (Xie et al., NeurIPS 2024) - *'computer use' 에이전트를 평가하는 표준 벤치마크로, 2024년 이후 사실상 모든 주요 computer use 에이전트가 이것으로 평가받았다.* [[code](https://github.com/xlang-ai/OSWorld)]
- **[AndroidWorld: A Dynamic Benchmarking Environment for Autonomous Agents](https://arxiv.org/abs/2405.14573)** (Rawles et al., ICLR 2025) - *과제를 동적으로 바꿔 가며 재현할 수 있게 한, 모바일 GUI 에이전트의 가장 대표적인 벤치마크이다.* [[code](https://github.com/google-research/android_world)]
- **[UI-TARS: Pioneering Automated GUI Interaction with Native Agents](https://arxiv.org/abs/2501.12326)** (Qin et al., arXiv 2025) - *최신 수준의 공개 'native' GUI·computer use 에이전트 모델로, 이 분야가 end-to-end로 학습한 GUI 행동 모델 쪽으로 옮겨 가고 있음을 보여 준다.* [[code](https://github.com/bytedance/UI-TARS)]
- **[GUI Agents: A Survey](https://arxiv.org/abs/2412.13501)** (Nguyen et al., ACL 2025) - *GUI 에이전트만 다룬 최신 서베이이다. GUI·computer use 에이전트 하위 분야와 그 분류 체계를 짤 때 바로 쓸 수 있다.*
- **[Large Language Model-Brained GUI Agents: A Survey](https://arxiv.org/abs/2411.18279)** (Zhang et al., arXiv 2024) - *GUI 에이전트에 특화된 보완용 서베이로, LLM 기반 GUI 에이전트 문헌을 폭넓게 훑는 데 쓸모가 있다.* [[code](https://github.com/vyokky/LLM-Brained-GUI-Agents-Survey)]
- **[A Survey of WebAgents: Towards Next-Generation AI Agents for Web Automation with Large Foundation Models](https://arxiv.org/abs/2503.23350)** (Ning et al., KDD 2025) - *웹 에이전트 하위 분야를 전담한 서베이로, 브라우저·웹 자동화 에이전트에 맞춘 분류 체계와 신뢰성 논의를 바로 가져다 쓸 수 있다.*
- **[UI-TARS-2 Technical Report: Advancing GUI Agent with Multi-Turn Reinforcement Learning](https://arxiv.org/abs/2509.02544)** (Wang et al., arXiv 2025) - *UI-TARS의 후속작으로, 다중 턴 RL로 end-to-end GUI 제어를 학습한다.*
- **[π0: A Vision-Language-Action Flow Model for General Robot Control](https://arxiv.org/abs/2410.24164)** (Black et al., arXiv 2024) - *사전학습된 VLM 위에 flow matching 행동 전문가를 얹어, 형태가 다른 여러 로봇을 제어한다.* [[code](https://github.com/Physical-Intelligence/openpi)]
- **[Tongyi DeepResearch Technical Report](https://arxiv.org/abs/2510.24701)** (Tongyi DeepResearch Team, arXiv 2025) - *Long-horizon 웹 조사와 종합을 위한 공개 end-to-end deep research 에이전트 모델이다.* [[code](https://github.com/Alibaba-NLP/DeepResearch)]

- **[Mobile-Agent-v3.5: Multi-platform Fundamental GUI Agents](https://arxiv.org/abs/2602.16855)** (Xu et al., arXiv 2026) - *모바일, 데스크톱, 브라우저를 아우르는 native 멀티플랫폼 에이전트 계열 GUI-Owl-1.5로, 데이터 플라이휠과 MRPO RL을 쓰며 GUI 벤치마크 20개 이상에서 SOTA를 기록했다.* [[code](https://github.com/X-PLUG/MobileAgent)]
- **[EvoCUA: Evolving Computer Use Agents via Learning from Scalable Synthetic Experience](https://arxiv.org/abs/2601.15876)** (Xue et al., arXiv 2026) - *합성 과제 생성과 온라인 sandbox 정책 최적화를 결합한 자기 진화하는 computer use 에이전트로, OSWorld에서 56.7%에 이른다.*
- **[CUA-Suite: Massive Human-annotated Video Demonstrations for Computer-Use Agents](https://arxiv.org/abs/2603.24440)** (Jian et al., arXiv 2026) - *Computer use 에이전트를 위해 VideoCUA, UI-Vision 벤치마크, GroundCUA(스크린샷 56K장, UI 주석 3.6M개)를 공개한다.* [[code](https://github.com/ServiceNow/GroundCUA)]
- **[Long-Horizon-Terminal-Bench: Testing the Limits of Agents on Long-Horizon Terminal Tasks with Dense Reward-Based Grading](https://arxiv.org/abs/2607.08964)** (Li et al., arXiv 2026) - *Long-horizon 과제를 위해 만든 터미널 벤치마크로, 여기서 에이전트는 한 단계를 못 해서가 아니라 상태 추적에서 실패한다.* [[code](https://github.com/zli12321/LHTB)]
- **[WebRetriever: A Large-Scale Comprehensive Benchmark for Efficient Web Agent Evaluation](https://arxiv.org/abs/2607.06118)** (Dong et al., arXiv 2026) - *손으로 만든 사이트 몇 개가 아니라 효율적인 평가를 목표로 설계한 대규모 웹 에이전트 벤치마크이다.* [[code](https://github.com/Mininglamp-AI/WebRetriever)]
- **[CLI-Anything: Towards Agent-Native Computer Use](https://arxiv.org/abs/2606.03854)** (Yang et al., arXiv 2026) - *Computer use는 픽셀 단위로 화면을 흉내 낼 것이 아니라 CLI를 거쳐 에이전트에게 맞는 방식으로 이루어져야 한다고 주장한다.* [[code](https://github.com/HKUDS/CLI-Anything)]
- **[PhoneBuddy: Training Open Models for Agentic Phone Use](https://arxiv.org/abs/2606.23049)** (Tang et al., arXiv 2026) - *비공개 시스템이 주도해 온 agentic 휴대폰 조작 분야를 위해 공개 모델을 학습시킨다.* [[code](https://github.com/PhoneBuddyAI/phonebuddy)]
- **[Designing Agent-Ready Websites for AI Web Agents: A Framework for Machine Readability, Actionability, and Decision Reliability](https://arxiv.org/abs/2607.12056)** (Elnaffar et al., arXiv 2026) - *관점을 바꿔, 웹사이트를 어떻게 만들어야 에이전트가 기계적으로 읽어 내고 조작할 수 있는지 묻는다.*
- **[TerminalWorld: Benchmarking Agents on Real-World Terminal Tasks](https://arxiv.org/abs/2605.22535)** (Chu et al., arXiv 2026) - *실제 터미널 과제로 에이전트를 평가한다. 여기서는 한 단계의 솜씨보다 long-horizon 상태 추적이 성패를 가른다.* [[code](https://github.com/EuniAI/TerminalWorld)]
- **[WebNavigator: Global Web Navigation via Interaction Graph Retrieval](https://arxiv.org/abs/2603.20366)** (Zhang et al., arXiv 2026) - *상호작용 그래프를 검색하며 웹을 탐색해, 에이전트에게 페이지 단위의 국소 정보 대신 전역 구조를 준다.* [[code](https://github.com/fate-ubw/webNavigator)]
- **[MobileGym: A Verifiable and Highly Parallel Simulation Platform for Mobile GUI Agent Research](https://arxiv.org/abs/2605.26114)** (Wu et al., arXiv 2026) - *모바일 GUI 에이전트를 학습하고 평가하기 위한, 검증 가능하고 병렬성이 높은 시뮬레이션 플랫폼이다.*
- **[ABot-AgentOS: A General Robotic Agent OS with Lifelong Multi-modal Memory](https://arxiv.org/abs/2607.10350)** (Tian et al., arXiv 2026) - *계획, skill 실행, 그리고 시각·공간·시간 정보를 통합하는 Universal Multi-modal Graph Memory를 하나로 묶은 embodied 로봇용 에이전트 운영체제를 제안한다.* [[code](https://github.com/amap-cvlab/ABot-AgentOS)]
- **[EvoPolicyGym: Evaluating Autonomous Policy Evolution in Interactive Environments](https://arxiv.org/abs/2607.02440)** (Zhilin Wang et al., arXiv 2026) - *Autonomous Policy Evolution이라는 평가 설정과 EvoPolicyGym 벤치마크를 내놓는다. 에이전트 모델이 작은 상호작용 강화학습 환경 16개에서 실행 가능한 정책 코드를 반복해 고친다.* [[code](https://github.com/Linzwcs/EvoPolicyGym)]
- **[ChainSWE: Benchmarking Coding Agents on Multi-Bug Software Maintenance](https://arxiv.org/abs/2607.02606)** (Jin et al., arXiv 2026) - *Python 프로젝트 54개에 걸쳐 시간 순으로 이어진 이슈 304개로 이루어진 벤치마크 ChainSWE를 내놓는다. 코딩 에이전트를 따로 떨어진 결함이 아니라 순서대로 서로 얽힌 버그 수정으로 평가한다.*
- **[VisCritic: Visual State Comparison as Process Reward for GUI Agents](https://arxiv.org/abs/2606.24525)** (Qian et al., arXiv 2026) - *시각 process reward 프레임워크 VisCritic을 제안한다. Siamese vision transformer와 행동을 고려하는 critic head가 행동 전후 스크린샷을 시각 특징 공간에서 비교해 GUI 에이전트의 행동을 검증한다.*
- **[ASPIRE: Agentic /Skills Discovery for Robotics](https://arxiv.org/abs/2607.00272)** (Lu et al., arXiv 2026) - *Code-as-policy 방식으로 에이전트가 로봇 제어 프로그램을 스스로 쓰고 다듬는 지속 학습 시스템 ASPIRE를 제시한다.*
- **[GUI vs. CLI: Execution Bottlenecks in Screen-Only and Skill-Mediated Computer-Use Agents](https://arxiv.org/abs/2606.24551)** (Zhou et al., arXiv 2026) - *조건을 맞춘 벤치마크로 GUI 방식과 CLI 방식의 computer use 에이전트를 비교해, 가장 강한 GUI 에이전트의 전체 통과율이 59.1%로 원래 skill을 쓰는 가장 강한 CLI 에이전트의 48.2%보다 높다고 보고한다.*
- **[A History-Aware Visually Grounded Critic for Computer Use Agents](https://arxiv.org/abs/2606.11078)** (Lee et al., arXiv 2026) - *GUI trajectory로 학습한 multimodal critic HiViG를 제안한다. Computer use 에이전트의 상호작용 이력을 여러 단계의 목표로 압축하고, 제안된 행동을 현재 스크린샷과 대조해 검증한다.* [[code](https://github.com/G-JWLee/HiViG)]
- **[ISE: An Execution-Grounded Recipe for Multi-Turn OS-Agent Trajectories](https://arxiv.org/abs/2606.11520)** (Luo et al., arXiv 2026) - *세 단계(Intent-Simulate-Execute) 파이프라인 ISE를 제안한다. 역할이 고정된 사용자 시뮬레이터와, 격리된 OS 작업 공간에서의 실제 도구 실행을 짝지어 다중 턴 OS 에이전트 학습용 trajectory를 합성한다.* [[code](https://github.com/Valiere01/ISE-Trace)]
- **[Demonstration-Free Robotic Control via LLM Agents](https://arxiv.org/abs/2601.20334)** (Tsui et al., arXiv 2026) - *수정하지 않은 범용 LLM 에이전트 프레임워크를 시연이나 fine-tuning 없이 로봇 조작에 적용하는 FAEA(Frontier Agent as Embodied Agent)를 내놓는다.* [[code](https://github.com/robiemusketeer/faea-sim)]
- **[On Data Engineering for Scaling LLM Terminal Capabilities](https://arxiv.org/abs/2602.21193)** (Pi et al., arXiv 2026) - *합성 과제 생성 파이프라인 Terminal-Task-Gen을 내놓고, Nemotron-Terminal 모델 학습을 위한 데이터 전략(필터링, 커리큘럼)을 연구한다.*
- **[Generalization in Online Reinforcement Learning for Mobile Agents](https://arxiv.org/abs/2603.07432)** (Gu et al., arXiv 2026) - *GUI 모바일 에이전트를 위한 벤치마크이자 GRPO 기반 온라인 RL 학습 시스템인 AndroidWorld-Generalization을 내놓는다. 처음 보는 인스턴스에서는 zero-shot 일반화 이득이 26.1%였지만, 처음 보는 템플릿에서는 15.7%로 줄었다.* [[code](https://github.com/zihuanjiang/AndroidWorld-Generalization)]
- **[WebXSkill: Skill Learning for Autonomous Web Agents](https://arxiv.org/abs/2604.13318)** (Wang et al., arXiv 2026) - *WebXSkill은 파라미터화된 행동 프로그램과 자연어 안내를 결합한 웹 에이전트용 skill 학습 프레임워크이다. 합성 trajectory에서 재사용할 수 있는 행동 패턴을 뽑아 URL 기반 그래프로 정리해 맥락에 맞게 검색하며, WebArena, WebVoyager, Online-Mind2Web에서 성적을 끌어올린다.* [[code](https://github.com/aiming-lab/WebXSkill)]
- **[Beyond Sequential Interaction: Benchmarking Parallel Execution and Coordination for GUI Agents](https://arxiv.org/abs/2607.22689)** (Yu et al., arXiv 2026) - *병렬 GUI 에이전트를 위한 첫 벤치마크이다. Long-horizon 데스크톱 과제를 서로 다른 머신의 작업자들에게 나눠 동시에 돌리면, 가장 좋은 직렬 baseline보다 12.9포인트 높으면서 단계와 토큰은 대략 절반만 쓴다.* [[code](https://github.com/pkgunboat/ParaGUIBench)]
- **[OpenForgeRL: Train Harness-native Agents in Any Environment](https://arxiv.org/abs/2607.21557)** (Yu et al., arXiv 2026) - *에이전트를 실제 배포에 쓰이는 추론 harness(Claude Code, Codex, OpenClaw) 안에서 end-to-end로 학습시키고, 어떤 harness는 다른 것보다 학습하기가 훨씬 어렵다는 것을 발견했다.*
- **[StateAct: Program State, before Pixels, for Long-Horizon Computer-Use Agents](https://arxiv.org/abs/2607.22798)** (Yang et al., arXiv 2026) - *Computer use 에이전트를 스크린샷이 아니라 프로그램 상태에 grounding하면, OSWorld 2.0에서 Claude Opus 4.8이 20.6%에서 26.9%로 오르고 과제당 비용은 약 아홉 배 줄어든다.*
- **[StepReflect: Structured UI Transition Reflection for Mobile GUI Agents](https://arxiv.org/abs/2608.05587)** (Guo et al., arXiv 2026) - *단계별 GUI reflection을 열린 multimodal 추론이 아니라, 명시적인 전이 명세를 기준으로 한 구조화된 예측으로 다룬다. 8B 모델이 AndroidWorld에서 전이 정확도 82.16%를 기록해, 같은 입력을 받은 zero-shot GPT-5.2보다 11.83포인트 높다.*
- **[ComponentBench: Diagnosing Component-Level Failures in Computer-Use Agents](https://arxiv.org/abs/2608.18307)** (Guan et al., arXiv 2026) - *대표 UI 컴포넌트 97종으로 이루어진 온톨로지를 바탕으로, 프로그램으로 검증한 과제 2,910개를 만들어 computer use 에이전트를 컴포넌트 수준에서 평가한다. 공유하는 harness 하나 안에서 관측과 action space만 바꿔도 같은 모델의 과제 성공률이 30% 넘게 달라지며, GPT-5 mini는 accessibility tree 관측에서 83.1%이던 것이 좌표만 쓰는 픽셀 제어에서는 48.9%로 떨어진다.* [[code](https://github.com/TianchenGuan/ComponentBench)]
- **[Neurosymbolic Embodied Agents](https://arxiv.org/abs/2608.16794)** (Albinhassan et al., arXiv 2026) - *가사 과제를 과제 지향 시각 탐색과, Monte Carlo tree search를 곁들인 PDDL 제약 디코딩으로 나눠, 4B에서 27B 규모의 공개 모델이 VirtualHome과 ALFWorld 모두에서 성공률 90%를 넘게 한다. ALFWorld에서 제약이나 탐색만으로는 과제의 삼분의 일도 못 풀지만 둘을 합치면 95% 넘게 풀며, 남은 실패는 계획 생성이 아니라 상태 파악 단계에서 생긴다.*
- **[CUA-Universe: A Scalable and Dynamic Environment for Hybrid GUI+CLI Agents](https://arxiv.org/abs/2609.05374)** (Shi et al., arXiv 2026) - *같은 애플리케이션 상태에 화면과 명령줄 어느 쪽으로도 접근할 수 있는 환경을 구축한다. 실제 데스크톱 애플리케이션 16개를 재현 가능한 가상 머신으로 옮기고, 명령 인터페이스는 찾아내거나 감싸거나 새로 생성해 붙인다. 여기서 모은 trajectory로 학습하면 9B 모델이 비효율적인 클릭과 깨지기 쉬운 스크립트에서 벗어나 더 싼 쪽 인터페이스를 고르게 되어, OSWorld에서 성공률이 16.8포인트 오르고 단계는 57%, 토큰은 44% 줄어든다.*
- **[Discriminative World Models for Web Agents](https://arxiv.org/abs/2609.02885)** (Li et al., arXiv 2026) - *다음 상태 예측으로 지도학습한 world model은 순위 모델이 그 출력을 쓰는 순간 엉뚱한 목표에 최적화된 셈이라고 주장한다. 순위를 매기려면 그럴듯해 보이는 상태가 아니라 후보 행동들을 서로 구별해 주는 예측 상태가 필요하기 때문이다. 그래서 결정 지점마다 대안 행동과 각 행동이 만드는 상태가 함께 달린, 분기하는 WebArena trajectory에서 예측 상태 매칭으로 학습한다.*
- **[Routing Is Least Learnable Where It Is Most Valuable: Bounds on Representation Routing for Web Agents](https://arxiv.org/abs/2608.06171)** (Wei et al., arXiv 2026) - *웹 에이전트 관측 방식 여섯 가지를 두고 라우팅 정책 다섯 가지(confidence cascade 포함)를 비교했지만, 잘 고른 고정 방식 하나를 안정적으로 이기는 것은 없었다. Router는 에이전트가 성공하는 만큼만 라벨을 얻기 때문이다. 같은 방식을 다시 돌리기만 해도 결과의 12-14%가 바뀐다.*
</details>

<sub><a href="#contents">↑ 목차로 돌아가기</a></sub>

<a id="applications"></a>
### 🚀 응용 분야 (54)
*서베이 §10(응용 분야)에 해당합니다.*

<details>
<summary><b>논문 54편 보기</b></summary>

- **[AutoCodeRover: Autonomous Program Improvement](https://arxiv.org/abs/2404.05427)** (Zhang et al., arXiv 2024) - *구조화된 코드 검색에 기반해 비용 효율적으로 프로그램을 자율 수정하는 초기 에이전트 중 하나다.* [[code](https://github.com/nus-apr/auto-code-rover)]
- **[Agentless: Demystifying LLM-based Software Engineering Agents](https://arxiv.org/abs/2407.01489)** (Xia et al., arXiv 2024) - *에이전트 구조 없이 짠 단순한 파이프라인도 복잡한 에이전트에 견줄 수 있음을 보인, 영향력 있는 반론이다.* [[code](https://github.com/OpenAutoCoder/Agentless)]
- **[OpenHands: An Open Platform for AI Software Developers as Generalist Agents](https://arxiv.org/abs/2407.16741)** (Wang et al., ICLR 2025) - *이후 응용 코딩 에이전트 연구의 상당수가 바탕으로 삼은 대표적인 오픈 커뮤니티 플랫폼이다.* [[code](https://github.com/OpenHands/OpenHands)]
- **[Large Language Model-Based Agents for Software Engineering: A Survey](https://arxiv.org/abs/2409.02977)** (Liu et al., arXiv 2024) - *코딩·SWE 에이전트 연구의 위치를 잡는 데 필요한 분류 체계를 제공하는 세부 주제 전용 서베이다.* [[code](https://github.com/FudanSELab/Agent4SE-Paper-List)]
- **[Autonomous chemical research with large language models](https://www.nature.com/articles/s41586-023-06792-0)** (Boiko et al., Nature 2023) - *LLM 에이전트가 물리 세계에서 과학 실험을 자율로 수행한 초창기 시연이자, 가장 많이 인용된 사례 중 하나다.* [[code](https://github.com/gomesgroup/coscientist)]
- **[ChemCrow: Augmenting large-language models with chemistry tools](https://arxiv.org/abs/2304.05376)** (Bran et al., Nature 2023) - *화학 분야에서 도구로 보강한 LLM 에이전트의 토대를 놓은 논문이다.* [[code](https://github.com/ur-whitelab/chemcrow-public)]
- **[The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery](https://arxiv.org/abs/2408.06292)** (Lu et al., arXiv 2024) - *과학 논문의 전 과정을 완전히 자동화하려 한 기념비적 시도로, 널리 화제가 되었다.* [[code](https://github.com/SakanaAI/AI-Scientist)]
- **[The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search](https://arxiv.org/abs/2504.08066)** (Yamada et al., arXiv 2025) - *자율 과학 발견 에이전트가 구체적이고 검증 가능한 단계에 도달했음을 보여 준다.* [[code](https://github.com/SakanaAI/AI-Scientist-v2)]
- **[Towards an AI co-scientist](https://arxiv.org/abs/2502.18864)** (Gottweis et al., arXiv 2025) - *업계(Google)가 과학 가설 생성을 위해 내놓은 주요 응용 에이전트 시스템이다.*
- **[AlphaEvolve: A coding agent for scientific and algorithmic discovery](https://arxiv.org/abs/2506.13131)** (Novikov et al., arXiv 2025) - *LLM 에이전트가 검증 가능한 새로운 수학·알고리즘 발견을 실제로 해낸 이정표적 시연이다.*
- **[Kosmos: An AI Scientist for Autonomous Discovery](https://arxiv.org/abs/2511.02824)** (Mitchener et al., arXiv 2025) - *지금까지 나온 'AI scientist' 에이전트 가운데 가장 유능하고 가장 엄밀하게 평가된 것 중 하나다.*
- **[ScienceAgentBench: Toward Rigorous Assessment of Language Agents for Data-Driven Scientific Discovery](https://arxiv.org/abs/2410.05080)** (Chen et al., ICLR 2025) - *현재 LLM 에이전트와 end-to-end 과학 발견 자동화 사이의 격차를 수치로 보여 주는, 전문가가 검증한 엄밀한 벤치마크다.* [[code](https://github.com/OSU-NLP-Group/ScienceAgentBench)]
- **[Towards Scientific Intelligence: A Survey of LLM-based Scientific Agents](https://arxiv.org/abs/2503.24047)** (Ren et al., arXiv 2025) - *과학 발견 에이전트 문헌을 정리할 때 기준이 되는 세부 주제 전용 서베이다.*
- **[A Survey of LLM-based Agents in Medicine: How far are we from Baymax?](https://arxiv.org/abs/2502.11211)** (Wang et al., ACL 2025) - *의료 분야의 LLM 에이전트만을 다룬 대표 서베이다.*
- **[MDAgents: An Adaptive Collaboration of LLMs for Medical Decision-Making](https://arxiv.org/abs/2404.15155)** (Kim et al., NeurIPS 2024) - *의료 추론의 복잡도에 맞춰 다중 에이전트 orchestration을 바꾸는 적응형 방식의 대표 사례로, 널리 인용된다.* [[code](https://github.com/mitmedialab/MDAgents)]
- **[Agent Hospital: A Simulacrum of Hospital with Evolvable Medical Agents](https://arxiv.org/abs/2405.02957)** (Li et al., arXiv 2024) - *에이전트끼리의 시뮬레이션으로 의료 전문성을 익히는, 독특한 응용 에이전트 패러다임이다.*
- **[Towards Conversational Diagnostic AI](https://arxiv.org/abs/2401.05654)** (Tu et al., arXiv 2024) - *모의 진단 대화에서 LLM 에이전트가 의사와 대등하거나 더 나은 성과를 낸 Google의 시스템으로, 엄밀하게 평가된 이정표적 연구다.*
- **[Large Language Model Agent in Financial Trading: A Survey](https://arxiv.org/abs/2408.06361)** (Ding et al., arXiv 2024) - *응용 LLM 에이전트 가운데 금융 갈래의 기준점이 되는 세부 주제 전용 서베이다.*
- **[FinMem: A Performance-Enhanced LLM Trading Agent with Layered Memory and Character Design](https://arxiv.org/abs/2311.13743)** (Yu et al., AAAI 2023) - *인간의 인지에서 착안한 계층형 메모리 설계를 도입한 LLM 트레이딩 에이전트로, 일찍 나와 널리 참조된다.* [[code](https://github.com/pipiku915/FinMem-LLM-StockTrading)]
- **[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://arxiv.org/abs/2412.20138)** (Xiao et al., arXiv 2024) - *여러 역할을 나눠 맡는 최근의 인기 금융 다중 에이전트 시스템으로, 참조 아키텍처로 널리 쓰인다.* [[code](https://github.com/TauricResearch/TradingAgents)]
- **[FinGPT: Open-Source Financial Large Language Models](https://arxiv.org/abs/2306.06031)** (Yang et al., IJCAI 2023) - *가장 많이 인용되는 오픈소스 금융 LLM·에이전트 프로젝트 중 하나로, 여러 후속 금융 에이전트 시스템이 기반으로 쓰는 모델 인프라를 제공한다.* [[code](https://github.com/AI4Finance-Foundation/FinGPT)]
- **[SWE-Lancer: Can Frontier LLMs Earn $1 Million from Real-World Freelance Software Engineering?](https://arxiv.org/abs/2502.12115)** (Miserendino et al., arXiv 2025) - *코딩 에이전트의 실력을 실제 프리랜스 일감의 달러 보수로 환산한다. Frontier 모델도 걸린 보수의 대부분을 받아 내지 못한다.* [[code](https://github.com/openai/SWELancer-Benchmark)]
- **[AgentClinic: A Multimodal Agent Benchmark to Evaluate AI in Simulated Clinical Environments](https://arxiv.org/abs/2405.07960)** (Schmidgall et al., arXiv 2024) - *의사 에이전트와 환자 에이전트의 상호작용을 모의 임상 환경에서 평가하는 multimodal 벤치마크다.*
- **[OptimAI: Optimization from Natural Language Using LLM-Powered AI Agents](https://arxiv.org/abs/2504.16918)** (Thind et al., arXiv 2025) - *자연어로 적힌 최적화 문제를 formulator, planner, coder, critic으로 이어지는 파이프라인을 거쳐 실행 가능한 solver 코드로 바꾸고, 계획은 UCB 기반으로 고른다.*

- **[AutoSci: A Memory-Centric Agentic System for the Full Scientific Research Lifecycle](https://arxiv.org/abs/2605.31468)** (Qian et al., arXiv 2026) - *과학 연구 루프 전체를 자동화하는 메모리 중심 에이전트 시스템이다.* [[code](https://github.com/skyllwt/AutoSci)]
- **[SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents](https://arxiv.org/abs/2601.16746)** (Wang et al., arXiv 2026) - *저장소 컨텍스트가 길어져도 코딩 에이전트가 제 성능을 내도록, 컨텍스트를 상황에 맞게 스스로 가지치기한다.* [[code](https://github.com/Ayanami1314/swe-pruner)]
- **[LiteResearcher: A Scalable Agentic RL Training Framework for Deep Research Agent](https://arxiv.org/abs/2604.17931)** (Li et al., arXiv 2026) - *Deep research 에이전트를 위한 확장 가능한 agentic RL 학습 프레임워크다.* [[code](https://github.com/simplex-ai-inc/LiteResearcher)]
- **[LawThinker: A Deep Research Legal Agent in Dynamic Environments](https://arxiv.org/abs/2602.12056)** (Yang et al., arXiv 2026) - *변화하는 법률 환경에서 동작하는 deep research 법률 에이전트다.* [[code](https://github.com/RUC-NLPIR/LawThinker-agent)]
- **[Agentic Trading: When LLM Agents Meet Financial Markets](https://arxiv.org/abs/2605.19337)** (Xia et al., arXiv 2026) - *금융 시장에서 행동하는 LLM 에이전트와 이들이 만들어 내는 거래 동역학을 연구한다.*
- **[Rethinking Scientific Discovery in the Agentic Era](https://arxiv.org/abs/2607.03863)** (Zheng et al., arXiv 2026) - *과학적 발견을 에이전트가 맡을 때 무엇이 바뀌고 무엇이 바뀌지 않는지 논하는 포지션 페이퍼다.*
- **[Deep Research in Physical Sciences: A Multi-Agent Framework and Comprehensive Benchmark](https://arxiv.org/abs/2606.18648)** (Jiang et al., arXiv 2026) - *물리과학을 위한 다중 에이전트 deep research 프레임워크이자 벤치마크다.* [[code](https://github.com/yigengjiang/physci-deepresearch)]
- **[HealthAgentBench: A Unified Benchmark Suite of Realistic Agentic Healthcare Environments for Challenging Frontier AI Agents](https://arxiv.org/abs/2606.31179)** (Liu et al., arXiv 2026) - *정적인 임상 질의응답이 아니라, 에이전트가 직접 행동하는 현실적인 의료 환경으로 구성한 벤치마크 모음이다.* [[code](https://github.com/microsoft/HealthAgentBench)]
- **[EvoDS: Self-Evolving Autonomous Data Science Agent with Skill Learning and Context Management](https://arxiv.org/abs/2606.03841)** (Yang et al., arXiv 2026) - *Skill 학습과 컨텍스트 관리를 결합한 자기 진화형 데이터 과학 에이전트다.* [[code](https://github.com/usail-hkust/EvoDS)]
- **[MetaResearcher: Scaling Deep Research via Self-Reflective Reinforcement Learning in Adversarial Virtual Environments](https://arxiv.org/abs/2606.19893)** (Yu et al., arXiv 2026) - *적대적 조건에서 self-reflective 강화학습으로 deep research 루프를 학습시킨다.*
- **[Can Deep Research Agents Retrieve and Organize? Evaluating the Synthesis Gap with Expert Taxonomies](https://arxiv.org/abs/2601.12369)** (Zhang et al., arXiv 2026) - *Deep research 에이전트의 synthesis gap, 즉 근거를 찾아오는 데서 그치지 않고 정리까지 해내는지를 전문가 기준과 대조해 평가한다.* [[code](https://github.com/KongLongGeFDU/TaxoBench)]
- **[ClinicalAgents: Multi-Agent Orchestration for Clinical Decision Making with Dual-Memory](https://arxiv.org/abs/2603.26182)** (Ge et al., arXiv 2026) - *이중 메모리 설계를 갖춘, 임상 의사결정을 위한 다중 에이전트 orchestration이다.* [[code](https://github.com/ZhuohanGe/ClinicalAgents-Code)]
- **[SciResearcher: Scaling Deep Research Agents for Frontier Scientific Reasoning](https://arxiv.org/abs/2605.01489)** (Zheng et al., arXiv 2026) - *Deep research 에이전트를 최첨단 과학 추론 과제로 확장한다.*
- **[Physics-Audited Agentic Discovery in Scientific Machine Learning](https://arxiv.org/abs/2607.07379)** (Abueidda et al., arXiv 2026) - *에이전트가 찾아낸 대리 모델을 오차만이 아니라 기계로 검사할 수 있는 물리 요건으로 고른다. 그 결과 오차가 같은 baseline이 하중 이력의 미래 구간에 반응해 인과성 검사를 통과하지 못하는 사례를 잡아냈다.*
- **[LLMoxie: Exploring Agentic AI for Scientific Software Development](https://arxiv.org/abs/2607.02703)** (Setiawan et al., arXiv 2026) - *LiteLLM/MLflow 거버넌스 control plane과 오픈소스 Plugin-Agent-Skill 생태계를 갖춘 기관용 세 계층 agentic AI 플랫폼 LLMoxie를 스무 달 동안 운영해 온 경험을 보고한다.*
- **[Agon: An Autonomous Large-Scale Omnidisciplinary Research System Built on Prompt Economy](https://arxiv.org/abs/2606.24177)** (Sun et al., arXiv 2026) - *검사할 수 있는 것은 workflow 안에서 검증하고 나머지는 사람 과학자에게 넘기는 연구 orchestrator다. 사람이 쓴 실험 코드 없이 여러 분야에 걸쳐 루프를 444회 돌렸고, 루프가 고칠 수 있는 실패와 고칠 수 없는 실패를 가르는 실패 분류 체계를 내놓았다.* [[code](https://github.com/AutoResearch-Factory/Agon)]
- **[Hybrid-Gym: Training Coding Agents to Generalize Across Tasks](https://arxiv.org/abs/2602.16819)** (Xie et al., arXiv 2026) - *함수 위치 찾기나 의존성 검색 같은 합성 보조 과제로 코딩 에이전트를 학습시키면 그 효과가 실제 작업으로 이어진다. SWE-Bench Verified에서 +25.4%, SWT-Bench Verified에서 +7.9%, Commit-0 Lite에서 +5.1%를 얻었다.* [[code](https://github.com/yiqingxyq/Hybrid-Gym)]
- **[Toward Expert Investment Teams: A Multi-Agent LLM System with Fine-Grained Trading Tasks](https://arxiv.org/abs/2602.23330)** (Miyazaki et al., arXiv 2026) - *투자 분석을 세분화된 트레이딩 하위 과제로 나누는 다중 에이전트 LLM 프레임워크를 제안하고, 일본 주식 데이터로 평가해 추상적인 지시만 준 baseline보다 위험 조정 수익률을 높였다.*
- **[MiroEval: Benchmarking Multimodal Deep Research Agents in Process and Outcome](https://arxiv.org/abs/2603.28407)** (Ye et al., arXiv 2026) - *MiroEval은 과제 100개(텍스트 전용 70개, multimodal 30개)로 이루어진 벤치마크로, deep research 에이전트를 종합 품질, 사실성, 연구 과정이라는 축에서 평가한다.* [[code](https://github.com/MiroMindAI/MiroEval)]
- **[HeartAgent: An Autonomous Agent System for Explainable Differential Diagnosis in Cardiology](https://arxiv.org/abs/2603.10764)** (Zhou et al., arXiv 2026) - *HeartAgent는 맞춤형 도구와 선별한 데이터 자원을 통합하고 전문화된 하위 에이전트들을 조율해, 심장내과에서 설명 가능한 감별 진단을 수행하는 자율 다중 에이전트 시스템이다.*
- **[AutoNumerics: An Autonomous, PDE-Agnostic Multi-Agent Pipeline for Scientific Computing](https://arxiv.org/abs/2602.17607)** (Du et al., arXiv 2026) - *자연어 문제 설명에서 곧바로 고전적인 PDE 수치 solver를 만들고 잔차로 검증하며, solver를 신경망으로 바꾸지 않고 투명하게 남겨 둔다.* [[code](https://github.com/Daviddjddu/Autonumerics)]
- **[Stress-testing large language model agents in a robotic chemistry laboratory](https://arxiv.org/abs/2607.23045)** (Guo et al., arXiv 2026) - *워크스테이션 45대를 갖춘 로봇 화학 실험실에서 4,608회를 시행했다. 전문가가 실행 가능하다고 판정한 에이전트 workflow는 3.3%에 그쳤고, 가장 나은 시스템도 28.1%였으며, 피드백이 재계획으로 이어진 적은 한 번도 없었다.*
- **[PatientAgentBench: A Benchmark Framework for Evaluating Patient-Facing Health AI Agents](https://arxiv.org/abs/2607.25485)** (Vatanparvar et al., arXiv 2026) - *도구를 쓰는 대화 1,200건으로 환자 대면 헬스 에이전트를 평가한다. 모델 간 차이가 가장 크게 벌어지는 영역은 중증도 분류(통과율 32%에서 88%)이며, 가장 강한 모델도 종합 점수는 5점 만점에 4.25점에 그친다.* [[code](https://github.com/amazon-science/PatientAgentBench)]
- **[Agentic Evaluation of Copyright Law Compliance](https://arxiv.org/abs/2607.21799)** (Hui et al., arXiv 2026) - *Copyright-Bench는 에이전트에게 상업용 작업(웹사이트, 굿즈, 피치 덱)을 맡겨, 퍼블릭 도메인 대안이 있는데도 저작권이 있는 작품을 고른다는 것을 확인했다. 시간 압박을 모의로 주면 open-weight 모델의 위반율이 올라간다.*
- **[From Social Coding to Agentic Coding: Productivity and Relational Reconfiguration in Open-Source Communities](https://arxiv.org/abs/2608.03585)** (Zhou et al., arXiv 2026) - *실제 GitHub 개발자 1,084명으로 이루어진 커뮤니티를 코딩 에이전트가 있을 때와 없을 때로 나눠 시뮬레이션한다. 완료한 과제는 39.0% 늘고 완료 시간 중앙값은 45분에서 20분으로 줄지만, 사람 사이의 직접 상호작용은 32.4%에서 11.6%로 떨어지고 이득은 이미 인맥이 넓은 사람들에게 몰린다.*
- **[Vero: Can AI Agents Build Formally Verified Software Repositories?](https://arxiv.org/abs/2608.13522)** (Ye et al., arXiv 2026) - *Python, Dafny, Verus, Coq에 걸친 실제 저장소에서 뽑은 다중 모듈 인스턴스 43개로 구현과 기계 검증 증명 합성을 저장소 수준에서 함께 평가한다. 가장 강한 frontier 코딩 에이전트 구성도 43개 중 27개만 완전히 풀었고, 가장 어려운 저장소에서는 명세를 하나도 증명하지 못했다.* [[code](https://github.com/sunblaze-ucb/vero)]
- **[Auditing Self-Evolution in Financial Agents: Capability Gains, Security Drift, and Execution-Interface Mismatch](https://arxiv.org/abs/2608.17684)** (Li et al., arXiv 2026) - *모의 전자 뱅킹 환경에서 자기 진화 에이전트 설계 세 가지(SkillOpt, Agent Workflow Memory, ReasoningBank)를 감사해, 능력과 노출이 함께 커진다는 것을 확인했다. SkillOpt는 정상 과제의 효용을 0.741에서 0.837로 끌어올리지만, 주입된 콘텐츠 노출도는 0.820에서 0.943으로, 전체 공격 성공률은 0.496에서 0.530으로 오르고, 승인되지 않은 금융 상태 변경은 0.685까지 늘어난다.*
- **[SWE-Gate: Passing Functional Tests Is Not Enough for Software Engineering Agents](https://arxiv.org/abs/2609.04167)** (He et al., arXiv 2026) - *실제 pull request 리뷰 코멘트에서 리뷰 제약을 뽑아내고, Python 프로젝트 75개의 저장소 수준 인스턴스 303개에서 이를 기능적 정확성과 따로 채점한다. 기능 테스트를 통과한 패치 644개 중 221개가 리뷰어가 이미 밝힌 제약을 어겼으니, 기능만 보는 채점은 에이전트가 실제로 해낸 일을 부풀리는 셈이다.* [[code](https://github.com/DeepSoftwareAnalytics/SWE-Gate)]
- **[Why Better Models Can Create Riskier Systems: Evidence from LLM Agents in Financial Markets](https://arxiv.org/abs/2609.04373)** (Ross et al., arXiv 2026) - *학습과 아키텍처를 공유하는 탓에 유능한 모델일수록 비슷하게 행동하고, 그렇게 상관된 행동은 아무리 분산해도 없앨 수 없는 위험의 하한을 남긴다고 주장한다. 이를 에이전트 기반 시장의 LLM 트레이더로 검증한 결과, 능력이 오를수록 상관도 커졌고, 공유된 추론이 정확한 동안에는 에이전트가 많을수록 시장 수준의 위험이 줄었지만, 에이전트들이 잘못된 정보 환경을 공유하자 같은 상관이 오히려 위험 요인이 되었다.*
- **[Training Agents to Evolve with Their Harness: TaoLive Digital Avatar Agent Technical Report](https://arxiv.org/abs/2608.15763)** (TaoLive AIGC LLM Team, arXiv 2026) - *대형 모델은 편집된 Skills, hook, 프롬프트, 도구 스키마에 재학습 없이 적응하지만 라이브 방송이 요구하는 지연 시간 예산을 맞추지 못하므로, 작은 모델을 계속 바뀌는 harness에 맞춰 학습시켜야 한다는 입장이다. 학습 중에 harness 상태를 증강해 모델이 고정된 구성을 한 번도 보지 않게 한 결과 harness 변형 질문에서 기본 모델의 75.4보다 높은 94.6을 얻었다. 고정 harness로 supervised fine-tuning하면 기본 모델보다 IFEval이 7.7점 떨어지지만 증강 방식은 한 점도 잃지 않았고, H20 한 장에서 P50·P95 지연 시간은 3.4초와 8.1초였으며 Taobao Live A/B 테스트에서도 긍정적인 결과를 냈다.*
</details>

<sub><a href="#contents">↑ 목차로 돌아가기</a></sub>

## ⚖️ 제3부: 전반에 걸친 과제

<a id="evaluation"></a>
### 📊 평가와 벤치마크 (50)
*서베이 §9(평가와 벤치마크)에 해당합니다.*

<details>
<summary><b>논문 50편 보기</b></summary>

- **[GAIA: a benchmark for General AI Assistants](https://arxiv.org/abs/2311.12983)** (Mialon et al., ICLR 2024) - *도구를 쓰는 범용 에이전트 어시스턴트의 기준 벤치마크다. 널리 쓰이는 공개 순위표들이 이를 바탕으로 frontier 에이전트의 발전을 추적한다.*
- **[SWE-bench: Can Language Models Resolve Real-World GitHub Issues?](https://arxiv.org/abs/2310.06770)** (Jimenez et al., ICLR 2024) - *코딩·소프트웨어 공학 에이전트의 사실상 표준 벤치마크이며, 여기서 SWE-bench Verified/Lite/Live/Multimodal 계열이 파생되었다.* [[code](https://github.com/SWE-bench/SWE-bench)]
- **[MLAgentBench: Evaluating Language Agents on Machine Learning Experimentation](https://arxiv.org/abs/2310.03302)** (Huang et al., arXiv 2023) - *'AI 연구 에이전트'·'ML 엔지니어링 에이전트' 평가라는 하위 분야의 선구적 벤치마크로, MLE-bench, RE-Bench 등의 전신이다.* [[code](https://github.com/snap-stanford/MLAgentBench)]
- **[τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains](https://arxiv.org/abs/2406.12045)** (Yao et al., arXiv 2024) - *에이전트와 사용자의 상호작용, 그리고 정책 준수를 처음으로 평가한 벤치마크로, 기업·고객 서비스 에이전트 평가에서 표준 참조점이 되었다.* [[code](https://github.com/sierra-research/tau-bench)]
- **[AgentBoard: An Analytical Evaluation Board of Multi-turn LLM Agents](https://arxiv.org/abs/2401.13178)** (Ma et al., NeurIPS 2024) - *통과/실패만 보는 거친 채점의 빈틈을 메우는 통합 평가 도구 모음으로 널리 쓰이며, 평가 방법론의 틀을 잡는 데 직접 참고가 된다.* [[code](https://github.com/hkust-nlp/AgentBoard)]
- **[SmartPlay: A Benchmark for LLMs as Intelligent Agents](https://arxiv.org/abs/2310.01557)** (Wu et al., ICLR 2024) - *능력을 쪼개어 평가하는 방법론으로, 이후 에이전트 능력을 세밀하게 나눠 재는 벤치마크들에 영향을 주었다.* [[code](https://github.com/microsoft/SmartPlay)]
- **[TravelPlanner: A Benchmark for Real-World Planning with Language Agents](https://arxiv.org/abs/2402.01622)** (Xie et al., ICML 2024) - *제약이 많은 복잡한 다중 도구 계획을 시험하는 스트레스 테스트로 널리 인용되며, 에이전트가 아직 long-horizon 계획을 믿을 만하게 해내지 못한다는 것을 보여 준다.* [[code](https://github.com/OSU-NLP-Group/TravelPlanner)]
- **[InterCode: Standardizing and Benchmarking Interactive Coding with Execution Feedback](https://arxiv.org/abs/2306.14898)** (Yang et al., NeurIPS 2023) - *실행 피드백을 주고받는 상호작용형 평가 패러다임을 세웠고, 이후의 코딩 에이전트와 터미널 에이전트 벤치마크가 이를 바탕으로 한다.* [[code](https://intercode-benchmark.github.io)]
- **[GTA: A Benchmark for General Tool Agents](https://arxiv.org/abs/2407.08713)** (Wang et al., NeurIPS 2024) - *앞선 합성 도구 사용 벤치마크가 남긴 현실성의 빈틈(암묵적 의도, 실제 multimodal 컨텍스트)을 메운다.* [[code](https://github.com/open-compass/GTA)]
- **[Survey on Evaluation of LLM-based Agents](https://arxiv.org/abs/2503.16416)** (Yehudai et al., arXiv 2025) - *주제에 정확히 들어맞는 서베이로, 새 에이전트 서베이의 평가 절에 바로 쓸 수 있는 분류 체계를 제공한다.*
- **[Evaluation and Benchmarking of LLM Agents: A Survey](https://arxiv.org/abs/2507.21504)** (Mohammadi et al., KDD 2025) - *Yehudai 등의 서베이와 독립적으로 쓰여 그것을 보완하는 세부 주제 서베이로, 분류 체계가 빠짐없이 다루는지 교차 확인하는 데 유용하다.*
- **[τ²-Bench: Evaluating Conversational Agents in a Dual-Control Environment](https://arxiv.org/abs/2506.07982)** (Barres et al., arXiv 2025) - *사용자와 에이전트가 모두 환경을 조작하는 설정으로 τ-bench를 확장한다.* [[code](https://github.com/sierra-research/tau2-bench)]
- **[Agent-as-a-Judge: Evaluate Agents with Agents](https://arxiv.org/abs/2410.10934)** (Zhuge et al., arXiv 2024) - *에이전트로 에이전트를 평가하는 방식을 체계화했고, 심판 순환성 문제를 논할 때 기준점이 된다.* [[code](https://github.com/metauto-ai/agent-as-a-judge)]
- **[Holistic Agent Leaderboard: The Missing Infrastructure for AI Agent Evaluation](https://arxiv.org/abs/2510.11977)** (Kapoor et al., arXiv 2025) - *에이전트를 대규모로 다시 평가하면서 정확도와 함께 비용도 보고하는 표준화된 harness다.*
- **[Dr. Bench: A Multidimensional Evaluation for Deep Research Agents, from Answers to Reports](https://arxiv.org/abs/2510.02190)** (Yao et al., arXiv 2025) - *Deep research 에이전트를 답변부터 보고서까지, 의미적 품질, 주제 집중도, 검색 신뢰성의 측면에서 평가한다.* [[code](https://github.com/EVIGBYEN/DrBench)]
- **[Terminal-Bench: Benchmarking Agents on Hard, Realistic Tasks in Command Line Interfaces](https://arxiv.org/abs/2601.11868)** (Merrill et al., arXiv 2026) - *어렵고 현실적인 커맨드라인 과제로 구성되며, 터미널 에이전트의 사실상 표준이다.* [[code](https://github.com/laude-institute/terminal-bench)]

- **[Can AI Agents Answer Your Data Questions? A Benchmark for Data Agents (DataAgentBench)](https://arxiv.org/abs/2603.20576)** (Ma et al., arXiv 2026) - *이질적인 데이터베이스 시스템에 걸친 벤치마크다. 복잡한 데이터 질문에서 frontier 모델의 정확도는 38%에 그친다.* [[code](https://github.com/ucbepic/DataAgentBench)]
- **[AgencyBench: Benchmarking the Frontiers of Autonomous Agents in 1M-Token Real-World Contexts](https://arxiv.org/abs/2601.11044)** (Li et al., arXiv 2026) - *최대 1M 토큰 컨텍스트에서 자율 에이전트를 시험하는 실제 long-horizon 시나리오 32개로 구성된다.* [[code](https://github.com/GAIR-NLP/AgencyBench)]
- **[Agent-Diff: Benchmarking LLM Agents on Enterprise API Tasks via Code Execution with State-Diff-Based Evaluation](https://arxiv.org/abs/2602.11224)** (Pysklo et al., arXiv 2026) - *기업 API 과제에서 에이전트를 평가하는 벤치마크로, sandbox에서 코드를 실행하게 하고 성공 여부는 trace 일치가 아니라 state diff로 판정한다.* [[code](https://github.com/agent-diff-bench/agent-diff)]
- **[When Tools Fail: Benchmarking Dynamic Replanning and Anomaly Recovery in LLM Agents (ToolMaze)](https://arxiv.org/abs/2606.05806)** (Zhu et al., arXiv 2026) - *도구 호출이 실패할 때 에이전트가 계획을 다시 세우고 복구하는지를, 교란 유형 분류 체계를 갖춘 DAG 기반 벤치마크로 시험한다.* [[code](https://github.com/Zhudongsheng75/ToolMaze)]
- **[Agent-ValueBench: A Comprehensive Benchmark for Evaluating Agent Values](https://arxiv.org/abs/2605.10365)** (Dong et al., arXiv 2026) - *에이전트의 가치관만을 다룬 첫 벤치마크로, 가치 체계 28개에 걸쳐 실행 가능한 환경 394개와 가치 충돌 과제 4,335개를 담았다.*
- **[How Many Tasks Are Enough for Agent Benchmark Decisions? A Replay Analysis of Public LLM Agent Benchmarks](https://arxiv.org/abs/2607.12338)** (Huang et al., arXiv 2026) - *벤치마크 순위를 믿으려면 과제가 실제로 몇 개나 필요한지를 replay 분석으로 따진다.* [[code](https://github.com/WilliamWJHuang/How-Many-Tasks-Are-Enough-for-Agent-Benchmark-Decisions)]
- **[Beyond Static Leaderboards: Predictive Validity for the Evaluation of LLM Agents](https://arxiv.org/abs/2606.19704)** (Patel et al., arXiv 2026) - *에이전트 순위표로 실제 배포에서의 성능을 가늠하려면 점수만이 아니라 예측 타당도가 필요하다고 주장한다.*
- **[AgentGym2: Benchmarking Large Language Model Agents in De-Idealized Real-World Environments](https://arxiv.org/abs/2607.05174)** (Xi et al., arXiv 2026) - *이상화를 걷어 낸 환경에서 에이전트를 평가해, 깔끔한 벤치마크 세계와 실제 세계의 간극을 좁힌다.* [[code](https://github.com/hotdog-zz/Agentgym2)]
- **[Measuring Harness-Induced Belief Divergence in Multi-Step LLM Agents](https://arxiv.org/abs/2607.04528)** (Yi et al., arXiv 2026) - *Harness 하나만으로 에이전트의 믿음이 단계를 거치며 얼마나 달라지는지 측정해, 에이전트 평가의 교란 요인 하나를 분리해 낸다.* [[code](https://github.com/Hik289/Harness-induce-bias)]
- **[Rethinking the Evaluation of Harness Evolution for Agents](https://arxiv.org/abs/2607.12227)** (Wang et al., arXiv 2026) - *Harness도 모델만큼 점수에 영향을 준다는 점을 들어, harness의 진화를 어떻게 평가해야 할지 다시 따져 본다.* [[code](https://github.com/rethinking-harness-evolution/code)]
- **[ReliabilityBench: Evaluating LLM Agent Reliability Under Production-Like Stress Conditions](https://arxiv.org/abs/2601.06112)** (Gupta et al., arXiv 2026) - *깔끔한 단일 실행이 아니라 실제 서비스에 가까운 부하 조건에서 에이전트의 신뢰성을 평가한다.*
- **[AgentAtlas: Beyond Outcome Leaderboards for LLM Agents](https://arxiv.org/abs/2605.20530)** (Mazaheri et al., arXiv 2026) - *결과 순위표만 보는 데서 벗어나, 에이전트의 제어가 어디서 실패하는지를 결정 단위로 진단한다.*
- **[CUBE: A Standard for Unifying Agent Benchmarks](https://arxiv.org/abs/2603.15798)** (Lacoste et al., arXiv 2026) - *제각각인 에이전트 벤치마크를 하나의 인터페이스로 묶는 표준을 제안한다.* [[code](https://github.com/The-AI-Alliance/cube-standard)]
- **[UniClawBench: A Universal Benchmark for Proactive Agents on Real-World Tasks](https://arxiv.org/abs/2607.08768)** (Chen et al., arXiv 2026) - *능력 중심의 이중 언어 벤치마크 UniClawBench를 내놓는다. 과제 400개는 실제로 돌아가는 Docker 환경에서 단계별 체크포인트를 두고 실행된다. 능동형 LLM 에이전트를 skill 활용, 탐색, 긴 컨텍스트 추론, multimodal 이해, 여러 플랫폼 간 조율에 걸쳐 평가하며, 숨겨진 감독 에이전트를 두어 다중 턴 피드백으로 채점 기준이 새어 나가지 않게 한다.* [[code](https://github.com/HKU-MMLab/UniClawBench)]
- **[PolyWorkBench: Benchmarking LLM Agents for Cross-Lingual Long-Horizon Workflows](https://arxiv.org/abs/2607.06008)** (Li et al., arXiv 2026) - *상거래, 지식 업무, 법률 분석, 현지화, 제조를 아우르는 과제 67개로, 다국어 long-horizon 업무 workflow에서 LLM 에이전트를 평가하는 벤치마크 PolyWorkBench를 내놓는다. Rubric 기반 구조 채점, 실행 가능한 상태 검사, LLM 심판을 섞어 채점한다. 언어에 따라 성능 편차가 크고, 더 어려운 교차 언어 과제에서는 성능이 급격히 떨어진다.*
- **[EvoAgentBench: Benchmarking Agent Self-Evolution via Ability Transfer](https://arxiv.org/abs/2607.05202)** (Gao et al., arXiv 2026) - *LLM 에이전트의 자기 진화를 절차 지식의 전이로 보고 평가하는 벤치마크를 내놓는다. 에이전트 실행 trace에 근거한 'Ability'를 뽑아 웹 조사, 알고리즘 추론, 소프트웨어 공학, 지식 업무에 걸친 도메인별 Ability Graph로 조직한다. 선별해 다듬은 Ability는 모델 계열을 넘어 안정적으로 전이되지만, 모든 설정에서 이득을 내는 자동 방법은 없다.*
- **[Act As a Real Researcher: A Suite of Benchmarks Evaluating Frontier LLMs and Agentic Harnesses in Research Lifecycle](https://arxiv.org/abs/2606.07462)** (Wang et al., arXiv 2026) - *Frontier LLM과 agentic harness가 연구 전 과정에 걸쳐 초급 연구 인턴 수준의 과제를 해낼 수 있는지 평가하는 컨테이너 기반 벤치마크 모음 AARRI-Bench를 소개한다.* [[code](https://github.com/AARR-bench/AARRI-bench)]
- **[ReplicatorBench: Benchmarking LLM Agents for Replicability in Social and Behavioral Sciences](https://arxiv.org/abs/2602.11354)** (Nguyen et al., arXiv 2026) - *사람이 검증한 재현 가능 주장과 재현 불가능 주장으로 이루어진 벤치마크 ReplicatorBench를 내놓고, 데이터 수집, 실험 설계와 실행, 결과 해석에 걸쳐 LLM 에이전트가 사회·행동과학 연구를 재현하는 능력을 평가한다. 에이전트는 실험을 설계하고 돌리는 일은 잘하지만, 재현에 필요한 새 데이터를 찾아오는 데서 막힌다.* [[code](https://github.com/CenterForOpenScience/llm-benchmarking)]
- **[Benchmark Test-Time Scaling of General LLM Agents](https://arxiv.org/abs/2602.18998)** (Li et al., arXiv 2026) - *검색, 코딩, 추론, 도구 사용에 걸쳐 범용 LLM 에이전트를 평가하는 통합 벤치마크 General AgentBench를 내놓는다. 순차적 test-time scaling은 컨텍스트 한계 때문에, 병렬 test-time scaling은 검증 격차 때문에 성능을 끌어올리지 못하며, 앞선 에이전트 열 개는 도메인별 평가에서 범용 설정으로 옮겨 오면 성능이 크게 떨어진다.* [[code](https://github.com/cxcscmu/General-AgentBench)]
- **[BenchGuard: Who Guards the Benchmarks? Automated Auditing of LLM Agent Benchmarks](https://arxiv.org/abs/2604.24955)** (Tu et al., arXiv 2026) - *Frontier 모델에게 벤치마크 자체를 점검하게 해, ScienceAgentBench에서 과제를 풀 수 없게 만든 오류를 포함해 저자가 인정한 문제 12건을 찾아냈다. BIXBench에서는 과제 50개짜리 감사 한 번에 미화 15달러 미만을 들여 전문가가 짚은 문제의 83.3%를 잡아냈다.*
- **[Automated Benchmark Auditing for AI Agents and Large Language Models](https://arxiv.org/abs/2605.26079)** (Wang et al., arXiv 2026) - *Auto Benchmark Audit(ABA)이라는 agentic 프레임워크를 내놓는다. 아홉 개 도메인의 벤치마크 168개를 감사해 과제의 25.7% 이상에서 치명적 문제(모호한 설계, 실행 충돌, 틀린 정답)를 찾았고, 이 과제를 걸러 내면 모델 순위가 뒤바뀌며 SWE-bench Verified와 Terminal-Bench 2의 평균 점수가 각각 9.9%, 9.6% 오른다.*
- **[PerspectiveGap: A Benchmark for Multi-Agent Orchestration Prompting](https://arxiv.org/abs/2606.08878)** (Sun et al., arXiv 2026) - *Orchestration 프롬프트 작성을 별도의 능력으로 떼어 낸다. 토폴로지 10종에 걸친 시나리오 110개에서 모델 33개의 평균 통과율은 17.2%다.* [[code](https://github.com/WhymustIhaveaname/PerspectiveGap)]
- **[ClawBench: Can AI Agents Complete Everyday Online Tasks?](https://arxiv.org/abs/2604.08523)** (Zhang et al., arXiv 2026) - *실제 운영 중인 사이트 144곳에서 브라우저 에이전트에게 일상 과제 153개를 맡기되, 마지막 요청을 가로채 실제 구매나 예약은 일어나지 않게 한다. 시험한 모델 가운데 가장 강한 모델이 해낸 과제는 셋 중 하나다.* [[code](https://github.com/TIGER-AI-Lab/ClawBench)]
- **[Do Agent Benchmarks Measure Capability? Protocol Validity in the Age of Agentic AI](https://arxiv.org/abs/2607.22368)** (Shao et al., arXiv 2026) - *에이전트 벤치마크 15개의 trace 2,385개를 감사해, Frontier Science와 AutoLab 과제의 대략 셋 중 둘에서 노출 문제와 reward hacking을 찾아냈고, 이 때문에 점수가 0.45에서 1.00만큼 부풀려졌다.*
- **[The Hidden Footprint: Making Storage a First-Class Metric for LLM Agent Evaluation](https://arxiv.org/abs/2607.11149)** (Yu et al., arXiv 2026) - *정확도가 똑같은 에이전트 구성도 디스크에 남기는 바이트 수는 15.7배 차이가 난다. 그러니 영구 저장소 사용량도 정확도, 재구성 가능성과 함께 보고해야 한다.*
- **[OmegaUse-OfficeVal: Benchmarking LLM Agents on Long-Horizon Office-Suite Tasks with Economic Grounding](https://arxiv.org/abs/2607.27155)** (Zhou et al., arXiv 2026) - *사람이 하면 평균 2.32시간이 걸리는 long-horizon 사무 과제 100개에, 대체하는 노동만큼 값을 매긴다. Frontier 모델은 사람보다 훨씬 저렴하지만 결과물 품질은 한참 못 미쳤다.* [[code](https://omegause-officeval.github.io)]
- **[AV-AIVAT: 74x Cheaper Agent Evaluation with Certified Anytime-Valid Stopping in Imperfect-Information Games](https://arxiv.org/abs/2608.06362)** (Li et al., arXiv 2026) - *분산 감소와 연속 모니터링되는 confidence sequence를 짝지어, 명시한 confidence level을 무효로 만들지 않고도 증거가 확정되는 즉시 에이전트 비교를 멈출 수 있게 한다. 짝지은 포커 핸드 71,439개에서 원시 결과만으로는 중앙값 기준 74배 많은 게임이 필요했다.*
- **[PATH-Bench: Path-Dependent Evaluation of Lifelong Agents](https://arxiv.org/abs/2608.01149)** (Yang et al., arXiv 2026) - *평생 학습 에이전트를 과제 하나하나가 아니라 경험이 쌓인 순서에 따라 평가하며 순방향 전이, 역방향 전이, 망각을 잰다. 전이가 강하다고 해서 기억이 유지되는 것은 아니며, 나중의 경험이 앞서 얻은 이득을 되돌릴 수 있음을 보였다.*
- **[Benchmarking LLM Judges for Mobile Agent Evaluation](https://arxiv.org/abs/2608.11434)** (Wang et al., arXiv 2026) - *사람이 주석을 단 모바일 에이전트 trajectory 931개로 LLM-as-judge 방법 여섯 가지를 시험했다. 샘플링한 스크린샷만 보는 단순한 baseline이 전용으로 만든 심판과 대등하거나 더 나았고, 심판 품질을 좌우한 것은 파이프라인이 아니라 backbone 모델이었으며, 두 backend는 각각 보수적인 쪽과 관대한 쪽으로 정반대의 실패 양상을 보였다.*
- **[OmnilingualGAIA2: Evaluating the Multilingual Gap in Frontier AI Agents](https://arxiv.org/abs/2608.08775)** (Caciolai et al., arXiv 2026) - *GAIA2를 다섯 가지 문자 체계에 걸친 열 개 언어로 넓히자 pass@3 기준 8.8에서 18.4점의 언어 간 격차가 나타났다. 이 격차는 정량 추론이 아니라 도구 orchestration에 몰려 있고 모델 규모를 키워도 좁혀지지 않는다. Error attribution으로는 격차의 55%가 모델에서 비롯되며, 번역 contamination은 시나리오·언어 쌍의 6.4% 이내로 한정된다.*
- **[LoopArena: Benchmarking Models as Runtime Controllers for Loop Engineering](https://arxiv.org/abs/2608.28281)** (Wang et al., arXiv 2026) - *코드를 짜는 모델이 아니라 방향을 잡는 모델을 채점한다. 코딩 라운드가 끝날 때마다 평가 대상인 Controller가 구조화된 실행 요약을 읽고, 따로 고정해 둔 Worker에게 다음에 할 일, 검증할 것, 멈출지 여부를 지시한다. 실행 범위와 비용을 맞바꾸는 세 가지 설정에서 전체 과제의 엄격한 성공률은 최고 24.69%였고, Worker를 전혀 돌리지 않는 저렴한 설정도 Spearman 상관 0.97로 비싼 설정과 거의 같은 Controller 순위를 냈다.* [[code](https://github.com/AMAP-ML/LoopArena)]
- **[τ^τ-Bench: An Environment for End-To-End, Realistic Agent Construction](https://arxiv.org/abs/2609.04611)** (Shi et al., arXiv 2026) - *에이전트를 만드는 일 자체를 과제로 삼는다. 개발자 에이전트는 코드베이스, 운영 중인 API, 요구 사항을 쥔 고객, 서빙 비용 상한을 넘겨받아 고객 서비스 에이전트를 출시하고, 이 에이전트는 held-out 모의 사용자에게 배포되어 채점된다. 과제 53개에서 가장 강한 구성이 평가 시뮬레이션의 23.9%를 통과한 반면 전문가가 작성한 상한은 82.2%였다. 실패도 기록을 얕게 조회하고, 고객에게 거의 아무것도 알리지 않고, 처음 돌아가는 아키텍처를 그대로 내보내는, 누가 봐도 사람 같은 방식이었다.*
- **[Autonomous Evaluation and Refinement of Digital Agents](https://arxiv.org/abs/2404.06474)** (Pan et al., COLM 2024) - *비용 수준이 서로 다른 에이전트 평가자를 여러 개 만들었고, oracle 지표와의 일치율은 74.4에서 92.9%였다. 이를 보상으로 써서 추가 감독 없이 WebArena의 최고 성능을 29% 끌어올렸다.* [[code](https://github.com/Berkeley-NLP/Agent-Eval-Refine)]
- **[JEV-as-a-Judge: Accept When Confident, Escalate When Unsure](https://arxiv.org/abs/2609.26550)** (Li et al., arXiv 2026) - *텍스트 대신 결정을 돌려주는 심판은 일반적인 선호와 사실성 판정에서 가장 강한 LLM 심판에 세 포인트 이내로 따라붙으면서 비용은 그 0.36%에 그친다. 유도 과정을 검산해야 하거나 틀린 답이 그럴듯하게 쓰였을 때는 더 뒤처지며, 받아들이거나 escalation하는 cascade는 더 강한 심판 정확도의 99%를 유지한다.*
</details>

<sub><a href="#contents">↑ 목차로 돌아가기</a></sub>

<a id="safety"></a>
### 🛡️ 안전과 정렬 (59)
*서베이 §11(안전·보안·신뢰성)에 해당합니다.*

<details>
<summary><b>논문 59편 보기</b></summary>

- **[Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection](https://arxiv.org/abs/2302.12173)** (Greshake et al., arXiv 2023) - *이후 거의 모든 LLM 에이전트 보안 연구의 바탕이 된 indirect prompt injection 위협 모델을 처음 세운 논문이다.* ⭐ [[code](https://github.com/greshake/llm-security)]
- **[AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents](https://arxiv.org/abs/2406.13352)** (Debenedetti et al., NeurIPS 2024) - *Prompt injection 공격에 대한 에이전트의 견고성과 방어 기법을 재는, 가장 널리 쓰이는 표준 테스트베드다.* [[code](https://github.com/ethz-spylab/agentdojo)]
- **[InjecAgent: Benchmarking Indirect Prompt Injections in Tool-Integrated Large Language Model Agents](https://arxiv.org/abs/2403.02691)** (Zhan et al., ACL 2024) - *도구를 통합한 에이전트가 indirect prompt injection에 얼마나 취약한지 정량화하는 표준 참조 벤치마크다.* [[code](https://github.com/uiuc-kang-lab/InjecAgent)]
- **[WASP: Benchmarking Web Agent Security Against Prompt Injection Attacks](https://arxiv.org/abs/2504.18575)** (Evtimov et al., arXiv 2025) - *Prompt injection 평가를 단일 단계 도구 호출에서 현실적인 다단계 자율 웹 브라우징 에이전트로 넓힌다.* [[code](https://github.com/facebookresearch/wasp)]
- **[R-Judge: Benchmarking Safety Risk Awareness for LLM Agents](https://arxiv.org/abs/2401.10019)** (Yuan et al., EMNLP 2024) - *에이전트의 안전 모니터링 구성 요소로서 LLM 자체의 위험 인식·판단 능력을 평가하는 벤치마크로, 널리 인용된다.* [[code](https://github.com/Lordog/R-Judge)]
- **[Identifying the Risks of LM Agents with an LM-Emulated Sandbox](https://arxiv.org/abs/2309.15817)** (Ruan et al., ICLR 2024) - *실제 도구에 접근하지 않고도 도구 사용 에이전트를 red teaming하고 위험을 찾아내는, 확장 가능한 기초 방법론이다.* [[code](https://github.com/ryoungj/ToolEmu)]
- **[AgentHarm: A Benchmark for Measuring Harmfulness of LLM Agents](https://arxiv.org/abs/2410.09024)** (Andriushchenko et al., ICLR 2025) - *에이전트 오용 위험을 챗봇 jailbreak 위험과 구분한 핵심 벤치마크로, 에이전트로서의 능력이 해악의 가능성을 키운다는 것을 보였다.* [[code](https://github.com/UKGovernmentBEIS/inspect_evals)]
- **[Evil Geniuses: Delving into the Safety of LLM-based Agents](https://arxiv.org/abs/2311.11855)** (Tian et al., arXiv 2023) - *다중 에이전트 LLM 협업이 안전 위험을 줄이기는커녕 키운다는 것을 보인 초기의 체계적 연구 중 하나다.* [[code](https://github.com/T1aNS1R/Evil-Geniuses)]
- **[BadAgent: Inserting and Activating Backdoor Attacks in LLM Agents](https://arxiv.org/abs/2406.03007)** (Wang et al., ACL 2024) - *에이전트 backdoor가 이후의 안전 fine-tuning을 거쳐도 제거되지 않는다는 것을 보인 선구적 연구로, 에이전트 공급망 보안 문제가 제기되는 계기가 되었다.* [[code](https://github.com/DPamK/BadAgent)]
- **[AgentPoison: Red-teaming LLM Agents via Poisoning Memory or Knowledge Bases](https://arxiv.org/abs/2407.12784)** (Chen et al., NeurIPS 2024) - *메모리·지식 베이스 poisoning을, 메모리로 보강한 LLM 에이전트에만 있고 학습도 필요 없는 별개의 attack surface로 정립했다.* [[code](https://github.com/AI-secure/AgentPoison)]
- **[Agent Security Bench (ASB): Formalizing and Benchmarking Attacks and Defenses in LLM-based Agents](https://arxiv.org/abs/2410.02644)** (Zhang et al., arXiv 2024) - *LLM 에이전트를 겨냥한 다양한 공격·방어 유형을 하나의 평가 프레임워크로 묶은, 가장 큰 통합 분류 체계이자 벤치마크다.* [[code](https://github.com/agiresearch/ASB)]
- **[TrustAgent: Towards Safe and Trustworthy LLM-based Agents](https://arxiv.org/abs/2402.01586)** (Hua et al., EMNLP 2024) - *에이전트 안전을 위한 장치로 constitution을 따르는 계획을 제안한, 영향력 있는 초기 방어·완화 프레임워크다.* [[code](https://github.com/agiresearch/TrustAgent)]
- **[SafeAgentBench: A Benchmark for Safe Task Planning of Embodied LLM Agents](https://arxiv.org/abs/2412.13178)** (Yin et al., arXiv 2024) - *에이전트 안전 평가를 디지털·텍스트 영역에서 물리 세계의 embodied 위험으로 넓혀, 안전 실패가 로보틱스에서도 나타난다는 것을 보였다.* [[code](https://github.com/shengyin1224/SafeAgentBench)]
- **[AI Agents That Matter](https://arxiv.org/abs/2407.01502)** (Kapoor et al., arXiv 2024) - *에이전트 능력에 관한 주장을 평가하는 방식을 바꿔 놓은, 널리 인용되는 비판이다. 에이전트의 위험과 이득 사이의 균형을 믿을 만하게 평가하는 문제와 직결된다.*
- **[Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training](https://arxiv.org/abs/2401.05566)** (Hubinger et al., arXiv 2024) - *현재의 safety training 파이프라인이 숨겨진 기만 행동이나 정렬되지 않은 행동을 없애지 못할 수 있음을 보인 이정표적 시연으로, 에이전트 신뢰성 논의에 직접적인 근거가 된다.* [[code](https://github.com/anthropics/sleeper-agents-paper)]
- **[Frontier Models are Capable of In-context Scheming](https://arxiv.org/abs/2412.04984)** (Meinke et al., arXiv 2024) - *Frontier 자율 에이전트에 in-context scheming 능력이 있다는 첫 체계적 실증 근거로, 자율성과 관련된 정렬 위험에서 핵심 쟁점이다.*
- **[Emergent Misalignment: Narrow Finetuning can Produce Broadly Misaligned LLMs](https://arxiv.org/abs/2502.17424)** (Betley et al., arXiv 2025) - *에이전트 능력을 겨냥한 좁고 겉보기에 무해한 fine-tuning이 광범위하고 예측할 수 없는 안전 실패를 낳을 수 있다는, 최근 큰 영향을 준 발견이다.* [[code](https://github.com/emergent-misalignment/emergent-misalignment)]
- **[AI Deception: A Survey of Examples, Risks, and Potential Solutions](https://arxiv.org/abs/2308.14752)** (Park et al., arXiv 2023) - *AI의 기만을 실증에 근거한 별개의 위험 범주로 정립한 기초 서베이다. 이 범주는 에이전트의 신뢰성과 정렬에서 중심을 차지한다.*
- **[AI Alignment: A Comprehensive Survey](https://arxiv.org/abs/2310.19852)** (Ji et al., arXiv 2023) - *가장 포괄적인 일반 정렬 서베이 중 하나로, 에이전트 특화 안전 연구의 바탕이 되는 개념 틀(RICE, forward/backward alignment)을 제공한다.* [[code](https://github.com/PKU-Alignment/AlignmentSurvey)]
- **[A Survey on Trustworthy LLM Agents: Threats and Countermeasures](https://arxiv.org/abs/2503.09648)** (Yu et al., arXiv 2025) - *이 하위 분야에 가장 직접 맞닿은 최근 서베이로, 에이전트 특유의 안전·보안 위협 유형을 거의 모두 아우르는 분류 체계를 제공한다.* [[code](https://github.com/Ymm-cll/TrustAgent)]
- **[A Comprehensive Survey in LLM(-Agent) Full Stack Safety: Data, Training and Deployment](https://arxiv.org/abs/2504.15585)** (Wang et al., arXiv 2025) - *LLM 생애 주기 전체를 다루는 대규모 안전 서베이로, 에이전트 특유의 위험을 더 넓은 LLM 안전 파이프라인 안에 자리매김한다. 에이전트 위험을 더 큰 안전 스택의 한 단계로 보는 틀을 잡는 데 유용하다.*
- **[A Survey on Autonomy-Induced Security Risks in Large Model-Based Agents](https://arxiv.org/abs/2506.23844)** (Su et al., arXiv 2025) - *이 세부 주제의 핵심 명제, 즉 에이전트 특유의 새로운 보안 위험이 바탕이 되는 LLM만이 아니라 자율성 그 자체에서 비롯된다는 주장을 정면으로 내세운다.*
- **[Discovering Language Model Behaviors with Model-Written Evaluations](https://arxiv.org/abs/2212.09251)** (Perez et al., arXiv 2022) - *RLHF 학습 규모와, 자기 보존이나 권력 추구에 가까운 선호가 모델의 답변에 새로 나타나는 현상을 연결한 초기의 중요한 실증 근거로, 자율 에이전트 정렬 문제를 앞서 제기했다.* [[code](https://github.com/anthropics/evals)]
- **[Towards Understanding Sycophancy in Language Models](https://arxiv.org/abs/2310.13548)** (Sharma et al., arXiv 2023) - *아첨을 견고성·정렬의 실패 양상으로 다룬 핵심 실증 연구로, 자율적으로 결정을 내리며 정직한 평가를 해야 하는 에이전트에 직접적인 시사점을 준다.* [[code](https://github.com/meg-tong/sycophancy-eval)]
- **[Design Patterns for Securing LLM Agents against Prompt Injections](https://arxiv.org/abs/2506.08837)** (Beurer-Kellner et al., arXiv 2025) - *신뢰할 수 없는 입력을 읽은 뒤 에이전트가 할 수 있는 일을 제한하는 아키텍처 패턴을 모은 목록이다.*
- **[OS-Harm: A Benchmark for Measuring Safety of Computer Use Agents](https://arxiv.org/abs/2506.14866)** (Kuntz et al., arXiv 2025) - *에이전트 안전 측정을 실제 인터페이스를 다루는 computer use 에이전트로 넓힌다.*
- **[The 2025 AI Agent Index: Documenting Technical and Safety Features of Deployed Agentic AI Systems](https://arxiv.org/abs/2602.17753)** (Staufer et al., FAccT 2026) - *배포된 에이전트 시스템 30개를 조사한 실증 색인으로, 능력 정보와 안전 정보 사이의 투명성 격차를 기록했다.*

- **[AgentDoG: A Diagnostic Guardrail Framework for AI Agent Safety and Security](https://arxiv.org/abs/2601.18491)** (Liu et al., arXiv 2026) - *에이전트 위험을 하나로 정리한 분류 체계를 바탕으로, 이진 라벨 대신 안전하지 않은 trajectory의 근본 원인을 짚어 주는 진단형 guardrail을 만든다.* [[code](https://github.com/AI45Lab/AgentDoG)]
- **[The Landscape of Prompt Injection Threats in LLM Agents: From Taxonomy to Analysis](https://arxiv.org/abs/2602.10453)** (Wang et al., arXiv 2026) - *LLM 에이전트를 노리는 indirect prompt injection 위협을 분류 체계로 정리하고, 방어가 놓치는 빈틈을 분석한다.*
- **[ARGUS: Defending LLM Agents Against Context-Aware Prompt Injection](https://arxiv.org/abs/2605.03378)** (Weng et al., arXiv 2026) - *에이전트의 결정이 믿을 만한 근거에 기대고 있는지 감사하는 영향 provenance 그래프를 만들어, 공격 성공률을 3.8%로 낮춘다.*
- **[Provably Secure Agent Guardrail](https://arxiv.org/abs/2605.29251)** (Wu et al., arXiv 2026) - *에이전트가 행동하기 전에 의도를 일차 논리 제약으로 형식화하도록 강제해, 공격 성공과 오탐이 한 건도 나오지 않게 한다.*
- **[AutoRISE: Agent-Driven Strategy Evolution for Red-Teaming Large Language Models](https://arxiv.org/abs/2604.22871)** (Gautam et al., arXiv 2026) - *코딩 에이전트가 프롬프트만이 아니라 실행 가능한 공격 전략 자체를 진화시켜, 모델 11개에서 jailbreak 공격 성공률을 17포인트 높인다.*
- **[When Agents Remember Too Much: Memory Poisoning Attacks on Large Language Model Agents](https://arxiv.org/abs/2607.06595)** (Torres et al., arXiv 2026) - *에이전트를 노리는 memory poisoning 공격을 다룬다. 오래 남는 상태를 오염시켜 침해 효과가 세션이 끝난 뒤에도 남게 한다.*
- **[Agent Data Injection Attacks are Realistic Threats to AI Agents](https://arxiv.org/abs/2607.05120)** (Choi et al., arXiv 2026) - *에이전트 입력에 데이터를 주입하는 공격이 억지로 꾸민 실험실 설정이 아니라 현실적인 위협임을 보인다.*
- **[AgentAbstain: Do LLM Agents Know When Not to Act?](https://arxiv.org/abs/2607.10059)** (Liu et al., arXiv 2026) - *에이전트가 행동하지 말아야 할 때를 아는지 묻고, 행동을 삼가는 것을 그 자체로 중요한 안전 행동으로 다룬다.* [[code](https://github.com/AntiQuality/agentabstain)]
- **[Prismata: Confining Cross-Site Prompt Injection in Web Agents](https://arxiv.org/abs/2607.08147)** (Villa et al., arXiv 2026) - *웹 에이전트의 cross-site prompt injection을, 모델이 스스로 막아 주리라 믿는 대신 경계에서 격리한다.*
- **[The Balkanization of Execution-Security Research for AI Coding Agents: Isolation, Access Control, and Time-of-Check-to-Time-of-Use Vulnerabilities](https://arxiv.org/abs/2607.05743)** (Rashidi et al., arXiv 2026) - *코딩 에이전트의 실행 보안 연구가 격리, 접근 제어, 관련 방어로 조각나 있는 현황을 정리한다.*
- **[Supply-Chain Poisoning Attacks Against LLM Coding Agent Skill Ecosystems](https://arxiv.org/abs/2604.03081)** (Qu et al., arXiv 2026) - *코딩 에이전트가 설치해 쓰는 skill 생태계를 노린 공급망 poisoning 공격을 시연한다.*
- **[Overcoming the Retrieval Barrier: Indirect Prompt Injection in the Wild for LLM Systems](https://arxiv.org/abs/2601.07072)** (Chang et al., arXiv 2026) - *실사용 환경의 indirect prompt injection을 연구해, 실제 LLM 시스템에서는 검색 장벽이 가정보다 약하다는 것을 보인다.*
- **[PISmith: Reinforcement Learning-based Red Teaming for Prompt Injection Defenses](https://arxiv.org/abs/2603.13026)** (Yin et al., arXiv 2026) - *Prompt injection 방어를 자동으로 스트레스 테스트하는 강화학습 기반 red teaming이다.* [[code](https://github.com/albert-y1n/PISmith)]
- **[MOSAIC: Knowledge-Guided CLI Command Composition Attack in LLM Coding Agents](https://arxiv.org/abs/2607.02857)** (Wu et al., arXiv 2026) - *LLM 코딩 에이전트에서 하나하나는 무해한 CLI 명령들이 위험한 생산자·소비자 상태 관계를 이루는 조합 수준의 attack surface를 찾아내고, MOSAIC을 제안한다.*
- **[KidnapRAG: A Black-Box Attack for Hijacking Reasoning in Agentic Retrieval-Augmented Generation Systems](https://arxiv.org/abs/2607.00422)** (Choi et al., arXiv 2026) - *프롬프트, trace, 파라미터에 전혀 접근하지 않고 역할이 정해진 문서 세 개(Bait, Chain-Link, Mal-Ins)로 agentic RAG를 black-box poisoning한다. 세 문서는 각각 첫 검색 결과에 들어가고, 질의 재작성을 유도하고, 공격자가 통제하는 근거를 공급한다.* [[code](https://github.com/chanwoochoi316/KidnapRAG)]
- **[(A)I Sees What You Don't: Exploiting New Attack Surfaces in Third-Party Mobile Agents](https://arxiv.org/abs/2607.00333)** (Zhang et al., arXiv 2026) - *VLM 기반 서드파티 모바일 에이전트에서 지금까지 정리되지 않은 attack surface 두 가지를 찾아낸다. 하나는 사람과 기계가 화면을 다르게 보는 데서 생기는 화면 인식 surface이고, 다른 하나는 에이전트의 실행 파이프라인을 가로채거나 조작하는 오용 채널 surface이다. 인기 프레임워크 다섯 개에서 구체적인 공격 일곱 가지를 보였는데, 특별한 권한이 없는 악성 앱도 에이전트의 행동을 가로챌 수 있고 심하면 임의 명령 실행까지 이어진다.*
- **[Beware of Agentic Botnets: Scalable Untargeted Promptware Attacks via Universal and Transferable Adversarial HalluSquatting](https://arxiv.org/abs/2607.07433)** (Spira et al., arXiv 2026) - *Adversarial hallucination squatting이라는 공격을 내놓는다. 공격자는 인기 저장소와 skill을 두고 LLM이 hallucination으로 지어내는 리소스 식별자의 분포를 모델링하고, 그 이름을 먼저 등록해 적대적 프롬프트를 올려 둔다. Hallucination으로 만들어진 식별자는 저장소 복제 시나리오의 최대 85%, skill 설치 시나리오의 최대 100%에서 나타나고, 모델을 넘어 전이되며, 실제 운영 중인 LLM 애플리케이션에서 원격 코드 실행으로 이어진다.*
- **[BackdoorAgent: A Unified Framework for Backdoor Attacks on LLM-based Agents](https://arxiv.org/abs/2601.04566)** (Feng et al., arXiv 2026) - *LLM 에이전트 workflow(계획, 메모리, 도구 사용)에 계측 장치를 달아 여러 단계의 trajectory에 걸쳐 backdoor trigger를 주입하고 추적하고 평가하는, 단계를 구분하는 프레임워크와 벤치마크를 내놓는다.* [[code](https://github.com/Yunhao-Feng/BackdoorAgent)]
- **[Defense Against Indirect Prompt Injection via Tool Result Parsing](https://arxiv.org/abs/2601.04795)** (Yu et al., arXiv 2026) - *도구 출력을 추출하고 정제하는 도구 결과 파싱 방어를 제안해, 과제 수행 능력은 지키면서 LLM 에이전트를 노린 indirect prompt injection의 공격 성공률을 낮춘다. AgentDojo 벤치마크에서 평가했다.* [[code](https://github.com/qiang-yu/agentdojo/tree/tool-result-extract)]
- **[ICON: Indirect Prompt Injection Defense for Agents based on Inference-Time Correction](https://arxiv.org/abs/2602.20708)** (Wang et al., arXiv 2026) - *Latent space 분석으로 indirect prompt injection을 탐지하고 attention 조작으로 무력화하면서도 과제 수행 능력을 지키는, LLM 에이전트용 추론 시점 방어를 제안한다.*
- **[An AI Agent Execution Environment to Safeguard User Data](https://arxiv.org/abs/2604.19657)** (Stanley et al., arXiv 2026) - *정보 흐름 제어로 사용자의 개인 데이터가 AI 모델과 그 제공자를 포함해 어디에 어떻게 공개될지를 사용자가 정한 권한대로 강제하는 AI 에이전트 실행 환경 GAAP을 소개한다.*
- **[Protocol-Level Attacks on Agentic Commerce Platforms: A Cross-Platform Taxonomy, AIP-Bench, and Unified Defense](https://arxiv.org/abs/2607.21824)** (Louck, arXiv 2026) - *에이전트 커머스 보안을 모델이 아니라 그 아래 프로토콜 계층에서 살핀다. 플랫폼 세 곳에 걸친 프로토콜 취약점 33개는 모델과 상관없이 결정론적으로 악용되며, 그중 세 개를 엮으면 end-to-end 결제 탈취가 된다.*
- **[IssueTrojanBench: Benchmarking AI Coding Agents Against Malicious Issue Requests](https://arxiv.org/abs/2607.20759)** (Singh et al., arXiv 2026) - *배포된 Cursor, Claude Code, Codex Desktop에서 악의적인 이슈 요청의 66.5%가 모든 guardrail을 빠져나가며, 실제로 일어난 거절도 에이전트 프레임워크가 아니라 모델에서 나왔다.*
- **[Rethinking MCP Security: A Large-Scale Study of Runtime MCP Servers and Security Scanner Reliability](https://arxiv.org/abs/2607.11086)** (Chen et al., arXiv 2026) - *실사용 중인 MCP 서버 64,611개를 모았고 그중 37,000개 이상이 실행 가능했다. 이를 감사하는 스캐너들은 오탐이 많아, 표본 경보 가운데 수작업 검증을 통과한 것이 절반도 되지 않았다.*
- **[Agent Against Agent: An Agentic System for Automatic Prompt Injection Red Teaming](https://arxiv.org/abs/2608.05108)** (Wang et al., arXiv 2026) - *한 대상에 맞춘 RL 공격자 대신 전이 가능한 prompt injection 전략 라이브러리를 만들고, 이를 추가 학습 없이 처음 보는 모델에 재사용한다. 샘플당 열 번 안팎의 질의로 Gemini-2.5-Pro에서 76.2%, AgentDojo에서 86.7%의 공격 성공률을 냈다.* [[code](https://github.com/Wang-Yanting/PIMiner)]
- **[LoginTrap: Uncovering Task-Agnostic Phishing-Style Indirect Prompt Injection Attacks against LLM-based Web Agents](https://arxiv.org/abs/2608.04741)** (Guo et al., arXiv 2026) - *웹 에이전트를 설득해 로그인하게 만들 수 있음을 보인다. 공격자가 통제하는 페이지 내용이 인증을 과제의 전제 조건처럼 보이게 해 에이전트를 공격자의 로그인 페이지로 이끌며, 사용자의 과제를 모르고도 평균 86%의 end-to-end 성공률을 낸다.*
- **[Emergent Misaligned Communication in Long-Horizon Multi-Agent LLM Commerce](https://arxiv.org/abs/2608.14825)** (Li et al., arXiv 2026) - *Frontier 모델 13개에 걸쳐 한 해 동안 이어지는 자판기 운영 시뮬레이션 20회에서 오간 에이전트 간 이메일 2,583통 중 12.6%가, 일부러 유도하지 않았는데도 거짓 사실 주장, 조작, 담합, 위협을 담고 있었다. 이 행동은 상호적이고(정렬되지 않은 답장이 나올 odds 1.65배) 스트레스에 좌우되며(재고가 적을 때 1.58배), 모델의 성능 순위로는 예측되지 않는다.*
- **[Governance at the Boundary: How Agent Decomposition Degrades Policy Compliance](https://arxiv.org/abs/2608.16055)** (Li et al., arXiv 2026) - *에이전트를 쪼개면 인계 경계에서 통제 가능성이 떨어진다. KYC/AML 에피소드 626개에서 32B open-weight 모델이 발견한 정책 관련 사실을 희석해 넘긴 비율은 단일 루프에서 0%, 고정 파이프라인에서 56%, orchestrator·하위 에이전트 구조에서 85%였고, 같은 메커니즘이 과소 escalation과 과잉 escalation을 모두 낳는다.*
- **[What's in Your Agent's Context? Context Privilege Escalation Attacks against AI Agent Harness](https://arxiv.org/abs/2609.01222)** (Li et al., arXiv 2026) - *실제 harness가 컨텍스트를 조립하는 방식을 체계화하고, 그 설계에서 자연히 생기는 권한 상승 경로 두 가지를 짚는다. 하나는 낮은 권한의 출처에서 온 공격자 통제 콘텐츠가 더 높은 권한의 메시지 역할에 들어가는 경로이고, 다른 하나는 공격자 통제 콘텐츠가 처음 들어온 범위를 넘어 계속 남는 경로다. Claude Code와 Codex를 포함한 harness 12개에서 이를 시연했고, 피해는 원격 코드 실행과 조작된 도구·skill 호출에까지 이르렀다.*
- **[BAITBENCH: Measuring Agent Reward Hacking with Optional Shortcuts Planted in ML Tasks](https://arxiv.org/abs/2608.30724)** (Prasad et al., arXiv 2026) - *합성 표 형식 ML 과제 세 개에 각각, 공개 점수는 부풀리지만 숨겨진 테스트 세트에서는 실패하고 명시된 규칙은 어기지 않는 선택적 지름길을 심어 둔다. Frontier 에이전트 일곱 개의 실행 중 57.1%가 이 지름길을 택했고, 일곱 중 다섯은 절반을 넘었으며, 프롬프트로 부정행위를 하지 말라고 해도 평균은 절반 위에 머물렀다.*
- **[LlamaFirewall: An open source guardrail system for building secure AI agents](https://arxiv.org/abs/2505.03574)** (Chennabasappa et al., arXiv 2025) - *작은 jailbreak 분류기, injection과 목표 이탈을 살피는 chain-of-thought 감사기, 정적 코드 스캐너를 에이전트를 둘러싼 마지막 런타임 계층으로 쌓는다. AgentDojo에서 86M 분류기 하나만으로 공격 성공률이 17.6%에서 7.5%로 줄고, 감사기를 더하면 1.75%까지 내려간다.* [[code](https://github.com/meta-llama/PurpleLlama/tree/main/LlamaFirewall)]
- **[Type-Safe Is Not Error-Free: A Constrained Decision Head Follows the Option Name, Not the Rubric Bound to It](https://arxiv.org/abs/2609.26758)** (Sun and Xu, arXiv 2026) - *선택지 이름과 rubric의 짝을 바꿔 보니, 타입이 정해진 결정을 내는 decision model은 rubric이 아니라 이름을 따랐다. Workflow 결정 1,200건에서 0/1을 no/yes로 바꿔 부르자 백 건당 70.4건이 더 뒤집혔고, Jev도 같은 역전을 보였으며, type error 비율은 내내 0%였다.*
</details>

<sub><a href="#contents">↑ 목차로 돌아가기</a></sub>

## 🔗 관련 Awesome 리스트

같은 분야에서 함께 볼 만한 읽을거리 목록입니다:

- [js-lee-AI/awesome-agent-loop-papers](https://github.com/js-lee-AI/awesome-agent-loop-papers): **후속 서베이의 논문 목록**으로, 에이전트 루프 자체를 다룹니다. 제어 전략, 학습된 루프, skill, harness, 그리고 루프에서 생기는 평가·안전 문제에 관한 논문을 모았습니다. ![stars](https://img.shields.io/github/stars/js-lee-AI/awesome-agent-loop-papers?style=social)
- [Hannibal046/Awesome-LLM](https://github.com/Hannibal046/Awesome-LLM): 대규모 언어 모델 논문, 도구, 자료를 모은 대표적인 목록입니다. ![stars](https://img.shields.io/github/stars/Hannibal046/Awesome-LLM?style=social)
- [ysymyth/awesome-language-agents](https://github.com/ysymyth/awesome-language-agents): CoALA 프레임워크를 축으로 언어 에이전트 읽을거리를 정리했습니다. ![stars](https://img.shields.io/github/stars/ysymyth/awesome-language-agents?style=social)
- [WooooDyy/LLM-Agent-Paper-List](https://github.com/WooooDyy/LLM-Agent-Paper-List): 서베이 *The Rise and Potential of LLM-Based Agents*(Fudan NLP)를 바탕으로 만든 에이전트 논문 목록입니다. ![stars](https://img.shields.io/github/stars/WooooDyy/LLM-Agent-Paper-List?style=social)
- [luo-junyu/Awesome-Agent-Papers](https://github.com/luo-junyu/Awesome-Agent-Papers): 서베이를 바탕으로 만든 목록으로, 분류 체계에 따라 에이전트의 구축, 협업, 진화를 다룹니다. ![stars](https://img.shields.io/github/stars/luo-junyu/Awesome-Agent-Papers?style=social)
- [e2b-dev/awesome-ai-agents](https://github.com/e2b-dev/awesome-ai-agents): 오픈소스와 클로즈드 소스 **에이전트 제품과 프레임워크**를 이미지와 영상까지 곁들여 폭넓게 모은 디렉터리로, 논문보다는 에이전트를 만드는 도구가 중심입니다. ![stars](https://img.shields.io/github/stars/e2b-dev/awesome-ai-agents?style=social)
- [kyrolabs/awesome-agents](https://github.com/kyrolabs/awesome-agents): 엄선한 에이전트 프레임워크와 라이브러리를 모았고, 항목마다 실시간 스타 배지가 붙어 있습니다. ![stars](https://img.shields.io/github/stars/kyrolabs/awesome-agents?style=social)

> 관련 목록을 운영하고 계신가요? [PR을 열어](CONTRIBUTING.md) 여기에 추가해 주세요. 기꺼이 서로 링크를 걸겠습니다.

<sub><a href="#contents">↑ 목차로 돌아가기</a></sub>

## 📄 인용

Preprints.org에 게재한 서베이의 제목은 **[LLM Agents: A Survey](https://www.preprints.org/manuscript/202608.0265)**, DOI는 [`10.20944/preprints202608.0265.v1`](https://doi.org/10.20944/preprints202608.0265.v1)입니다. 인용하실 때는 이 버전이 명시된 기록을 써 주세요. 같은 47쪽 논문을 이 저장소의 [`paper/llm-agents-a-survey.pdf`](paper/llm-agents-a-survey.pdf)에도 올려 두었으니 GitHub를 떠나지 않고 읽으실 수 있습니다.

이 목록이나 서베이가 도움이 되셨다면 다음과 같이 인용해 주세요:

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

GitHub의 **Cite this repository** 버튼은 [`CITATION.cff`](CITATION.cff)를 읽어 같은 기록을 APA나 BibTeX 형식으로 보여 줍니다.

후속 서베이 *The Agent Loop: A Survey of Control Strategies, Skills, and Harnesses for LLM Agents*는 따로 등록되어 있으며, DOI는 [`10.2139/ssrn.7186738`](https://ssrn.com/abstract=7186738)입니다. 실제로 참고하신 쪽을 인용해 주세요.

## 🤝 기여하기

에이전트 논문은 한 사람이 따라갈 수 있는 속도보다 빠르게, 한 달에 새 논문 천 편 안팎으로 쏟아지고 있습니다. 이 목록을 위해 열심히 읽었지만 **좋은 논문과 방법을 분명히 놓쳤습니다**. 여기 들어가야 할 논문이 있다면(**직접 쓰신 논문도 좋습니다**) 도와주세요:

- 알맞은 절에 확인 가능한 링크와 *왜 중요한지* 한 줄 설명(구현이 있다면 `[code]` 링크도)을 붙여 **PR을 열어** 주시거나,
- 링크를 담아 **[이슈](https://github.com/js-lee-AI/awesome-llm-agent-papers/issues)를 열어** 주세요. 제가 빠르게 살펴보겠습니다.

오류 수정, 더 정확한 설명, 아예 새로운 절도 똑같이 환영합니다. 항목 형식은 **[CONTRIBUTING.md](CONTRIBUTING.md)** 파일에 정리해 두었습니다.

## 👥 기여자

이 목록은 커뮤니티가 함께 관리합니다. 논문을 제안하고, 검증하고, 설명을 달아 주신 모든 분께 감사드립니다:

<details>
<summary><b>기여자 13명 보기</b></summary>

| | 기여자 | 기여 내용 |
|---|---|---|
| <a href="https://github.com/shubhamrgandhi"><img src="https://github.com/shubhamrgandhi.png?size=48" width="48" height="48" alt="@shubhamrgandhi"></a> | **[@shubhamrgandhi](https://github.com/shubhamrgandhi)** | 계획과 추론 절에 작은 critic 모델로 더 큰 코딩 에이전트를 이끄는 Steer, Don't Solve([#16](https://github.com/js-lee-AI/awesome-llm-agent-papers/pull/16)), 도구 사용 절에 검증기 없이 학습하는 에이전트를 위한 rubric 기반 credit assignment인 DRACO([#17](https://github.com/js-lee-AI/awesome-llm-agent-papers/pull/17)) 추가. 제1저자가 직접 제출 |
| <a href="https://github.com/sunyuhan19981208"><img src="https://github.com/sunyuhan19981208.png?size=48" width="48" height="48" alt="@sunyuhan19981208"></a> | **[@sunyuhan19981208](https://github.com/sunyuhan19981208)** | 응용 분야 절에 harness가 바뀌어도 계속 작동하도록 작은 모델을 학습시키는 TaoLive 보고서 추가. 저자 중 한 명이 제출([#15](https://github.com/js-lee-AI/awesome-llm-agent-papers/pull/15)) |
| <a href="https://github.com/burgerseater"><img src="https://github.com/burgerseater.png?size=48" width="48" height="48" alt="@burgerseater"></a> | **[@burgerseater](https://github.com/burgerseater)** | 평가와 벤치마크 절에 코드를 쓰는 모델이 아니라 코딩 에이전트의 방향을 잡는 모델을 채점하는 벤치마크 LoopArena. 저자 중 한 명이 제안([#14](https://github.com/js-lee-AI/awesome-llm-agent-papers/issues/14)) |
| <a href="https://github.com/dukesun99"><img src="https://github.com/dukesun99.png?size=48" width="48" height="48" alt="@dukesun99"></a> | **[@dukesun99](https://github.com/dukesun99)** | 메모리 절에 Corpus2Skill, 다중 에이전트 시스템 절에 OrchMAS, 서베이와 포지션 페이퍼 절에 에이전트를 위한 IR 포지션 페이퍼 추가. 세 편 모두에 저자로 참여한 분이 제출([#13](https://github.com/js-lee-AI/awesome-llm-agent-papers/pull/13)) |
| <a href="https://github.com/zhongzero"><img src="https://github.com/zhongzero.png?size=48" width="48" height="48" alt="@zhongzero"></a> | **[@zhongzero](https://github.com/zhongzero)** | 메모리 절에 예측을 위한 이중 에이전트 메모리 아키텍처 ForeDreamer 추가. 저자 중 한 명이 제출([#12](https://github.com/js-lee-AI/awesome-llm-agent-papers/pull/12)) |
| <a href="https://github.com/Nicolas99-9"><img src="https://github.com/Nicolas99-9.png?size=48" width="48" height="48" alt="@Nicolas99-9"></a> | **[@Nicolas99-9](https://github.com/Nicolas99-9)** | 다중 에이전트 시스템 절에 사람 행동에 맞춘 대규모 도시 시뮬레이션 CityReal 추가([#10](https://github.com/js-lee-AI/awesome-llm-agent-papers/pull/10)) |
| <a href="https://github.com/BobbyZhouZijian"><img src="https://github.com/BobbyZhouZijian.png?size=48" width="48" height="48" alt="@BobbyZhouZijian"></a> | **[@BobbyZhouZijian](https://github.com/BobbyZhouZijian)** | 에이전트 아키텍처와 프레임워크 절에 자율 다중 에이전트 진화 프레임워크 CORAL 추가. 저자 중 한 명이 제출([#9](https://github.com/js-lee-AI/awesome-llm-agent-papers/pull/9)) |
| <a href="https://github.com/razzant"><img src="https://github.com/razzant.png?size=48" width="48" height="48" alt="@razzant"></a> | **[@razzant](https://github.com/razzant)** | 에이전트 아키텍처와 프레임워크 절에 스스로 발전하는 코딩 에이전트 harness Ouroboros 추가. 메인테이너가 직접 제출([#8](https://github.com/js-lee-AI/awesome-llm-agent-papers/pull/8)) |
| <a href="https://github.com/reacher-z"><img src="https://github.com/reacher-z.png?size=48" width="48" height="48" alt="@reacher-z"></a> | **[@reacher-z](https://github.com/reacher-z)** | 평가와 벤치마크 절에 deep research 에이전트 평가 Dr. Bench 추가, 저자 중 한 명이 제출([#7](https://github.com/js-lee-AI/awesome-llm-agent-papers/pull/7)). 같은 절에 실제 웹에서 돌리는 브라우저 에이전트 벤치마크 ClawBench 추가([#3](https://github.com/js-lee-AI/awesome-llm-agent-papers/pull/3)) |
| <a href="https://github.com/JEONGSEJIN"><img src="https://github.com/JEONGSEJIN.png?size=48" width="48" height="48" alt="@JEONGSEJIN"></a> | **[@JEONGSEJIN](https://github.com/JEONGSEJIN)** | 상호작용 환경 절에 WebAgent와 world model로 보강한 웹 에이전트 추가([#6](https://github.com/js-lee-AI/awesome-llm-agent-papers/pull/6)) |
| <a href="https://github.com/jinmang2"><img src="https://github.com/jinmang2.png?size=48" width="48" height="48" alt="@jinmang2"></a> | **[@jinmang2](https://github.com/jinmang2)** | 에이전트 메모리 시스템 6개: MemoryOS, Zep, Nemori, MemOS, G-Memory, ACE([#2](https://github.com/js-lee-AI/awesome-llm-agent-papers/pull/2)) |
| <a href="https://github.com/WhymustIhaveaname"><img src="https://github.com/WhymustIhaveaname.png?size=48" width="48" height="48" alt="@WhymustIhaveaname"></a> | **[@WhymustIhaveaname](https://github.com/WhymustIhaveaname)** | 연구 에이전트·orchestration 논문 3편: AutoNumerics, OptimAI, PerspectiveGap([#1](https://github.com/js-lee-AI/awesome-llm-agent-papers/pull/1)). Agon 코드 링크, 그리고 잘려 있던 설명 아홉 개를 다시 쓰게 된 제보([#5](https://github.com/js-lee-AI/awesome-llm-agent-papers/pull/5)) |
| <a href="https://github.com/js-lee-AI"><img src="https://github.com/js-lee-AI.png?size=48" width="48" height="48" alt="@js-lee-AI"></a> | **[@js-lee-AI](https://github.com/js-lee-AI)** | 메인테이너 |
</details>

<sub>누가 <code>git commit</code>을 실행했는지가 아니라 실제 기여에 공이 돌아가도록, 자동 생성하지 않고 손으로 정리했습니다. 커밋 단위 이력은 <a href="https://github.com/js-lee-AI/awesome-llm-agent-papers/graphs/contributors">기여자 그래프</a>에서 보실 수 있습니다.</sub>

여기에 아바타를 올리고 싶으신가요? **[CONTRIBUTING.md](CONTRIBUTING.md)** 파일에 방법이 있습니다. 형식을 잘 갖춘 PR 하나면 충분합니다.

## 📜 라이선스

[MIT 라이선스](LICENSE)로 공개합니다.

## 🗓️ 업데이트 기록

- **2026-09-24**: 서베이를 [GitBook](https://llm-agents-a-survey.gitbook.io/llm-agents-a-survey-docs/)에 온라인 책으로 올렸습니다. 이 분야를 처음 접하는 분을 위해 기본 개념부터 설명합니다.
- **2026-09-24**: 한국어, 간체 중국어, 일본어판을 추가했습니다. 맨 위에서 언어를 고를 수 있습니다. 설명과 본문은 번역했고, 논문 제목과 전문 용어는 영어 그대로 두었습니다. 번역하면서 문장 중간에서 끊긴 설명과 1저자가 빠진 항목을 찾아 고쳤습니다.
- **2026-09-23**: 논문 열두 편을 추가했습니다. 에이전트 루프 안에서 글을 쓰는 대신 정해진 선택지 중 하나를 고르고, 확신이 없으면 LLM에 넘기는 모델을 다룬 논문들입니다. Jev가 공개되면서 이런 방식이 널리 알려졌고, 열두 편 중 네 편은 Jev를 직접 다룹니다. 그중 한 편에서는 Jev가 type error를 한 번도 내지 않았지만, 선택지에 적힌 rubric이 아니라 선택지 이름만 보고 답을 골랐습니다. 520편에서 532편으로 늘었습니다.
- **2026-09-16**: 커뮤니티 기여 세 건을 병합했으며, 모두 논문 저자가 직접 보내 주셨습니다. 추가한 논문은 harness 변화를 고려한 TaoLive 학습 보고서([@sunyuhan19981208](https://github.com/sunyuhan19981208), [#15](https://github.com/js-lee-AI/awesome-llm-agent-papers/pull/15)), 그리고 Steer, Don't Solve와 DRACO([@shubhamrgandhi](https://github.com/shubhamrgandhi), [#16](https://github.com/js-lee-AI/awesome-llm-agent-papers/pull/16)와 [#17](https://github.com/js-lee-AI/awesome-llm-agent-papers/pull/17))입니다. 설명에는 논문에 나온 수치를 넣었습니다. TaoLive 설명 첫머리에는 고정 harness로 fine-tuning하면 instruction following이 7.7점 떨어지지만 harness 상태 증강은 떨어지지 않는다는 결과를 적었습니다. 517편에서 520편으로 늘었습니다.
- **2026-09-16**: 기여자 표도 각 절처럼 접었다 펼 수 있게 했고, 표의 인원수도 `sync_counts.py`가 자동으로 맞춥니다.
- **2026-09-07**: 2026년 5월 이후 나온 논문 20편을 절마다 두 편씩 추가했습니다. LoopArena는 저자 중 한 명인 [@burgerseater](https://github.com/burgerseater)가 [#14](https://github.com/js-lee-AI/awesome-llm-agent-papers/issues/14)에서 추천한 논문입니다. 부정적인 결과를 보고한 논문이 여럿인데, 그중 하나에서는 frontier 에이전트가 프롬프트로 하지 말라고 해도 실행의 57%에서 미리 심어 둔 지름길을 택했습니다. 497편에서 517편으로 늘었습니다.
- **2026-09-03**: 세 편 모두에 저자로 참여한 [@dukesun99](https://github.com/dukesun99)가 보내 준 논문 세 편입니다([#13](https://github.com/js-lee-AI/awesome-llm-agent-papers/pull/13)). Corpus2Skill은 메모리에, OrchMAS는 다중 에이전트 시스템에, Information Retrieval Misses the Mark for LLM Agents는 서베이와 포지션 페이퍼에 넣었습니다. 마지막 논문은 이 목록에 처음 실린 SSRN 논문입니다. Corpus2Skill 설명에는 데이터셋 열한 개에 대한 결과를 넣었습니다. 그중 세 개에서는 코퍼스 탐색 방식의 성능이 더 낮았습니다. 494편에서 497편으로 늘었습니다.
- **2026-08-25**: 저자 중 한 명인 [@zhongzero](https://github.com/zhongzero)가 ForeDreamer를 메모리에 추가했습니다([#12](https://github.com/js-lee-AI/awesome-llm-agent-papers/pull/12)). 설명 첫 문장에는 이 시스템의 차별점을 적었습니다. 이 시스템은 검색 결과를 곧바로 에이전트에 넣지 않고, 예측하기 전에 웹에서 찾은 근거를 구조화된 메모리로 정리해 둡니다. 493편에서 494편으로 늘었습니다.
- **2026-08-20**: 2026년 8월 논문 20편을 절마다 두 편씩 추가했습니다. 부정적인 결과를 보고한 논문이 여럿인데, 모델 규모를 키워도 다국어 성능 격차가 줄지 않는다는 연구가 그 예입니다. 473편에서 493편으로 늘었습니다.
- **2026-08-20**: 병합한 커뮤니티 기여는 Dr. Bench([@reacher-z](https://github.com/reacher-z), [#7](https://github.com/js-lee-AI/awesome-llm-agent-papers/pull/7))와 CityReal([@Nicolas99-9](https://github.com/Nicolas99-9), [#10](https://github.com/js-lee-AI/awesome-llm-agent-papers/pull/10)) 두 건입니다. 471편에서 473편으로 늘었습니다.
- **2026-08-12**: 커뮤니티 기여 네 건을 병합했습니다. Ouroboros([@razzant](https://github.com/razzant), [#8](https://github.com/js-lee-AI/awesome-llm-agent-papers/pull/8)), CORAL([@BobbyZhouZijian](https://github.com/BobbyZhouZijian), [#9](https://github.com/js-lee-AI/awesome-llm-agent-papers/pull/9)), 그리고 WebAgent와 world model로 보강한 웹 에이전트([@JEONGSEJIN](https://github.com/JEONGSEJIN), [#6](https://github.com/js-lee-AI/awesome-llm-agent-papers/pull/6))입니다. 바로 위 항목에서 복사되어 들어온 코드 링크 하나는 뺐습니다. 467편에서 471편으로 늘었습니다.
- **2026-08-08**: 2026년 8월 논문 16편을 열 개 절 전체에 추가했고, 공식 저장소가 있으면 링크를 달았습니다. 451편에서 467편으로 늘었습니다.
- **2026-08-08**: 이전에 논문을 한꺼번에 추가하면서 설명 아홉 개가 문장 중간에서 잘렸는데, 모두 고쳤습니다. Agon에는 [@WhymustIhaveaname](https://github.com/WhymustIhaveaname)이 [#5](https://github.com/js-lee-AI/awesome-llm-agent-papers/pull/5)에서 알려 준 `[code]` 링크를 달았습니다. 이런 문제는 이제 `scripts/check_glosses.py`로 검사합니다.
- **2026-08-06**: 서베이가 Preprints.org에 DOI `10.20944/preprints202608.0265.v1`로 게재되었습니다. 이제 인용 블록, `CITATION.cff`, 상단 링크가 이 저장소의 PDF 대신 버전이 명시된 기록을 가리킵니다.
- **2026-07-31**: 2026년 7월 논문 30편을 절마다 세 편씩 추가했고, 공식 저장소가 있으면 링크를 달았습니다. 421편에서 451편으로 늘었습니다.
- **2026-07-26**: ClawBench 관리에 참여하고 있는 [@reacher-z](https://github.com/reacher-z)가 ClawBench를 평가와 벤치마크에 추가했습니다. 420편에서 421편으로 늘었습니다.
- **2026-07-25**: 첫 커뮤니티 기여입니다. [@jinmang2](https://github.com/jinmang2)가 에이전트 메모리 시스템 +6개(MemoryOS, Zep, Nemori, MemOS, G-Memory, ACE)를, [@WhymustIhaveaname](https://github.com/WhymustIhaveaname)이 연구 에이전트·orchestration 논문 +3편(AutoNumerics, OptimAI, PerspectiveGap)을 보내 주었습니다.
- **2026-07-19**: 2026년 1월부터 7월까지 나온 논문 78편을 열 개 절 전체에 추가했고, 공식 저장소가 있으면 링크를 달았습니다.
- **2026-07-19**: 2026년 1월부터 5월까지 나온 논문 30편(절마다 세 편)을 추가했고, 공식 저장소가 있으면 링크를 달았습니다.
- **2026-07-16**: 2026년 6월과 7월 논문 50편을 열 개 절 전체에 추가했고, 공식 저장소가 있으면 링크를 달았습니다.
- **2026-07-12**: 2026년 논문 42편을 열 개 절 전체에 추가했습니다. 실시간 스타 수를 보여 주는 **주목할 10편 (2026)** 절을 새로 만들고, 관련 목록에는 실시간 스타 배지를 달았습니다. 211편에서 253편으로 늘었습니다.
- **2026-07-09**: agentic RL, 프로토콜, deep research, frontier 평가와 안전에 관한 논문 27편을 추가했습니다. 184편에서 211편으로 늘었습니다.
- **2026-07-08**: 첫 공개입니다. 설명을 단 논문 184편을 서베이의 분류 체계에 따라 정리했습니다.
