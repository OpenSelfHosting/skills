# Contributing

Contributions that solve a real recurring problem are welcome: new skills, better instructions, evaluation cases, docs, accessibility, and validation improvements.

## Before opening a PR

1. Search the [skill catalog](README.md) to avoid duplicating an existing workflow.
2. Read [the authoring guide](docs/skill-authoring-guide.md) and [testing guide](docs/testing-and-evaluation.md).
3. Keep each skill focused. Explain when it should activate and when it should not.
4. Include at least three realistic evaluation cases for every new skill. Add edge cases for important failure modes.
5. Keep core instructions concise and portable. Any required external tool, dependency, network access, or side effect must be stated explicitly.
6. Add no secrets, personal data, tracking, hidden network requests, or unreviewed executable payloads.
7. Run the validator and tests:
   ```bash
   python scripts/validate_skills.py
   python -m unittest discover -s tests -v
   ```
8. Update the README catalog and changelog when user-facing skills are added, changed, or removed.

## Pull request description

Include the user problem, why this should be a distinct skill, key workflow choices, evaluation cases added/changed, commands run and actual results, known limitations, and any security or compatibility considerations.

## Review criteria

Maintainers assess distinct value, trigger precision, actionable steps, evidence grounding, verification quality, safety boundaries, portability, evaluation coverage, and maintainability. A skill may be rejected if it is overly broad, duplicates another skill, makes unsupported guarantees, or tells agents to bypass safeguards.

## Conduct

Be constructive, evidence-based, inclusive, and respectful. See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
