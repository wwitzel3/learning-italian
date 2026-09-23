## Agent skills

### Issue tracker

Issues live as local markdown files under `.scratch/<feature>/`. See `docs/agents/issue-tracker.md`.

### Triage labels

Default five-role vocabulary (needs-triage, needs-info, ready-for-agent, ready-for-human, wontfix). See `docs/agents/triage-labels.md`.

### Domain docs

Single-context: one `CONTEXT.md` + `docs/adr/` at the repo root. See `docs/agents/domain.md`.

## Review gates

Run both gates before you report work done or commit it.

- **Prose a human reads** (site pages, specs and tickets in `.scratch/`, `CONTEXT.md`, ADRs, READMEs, commit and PR messages): read `.claude/skills/unslop/SKILL.md` and apply every rule to the text.
- **Code changes** (source, tests, config): invoke the `comment-sicko` skill on the diff against `main`. Defer to its fresh read over your own comments.
