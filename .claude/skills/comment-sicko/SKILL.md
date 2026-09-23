---
name: comment-sicko
description: Spawn Comment Sicko on a code diff, act on accepted findings, delete condemned comments. Run before finalizing any code change.
---

# comment-sicko

Get a hostile fresh-context read of the comments in a change, then act on it.

Source: adapted from `backnotprop/pstack` `skills/no-comments`, without the `/architect`
and `principle-*` dependencies that repo carries. Pairs with the `Comment Sicko` agent
in `.claude/agents/comment-sicko.md`.

The agent that wrote the code will defend its comments. Defer to Comment Sicko's fresh read.

## Scope

Use the caller's files or diff. Otherwise use the current diff against the base branch
(default `main`), including the working tree.

## Steps

1. Spawn `Task` with `subagent_type: "Comment Sicko"`. Pass the scope. Do not restate its rules.
2. Read its report. For each flag, accept or reject:
   - Reject flags that touch application code it should not, escape the scope, or delete a comment protected by one of its listed exceptions (legal headers, external-constraint notes, valid lint/type suppressions, public-API doc contracts, issue/ADR/RFC links).
   - Reject a `MUST KILL` whose stated reason misreads the code. Confirm the claim by reading nearby code and `git blame` / `git log` on the symbol before accepting.
   - Accept the rest.
3. Delete every comment tied to an accepted flag. Do not rewrite a comment into a shorter version of itself.
4. For each accepted `MUST KILL`, make the smallest change that makes the behavior obvious without the comment: rename, extract, add a type, restructure. If that is out of scope for this change, leave the code and report the `MUST KILL` as open work.
5. Constraint comments (`do not remove`, `talk to X first`): leave the ones about things outside our control. Delete the ones about our own code and report them as open work.
6. Report: files touched, comments deleted, `MUST KILL`s resolved vs open, constraint comments left in place.
