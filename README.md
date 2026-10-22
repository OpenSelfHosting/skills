# OpenSelfHosting Skills

**Portable, practical workflows for AI agents that help people understand, change, test, secure, document, and ship software.**

OpenSelfHosting Skills is an open-source, community-maintained collection built on the [Agent Skills open format](https://agentskills.io/specification). Each skill lives in its own directory and includes a `SKILL.md` file with task triggers, an actionable workflow, verification expectations, and safety boundaries. Evaluation scenarios and repository checks help contributors maintain quality as the collection grows.

> Skills guide an agent's workflow; they do not grant tools, permissions, or capabilities that the host agent does not have. Always review a skill before installing it, especially if it includes executable scripts.

## Install

The recommended installer is the open-source [`skills` CLI](https://github.com/vercel-labs/skills). Run these commands in the project where you want the skills available:

```bash
# List the skills available from this repository
npx skills add OpenSelfHosting/skills --list

# Install one skill into your current project
npx skills add OpenSelfHosting/skills --skill systematic-debugging

# Install selected skills for a supported agent
npx skills add OpenSelfHosting/skills --skill code-review --agent claude-code

# Install a skill globally for your user (where supported)
npx skills add OpenSelfHosting/skills --skill codebase-onboarding -g
```

To inspect the full installer options, run `npx skills add --help`. Agent identifiers and install locations depend on the installed CLI version and host applications. If the organization/repository is not published yet, replace `OpenSelfHosting/skills` with the GitHub owner/repository after publishing it.

## Skill catalog

| Skill | Use it for |
|---|---|
| [`codebase-onboarding`](skills/codebase-onboarding/SKILL.md) | Understand an unfamiliar repository before changing it |
| [`systematic-debugging`](skills/systematic-debugging/SKILL.md) | Reproduce bugs, find root causes, and verify a fix |
| [`code-review`](skills/code-review/SKILL.md) | Review diffs for material defects and actionable risks |
| [`test-driven-changes`](skills/test-driven-changes/SKILL.md) | Implement behavior changes with meaningful regression tests |
| [`ci-failure-triage`](skills/ci-failure-triage/SKILL.md) | Diagnose failed or flaky CI/CD pipelines |
| [`security-review`](skills/security-review/SKILL.md) | Review application and configuration security defensively |
| [`dependency-health`](skills/dependency-health/SKILL.md) | Review dependency updates, risk, and reproducibility |
| [`database-migration-review`](skills/database-migration-review/SKILL.md) | Reduce schema migration and data-loss risks |
| [`api-contract-review`](skills/api-contract-review/SKILL.md) | Evaluate API compatibility and interface behavior |
| [`docs-maintenance`](skills/docs-maintenance/SKILL.md) | Keep docs and examples aligned with actual code |
| [`pull-request-prep`](skills/pull-request-prep/SKILL.md) | Prepare a scoped, evidence-based pull request |
| [`release-readiness`](skills/release-readiness/SKILL.md) | Make a risk-based release go/no-go assessment |
| [`skill-authoring`](skills/skill-authoring/SKILL.md) | Create, test, and improve Agent Skills |
| [`research-with-sources`](skills/research-with-sources/SKILL.md) | Perform source-backed research with transparent uncertainty |

## Design principles

- **Action over slogans:** every skill has a workflow and an expected output.
- **Evidence over confidence theater:** distinguish inspected facts, hypotheses, and checks that actually ran.
- **Safe by default:** preserve user changes, avoid destructive operations, and disclose side effects and uncertainty.
- **Portable by design:** use the standard `SKILL.md` structure and avoid assuming one vendor's tools.
- **Focused context:** load extra references only when needed; do not bury the primary workflow under encyclopedic material.
- **Testable:** contributors add realistic evaluations and run repository validation.

## Quality status

The repository includes a dependency-free structural validator, automated tests, and evaluation cases. These checks validate repository structure and evaluation metadata; they **do not prove that every language-model output will follow a skill correctly**. Compatibility claims should be based on hands-on tests in the named host agent and version.

## Repository map

```text
skills/             Reusable Agent Skills (each has SKILL.md)
evals/              Representative prompts and behavior rubrics per skill
docs/               Authoring, testing, and release guidance
scripts/            Dependency-free repository validation tools
tests/              Tests for the repository validator
.github/            CI, issue templates, and pull request template
```

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md), [the authoring guide](docs/skill-authoring-guide.md), and [the evaluation guide](docs/testing-and-evaluation.md) before submitting a skill. New skills should solve a distinct, repeatable problem and include at least three realistic evaluation cases.

## Security

Review skill instructions and scripts before installation. Report suspected vulnerabilities using the private reporting option in GitHub Security Advisories for this repository, if enabled, or contact the maintainers through the organization's official GitHub presence. See [SECURITY.md](SECURITY.md).

## License

The project and included skills are released under the MIT License unless a file states otherwise. See [LICENSE](LICENSE).

## Language

The primary repository documentation is in English to make community contributions easier. An Arabic quick-start guide is available at [docs/getting-started-ar.md](docs/getting-started-ar.md).
