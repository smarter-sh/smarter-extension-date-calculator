"""Tests of the date_calculator tool."""

import unittest

from date_calculator.tools import DateCalculator

from smarter.apps.llmtool.extension.testing import call_tool


def calculate(**arguments):
    return call_tool(DateCalculator, arguments)


class TestDateCalculator(unittest.TestCase):
    """Test every operation, and its errors."""

    def test_cache_ttl(self):
        """The tool changes nothing, and its result doesn't depend on who asks, so a result is cached for an hour."""
        self.assertEqual(DateCalculator.cache_ttl, 3600)

    def test_difference(self):
        result = calculate(dates=["1966-12-31", "2026-02-27"], operation="difference")
        self.assertEqual(result["difference_days"], 21608)
        self.assertEqual(result["difference_years"], 59.16)

    def test_add_and_subtract(self):
        self.assertEqual(calculate(dates=["2026-10-15"], operation="add", days=30), {"result": "2026-11-14"})
        self.assertEqual(
            calculate(dates=["10/15/2026 14:30"], operation="subtract", days=1), {"result": "2026-10-14T14:30:00"}
        )

    def test_oldest_and_newest(self):
        dates = ["2026-10-15", "March 3, 1999", "2001-01-01"]
        self.assertEqual(calculate(dates=dates, operation="oldest"), {"oldest": "1999-03-03T00:00:00"})
        self.assertEqual(calculate(dates=dates, operation="newest"), {"newest": "2026-10-15T00:00:00"})

    def test_convert(self):
        self.assertEqual(
            calculate(dates=["2026-10-15"], operation="convert", date_format="US"), {"converted": "10/15/2026"}
        )
        self.assertEqual(
            calculate(dates=["2026-10-15"], operation="convert", date_format="EU"), {"converted": "15/10/2026"}
        )
        self.assertEqual(
            calculate(dates=["2026-10-15"], operation="convert", date_format="ISO"),
            {"converted": "2026-10-15T00:00:00"},
        )

    def test_errors(self):
        cases = [
            ({"dates": ["not a date"], "operation": "oldest"}, "Could not read a date"),
            ({"dates": ["2026-10-15"], "operation": "difference"}, "exactly two dates"),
            ({"dates": ["2026-10-15", "2026-10-16"], "operation": "add", "days": 1}, "exactly one date"),
            ({"dates": ["2026-10-15"], "operation": "add"}, "needs days"),
            ({"dates": ["2026-10-15"], "operation": "convert"}, "needs date_format"),
            ({"dates": ["9999-12-31"], "operation": "add", "days": 2}, "out of range"),
            ({"dates": [], "operation": "oldest"}, "Invalid arguments"),
            ({"dates": ["2026-10-15"], "operation": "multiply"}, "Invalid arguments"),
        ]
        for arguments, message in cases:
            with self.subTest(arguments=arguments):
                self.assertIn(message, calculate(**arguments)["error"])

    def test_definition(self):
        self.assertEqual(DateCalculator.problems(), [])
