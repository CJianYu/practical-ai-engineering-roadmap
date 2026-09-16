# Annotated Resource Guide

Use resources to unblock a build, not to postpone one. Pick one primary course per phase and treat everything else as reference material.

## Overall map

### Andrew Ng — AI Engineering Skills Map

- Link: https://www.andrewng.org/writing
- Use it for: the high-level capability model—building AI applications, software fundamentals, coding agents, and shaping the build.
- Do not use it as: a week-by-week implementation curriculum. This repository supplies that layer.

### Stanford CS329Z — Engineering AI Agents

- Link: https://cs329z.stanford.edu/
- Use it for: a rigorous agent-engineering spine covering RAG, tools, agent loops, data, evals, safety, coding agents, and projects.
- Best for: developers with some NLP/ML background who will do the assignments or equivalent projects.

## LLM foundations

### How Transformer LLMs Work

- Link: https://learn.deeplearning.ai/courses/how-transformer-llms-work/
- Use it for: a compact visual mental model of tokenization, embeddings, attention, and transformer blocks.
- Stop when: you can explain inference and context limitations well enough to design an application boundary.

### Stanford CS336

- Link: https://stanford-cs336.github.io/
- Use it for: deeper model construction, training systems, scaling, data, and alignment.
- Treat as optional when: your target is Applied AI Engineering rather than model training.

## Agent engineering

### DeepLearning.AI — Agentic AI

- Link: https://www.deeplearning.ai/courses/agentic-ai
- Use it for: reflection, tool use, planning, multi-step workflows, and rapid practical orientation.
- Follow with: a framework-light implementation and evals.

### Anthropic — Building Effective Agents

- Link: https://www.anthropic.com/research/building-effective-agents
- Use it for: choosing composable workflows before adding autonomy.

### Hugging Face Agents Course

- Link: https://huggingface.co/learn/agents-course/unit0/introduction
- Use it for: hands-on experimentation with open-source agent tooling.

## RAG

### DeepLearning.AI — Retrieval Augmented Generation

- Link: https://www.deeplearning.ai/courses/retrieval-augmented-generation
- Use it for: a structured path across search, chunking, vector stores, metadata, deployment, and evaluation.
- Pair with: a labeled retrieval dataset from your own project.

## Evaluation

### OpenAI — Evals guide

- Link: https://platform.openai.com/docs/guides/evals
- Use it for: practical eval design and implementation patterns.

### Stanford CS329Z evaluation modules

- Link: https://cs329z.stanford.edu/
- Use it for: benchmark structure, code graders, model judges, reliability, and error analysis.

## Safety

### OWASP Top 10 for LLM Applications

- Link: https://genai.owasp.org/llm-top-10/
- Use it for: threat categories and a vocabulary for reviewing architecture.
- Do not use it as: a substitute for a system-specific threat model and adversarial tests.

### Model Context Protocol specification

- Link: https://modelcontextprotocol.io/specification/
- Use it for: understanding the protocol and security boundaries when exposing tools and data.

## Production

### CMU — Machine Learning in Production

- Link: https://mlip-cmu.github.io/
- Use it for: engineering AI-enabled products beyond model benchmarks, including architecture, quality, risk, and operations.

### DeepLearning.AI — Machine Learning in Production

- Link: https://www.deeplearning.ai/courses/machine-learning-in-production
- Use it for: project scoping, data requirements, deployment, and continuous improvement.

## Resource inclusion rules

A new link should meet at least one condition:

- it is a primary source or official documentation;
- it contains a reproducible experiment or implementation;
- it teaches a gap not already covered;
- it provides production evidence, a postmortem, or a useful benchmark.

Every pull request must explain **when a learner should use the resource** and what existing item it complements or replaces.
