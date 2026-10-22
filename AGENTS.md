# Repository Instructions for AI Agents

- Read `README.md`, `CONTRIBUTING.md`, and `docs/skill-authoring-guide.md` before making collection-wide changes.
- Keep each skill focused on one recurring job, portable across compatible Agent Skills hosts, and clear about unavailable tools.
- Preserve user changes; never run destructive actions, production writes, or deployments without explicit authorization.
- Every skill must have matching frontmatter and directory name, at least three evaluation cases, and a README catalog entry.
- Do not claim behavioral compatibility with an agent/version without testing it directly.
- Run `python scripts/validate_skills.py` and `python -m unittest discover -s tests -v` before proposing a change.
- Avoid external dependencies in repository validation unless a maintainer approves the tradeoff.
