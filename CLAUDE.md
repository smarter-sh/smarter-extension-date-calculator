# CLAUDE.md

Guidance for Claude Code (and other coding agents) working in this repository.

This is the **Date Calculator** Smarter Extension (slug `date-calculator`, package
`date_calculator`), an official extension that does date arithmetic for LLMs. Its one tool,
`date_calculator`, takes an `operation` (difference, add, subtract, oldest, newest, convert) and
one or more dates in any common format, read with python-dateutil. It has no settings.

A Smarter Extension is a Python package that a Smarter platform installs from the signed registry
(smarter-sh/extensions-registry) and runs inside itself. Its tools subclass
`smarter.apps.llmtool.extension.SmarterExtensionTool`, so the tests run against a checkout of
smarter-sh/smarter: the sibling `../smarter` and its `smarter-app` container.

Detailed know-how lives in the Agent Skills under `skills/` (symlinked to `.claude/skills`).
**Load `smarter-extension-development` first for any change.**

## Hard rules

1. **Never run git write commands.** "Write a git commit" means print the command as text. See
   `smarter-extension-git-commits`.
2. **Never edit `version` in `pyproject.toml`, or `CHANGELOG.md`.** semantic-release writes them
   on each push to `main`, and the commit type decides the release. See `smarter-extension-release`.
3. **Run the tests yourself**, after any change:
   `scripts/run-tests.sh --validate`. Never ask the user to.
   Report failures honestly.
4. **The `smarter-app` container holds live cloud credentials.** Tests mock every third-party
   service and use placeholder keys. Don't run anything there that writes to real infrastructure.
5. **Import only what the platform installs** (`../smarter/smarter/requirements/base.txt`), and
   use relative imports inside the package.
6. **Files from the template stay identical** in every official extension: `release.config.js`,
   `package.json`, `.github/workflows/`, `scripts/`, `skills/`. Change them in
   smarter-sh/smarter-extension-cookiecutter and every official extension, or not at all.
7. **This repository is public.** No API keys, tokens, account ids or private hostnames.

## Commit authorship

You are the author: `--author="Claude <noreply@anthropic.com>"`. Lawrence McDaniel is the
co-author: the last `-m` is `Co-authored-by: Lawrence McDaniel <lpm0073@gmail.com>`. See
`smarter-extension-git-commits`.

## Repository map

| Path                         | Contents                                                       |
| ---------------------------- | -------------------------------------------------------------- |
| `pyproject.toml`             | `[project]` and `[tool.smarter]`: slug, tools                  |
| `date_calculator/__init__.py` | The extension's documentation (module docstring, RST)         |
| `date_calculator/tools.py`   | `DateCalculator`, the `date_calculator` tool, and its arguments |
| `tests/`                     | unittest tests                                                 |
| `scripts/`                   | `set_version.py`, `package.py`, run by semantic-release        |
| `.github/workflows/`         | `test.yml` (tests + Codecov), `release.yml` (semantic-release) |

## Definition of done

- The change follows the existing pattern, and the tests cover it (coverage stays at 100%).
- You ran `scripts/run-tests.sh --validate`, and black and isort on the changed files.
- The package docstring, README and field descriptions match the code.
- Your summary says what changed, what you verified, what you skipped, and which commit type (and
  so which release) the change needs.
