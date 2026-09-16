# Repository Setup

Recommended GitHub settings after the initial push.

## Metadata

**Name**

```text
practical-ai-engineering-roadmap
```

**Description**

```text
An eval-driven, project-based roadmap for software engineers becoming Applied AI Engineers.
```

**Topics**

```text
ai-engineering
applied-ai
llm
rag
ai-agents
evals
llmops
roadmap
generative-ai
learning-path
```

## Visibility and branch

- Visibility: Public
- Default branch: `main`
- Enable Issues and Discussions
- Allow squash merge
- Delete head branches after merge

## Suggested first labels

```text
bug
curriculum
documentation
good first issue
help wanted
lab
resource
translation
```

## First release

Create release `v0.1.0` with the title:

```text
Practical AI Engineering Roadmap — first public release
```

Release summary:

```text
A 12-week, project-based and eval-driven path for software engineers transitioning into Applied AI Engineering. The first release includes the full curriculum, two runnable labs, a capstone specification, evaluation templates, bilingual documentation, and CI validation.
```

## Push with GitHub CLI

After authenticating `gh`:

```bash
gh repo create CJianYu/practical-ai-engineering-roadmap \
  --public \
  --description "An eval-driven, project-based roadmap for software engineers becoming Applied AI Engineers." \
  --source . \
  --remote origin \
  --push

gh repo edit CJianYu/practical-ai-engineering-roadmap \
  --add-topic ai-engineering,applied-ai,llm,rag,ai-agents,evals,llmops,roadmap,generative-ai,learning-path \
  --enable-issues \
  --enable-discussions
```
