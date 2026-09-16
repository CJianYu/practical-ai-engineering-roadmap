# Learning Philosophy

## Build one system deeply

A collection of tiny demos proves familiarity. A single system with data, tools, evals, safety, deployment, and documented trade-offs proves engineering ability.

## Evals before optimization

Before changing a prompt, model, retriever, or framework, identify the failure slice and define how improvement will be measured. Otherwise, iteration becomes anecdotal.

## Framework-light first

Implement the basic loop once: model call, tool request, validation, execution, state update, termination. Frameworks are valuable after you know which complexity they remove and which complexity they hide.

## Component metrics and end-to-end metrics

A system can have good retrieval and still fail the user. It can have a strong final answer while selecting unsafe tools. Measure both components and outcomes.

## Prefer bounded autonomy

Start with read-only tools and deterministic workflows. Add an agent loop, write access, and long-running tasks only after the previous level is evaluated.

## Learn in public, but protect data

Publishing weekly artifacts creates accountability and a visible portfolio. Use synthetic or explicitly shareable data; never publish secrets, customer content, private analytics, or employer code.

## Explain decisions

The most valuable portfolio artifact is often not the code. It is a short explanation of what failed, what you changed, why the metric moved, and what trade-off you accepted.
