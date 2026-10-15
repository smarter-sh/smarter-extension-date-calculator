# Smarter Extension: Date Calculator

[![Build Status](https://img.shields.io/github/actions/workflow/status/smarter-sh/smarter-extension-date-calculator/release.yml?label=build&logo=github)](https://github.com/smarter-sh/smarter-extension-date-calculator/actions/workflows/release.yml)
[![Test Status](https://github.com/smarter-sh/smarter-extension-date-calculator/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/smarter-sh/smarter-extension-date-calculator/actions/workflows/test.yml)
[![Coverage](https://img.shields.io/codecov/c/github/smarter-sh/smarter-extension-date-calculator/main?label=coverage&logo=codecov)](https://codecov.io/gh/smarter-sh/smarter-extension-date-calculator)
[![Latest Release](https://img.shields.io/github/v/release/smarter-sh/smarter-extension-date-calculator?label=release)](https://github.com/smarter-sh/smarter-extension-date-calculator/releases)
[![Official Smarter Extension](https://img.shields.io/badge/Smarter%20Extension-official-0b6e4f)](https://github.com/smarter-sh/extensions-registry)
[![Docs](https://img.shields.io/badge/Read%20the%20Docs-smarter.sh-blue?logo=readthedocs)](https://docs.smarter.sh/en/latest/smarter-framework/smarter-extensions.html)
[![License: GNU AGPL v3](https://img.shields.io/badge/License-AGPL_v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)

An official [Smarter Extension](https://docs.smarter.sh/en/latest/smarter-framework/smarter-extensions.html)
whose `date_calculator` tool does date arithmetic exactly: the difference between two dates, adding
or subtracting days, the oldest or newest of several dates, and converting a date to the ISO, US or
EU format. Dates may be in any common format.

List it in an LLMClient's manifest:

```yaml
spec:
  extensions:
    - date-calculator
```

Run the tests in a Smarter development container with
`python manage.py test_extension <path to this repository>`. CI runs them on every push and pull
request, against a source checkout of Smarter. Release by pushing a `v<version>` tag.
