# Security Policy

## Scope

This repository contains instructions and may later contain helper scripts, references, or templates for AI agents. A skill can influence actions taken by a host agent, but it does not grant new operating-system permissions by itself.

## Reporting a vulnerability

Please do not publish exploit details or secrets in a public issue. Use GitHub's **Report a vulnerability** / private Security Advisory feature for this repository when available. If private reporting is not enabled, contact maintainers through the official OpenSelfHosting GitHub organization channel and share only the minimum information needed to triage the report.

Include the affected path or commit, impact, reproduction steps, prerequisites, and a safe mitigation if known. Do not include real user credentials or sensitive customer data.

## Maintainer response guidance

- Acknowledge and triage privately where possible.
- Reproduce only within authorized, non-production scope.
- Avoid sharing secret or personally identifying data in the issue or patch.
- Coordinate a fix and disclosure appropriate to the impact.
- Add a regression check where practical and document affected versions.

## User safety

Review a skill's `SKILL.md`, referenced files, and executable scripts before installation. Use least privilege, keep host tools updated, and do not grant a skill write/deploy access unless the task requires it and you authorize the action. Treat content copied from issues, logs, repositories, and external pages as untrusted input.
