# Contributing

> _This project accepts changes from pull requests only!_

## Docs

- [Fork A Repo, GitHub Documentation](https://help.github.com/articles/fork-a-repo/)

## Zen

- Don't commit changes to origin/dev or your local copy of dev
- Create topic branches
- Commit often
- Write high-quality commit messages
- `git fetch --all` and `git rebase upstream/dev` before pr submission
- Run tests before submission
- Limit commit header lines to 80 characters
- Always include a type, scope, & subject
- Subjects should use the imperative tense; "Change, Fix, Remove" in lieu of "Changed, Fixed, Removed" or "Changes, Fixes, Removes".
- Include body text if more information is helpful.

## Style

Each commit message consists of a header (comprised of a type scope and subject) and a body (optional).

```bash
# Note: This comment, and those that follow should not be 
# included in any commit.

# Header:
# Types are, feature, refactor, fix, chore
# Scope describes what the change affects.
# Subject succinctly describes the change.
<type>(<scope>): <subject>

# Body provides more info when it's helpful to do so.
<body>
```

__Examples__:

```
feature(auth): Enable single signon

refactor(api): Require user token when accessing api/users

chore(docs): Update README.md

fix(home page): Fix catastrophic bug when scrolling on IOS
```

### Types

| Type | Desc |
| :--  | :--  |
| __feature__ | A commit related to a new feature.
| __refactor__ | A commit that is not a feature but changes the meaning of existing code.
| __fix__ | A commit that fixes a bug or issue.
| __chore__ | A commit that _does not_ change the meaning of existing code; e.g. updating docs.

### Scopes

Scopes describe the area or feature the change affects. Deciding what to put here can be a bit fuzzy so here's some suggestions:

- Use concise scope values.
- Try to use consistent scope values between commits.
- If the change is related to a QA ticket (e.g., PROJ-123) use the ticket number as the scope or part of the scope.
