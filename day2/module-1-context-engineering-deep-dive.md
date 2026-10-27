# Module 1 — Context Engineering Deep Dive

**Timebox:** 45–60 minutes

## Overview

This module covers important terms and aspects of prompt engineering.

## Cover: shaping what the model “knows” at run time (requirements, code/docs, constraints, examples)

- Show an example `AGENTS.md` file that includes the project goal, primary language, framework, coding best practices, testing instructions, and constraints (what to do and what not to do).
- Watch: <https://www.youtube.com/watch?v=KEK_WcSTiuE>
- Also: <https://www.youtube.com/watch?v=K-TjG63dRBE>, <https://www.youtube.com/watch?v=NlNuoH5PPl4> (mid video)

## Cover: context windows, drop-offs, and hallucination risk

- Context windows: <https://www.youtube.com/watch?v=-QVoIxEpFkM>
- Summary: similar to working memory, the amount of information the model can consider before it starts forgetting. Cover what counts toward the limit, how the model handles a full window, and common failure modes (e.g., forgetting early information).
- Token limits: characters, words, or subwords. A tokenizer splits text into tokens.
- Self-attention: word position affects how much the model weights each token.
- Context window size: prompts, responses, system prompt, documents, source code, and RAG all count toward the limit.
- “Forgetting” phenomenon: when context exceeds the window, the model ignores some content. Even within limits, larger windows require more compute, slower performance, and can still drop details.
- Hallucinations: a model confidently generates an answer that isn’t true. <https://openai.com/index/why-language-models-hallucinate/>

## Practice: “prime context” for a task and track what you intentionally include

- In the chat, ask Codex to write a simple Python script that does X (participants can pick the use case).

## Resources

- Recommended viewing: [OpenAI: Prompt Engineering is Dead (YouTube)](https://www.youtube.com/watch?v=8rABwKRsec4)
- Recommended reading:
  - [Evolution of LLM Usage Patterns](https://slalom.atlassian.net/wiki/spaces/AE1/pages/5157191684/1.+Evolution+of+LLM+Usage+Patterns)
  - [Introduction to Agents](https://slalom.atlassian.net/wiki/spaces/AE1/pages/5189238847/2.+Introduction+to+Agents)
  - [Context Windows](https://slalom.atlassian.net/wiki/spaces/AE1/pages/5171740744/Context+Windows)
  - [Priming Context](https://slalom.atlassian.net/wiki/spaces/AE1/pages/5171740776/Priming+Context)
  - [Persist Important Information: Memory, Plans, Task Lists](https://slalom.atlassian.net/wiki/spaces/AE1/pages/5171904521/Persist+important+information+Memory+Plans+Task+lists)
