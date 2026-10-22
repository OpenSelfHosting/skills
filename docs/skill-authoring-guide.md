# Skill Authoring Guide

This repository follows the [Agent Skills specification](https://agentskills.io/specification). Re-check the official specification when changing authoring rules; do not assume an optional field is supported by every host.

## Required shape

Each skill must be stored under `skills/<skill-name>/SKILL.md` and start with YAML frontmatter containing at least `name` and `description`:

```yaml
---
name: example-skill
description: Explains what the skill does and when to use it. Use when a user asks for the task this workflow covers.
license: MIT
metadata:
  author: OpenSelfHosting
  version: "1.0.0"
---
```

The `name` must match the containing folder. Use lowercase letters, digits, and single hyphens; do not begin/end with a hyphen or use consecutive hyphens. Keep the description specific and include natural language trigger phrases. Required field limits and any additional constraints are defined by the current official specification.

## Recommended body structure

1. Goal and scope.
2. Workflow with observable steps.
3. Decision points and edge cases.
4. Verification criteria and expected output.
5. Safety boundaries and prohibited shortcuts.
6. Reporting format, including uncertainty and checks not run.

## Principles

- Build for one recurring job, not a broad personality.
- Tell the agent what evidence to inspect and how to make decisions.
- Distinguish mandatory steps from optional suggestions.
- Never encourage unapproved destructive actions, external side effects, or secret disclosure.
- Be honest about unavailable tools, unverified assumptions, and checks not executed.
- Keep the main `SKILL.md` concise (under 500 lines; smaller is usually better).
- Put substantial reference material in `references/` and templates in `assets/` only when they improve the workflow.
- Link referenced files by a simple, relative path and make sure each target exists.
- Do not add executable scripts without a clear value, a usage note, and a safety review.
- Avoid mentioning a specific host agent unless the skill truly requires it. If it does, document the dependency and a fallback.

## Before proposing a new skill

Check the catalog for overlap. Prefer improving an existing skill if the task, inputs, workflow, and expected output are effectively the same. If two tasks need different permission boundaries, success criteria, or specialist knowledge, separate skills may be justified.

## Definition of done

- Frontmatter is valid and the folder matches `name`.
- The description accurately signals when the skill should activate.
- The workflow is actionable and bounded.
- The output criteria make completion reviewable.
- Risks and external side effects are addressed.
- At least three realistic evaluation cases exist in `evals/<skill-name>/cases.json`.
- The repository validator and tests pass.
- Hands-on tests have been performed before claiming compatibility with any specific host/version.
