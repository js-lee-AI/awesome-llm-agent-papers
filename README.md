<h1 align="center">🤖 Awesome LLM Agent Papers</h1>

<p align="center"><b>A curated, annotated reading list of 211 papers on LLM agents</b><br>
Companion repository to the survey <i>“LLM Agents: A Survey”</i></p>

<p align="center">
<a href="https://awesome.re"><img src="https://awesome.re/badge.svg" alt="Awesome"></a>
<img src="https://img.shields.io/badge/papers-211-blue" alt="Papers">
<img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License: MIT">
<img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg" alt="PRs Welcome">
</p>

<!-- Uncomment when the survey is on arXiv: [![arXiv](https://img.shields.io/badge/arXiv-XXXX.XXXXX-b31b1b.svg)](https://arxiv.org/abs/XXXX.XXXXX) -->
<!-- When this repo is made public, add dynamic badges (stars, last-commit, star-history). They render as "not found" on a private repo, so they are omitted for now. -->

<p align="center"><img src="assets/taxonomy.png" width="820" alt="Taxonomy of LLM-agent research"></p>

This repository collects must-read papers on **LLM-based agents**: language models equipped with planning, memory, tool use, and multi-agent coordination to pursue goals over long horizons. Papers follow the taxonomy of the accompanying survey, covering the core components of an agent, the environments and applications they are deployed in, and the cross-cutting concerns of evaluation and safety. Each entry links to the paper and, where an official implementation exists, to its code.

> ⭐ marks the [Starter Kit](#starter-kit): the ten papers to read first.

<a id="starter-kit"></a>
## ⭐ Starter Kit

New to the area? These ten papers give you the backbone of the field.

| # | Paper | Area | Why start here |
|---|-------|------|----------------|
| 1 | [ReAct: Synergizing Reasoning and Acting](https://arxiv.org/abs/2210.03629) | Planning | The template for the modern agent loop: interleave reasoning with actions. |
| 2 | [Reflexion: Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366) | Planning | Self-reflection stored in memory as a gradient-free improvement loop. |
| 3 | [Toolformer: LMs Can Teach Themselves to Use Tools](https://arxiv.org/abs/2302.04761) | Tool Use | The seminal self-supervised tool-use paper. |
| 4 | [Generative Agents: Interactive Simulacra](https://arxiv.org/abs/2304.03442) | Multi-Agent | Memory + reflection at population scale; the canonical agent-memory design. |
| 5 | [Voyager: An Open-Ended Embodied Agent](https://arxiv.org/abs/2305.16291) | Memory / Env. | Lifelong learning via a growing library of executable skills. |
| 6 | [Cognitive Architectures for Language Agents (CoALA)](https://arxiv.org/abs/2309.02427) | Foundations | The vocabulary (memory, action space, decision loop) this list is organized around. |
| 7 | [A Survey on LLM-based Autonomous Agents](https://arxiv.org/abs/2308.11432) | Survey | The canonical general survey of the field. |
| 8 | [LLM-based Multi-Agents: A Survey](https://arxiv.org/abs/2402.01680) | Multi-Agent | The standard reference for the multi-agent branch. |
| 9 | [AgentBench: Evaluating LLMs as Agents](https://arxiv.org/abs/2308.03688) | Evaluation | The standard cross-environment agent benchmark. |
| 10 | [Not what you've signed up for (Indirect Prompt Injection)](https://arxiv.org/abs/2302.12173) | Safety | The founding paper of the agent-security threat model. |

## Contents

- [⭐ Starter Kit](#starter-kit)
- **🧭 Background**
  - [📚 Surveys & Position Papers (27)](#surveys)
  - [🏗️ Agent Architectures & Frameworks (18)](#architectures)
- **🧱 Part I: Core Components**
  - [🧠 Planning & Reasoning (21)](#planning)
  - [💾 Memory (18)](#memory)
  - [🔧 Tool Use (17)](#tools)
  - [🤝 Multi-Agent Systems (22)](#multi-agent)
- **🌍 Part II: Agents in Context**
  - [🌐 Interactive Environments (23)](#environments)
  - [🚀 Applications (23)](#applications)
- **⚖️ Part III: Cross-Cutting Concerns**
  - [📊 Evaluation & Benchmarks (15)](#evaluation)
  - [🛡️ Safety & Alignment (27)](#safety)

## 🧭 Background

<a id="surveys"></a>
### 📚 Surveys & Position Papers (27)
*Corresponds to §1–§3 (Introduction, Background, Taxonomy).*

- **[A Survey on Large Language Model based Autonomous Agents](https://arxiv.org/abs/2308.11432)** (Wang et al., arXiv 2023) - *The canonical, most-cited general-purpose LLM-agent survey.* ⭐ [[code](https://github.com/Paitesanshi/LLM-Agent-Survey)]
- **[The Rise and Potential of Large Language Model Based Agents: A Survey](https://arxiv.org/abs/2309.07864)** (Xi et al., arXiv 2023) - *Co-foundational with Wang et al. 2023 as one of the two seminal general surveys.* [[code](https://github.com/WooooDyy/LLM-Agent-Paper-List)]
- **[Cognitive Architectures for Language Agents](https://arxiv.org/abs/2309.02427)** (Sumers et al., TMLR 2023) - *The most widely adopted conceptual/architectural vocabulary for describing LLM agents.* ⭐ [[code](https://github.com/ysymyth/awesome-language-agents)]
- **[ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)** (Yao et al., ICLR 2023) - *The single most-cited technical precursor of modern LLM agents.* ⭐ [[code](https://github.com/ysymyth/ReAct)]
- **[Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366)** (Shinn et al., NeurIPS 2023) - *Established the 'self-reflection + memory' loop as an alternative to gradient-based RL for agent self-improvement.* ⭐ [[code](https://github.com/noahshinn/reflexion)]
- **[Toolformer: Language Models Can Teach Themselves to Use Tools](https://arxiv.org/abs/2302.04761)** (Schick et al., NeurIPS 2023) - *Seminal tool-use paper anchoring the 'tool augmentation' pillar of LLM-agent taxonomies.* ⭐
- **[Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442)** (Park et al., arXiv 2023) - *Foundational demonstration of LLM-driven agent societies/simulation.* ⭐ [[code](https://github.com/joonspk-research/generative_agents)]
- **[Voyager: An Open-Ended Embodied Agent with Large Language Models](https://arxiv.org/abs/2305.16291)** (Wang et al., TMLR 2023) - *Seminal example of embodied, code-skill-based, lifelong-learning LLM agents.* ⭐ [[code](https://github.com/MineDojo/Voyager)]
- **[HuggingGPT: Solving AI Tasks with ChatGPT and its Friends in Hugging Face](https://arxiv.org/abs/2303.17580)** (Shen et al., NeurIPS 2023) - *Foundational example of the 'LLM-as-orchestrator-of-tools/models' agent pattern.* [[code](https://github.com/microsoft/JARVIS)]
- **[MRKL Systems: A Modular, Neuro-Symbolic Architecture that Combines Large Language Models, External Knowledge Sources and Discrete Reasoning](https://arxiv.org/abs/2205.00445)** (Karpas et al., arXiv 2022) - *Earliest widely-cited neuro-symbolic precursor to LLM tool-use/agent architectures.*
- **[Agent AI: Surveying the Horizons of Multimodal Interaction](https://arxiv.org/abs/2401.03568)** (Durante et al., arXiv 2024) - *Broadens the LLM-agent survey landscape to multimodal/embodied agent AI.*
- **[Igniting Language Intelligence: The Hitchhiker's Guide From Chain-of-Thought Reasoning to Language Agents](https://arxiv.org/abs/2311.11797)** (Zhang et al., arXiv 2023) - *Bridges the reasoning (CoT) literature and agent literature.* [[code](https://github.com/Zoeyyao27/CoT-Igniting-Agent)]
- **[Large Language Model based Multi-Agents: A Survey of Progress and Challenges](https://arxiv.org/abs/2402.01680)** (Guo et al., IJCAI 2024) - *The standard reference survey specifically for the multi-agent branch of LLM agents.* ⭐ [[code](https://github.com/taichengguo/LLM_MultiAgents_Survey_Papers)]
- **[Understanding the Planning of LLM Agents: A Survey](https://arxiv.org/abs/2402.02716)** (Huang et al., arXiv 2024) - *Fills the planning-specific gap in the foundational-survey landscape.*
- **[Tool Learning with Large Language Models: A Survey](https://arxiv.org/abs/2405.17935)** (Qu et al., arXiv 2024) - *The definitive survey for the tool-use pillar of LLM agents.* [[code](https://github.com/quchangle1/LLM-Tool-Survey)]
- **[A Survey on the Memory Mechanism of Large Language Model based Agents](https://arxiv.org/abs/2404.13501)** (Zhang et al., arXiv 2024) - *The standard survey for the memory subsystem of LLM agents.* [[code](https://github.com/nuster1128/LLM_Agent_Memory_Survey)]
- **[Agentic Large Language Models, a Survey](https://arxiv.org/abs/2503.23037)** (Plaat et al., arXiv 2025) - *A recent, widely-referenced general survey with a compact reasoning/acting/interacting taxonomy.*
- **[Large Language Model Agent: A Survey on Methodology, Applications and Challenges](https://arxiv.org/abs/2503.21460)** (Luo et al., arXiv 2025) - *One of the most comprehensive and recent (2025) general surveys.* [[code](https://github.com/luo-junyu/Awesome-Agent-Papers)]
- **[Fully Autonomous AI Agents Should Not Be Developed](https://arxiv.org/abs/2502.02649)** (Mitchell et al., arXiv 2025) - *A prominent, widely-discussed dissenting position paper on agent autonomy.*
- **[AI Agents vs. Agentic AI: A Conceptual Taxonomy, Applications and Challenges](https://arxiv.org/abs/2505.10468)** (Sapkota et al., arXiv 2025) - *Provides terminological/conceptual disambiguation increasingly cited given inconsistent usage in the field.*
- **[LLM-Based Human-Agent Collaboration and Interaction Systems: A Survey](https://arxiv.org/abs/2505.00753)** (Zou et al., arXiv 2025) - *Covers the human-agent cooperation branch identified in the earliest foundational surveys.* [[code](https://github.com/HenryPengZou/Awesome-Human-Agent-Collaboration-Interaction-Systems)]
- **[Levels of Autonomy for AI Agents](https://arxiv.org/abs/2506.12469)** (Feng et al., arXiv 2025) - *Offers a widely-cited operational framework for comparing autonomy across LLM-agent systems.*
- **[Advances and Challenges in Foundation Agents: From Brain-Inspired Intelligence to Evolutionary, Collaborative, and Safe Systems](https://arxiv.org/abs/2504.01990)** (Liu et al., arXiv 2025) - *A 48-author landmark survey organizing the field around brain-inspired cognitive modules, self-evolution, collective intelligence, and safety.*
- **[The Landscape of Agentic Reinforcement Learning for LLMs: A Survey](https://arxiv.org/abs/2509.02547)** (Zhang et al., arXiv 2025) - *The canonical survey of agentic RL: training LLMs as decision-making agents rather than passive generators.*
- **[A Comprehensive Survey of Self-Evolving AI Agents](https://arxiv.org/abs/2508.07407)** (Fang et al., arXiv 2025) - *Surveys techniques by which agents optimize their own components from interaction data, bridging foundation models and lifelong agentic systems.*
- **[Deep Research Agents: A Systematic Examination and Roadmap](https://arxiv.org/abs/2506.18096)** (Huang et al., arXiv 2025) - *First systematic survey of long-horizon autonomous research agents (search, tool use, report synthesis).*
- **[A Survey of AI Agent Protocols](https://arxiv.org/abs/2504.16736)** (Yang et al., arXiv 2025) - *Maps the emerging protocol layer (MCP, A2A, and successors) and proposes evaluation dimensions for agent interoperability standards.*

<a id="architectures"></a>
### 🏗️ Agent Architectures & Frameworks (18)
*Corresponds to §2 (Background) and the running examples throughout.*

- **[Auto-GPT for Online Decision Making: Benchmarks and Additional Opinions](https://arxiv.org/abs/2306.02224)** (Yang et al., arXiv 2023) - *Only peer-reviewed-adjacent empirical study of the widely-influential (but paper-less) AutoGPT autonomous-agent design pattern.* [[code](https://github.com/younghuman/LLMAgent)]
- **[AgentBench: Evaluating LLMs as Agents](https://arxiv.org/abs/2308.03688)** (Liu et al., ICLR 2024) - *The standard reference benchmark for measuring general single-agent capability across heterogeneous environments.* ⭐ [[code](https://github.com/THUDM/AgentBench)]
- **[WebArena: A Realistic Web Environment for Building Autonomous Agents](https://arxiv.org/abs/2307.13854)** (Zhou et al., ICLR 2024) - *The de facto standard testbed for web-browsing single-agent architectures.* [[code](https://github.com/web-arena-x/webarena)]
- **[Gorilla: Large Language Model Connected with Massive APIs](https://arxiv.org/abs/2305.15334)** (Patil et al., NeurIPS 2024) - *Key single-agent tool-use paper demonstrating that fine-tuning plus retrieval can make an agent reliably invoke large real-world API catalogs.* [[code](https://github.com/ShishirPatil/gorilla)]
- **[ReWOO: Decoupling Reasoning from Observations for Efficient Augmented Language Models](https://arxiv.org/abs/2305.18323)** (Xu et al., arXiv 2023) - *Influential efficiency-oriented alternative to the ReAct loop, illustrating the plan-then-execute vs. interleaved architectural design axis.* [[code](https://github.com/billxbf/ReWOO)]
- **[Tree of Thoughts: Deliberate Problem Solving with Large Language Models](https://arxiv.org/abs/2305.10601)** (Yao et al., NeurIPS 2023) - *A core deliberate-search reasoning architecture underpinning later single-agent planning/search frameworks like LATS.* [[code](https://github.com/princeton-nlp/tree-of-thought-llm)]
- **[WebGPT: Browser-assisted question-answering with human feedback](https://arxiv.org/abs/2112.09332)** (Nakano et al., arXiv 2021) - *Early pre-ChatGPT precursor to modern LLM web agents, establishing the browsing-tool-use-plus-human-feedback pattern.*
- **[SELF-REFINE: Iterative Refinement with Self-Feedback](https://arxiv.org/abs/2303.17651)** (Madaan et al., NeurIPS 2023) - *A minimal, widely-adopted single-agent self-improvement loop that is reused as a subroutine inside many larger agent architectures.* [[code](https://github.com/madaan/self-refine)]
- **[SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](https://arxiv.org/abs/2405.15793)** (Yang et al., NeurIPS 2024) - *Demonstrates how interface design materially changes single-agent capability, now standard in coding-agent design.* [[code](https://github.com/princeton-nlp/SWE-agent)]
- **[Language Agent Tree Search Unifies Reasoning, Acting, and Planning in Language Models](https://arxiv.org/abs/2310.04406)** (Zhou et al., ICML 2024) - *Represents the state-of-the-art convergence of search-based planning with the ReAct/Reflexion lineage.* [[code](https://github.com/lapisrocks/LanguageAgentTreeSearch)]
- **[Executable Code Actions Elicit Better LLM Agents](https://arxiv.org/abs/2402.01030)** (Wang et al., ICML 2024) - *Established 'code-as-action' as a leading alternative action-space design for single agents.* [[code](https://github.com/xingyaoww/code-act)]
- **[Describe, Explain, Plan and Select: Interactive Planning with Large Language Models Enables Open-World Multi-Task Agents](https://arxiv.org/abs/2302.01560)** (Wang et al., NeurIPS 2023) - *Key single-agent planning architecture for open-world/embodied tasks.* [[code](https://github.com/CraftJarvis/MC-Planner)]
- **[OS-Copilot: Towards Generalist Computer Agents with Self-Improvement](https://arxiv.org/abs/2402.07456)** (Wu et al., arXiv 2024) - *A leading recent example of a general-purpose, self-improving OS-level single agent, extending AutoGPT-style autonomy to real computer environments.* [[code](https://github.com/OS-Copilot/OS-Copilot)]
- **[AppAgent: Multimodal Agents as Smartphone Users](https://arxiv.org/abs/2312.13771)** (Zhang et al., CHI 2025) - *Representative recent single-agent architecture extending the ReAct/tool-use paradigm to GUI/mobile control.* [[code](https://github.com/TencentQQGYLab/AppAgent)]
- **[The Landscape of Emerging AI Agent Architectures for Reasoning, Planning, and Tool Calling: A Survey](https://arxiv.org/abs/2404.11584)** (Masterman et al., arXiv 2024) - *A survey specifically scoped to agent architecture design patterns, directly relevant to categorizing single-agent frameworks.*
- **[MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework](https://arxiv.org/abs/2308.00352)** (Hong et al., ICLR 2024) - *Widely cited framework showing how single-agent role/procedure templates improve reliability, marking the transition point between single- and multi-agent framework design.* [[code](https://github.com/geekan/MetaGPT)]
- **[Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, Long Context, and Next Generation Agentic Capabilities](https://arxiv.org/abs/2507.06261)** (Comanici et al., arXiv 2025) - *Frontier model report that treats agentic tool use and computer operation as headline capabilities.*
- **[Kimi K2: Open Agentic Intelligence](https://arxiv.org/abs/2507.20534)** (Kimi Team, arXiv 2025) - *Flagship open model built explicitly around agentic post-training at scale.* [[code](https://github.com/MoonshotAI/Kimi-K2)]

## 🧱 Part I: Core Components

<a id="planning"></a>
### 🧠 Planning & Reasoning (21)
*Corresponds to §4 (Planning and Reasoning).*

- **[Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://arxiv.org/abs/2201.11903)** (Wei et al., NeurIPS 2022) - *The foundational technique underlying virtually all LLM-agent reasoning/planning modules; the starting point for the whole CoT/ToT/ReAct lineage.*
- **[Self-Consistency Improves Chain of Thought Reasoning in Language Models](https://arxiv.org/abs/2203.11171)** (Wang et al., ICLR 2023) - *Standard inference-time ensembling/verification strategy widely reused inside agent reasoning and planning pipelines.*
- **[Large Language Models are Zero-Shot Reasoners](https://arxiv.org/abs/2205.11916)** (Kojima et al., NeurIPS 2022) - *Established that reasoning behavior is latent and promptable zero-shot, a key enabler for general-purpose agent prompting templates.* [[code](https://github.com/kojima-takeshi188/zero_shot_cot)]
- **[Least-to-Most Prompting Enables Complex Reasoning in Large Language Models](https://arxiv.org/abs/2205.10625)** (Zhou et al., ICLR 2023) - *Early formalization of task decomposition, a core planning primitive reused by nearly all subsequent LLM-agent task planners.*
- **[STaR: Bootstrapping Reasoning With Reasoning](https://arxiv.org/abs/2203.14465)** (Zelikman et al., NeurIPS 2022) - *Precursor to the RL-based reasoning-model training paradigm (e.g., DeepSeek-R1, o1) used to instill self-generated reasoning in agents.* [[code](https://github.com/ezelikman/STaR)]
- **[Graph of Thoughts: Solving Elaborate Problems with Large Language Models](https://arxiv.org/abs/2308.09687)** (Besta et al., AAAI 2024) - *Extends structured-reasoning/search frameworks used by agents beyond trees, improving quality and cost on complex multi-step tasks.* [[code](https://github.com/spcl/graph-of-thoughts)]
- **[Reasoning with Language Model is Planning with World Model](https://arxiv.org/abs/2305.14992)** (Hao et al., EMNLP 2023) - *Connects classical planning-as-search (MCTS, world models) with LLM reasoning, directly relevant to agent planning under uncertainty.* [[code](https://github.com/maitrix-org/llm-reasoners)]
- **[CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing](https://arxiv.org/abs/2305.11738)** (Gou et al., ICLR 2024) - *Bridges self-critique with tool-augmented verification, a key mechanism in modern agent frameworks that ground reflection in external feedback.* [[code](https://github.com/microsoft/ProphetNet/tree/master/CRITIC)]
- **[Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models](https://arxiv.org/abs/2305.04091)** (Wang et al., ACL 2023) - *Widely-used lightweight plan-then-execute template that many LLM agent planning modules adopt directly.* [[code](https://github.com/AGI-Edgerunners/Plan-and-Solve-Prompting)]
- **[ADaPT: As-Needed Decomposition and Planning with Language Models](https://arxiv.org/abs/2311.05772)** (Prasad et al., ACL 2024) - *Demonstrates adaptive, execution-conditioned planning that balances plan granularity against agent capability, an important refinement over static plan-and-execute agents.* [[code](https://github.com/archiki/ADaPT)]
- **[Self-Discover: Large Language Models Self-Compose Reasoning Structures](https://arxiv.org/abs/2402.03620)** (Zhou et al., NeurIPS 2024) - *Shows LLMs can self-select their own reasoning strategy per task, a meta-reasoning capability central to adaptive agent planning.*
- **[Buffer of Thoughts: Thought-Augmented Reasoning with Large Language Models](https://arxiv.org/abs/2406.04271)** (Yang et al., NeurIPS 2024) - *Represents reusable, memory-augmented reasoning-structure retrieval, connecting reasoning strategies with agent long-term memory design.* [[code](https://github.com/YangLing0818/buffer-of-thought-llm)]
- **[Large Language Models Cannot Self-Correct Reasoning Yet](https://arxiv.org/abs/2310.01798)** (Huang et al., ICLR 2024) - *A widely-cited cautionary/critical result that tempers over-reliance on self-critique loops in agent design, motivating external-feedback-grounded methods.*
- **[Training Language Models to Self-Correct via Reinforcement Learning](https://arxiv.org/abs/2409.12917)** (Kumar et al., ICLR 2025) - *Shows self-correction can be made genuinely effective via RL rather than prompting alone, directly informing reasoning-model post-training used in modern agents.*
- **[Let's Verify Step by Step](https://arxiv.org/abs/2305.20050)** (Lightman et al., ICLR 2024) - *Establishes process reward models/step-level verification, now a standard component for guiding search and self-critique in reasoning agents.* [[code](https://github.com/openai/prm800k)]
- **[DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/abs/2501.12948)** (Guo et al., Nature 2025) - *Landmark open reasoning-model release demonstrating RL-induced emergent planning/reflection behaviors now underpinning next-generation reasoning agents.* [[code](https://github.com/deepseek-ai/DeepSeek-R1)]
- **[Towards Reasoning in Large Language Models: A Survey](https://arxiv.org/abs/2212.10403)** (Huang et al., ACL 2023) - *One of the earliest and most-cited surveys specifically on LLM reasoning, a natural anchor citation for any LLM-agent survey's reasoning section.* [[code](https://github.com/jeffhj/LM-reasoning)]
- **[Large Language Models for Planning: A Comprehensive and Systematic Survey](https://arxiv.org/abs/2505.19683)** (Cao et al., arXiv 2025) - *A dedicated, up-to-date survey covering exactly the planning-strategies portion of this sub-topic, ideal for anchoring taxonomy claims.* [[code](https://github.com/Quester-one/Awesome-LLM-Planning)]
- **[When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs](https://arxiv.org/abs/2406.01297)** (Kamoi et al., ACL 2024) - *The key critical survey specific to self-critique/self-correction, essential for a balanced, rigorous treatment of reflection methods in an agent survey.* [[code](https://github.com/ryokamoi/llm-self-correction-papers)]
- **[Search-R1: Training LLMs to Reason and Leverage Search Engines with Reinforcement Learning](https://arxiv.org/abs/2503.09516)** (Jin et al., arXiv 2025) - *Canonical agentic-RL result: the model learns to interleave search-engine calls with its own reasoning from outcome rewards alone.* [[code](https://github.com/PeterGriffinJin/Search-R1)]
- **[ReTool: Reinforcement Learning for Strategic Tool Use in LLMs](https://arxiv.org/abs/2504.11536)** (Feng et al., arXiv 2025) - *RL that teaches a reasoning model when and how to invoke a code interpreter mid-derivation.*

<a id="memory"></a>
### 💾 Memory (18)
*Corresponds to §5 (Memory).*

- **[RET-LLM: Towards a General Read-Write Memory for Large Language Models](https://arxiv.org/abs/2305.14322)** (Modarressi et al., arXiv 2023) - *Early and influential structured/triplet-based read-write memory design, a precursor to graph- and KG-based agent memory systems.*
- **[MemoryBank: Enhancing Large Language Models with Long-Term Memory](https://arxiv.org/abs/2305.10250)** (Zhong et al., AAAI 2024) - *One of the first systems to bring a psychologically grounded (human-memory-inspired) forgetting/consolidation mechanism into LLM agent memory.* [[code](https://github.com/zhongwanjun/MemoryBank-SiliconFriend)]
- **[Augmenting Language Models with Long-Term Memory](https://arxiv.org/abs/2306.07174)** (Wang et al., NeurIPS 2023) - *Key architectural approach to giving the underlying language model itself (not just an agent scaffold) a trainable long-term memory retrieval mechanism.* [[code](https://github.com/Victorwz/LongMem)]
- **[Synapse: Trajectory-as-Exemplar Prompting with Memory for Computer Control](https://arxiv.org/abs/2306.07863)** (Zheng et al., ICLR 2024) - *Demonstrates retrieval-augmented episodic-trajectory memory for grounding agent decision-making in complex GUI/computer-control tasks.* [[code](https://github.com/ltzheng/Synapse)]
- **[ExpeL: LLM Agents Are Experiential Learners](https://arxiv.org/abs/2308.10144)** (Zhao et al., AAAI 2024) - *Influential paradigm for extracting reusable, transferable 'experience' knowledge from an agent's own memory rather than raw episodic replay.* [[code](https://github.com/LeapLabTHU/ExpeL)]
- **[Walking Down the Memory Maze: Beyond Context Limit through Interactive Reading (MemWalker)](https://arxiv.org/abs/2310.05029)** (Chen et al., arXiv 2023) - *Influential tree-structured (hierarchical) memory-navigation approach bridging long-context modeling and agentic memory retrieval.*
- **[MemGPT: Towards LLMs as Operating Systems](https://arxiv.org/abs/2310.08560)** (Packer et al., COLM 2024) - *One of the most widely cited and productized (Letta) architectures for tiered, self-managed long-term memory in LLM agents.* [[code](https://github.com/cpacker/MemGPT)]
- **[Think-in-Memory: Recalling and Post-thinking Enable LLMs with Long-Term Memory](https://arxiv.org/abs/2311.08719)** (Liu et al., arXiv 2023) - *Addresses inconsistent-reasoning pitfalls of naive memory recall by storing reasoning traces rather than raw text, influencing later 'reflective retrieval' memory designs.*
- **[Evaluating Very Long-Term Conversational Memory of LLM Agents](https://arxiv.org/abs/2402.17753)** (Maharana et al., ACL 2024) - *The standard benchmark used to evaluate and compare long-term conversational memory systems for LLM agents (used by Mem0, MIRIX, A-MEM, etc.).* [[code](https://github.com/snap-research/locomo)]
- **[Larimar: Large Language Models with Episodic Memory Control](https://arxiv.org/abs/2403.11901)** (Das et al., ICML 2024) - *Representative of the architecture-level (rather than prompt-level) approach to giving LLMs an editable, fast-updating episodic memory.* [[code](https://github.com/IBM/larimar)]
- **[HippoRAG: Neurobiologically Inspired Long-Term Memory for Large Language Models](https://arxiv.org/abs/2405.14831)** (Gutiérrez et al., NeurIPS 2024) - *A highly influential neuro-inspired long-term memory/RAG framework bridging knowledge-graph retrieval and agent memory, widely adopted as a strong baseline.* [[code](https://github.com/OSU-NLP-Group/HippoRAG)]
- **[On the Structural Memory of LLM Agents](https://arxiv.org/abs/2412.15266)** (Zeng et al., arXiv 2024) - *Provides a controlled empirical comparison of memory-structuring choices, useful evidence base for a survey's discussion of design trade-offs in agent memory.*
- **[A-MEM: Agentic Memory for LLM Agents](https://arxiv.org/abs/2502.12110)** (Xu et al., arXiv 2025) - *Representative of the newest generation of dynamically self-organizing (graph/note-linking) long-term memory systems for LLM agents.* [[code](https://github.com/WujiangXu/A-mem)]
- **[From Human Memory to AI Memory: A Survey on Memory Mechanisms in the Era of LLMs](https://arxiv.org/abs/2504.15965)** (Wu et al., arXiv 2025) - *A recent, comprehensive sub-topic survey giving a psychology-grounded taxonomy that a broader LLM-agent survey can cite for organizing the memory literature.*
- **[Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://arxiv.org/abs/2504.19413)** (Chhikara et al., arXiv 2025) - *A leading production-oriented, widely-deployed long-term memory system for LLM agents, frequently used as a state-of-the-art comparison point.* [[code](https://github.com/mem0ai/mem0)]
- **[MIRIX: Multi-Agent Memory System for LLM-Based Agents](https://arxiv.org/abs/2507.07957)** (Wang et al., arXiv 2025) - *Illustrates the current frontier trend of multi-agent, multi-type (multimodal) memory architectures for LLM-based agents.* [[code](https://github.com/Mirix-AI/MIRIX)]
- **[LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory](https://arxiv.org/abs/2410.10813)** (Wu et al., ICLR 2025) - *Decomposes long-term interactive memory into five separately testable abilities.* [[code](https://github.com/xiaowu0162/LongMemEval)]
- **[ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory](https://arxiv.org/abs/2509.25140)** (Ouyang et al., arXiv 2025) - *Distills strategy-level memory from both successful and failed trajectories so an agent self-evolves over a task stream.*

<a id="tools"></a>
### 🔧 Tool Use (17)
*Corresponds to §6 (Tool Use and Action Execution).*

- **[TALM: Tool Augmented Language Models](https://arxiv.org/abs/2205.12255)** (Parisi et al., arXiv 2022) - *Early, influential formulation of self-supervised bootstrapping for tool use in LMs, directly anticipating Toolformer's self-supervised approach.*
- **[API-Bank: A Comprehensive Benchmark for Tool-Augmented LLMs](https://arxiv.org/abs/2304.08244)** (Li et al., EMNLP 2023) - *One of the earliest and most cited dedicated benchmarks for evaluating and training tool-augmented dialogue LLMs.* [[code](https://github.com/AlibabaResearch/DAMO-ConvAI)]
- **[Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models](https://arxiv.org/abs/2304.09842)** (Lu et al., NeurIPS 2023) - *Prominent example of natural-language-planned tool composition/orchestration across heterogeneous tool types, widely cited in tool-use and compositional-reasoning literature.* [[code](https://github.com/lupantech/chameleon-llm)]
- **[Large Language Models as Tool Makers](https://arxiv.org/abs/2305.17126)** (Cai et al., arXiv 2023) - *Foundational for the tool-creation (as opposed to tool-use) direction, showing LLMs can author their own reusable tools rather than only calling pre-existing ones.* [[code](https://github.com/ctlllll/LLM-ToolMaker)]
- **[GPT4Tools: Teaching Large Language Model to Use Tools via Self-instruction](https://arxiv.org/abs/2305.18752)** (Yang et al., NeurIPS 2023) - *Widely used reference for open-source instruction-tuning approaches to multimodal tool use, complementing proprietary-model tool-use papers.* [[code](https://github.com/StevenGrove/GPT4Tools)]
- **[ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings](https://arxiv.org/abs/2305.11554)** (Hao et al., NeurIPS 2023) - *An influential alternative architecture for scalable tool selection that avoids the context-length bottleneck of prompt-based tool listing.* [[code](https://github.com/Ber666/ToolkenGPT)]
- **[ToolAlpaca: Generalized Tool Learning for Language Models with 3000 Simulated Cases](https://arxiv.org/abs/2306.05301)** (Tang et al., arXiv 2023) - *Key evidence that generalized tool-use capability is achievable in small open models via automatically synthesized tool-use corpora, influential for later synthetic-data tool-training pipelines.* [[code](https://github.com/tangqiaoyu/ToolAlpaca)]
- **[RestGPT: Connecting Large Language Models with Real-World RESTful APIs](https://arxiv.org/abs/2306.06624)** (Song et al., arXiv 2023) - *Demonstrates tool-use extended to complex, stateful real-world REST APIs beyond toy tool sets, with a benchmark still used for API-grounded agent evaluation.* [[code](https://github.com/Yifan-Song793/RestGPT)]
- **[ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world APIs](https://arxiv.org/abs/2307.16789)** (Qin et al., ICLR 2024) - *One of the largest and most cited tool-use datasets/frameworks, establishing ToolBench as a standard training/evaluation resource for open-source tool-use LLMs.* [[code](https://github.com/OpenBMB/ToolBench)]
- **[Tool Documentation Enables Zero-Shot Tool-Usage with Large Language Models](https://arxiv.org/abs/2308.00675)** (Hsieh et al., arXiv 2023) - *Reframes tool-use elicitation around documentation rather than demonstrations, an important and frequently cited methodological insight for scaling to many tools.*
- **[Small LLMs Are Weak Tool Learners: A Multi-LLM Agent](https://arxiv.org/abs/2401.07324)** (Shen et al., EMNLP 2024) - *Influential for the multi-agent/role-decomposition approach to tool learning, especially relevant to efficiently deploying tool-use in smaller open models.* [[code](https://github.com/X-PLUG/Multi-LLM-Agent)]
- **[StableToolBench: Towards Stable Large-Scale Benchmarking on Tool Learning of Large Language Models](https://arxiv.org/abs/2403.07714)** (Guo et al., ACL 2024) - *Widely used evaluation infrastructure paper that fixed reproducibility problems plaguing large-scale real-API tool-learning benchmarks.* [[code](https://github.com/THUNLP-MT/StableToolBench)]
- **[What Are Tools Anyway? A Survey from the Language Model Perspective](https://arxiv.org/abs/2403.15452)** (Wang et al., COLM 2024) - *A dedicated, LM-centric survey of tool use that is directly citable as a sub-topic survey reference for a broader LLM-agent survey.*
- **[ToolACE: Winning the Points of LLM Function Calling](https://arxiv.org/abs/2409.00920)** (Liu et al., arXiv 2024) - *Represents the state-of-the-art synthetic-data pipeline approach to training small open models for accurate function calling, rivaling GPT-4.*
- **[xLAM: A Family of Large Action Models to Empower AI Agent Systems](https://arxiv.org/abs/2409.03215)** (Zhang et al., arXiv 2024) - *Prominent industrial (Salesforce) effort establishing 'large action models' as a distinct model class optimized for agentic tool use, widely benchmarked against.* [[code](https://github.com/SalesforceAIResearch/xLAM)]
- **[The Berkeley Function Calling Leaderboard (BFCL): From Tool Use to Agentic Evaluation of Large Language Models](https://openreview.net/forum?id=2GmDdhBdDk)** (Patil et al., ICML 2025) - *The de facto standard leaderboard/benchmark for comparing LLM function-calling and tool-use performance, referenced by nearly all subsequent function-calling papers.* [[code](https://github.com/ShishirPatil/gorilla)]
- **[Model Context Protocol (MCP): Landscape, Security Threats, and Future Research Directions](https://arxiv.org/abs/2503.23278)** (Hou et al., arXiv 2025) - *Security analysis of the MCP ecosystem across the server lifecycle; the reference for protocol-layer supply-chain risk.*

<a id="multi-agent"></a>
### 🤝 Multi-Agent Systems (22)
*Corresponds to §7 (Multi-Agent Systems).*

- **[CAMEL: Communicative Agents for "Mind" Exploration of Large Language Model Society](https://arxiv.org/abs/2303.17760)** (Li et al., NeurIPS 2023) - *One of the earliest and most cited frameworks establishing autonomous agent-to-agent cooperation via role-play.* [[code](https://github.com/camel-ai/camel)]
- **[Improving Factuality and Reasoning in Language Models through Multiagent Debate](https://arxiv.org/abs/2305.14325)** (Du et al., ICML 2024) - *Seminal multi-agent debate paper popularizing 'society of minds'-style debate as a test-time technique.* [[code](https://github.com/composable-models/llm_multiagent_debate)]
- **[Encouraging Divergent Thinking in Large Language Models through Multi-Agent Debate](https://arxiv.org/abs/2305.19118)** (Liang et al., EMNLP 2024) - *Diagnoses a core failure mode motivating why multi-agent debate helps beyond self-consistency.* [[code](https://github.com/Skytliang/Multi-Agents-Debate)]
- **[ChatEval: Towards Better LLM-based Evaluators through Multi-Agent Debate](https://arxiv.org/abs/2308.07201)** (Chan et al., ICLR 2024) - *Shows multi-agent debate improves reliability of LLM-as-judge evaluation.* [[code](https://github.com/chanchimin/ChatEval)]
- **[AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation](https://arxiv.org/abs/2308.08155)** (Wu et al., arXiv 2023) - *Widely adopted industrial multi-agent orchestration framework (Microsoft).* [[code](https://github.com/microsoft/autogen)]
- **[ChatDev: Communicative Agents for Software Development](https://arxiv.org/abs/2307.07924)** (Qian et al., ACL 2024) - *Widely cited demonstration of end-to-end multi-agent collaboration for a complex real-world workflow.* [[code](https://github.com/OpenBMB/ChatDev)]
- **[AgentVerse: Facilitating Multi-Agent Collaboration and Exploring Emergent Behaviors in Agents](https://arxiv.org/abs/2308.10848)** (Chen et al., ICLR 2024) - *General-purpose, dynamically-composed multi-agent collaboration framework and study of emergent social dynamics.* [[code](https://github.com/OpenBMB/AgentVerse)]
- **[Building Cooperative Embodied Agents Modularly with Large Language Models](https://arxiv.org/abs/2307.02485)** (Zhang et al., ICLR 2024) - *Extends multi-agent collaboration and communication to embodied/physically-grounded settings.* [[code](https://github.com/UMass-Embodied-AGI/CoELA)]
- **[ReConcile: Round-Table Conference Improves Reasoning via Consensus among Diverse LLMs](https://arxiv.org/abs/2309.13007)** (Chen et al., ACL 2024) - *Combines heterogeneous LLM backbones with confidence-weighted persuasion/voting in agent debate/consensus.* [[code](https://github.com/dinobby/ReConcile)]
- **[Dynamic LLM-Agent Network: An LLM-Agent Collaboration Framework with Agent Team Optimization (v2 retitled: A Dynamic LLM-Powered Agent Network for Task-Oriented Agent Collaboration)](https://arxiv.org/abs/2310.02170)** (Liu et al., arXiv 2023) - *Introduces dynamic agent-team composition/topology optimization for multi-agent collaboration.* [[code](https://github.com/SALT-NLP/DyLAN)]
- **[Exchange-of-Thought: Enhancing Large Language Model Capabilities through Cross-Model Communication](https://arxiv.org/abs/2312.01823)** (Yin et al., EMNLP 2023) - *Provides a taxonomy of inter-agent communication paradigms, useful for surveying communication mechanisms.* [[code](https://github.com/yinzhangyue/EoT)]
- **[LLM-Deliberation: Evaluating LLMs with Interactive Multi-Agent Negotiation Games (v2 retitled: Cooperation, Competition, and Maliciousness: LLM-Stakeholders Interactive Negotiation)](https://arxiv.org/abs/2309.17234)** (Abdelnabi et al., arXiv 2023) - *Extends multi-agent LLM research into strategic/competitive communication (negotiation).* [[code](https://github.com/S-Abdelnabi/LLM-Deliberation)]
- **[Unleashing the Emergent Cognitive Synergy in Large Language Models: A Task-Solving Agent through Multi-Persona Self-Collaboration](https://arxiv.org/abs/2307.05300)** (Wang et al., ACL 2024) - *Boundary case showing multi-agent-style collaboration can be simulated within a single model via personas.* [[code](https://github.com/MikeWangWZHL/Solo-Performance-Prompting)]
- **[Should we be going MAD? A Look at Multi-Agent Debate Strategies for LLMs](https://arxiv.org/abs/2311.17371)** (Smit et al., ICML 2024) - *Important critical/empirical counterpoint on when multi-agent debate actually helps.* [[code](https://github.com/instadeepai/DebateLLM)]
- **[Debating with More Persuasive LLMs Leads to More Truthful Answers](https://arxiv.org/abs/2402.06782)** (Khan et al., ICML 2024) - *Connects multi-agent debate to AI-safety scalable oversight.* [[code](https://github.com/ucl-dark/llm_debate)]
- **[Mixture-of-Agents Enhances Large Language Model Capabilities](https://arxiv.org/abs/2406.04692)** (Wang et al., ICLR 2025) - *Influential architecture showing structured multi-agent aggregation can outperform any single strong proprietary model.* [[code](https://github.com/togethercomputer/MoA)]
- **[More Agents Is All You Need](https://arxiv.org/abs/2402.05120)** (Li et al., TMLR 2024) - *Crucial baseline showing much of multi-agent benefit can come from ensemble scaling rather than communication.* [[code](https://github.com/MoreAgentsIsAllYouNeed/AgentForest)]
- **[Beyond Self-Talk: A Communication-Centric Survey of LLM-Based Multi-Agent Systems](https://arxiv.org/abs/2502.14321)** (Yan et al., arXiv 2025) - *Most directly on-topic recent survey for communication within multi-agent LLM systems.*
- **[Multi-Agent Collaboration Mechanisms: A Survey of LLMs](https://arxiv.org/abs/2501.06322)** (Tran et al., arXiv 2025) - *Recent dedicated survey providing a structured taxonomy of collaboration mechanisms.*
- **[Language Agents as Optimizable Graphs](https://arxiv.org/abs/2402.16823)** (Zhuge et al., ICML 2024) - *GPTSwarm: formalizes multi-agent systems as computational graphs whose prompts and edges are jointly learned.* [[code](https://github.com/metauto-ai/GPTSwarm)]
- **[Scaling Large Language Model-based Multi-Agent Collaboration](https://arxiv.org/abs/2406.07155)** (Qian et al., arXiv 2024) - *Scales collaboration to 1000+ agents in explicit topologies; irregular graphs outperform regular ones (a collaborative scaling result).*
- **[AFlow: Automating Agentic Workflow Generation](https://arxiv.org/abs/2410.10762)** (Zhang et al., ICLR 2025) - *Searches over code-represented workflows to discover agentic pipelines automatically.*

## 🌍 Part II: Agents in Context

<a id="environments"></a>
### 🌐 Interactive Environments (23)
*Corresponds to §8 (Agents in Interactive Environments).*

- **[Do As I Can, Not As I Say: Grounding Language in Robotic Affordances](https://arxiv.org/abs/2204.01691)** (al., CoRL 2022) - *Foundational demonstration of LLM-as-planner grounded by real-world affordances for embodied robotic agents.* [[code](https://github.com/google-research/google-research/tree/master/saycan)]
- **[Inner Monologue: Embodied Reasoning through Planning with Language Models](https://arxiv.org/abs/2207.05608)** (al., CoRL 2022) - *Established the closed-loop, feedback-grounded planning pattern underlying subsequent embodied/GUI agent architectures.*
- **[ALFWorld: Aligning Text and Embodied Environments for Interactive Learning](https://arxiv.org/abs/2010.03768)** (Shridhar et al., ICLR 2021) - *Widely used benchmark for evaluating LLM-based embodied/household agents (ReAct, Reflexion), bridging text reasoning and embodied execution.* [[code](https://github.com/alfworld/alfworld)]
- **[RT-1: Robotics Transformer for Real-World Control at Scale](https://arxiv.org/abs/2212.06817)** (al., RSS 2023) - *Foundational large-scale robot-transformer model establishing the recipe later extended by RT-2 and OpenVLA.* [[code](https://github.com/google-research/robotics_transformer)]
- **[PaLM-E: An Embodied Multimodal Language Model](https://arxiv.org/abs/2303.03378)** (al., ICML 2023) - *Seminal embodied multimodal LLM showing internet-scale vision-language pretraining transfers to embodied robotic reasoning, inspiring RT-2 and VLA models.*
- **[RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control](https://arxiv.org/abs/2307.15818)** (al., CoRL 2023) - *Established the vision-language-action (VLA) modeling paradigm central to embodied/robotics agent research.*
- **[OpenVLA: An Open-Source Vision-Language-Action Model](https://arxiv.org/abs/2406.09246)** (al., CoRL 2024) - *Open-source counterpart to closed VLA models, democratizing research on LLM-driven robotic control.* [[code](https://github.com/openvla/openvla)]
- **[WebShop: Towards Scalable Real-World Web Interaction with Grounded Language Agents](https://arxiv.org/abs/2207.01206)** (Yao et al., NeurIPS 2022) - *Foundational, widely-used benchmark for grounded language web agents, predating and motivating later LLM-based web-navigation research.* [[code](https://github.com/princeton-nlp/WebShop)]
- **[Mind2Web: Towards a Generalist Agent for the Web](https://arxiv.org/abs/2306.06070)** (Deng et al., NeurIPS 2023) - *First benchmark and LLM-based agent explicitly designed for generalist web navigation on real websites; standard reference cited by subsequent web/GUI agent papers.* [[code](https://github.com/OSU-NLP-Group/Mind2Web)]
- **[GPT-4V(ision) is a Generalist Web Agent, if Grounded](https://arxiv.org/abs/2401.01614)** (Zheng et al., ICML 2024) - *First systematic demonstration that multimodal LLMs can act as generalist visual web agents, catalyzing the shift to vision-grounded web/GUI agents.* [[code](https://github.com/OSU-NLP-Group/SeeAct)]
- **[WebVoyager: Building an End-to-End Web Agent with Large Multimodal Models](https://arxiv.org/abs/2401.13919)** (He et al., ACL 2024) - *Key demonstration and benchmark for real-world, multimodal browser agents widely used to evaluate subsequent web-agent systems.* [[code](https://github.com/MinorJerry/WebVoyager)]
- **[CogAgent: A Visual Language Model for GUI Agents](https://arxiv.org/abs/2312.08914)** (Hong et al., arXiv 2023) - *One of the first large VLMs purpose-built for screenshot-only GUI grounding, establishing the high-resolution visual GUI agent architecture line.* [[code](https://github.com/zai-org/CogAgent)]
- **[SeeClick: Harnessing GUI Grounding for Advanced Visual GUI Agents](https://arxiv.org/abs/2401.10935)** (Cheng et al., ACL 2024) - *Established GUI grounding as a core sub-problem for visual GUI agents and introduced ScreenSpot, a standard grounding benchmark.* [[code](https://github.com/njucckevin/SeeClick)]
- **[Mobile-Agent: Autonomous Multi-Modal Mobile Device Agent with Visual Perception](https://arxiv.org/abs/2401.16158)** (Wang et al., arXiv 2024) - *Representative vision-centric mobile GUI agent design demonstrating cross-app, metadata-free operation.* [[code](https://github.com/X-PLUG/MobileAgent)]
- **[OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](https://arxiv.org/abs/2404.07972)** (Xie et al., NeurIPS 2024) - *Standard benchmark for evaluating 'computer-use' agents, used to evaluate essentially every major computer-use agent since 2024.* [[code](https://github.com/xlang-ai/OSWorld)]
- **[AndroidWorld: A Dynamic Benchmarking Environment for Autonomous Agents](https://arxiv.org/abs/2405.14573)** (al., ICLR 2025) - *Dominant reproducible benchmark for mobile GUI agents enabling dynamic task variation.* [[code](https://github.com/google-research/android_world)]
- **[UI-TARS: Pioneering Automated GUI Interaction with Native Agents](https://arxiv.org/abs/2501.12326)** (al., arXiv 2025) - *State-of-the-art open 'native' GUI/computer-use agent model showing the field's shift toward end-to-end trained GUI action models.* [[code](https://github.com/bytedance/UI-TARS)]
- **[GUI Agents: A Survey](https://arxiv.org/abs/2412.13501)** (al., ACL 2025) - *Direct, up-to-date survey specifically on GUI agents for structuring the GUI/computer-use agent sub-area and taxonomy.*
- **[Large Language Model-Brained GUI Agents: A Survey](https://arxiv.org/abs/2411.18279)** (Zhang et al., arXiv 2024) - *Complementary GUI-agent-specific survey valuable for comprehensive coverage of the LLM-driven GUI agent literature.* [[code](https://github.com/vyokky/LLM-Brained-GUI-Agents-Survey)]
- **[A Survey of WebAgents: Towards Next-Generation AI Agents for Web Automation with Large Foundation Models](https://arxiv.org/abs/2503.23350)** (Ning et al., KDD 2025) - *Dedicated survey for the web-agent sub-area, giving a ready-made taxonomy and trustworthiness discussion specific to browser/web automation agents.*
- **[UI-TARS-2 Technical Report: Advancing GUI Agent with Multi-Turn Reinforcement Learning](https://arxiv.org/abs/2509.02544)** (Wang et al., arXiv 2025) - *Successor to UI-TARS; multi-turn RL for end-to-end GUI control.*
- **[π0: A Vision-Language-Action Flow Model for General Robot Control](https://arxiv.org/abs/2410.24164)** (Black et al., arXiv 2024) - *Flow-matching action expert on a pretrained VLM, controlling many robot embodiments.* [[code](https://github.com/Physical-Intelligence/openpi)]
- **[Tongyi DeepResearch Technical Report](https://arxiv.org/abs/2510.24701)** (Tongyi DeepResearch Team, arXiv 2025) - *Open end-to-end deep-research agent model for long-horizon web research and synthesis.* [[code](https://github.com/Alibaba-NLP/DeepResearch)]

<a id="applications"></a>
### 🚀 Applications (23)
*Corresponds to §10 (Applications).*

- **[AutoCodeRover: Autonomous Program Improvement](https://arxiv.org/abs/2404.05427)** (Zhang et al., arXiv 2024) - *One of the first cost-efficient autonomous program-repair agents grounded in structured code search.* [[code](https://github.com/nus-apr/auto-code-rover)]
- **[Agentless: Demystifying LLM-based Software Engineering Agents](https://arxiv.org/abs/2407.01489)** (Xia et al., arXiv 2024) - *Influential counter-narrative showing simpler non-agentic pipelines can rival complex agents.* [[code](https://github.com/OpenAutoCoder/Agentless)]
- **[OpenHands: An Open Platform for AI Software Developers as Generalist Agents](https://arxiv.org/abs/2407.16741)** (al., ICLR 2025) - *The leading open community platform underlying much subsequent applied coding-agent research.* [[code](https://github.com/OpenHands/OpenHands)]
- **[Large Language Model-Based Agents for Software Engineering: A Survey](https://arxiv.org/abs/2409.02977)** (Liu et al., arXiv 2024) - *A dedicated sub-topic survey giving the taxonomy needed to situate coding/SWE agent work.* [[code](https://github.com/FudanSELab/Agent4SE-Paper-List)]
- **[Autonomous chemical research with large language models](https://www.nature.com/articles/s41586-023-06792-0)** (Boiko et al., Nature 2023) - *One of the earliest and most-cited demonstrations of an LLM agent performing autonomous physical-world scientific experimentation.* [[code](https://github.com/gomesgroup/coscientist)]
- **[ChemCrow: Augmenting large-language models with chemistry tools](https://arxiv.org/abs/2304.05376)** (Bran et al., Nature 2023) - *A foundational tool-augmented LLM agent paper for chemistry.* [[code](https://github.com/ur-whitelab/chemcrow-public)]
- **[The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery](https://arxiv.org/abs/2408.06292)** (Lu et al., arXiv 2024) - *A landmark, widely publicized attempt at fully automating the scientific-paper lifecycle.* [[code](https://github.com/SakanaAI/AI-Scientist)]
- **[The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search](https://arxiv.org/abs/2504.08066)** (Yamada et al., arXiv 2025) - *Marks a concrete, verifiable milestone for autonomous scientific discovery agents.* [[code](https://github.com/SakanaAI/AI-Scientist-v2)]
- **[Towards an AI co-scientist](https://arxiv.org/abs/2502.18864)** (Gottweis et al., arXiv 2025) - *A major industry (Google) applied-agent system for hypothesis generation in science.*
- **[AlphaEvolve: A coding agent for scientific and algorithmic discovery](https://arxiv.org/abs/2506.13131)** (Novikov et al., arXiv 2025) - *A landmark demonstration of an LLM agent making a genuine, verifiable new mathematical/algorithmic discovery.*
- **[Kosmos: An AI Scientist for Autonomous Discovery](https://arxiv.org/abs/2511.02824)** (Mitchener et al., arXiv 2025) - *One of the most capable and rigorously evaluated 'AI scientist' agents to date.*
- **[ScienceAgentBench: Toward Rigorous Assessment of Language Agents for Data-Driven Scientific Discovery](https://arxiv.org/abs/2410.05080)** (al., ICLR 2025) - *A rigorous, expert-validated benchmark quantifying the gap between current LLM agents and end-to-end scientific-discovery automation.* [[code](https://github.com/OSU-NLP-Group/ScienceAgentBench)]
- **[Towards Scientific Intelligence: A Survey of LLM-based Scientific Agents](https://arxiv.org/abs/2503.24047)** (Ren et al., arXiv 2025) - *The dedicated sub-topic survey for grounding the scientific-discovery-agent literature.*
- **[A Survey of LLM-based Agents in Medicine: How far are we from Baymax?](https://arxiv.org/abs/2502.11211)** (Wang et al., ACL 2025) - *The primary dedicated survey of LLM agents in healthcare.*
- **[MDAgents: An Adaptive Collaboration of LLMs for Medical Decision-Making](https://arxiv.org/abs/2404.15155)** (al., NeurIPS 2024) - *A widely cited example of adaptive multi-agent orchestration tailored to medical reasoning complexity.* [[code](https://github.com/mitmedialab/MDAgents)]
- **[Agent Hospital: A Simulacrum of Hospital with Evolvable Medical Agents](https://arxiv.org/abs/2405.02957)** (Li et al., arXiv 2024) - *A distinctive applied-agent paradigm for learning medical expertise via agent-agent simulation.*
- **[Towards Conversational Diagnostic AI](https://arxiv.org/abs/2401.05654)** (al., arXiv 2024) - *A landmark, rigorously evaluated Google system showing an LLM agent matching or exceeding physicians in simulated diagnostic dialogue.*
- **[Large Language Model Agent in Financial Trading: A Survey](https://arxiv.org/abs/2408.06361)** (Ding et al., arXiv 2024) - *The dedicated sub-topic survey needed to anchor the finance branch of applied LLM agents.*
- **[FinMem: A Performance-Enhanced LLM Trading Agent with Layered Memory and Character Design](https://arxiv.org/abs/2311.13743)** (Yu et al., AAAI 2023) - *An early, widely referenced LLM trading agent introducing human-cognition-inspired layered memory design.* [[code](https://github.com/pipiku915/FinMem-LLM-StockTrading)]
- **[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://arxiv.org/abs/2412.20138)** (Xiao et al., arXiv 2024) - *A recent, popular multi-role multi-agent finance system widely used as a reference architecture.* [[code](https://github.com/TauricResearch/TradingAgents)]
- **[FinGPT: Open-Source Financial Large Language Models](https://arxiv.org/abs/2306.06031)** (Yang et al., IJCAI 2023) - *One of the most cited open-source financial LLM/agent efforts, providing base-model infrastructure underlying many downstream financial agent systems.* [[code](https://github.com/AI4Finance-Foundation/FinGPT)]
- **[SWE-Lancer: Can Frontier LLMs Earn $1 Million from Real-World Freelance Software Engineering?](https://arxiv.org/abs/2502.12115)** (Miserendino et al., arXiv 2025) - *Prices coding-agent competence in real freelance dollars; frontier models leave most of the posted value unearned.* [[code](https://github.com/openai/SWELancer-Benchmark)]
- **[AgentClinic: A Multimodal Agent Benchmark to Evaluate AI in Simulated Clinical Environments](https://arxiv.org/abs/2405.07960)** (Schmidgall et al., arXiv 2024) - *Multimodal benchmark of simulated clinical settings for doctor-patient agent interaction.*

## ⚖️ Part III: Cross-Cutting Concerns

<a id="evaluation"></a>
### 📊 Evaluation & Benchmarks (15)
*Corresponds to §9 (Evaluation and Benchmarks).*

- **[GAIA: a benchmark for General AI Assistants](https://arxiv.org/abs/2311.12983)** (Mialon et al., ICLR 2024) - *Reference benchmark for generalist, tool-using agent assistants; underlies popular public leaderboards tracking frontier agent progress.*
- **[SWE-bench: Can Language Models Resolve Real-World GitHub Issues?](https://arxiv.org/abs/2310.06770)** (Jimenez et al., ICLR 2024) - *De facto standard benchmark for coding/software-engineering agents; spawned the SWE-bench Verified/Lite/Live/Multimodal family.* [[code](https://github.com/SWE-bench/SWE-bench)]
- **[MLAgentBench: Evaluating Language Agents on Machine Learning Experimentation](https://arxiv.org/abs/2310.03302)** (Huang et al., arXiv 2023) - *Seminal benchmark for the 'AI research agent'/'ML engineering agent' evaluation subfield, precursor to MLE-bench, RE-Bench, etc.* [[code](https://github.com/snap-stanford/MLAgentBench)]
- **[τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains](https://arxiv.org/abs/2406.12045)** (Yao et al., arXiv 2024) - *Pioneered evaluation of agent-user interaction and policy compliance; standard reference for enterprise/customer-service agent evaluation.* [[code](https://github.com/sierra-research/tau-bench)]
- **[AgentBoard: An Analytical Evaluation Board of Multi-turn LLM Agents](https://arxiv.org/abs/2401.13178)** (Ma et al., NeurIPS 2024) - *Widely-used unified evaluation toolkit addressing the coarse pass/fail scoring gap, directly relevant to evaluation-methodology framing.* [[code](https://github.com/hkust-nlp/AgentBoard)]
- **[SmartPlay: A Benchmark for LLMs as Intelligent Agents](https://arxiv.org/abs/2310.01557)** (Wu et al., ICLR 2024) - *Capability-decomposed evaluation methodology that influenced later fine-grained agent capability benchmarks.* [[code](https://github.com/microsoft/SmartPlay)]
- **[TravelPlanner: A Benchmark for Real-World Planning with Language Agents](https://arxiv.org/abs/2402.01622)** (Xie et al., ICML 2024) - *Widely-cited stress test for complex constrained multi-tool planning, illustrating agents' distance from reliable long-horizon planning.* [[code](https://github.com/OSU-NLP-Group/TravelPlanner)]
- **[InterCode: Standardizing and Benchmarking Interactive Coding with Execution Feedback](https://arxiv.org/abs/2306.14898)** (Yang et al., NeurIPS 2023) - *Established the interactive, execution-feedback evaluation paradigm underlying later coding-agent and terminal-agent benchmarks.* [[code](https://intercode-benchmark.github.io)]
- **[GTA: A Benchmark for General Tool Agents](https://arxiv.org/abs/2407.08713)** (Wang et al., NeurIPS 2024) - *Addresses realism gaps (implicit intent, authentic multimodal context) left by earlier synthetic tool-use benchmarks.* [[code](https://github.com/open-compass/GTA)]
- **[Survey on Evaluation of LLM-based Agents](https://arxiv.org/abs/2503.16416)** (Yehudai et al., arXiv 2025) - *Directly on-topic survey providing a ready-made taxonomy for a new agent survey's evaluation section.*
- **[Evaluation and Benchmarking of LLM Agents: A Survey](https://arxiv.org/abs/2507.21504)** (Mohammadi et al., KDD 2025) - *Independently-developed sub-topic survey complementing Yehudai et al., useful for cross-checking taxonomy coverage.*
- **[τ²-Bench: Evaluating Conversational Agents in a Dual-Control Environment](https://arxiv.org/abs/2506.07982)** (Barres et al., arXiv 2025) - *Extends τ-bench to settings where user and agent both act on the environment.* [[code](https://github.com/sierra-research/tau2-bench)]
- **[Agent-as-a-Judge: Evaluate Agents with Agents](https://arxiv.org/abs/2410.10934)** (Zhuge et al., arXiv 2024) - *Systematizes agentic evaluation of agents; the reference point for judge-circularity concerns.* [[code](https://github.com/metauto-ai/agent-as-a-judge)]
- **[Holistic Agent Leaderboard: The Missing Infrastructure for AI Agent Evaluation](https://arxiv.org/abs/2510.11977)** (Kapoor et al., arXiv 2025) - *Standardized harness that re-evaluates agents at scale with cost reported alongside accuracy.*
- **[Terminal-Bench: Benchmarking Agents on Hard, Realistic Tasks in Command Line Interfaces](https://arxiv.org/abs/2601.11868)** (Merrill et al., arXiv 2026) - *Hard, realistic command-line tasks; a de facto standard for terminal agents.* [[code](https://github.com/laude-institute/terminal-bench)]

<a id="safety"></a>
### 🛡️ Safety & Alignment (27)
*Corresponds to §11 (Safety, Security, and Trustworthiness).*

- **[Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection](https://arxiv.org/abs/2302.12173)** (Greshake et al., arXiv 2023) - *The founding paper of the indirect prompt injection threat model that underlies almost all later LLM-agent security research.* ⭐ [[code](https://github.com/greshake/llm-security)]
- **[AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents](https://arxiv.org/abs/2406.13352)** (Debenedetti et al., NeurIPS 2024) - *The most widely used standardized testbed for measuring agent robustness to prompt-injection attacks and defenses.* [[code](https://github.com/ethz-spylab/agentdojo)]
- **[InjecAgent: Benchmarking Indirect Prompt Injections in Tool-Integrated Large Language Model Agents](https://arxiv.org/abs/2403.02691)** (Zhan et al., ACL 2024) - *Standard reference benchmark for quantifying tool-integrated agents' susceptibility to indirect prompt injection.* [[code](https://github.com/uiuc-kang-lab/InjecAgent)]
- **[WASP: Benchmarking Web Agent Security Against Prompt Injection Attacks](https://arxiv.org/abs/2504.18575)** (Evtimov et al., arXiv 2025) - *Extends prompt-injection evaluation from single-step tool calls to realistic, multi-step autonomous web-browsing agents.* [[code](https://github.com/facebookresearch/wasp)]
- **[R-Judge: Benchmarking Safety Risk Awareness for LLM Agents](https://arxiv.org/abs/2401.10019)** (Yuan et al., EMNLP 2024) - *Widely cited benchmark for evaluating LLMs' own risk-awareness/judgment capability as a safety-monitoring component for agents.* [[code](https://github.com/Lordog/R-Judge)]
- **[Identifying the Risks of LM Agents with an LM-Emulated Sandbox](https://arxiv.org/abs/2309.15817)** (Ruan et al., ICLR 2024) - *Foundational scalable methodology for red-teaming/risk discovery in tool-using agents without needing real-world tool access.* [[code](https://github.com/ryoungj/ToolEmu)]
- **[AgentHarm: A Benchmark for Measuring Harmfulness of LLM Agents](https://arxiv.org/abs/2410.09024)** (Andriushchenko et al., ICLR 2025) - *Key benchmark distinguishing agent misuse risk from chatbot jailbreak risk, showing agentic capability compounds harm potential.* [[code](https://github.com/UKGovernmentBEIS/inspect_evals)]
- **[Evil Geniuses: Delving into the Safety of LLM-based Agents](https://arxiv.org/abs/2311.11855)** (Tian et al., arXiv 2023) - *One of the earliest systematic studies showing multi-agent LLM collaboration amplifies rather than mitigates safety risk.* [[code](https://github.com/T1aNS1R/Evil-Geniuses)]
- **[BadAgent: Inserting and Activating Backdoor Attacks in LLM Agents](https://arxiv.org/abs/2406.03007)** (Wang et al., ACL 2024) - *Seminal demonstration that agent backdoors survive downstream safety fine-tuning, motivating agent supply-chain security concerns.* [[code](https://github.com/DPamK/BadAgent)]
- **[AgentPoison: Red-teaming LLM Agents via Poisoning Memory or Knowledge Bases](https://arxiv.org/abs/2407.12784)** (Chen et al., NeurIPS 2024) - *Establishes memory/knowledge-base poisoning as a distinct, training-free attack surface unique to memory-augmented LLM agents.* [[code](https://github.com/AI-secure/AgentPoison)]
- **[Agent Security Bench (ASB): Formalizing and Benchmarking Attacks and Defenses in LLM-based Agents](https://arxiv.org/abs/2410.02644)** (Zhang et al., arXiv 2024) - *Largest unified taxonomy/benchmark integrating diverse attack and defense classes for LLM agents into one evaluation framework.* [[code](https://github.com/agiresearch/ASB)]
- **[TrustAgent: Towards Safe and Trustworthy LLM-based Agents](https://arxiv.org/abs/2402.01586)** (Hua et al., EMNLP 2024) - *Influential early defense/mitigation framework proposing constitution-guided planning as a mechanism for agent safety.* [[code](https://github.com/agiresearch/TrustAgent)]
- **[SafeAgentBench: A Benchmark for Safe Task Planning of Embodied LLM Agents](https://arxiv.org/abs/2412.13178)** (Yin et al., arXiv 2024) - *Extends agent-safety evaluation beyond digital/text domains to physical-world embodied hazards, showing safety failures generalize to robotics.* [[code](https://github.com/shengyin1224/SafeAgentBench)]
- **[AI Agents That Matter](https://arxiv.org/abs/2407.01502)** (Kapoor et al., arXiv 2024) - *Widely cited critique reshaping how the field evaluates agent capability claims, directly relevant to trustworthy assessment of agent risk/benefit tradeoffs.*
- **[Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training](https://arxiv.org/abs/2401.05566)** (Hubinger et al., arXiv 2024) - *Landmark demonstration that current safety-training pipelines can fail to remove hidden deceptive/misaligned behavior, directly informing agent trustworthiness concerns.* [[code](https://github.com/anthropics/sleeper-agents-paper)]
- **[Frontier Models are Capable of In-context Scheming](https://arxiv.org/abs/2412.04984)** (Meinke et al., arXiv 2024) - *First systematic empirical evidence of in-context scheming capability in frontier autonomous agents, a central concern for autonomy-related alignment risk.*
- **[Emergent Misalignment: Narrow Finetuning can Produce Broadly Misaligned LLMs](https://arxiv.org/abs/2502.17424)** (Betley et al., arXiv 2025) - *Recent, highly influential finding that narrow, seemingly innocuous fine-tuning of agentic capabilities can produce broad, unpredictable safety failures.* [[code](https://github.com/emergent-misalignment/emergent-misalignment)]
- **[AI Deception: A Survey of Examples, Risks, and Potential Solutions](https://arxiv.org/abs/2308.14752)** (Park et al., arXiv 2023) - *Foundational survey establishing AI deception as a distinct, empirically-grounded risk category central to agent trustworthiness and alignment.*
- **[AI Alignment: A Comprehensive Survey](https://arxiv.org/abs/2310.19852)** (Ji et al., arXiv 2023) - *One of the most comprehensive general alignment surveys, providing the conceptual scaffolding (RICE, forward/backward alignment) that agent-specific safety work builds on.* [[code](https://github.com/PKU-Alignment/AlignmentSurvey)]
- **[A Survey on Trustworthy LLM Agents: Threats and Countermeasures](https://arxiv.org/abs/2503.09648)** (Yu et al., arXiv 2025) - *The most directly on-topic recent survey for this sub-area, providing a taxonomy spanning nearly all agent-specific safety/security threat classes.* [[code](https://github.com/Ymm-cll/TrustAgent)]
- **[A Comprehensive Survey in LLM(-Agent) Full Stack Safety: Data, Training and Deployment](https://arxiv.org/abs/2504.15585)** (Wang et al., arXiv 2025) - *Large-scale lifecycle-wide safety survey situating agent-specific risks within the broader LLM safety pipeline, useful for framing agent risk as one stage of a larger safety stack.*
- **[A Survey on Autonomy-Induced Security Risks in Large Model-Based Agents](https://arxiv.org/abs/2506.23844)** (Su et al., arXiv 2025) - *Directly frames the core thesis of this sub-topic: that autonomy itself, not just the underlying LLM, is the source of new agent-specific security risks.*
- **[Discovering Language Model Behaviors with Model-Written Evaluations](https://arxiv.org/abs/2212.09251)** (Perez et al., arXiv 2022) - *Early, seminal empirical evidence connecting RLHF training scale to emergent self-preservation and power-seeking-adjacent expressed preferences, a precursor concern for autonomous agent alignment.* [[code](https://github.com/anthropics/evals)]
- **[Towards Understanding Sycophancy in Language Models](https://arxiv.org/abs/2310.13548)** (Sharma et al., arXiv 2023) - *Key empirical study of sycophancy as a robustness/alignment failure mode with direct implications for agents that must give honest assessments during autonomous decision-making.* [[code](https://github.com/meg-tong/sycophancy-eval)]
- **[Design Patterns for Securing LLM Agents against Prompt Injections](https://arxiv.org/abs/2506.08837)** (Beurer-Kellner et al., arXiv 2025) - *Catalogue of architectural patterns that constrain what an agent may do after reading untrusted input.*
- **[OS-Harm: A Benchmark for Measuring Safety of Computer Use Agents](https://arxiv.org/abs/2506.14866)** (Kuntz et al., arXiv 2025) - *Extends agent-safety measurement to computer-use agents operating real interfaces.*
- **[The 2025 AI Agent Index: Documenting Technical and Safety Features of Deployed Agentic AI Systems](https://arxiv.org/abs/2602.17753)** (Staufer et al., FAccT 2026) - *Empirical index of 30 deployed agentic systems; documents a capability-vs-safety transparency gap.*

## 📄 Citing

If this list or the survey is useful to you, please cite:

```bibtex
@article{lee2026llmagents,
  title  = {LLM Agents: A Survey},
  author = {Lee, Jungseob},
  year   = {2026},
  note   = {Manuscript. arXiv link to appear.}
}
```

## 🤝 Contributing

Contributions are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md). In short: add your paper to the right section of this README with a verifiable link, a one-line gloss, and a `[code]` link if an implementation exists, then open a pull request.

## 📜 License

Released under the [MIT License](LICENSE).

## 🗓️ Updates

- **2026-07**: Literature-update pass: +27 papers (agentic RL, protocols, deep research, frontier evaluation and safety), 184 to 211.
- **2026-07**: Initial release. 184 annotated papers, organized by the survey's taxonomy.
