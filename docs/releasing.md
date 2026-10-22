# Release Process

1. Merge only changes that pass CI and have been reviewed.
2. Confirm every changed skill has updated evaluation cases when behavior changed.
3. Run locally:
   ```bash
   python scripts/validate_skills.py
   python -m unittest discover -s tests -v
   ```
4. Review the whole diff and verify the README catalog matches the `skills/` directories.
5. Update `CHANGELOG.md` with user-visible changes and any compatibility caveats.
6. Create an annotated version tag (for example `v1.1.0`) only after maintainer approval. Follow semantic intent: patch for corrections, minor for new backward-compatible skills or substantial additions, major for breaking repository/install changes.
7. Publish release notes that list added/changed/removed skills, evaluation results, and host/version limitations. Do not describe structural validation as proof of model performance.
8. Test install commands against the published repository and a supported host after release.

This document does not authorize automatic publishing or deployment. Maintainers should protect release permissions and tag creation.
