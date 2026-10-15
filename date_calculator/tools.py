"""The date calculator extension's tools."""

import datetime
from typing import Literal, Optional

from dateutil import parser
from pydantic import BaseModel, Field, JsonValue

from smarter.apps.llmtool.extension import ExtensionContext, ExtensionToolError, SmarterExtensionTool

Operation = Literal["difference", "add", "subtract", "oldest", "newest", "convert"]
DateFormat = Literal["ISO", "US", "EU"]
FORMATS = {"US": "%m/%d/%Y", "EU": "%d/%m/%Y"}


class DateCalculatorArguments(BaseModel):
    """The arguments of the date_calculator tool."""

    dates: list[str] = Field(
        ...,
        min_length=1,
        description="The dates, in any common format, e.g. 2026-10-15 or 10/15/2026: two for difference, one "
        "for add, subtract and convert, and one or more for oldest and newest.",
    )
    operation: Operation = Field(..., description="The operation to perform.")
    days: Optional[int] = Field(
        None, description="The number of days to add or subtract: required for add and subtract."
    )
    date_format: Optional[DateFormat] = Field(None, description="The format to convert to: required for convert.")


class DateCalculator(SmarterExtensionTool):
    """
    Calculate with dates: the difference between two dates, a date plus or minus a number of days,
    the oldest or newest of several dates, or a date in the ISO, US or EU format.
    """

    name = "date_calculator"
    arguments_model = DateCalculatorArguments

    def call(self, arguments: DateCalculatorArguments, context: ExtensionContext) -> JsonValue:
        try:
            dates = [parser.parse(text) for text in arguments.dates]
        except (ValueError, OverflowError) as e:
            raise ExtensionToolError(f"Could not read a date: {e}") from e
        operation = arguments.operation
        if operation in ("oldest", "newest"):
            chosen = min(dates) if operation == "oldest" else max(dates)
            return {operation: chosen.isoformat()}
        if operation == "difference":
            if len(dates) != 2:
                raise ExtensionToolError("difference needs exactly two dates.")
            days = abs((dates[0] - dates[1]).days)
            return {
                "difference_days": days,
                "difference_weeks": round(days / 7, 2),
                "difference_months": round(days / 30.44, 2),
                "difference_years": round(days / 365.25, 2),
            }
        if len(dates) != 1:
            raise ExtensionToolError(f"{operation} needs exactly one date.")
        if operation in ("add", "subtract"):
            if arguments.days is None:
                raise ExtensionToolError(f"{operation} needs days.")
            delta = datetime.timedelta(days=arguments.days)
            try:
                result = dates[0] + delta if operation == "add" else dates[0] - delta
            except OverflowError as e:
                raise ExtensionToolError(f"The result is out of range: {e}") from e
            return {"result": result.date().isoformat() if result.time() == datetime.time() else result.isoformat()}
        if arguments.date_format is None:
            raise ExtensionToolError("convert needs date_format: ISO, US or EU.")
        if arguments.date_format == "ISO":
            return {"converted": dates[0].isoformat()}
        return {"converted": dates[0].strftime(FORMATS[arguments.date_format])}
