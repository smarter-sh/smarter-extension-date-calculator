"""
Date Calculator
===============

Date arithmetic, done exactly rather than guessed. Dates may be in any common format, such as
``2026-10-15``, ``10/15/2026`` or ``October 15, 2026``.

This extension has no settings.

Tools
-----

``date_calculator(dates, operation, days, date_format)``
    One of these operations:

    - ``difference``: the days, weeks, months and years between exactly two dates;
    - ``add`` and ``subtract``: a date plus or minus ``days``;
    - ``oldest`` and ``newest``: the earliest or latest of one or more dates;
    - ``convert``: one date in the ``ISO``, ``US`` (MM/DD/YYYY) or ``EU`` (DD/MM/YYYY) format.
"""
