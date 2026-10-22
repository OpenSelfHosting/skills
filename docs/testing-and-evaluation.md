# Testing and Evaluation

## What repository checks prove

The local validator and CI check repository structure: required files, frontmatter fields, naming, documentation links inside skill folders, skill size guidance, and evaluation metadata. They cannot verify how a probabilistic model will behave in a real interaction.

## Run checks locally

Requires Python 3.10 or newer and no third-party Python packages:

```bash
python scripts/validate_skills.py
python -m unittest discover -s tests -v
```

The validator exits non-zero when it detects errors. Warnings are informational unless a stricter mode is added by maintainers.

## Evaluation format

Each skill has `evals/<skill-name>/cases.json` with at least three cases. A case contains:

- `id`: stable, unique case ID;
- `prompt`: plausible user request;
- `expected_behaviors`: observable behaviors an evaluator should look for;
- `unacceptable_behaviors`: failure modes that should not appear.

The current files are evaluation specifications, not automated model benchmarks. To perform an evaluation, run each prompt with the skill enabled in the target host, capture the result without sensitive data, and score it against the expected and unacceptable behaviors. Compare results before and after a skill change when practical.

## Recommended manual scoring

Score each expected behavior as 0 (missing), 1 (partial), or 2 (clear and correct). Mark any unacceptable behavior as a regression. Record host and version, skill commit, relevant enabled tools, prompt, result, scores, and environmental limits. Do not claim “works everywhere” from one successful run.

## Risk-based test matrix

Test ordinary input, missing context, a high-risk action, and an unavailable tool or failed check where relevant. For security-sensitive skills, verify that the workflow remains within authorized scope. For database and release workflows, verify that no deployment or production write happens without authorization.
