"""Configurations to be used across all tests."""

import secrets
from datetime import datetime, timezone

import numpy as np
import pytest

from assignment import Assignment
from term import DEFAULT_PARTS_OF_YEAR, Term

# Static test vars, all ranges are half-open unless otherwise specified
SMALL_RANGE = (6, 10)

ASSIGN_NAME_FORMAT = 'assignment {}'
ASSIGN_CAT_FORMAT = 'category {}'
ASSIGN_POINTS_OUT_OF = 100.0
ASSIGN_POINTS_EARNED_RANGE = (50, 100)  # technically this is (50.0, 100.0]

TERM_NAME_FORMAT = 'term {}'
TERM_YEAR_RANGE = (1900, datetime.now(timezone.utc).year)
TERM_PARTS_OF_YEAR = DEFAULT_PARTS_OF_YEAR

# Initialize the random number generator with a good random seed
RNG = np.random.default_rng(secrets.randbits(128))


@pytest.fixture
def rng() -> np.random.Generator:
    """Grant access to the random number generator used by conftest."""
    return RNG


@pytest.fixture
def assign_statics() -> tuple[str, str, float, tuple[int, int]]:
    """Return all the values/formats/ranges used to build Assignment instances."""
    return (
        ASSIGN_NAME_FORMAT,
        ASSIGN_CAT_FORMAT,
        ASSIGN_POINTS_OUT_OF,
        ASSIGN_POINTS_EARNED_RANGE,
    )


@pytest.fixture
def assignment() -> Assignment:
    """Get a single Assignment made with the static test values."""
    return Assignment(
        ASSIGN_NAME_FORMAT.format(1),
        1,
        ASSIGN_CAT_FORMAT.format(1),
        ASSIGN_POINTS_OUT_OF,
        ASSIGN_POINTS_EARNED_RANGE[1]
        - round(RNG.random(), 2) * ASSIGN_POINTS_EARNED_RANGE[0],
    )


@pytest.fixture
def list_of_assignments() -> tuple[int, list[Assignment]]:
    """Get a list of Assignments made with the static test values.

    Returns:
        A tuple with the number of Assignments, a list of the Assignments

    """
    n = int(RNG.integers(*SMALL_RANGE))
    return n, [
        Assignment(
            ASSIGN_NAME_FORMAT.format(i + 1),
            i + 1,
            ASSIGN_CAT_FORMAT.format(1),
            ASSIGN_POINTS_OUT_OF,
            ASSIGN_POINTS_EARNED_RANGE[1]
            - round(RNG.random(), 2) * ASSIGN_POINTS_EARNED_RANGE[0],
        )
        for i in range(n)
    ]


@pytest.fixture
def term_statics() -> tuple[str, tuple[int, int], list[str]]:
    """Return all the values/formats/ranges used to build Term instances."""
    return (
        TERM_NAME_FORMAT,
        TERM_YEAR_RANGE,
        TERM_PARTS_OF_YEAR,
    )


@pytest.fixture
def term() -> Term:
    """Get a single Term made with the static test values."""
    return Term(
        TERM_NAME_FORMAT.format(1),
        int(RNG.integers(*TERM_YEAR_RANGE)),
        TERM_PARTS_OF_YEAR[0],
        part_of_year_names=TERM_PARTS_OF_YEAR,
    )


@pytest.fixture
def list_of_terms() -> tuple[int, list[Term]]:
    """Get a list of Terms made with the static test values.

    Returns:
        A tuple with the number of Terms, a list of the Terms

    """
    n = int(RNG.integers(*SMALL_RANGE))
    return n, [
        Term(
            TERM_NAME_FORMAT.format(i + 1),
            int(RNG.integers(*TERM_YEAR_RANGE)),
            TERM_PARTS_OF_YEAR[0],
            part_of_year_names=TERM_PARTS_OF_YEAR,
        )
        for i in range(n)
    ]
