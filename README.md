# Smarter Extension: Date Calculator

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
`python manage.py test_extension <path to this repository>`. Release by pushing a `v<version>` tag.
