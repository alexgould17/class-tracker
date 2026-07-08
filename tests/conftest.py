"""Configurations to be used across all tests."""

import secrets
from datetime import datetime, timezone

import numpy as np
import pytest

from assignment import Assignment
from school import DEFAULT_GRADE_POINTS, School
from school_class import Class
from term import DEFAULT_PARTS_OF_YEAR, Term

# Static test vars, all ranges are half-open unless otherwise specified
SMALL_RANGE = (6, 10)

ASSIGN_NAME_FORMAT = 'assignment {}'
ASSIGN_CAT_FORMAT = 'category {}'
ASSIGN_POINTS_OUT_OF = 100.0
ASSIGN_POINTS_EARNED_RANGE = (50.0, 100.0)  # technically this is (50.0, 100.0]

TERM_NAME_FORMAT = 'term {}'
TERM_YEAR_RANGE = (1900, datetime.now(timezone.utc).year)
TERM_PARTS_OF_YEAR = DEFAULT_PARTS_OF_YEAR.copy()

SCHOOL_IDENTIFIER_FORMAT = 'school {}'
SCHOOL_SHORT_NAME_FORMAT = 'short name {}'
SCHOOL_PRETTY_NAME_FORMAT = 'short name {}'
SCHOOL_GRADE_PTS = DEFAULT_GRADE_POINTS.copy()

CLASS_DEPT_FORMAT = 'dept {}'
CLASS_NUMBER_RANGE = (100, 600)
CLASS_SHORT_DESC_FORMAT = 'short desc {}'
CLASS_DESCRIPTION_FORMAT = 'description {}'
CLASS_GRADES = list(DEFAULT_GRADE_POINTS.keys())
CLASS_HRS_RANGE = (1, 5)
CLASS_TAG_FORMAT = 'tag {}'

# Initialize the random number generator with a good random seed
RNG = np.random.default_rng(secrets.randbits(128))

# Necessary to not have duplicate schools
SCHOOL_0 = School(
    SCHOOL_IDENTIFIER_FORMAT.format(0),
    SCHOOL_SHORT_NAME_FORMAT.format(0),
    SCHOOL_PRETTY_NAME_FORMAT.format(0),
    grade_pts=SCHOOL_GRADE_PTS,
)


@pytest.fixture
def rng() -> np.random.Generator:
    """Grant access to the random number generator used by conftest."""
    return RNG


@pytest.fixture
def assign_statics() -> tuple[str, str, float, tuple[float, float]]:
    """Get all the values/formats/ranges used to build Assignment instances.

    Returns:
        A tuple with the following in this order:
        - The name format string (takes 1 param, set to a 1-indexed int in fixtures)
        - The category format string (takes 1 param, set to a 1-indexed int in fixtures)
        - The maximum points_out_of for a test Assignment
        - A tuple representing the range of possible random values for points_earned for
          a test Assignment. Half-open, of the form (lo, hi]

    """
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
    """Return all the values/formats/ranges used to build Term instances.

    Returns:
        A tuple with the following in this order:
        - The name format string (takes 1 param, set to a 1-indexed int in fixtures)
        - A tuple containing the half-open range of possible random years for a test
          Term, of the form [lo, hi)
        - A list of strings that maps to the parts_of_year for all test Terms produced
          by fixtures. By default, fixture terms map to parts_of_year[0]

    """
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


@pytest.fixture
def school_statics() -> tuple[str, str, str, dict[str, float]]:
    """Return all the values/formats used to build School instances.

    Returns:
        A tuple with the following in this order:
        - The identifier format string (takes 1 param, a 1-indexed int in fixtures)
        - The short name format string (takes 1 param, a 1-indexed int in fixtures)
        - The pretty name format string (takes 1 param, a 1-indexed int in fixtures)
        - A dictionary that maps grade letters to grade points for all test Schools
          produced by fixtures

    """
    return (
        SCHOOL_IDENTIFIER_FORMAT,
        SCHOOL_SHORT_NAME_FORMAT,
        SCHOOL_PRETTY_NAME_FORMAT,
        SCHOOL_GRADE_PTS,
    )


@pytest.fixture
def school() -> School:
    """Get a single School made with the static test values.

    NOTE: Formatted with all 0's to prevent id conflict in test suite.
    """
    return SCHOOL_0


@pytest.fixture
def list_of_schools() -> tuple[int, list[School]]:
    """Get a list of Schools made with the static test values.

    Returns:
        A tuple with the number of Schools, a list of School instances

    """
    n = int(RNG.integers(*SMALL_RANGE))
    return n, [
        School(
            SCHOOL_IDENTIFIER_FORMAT.format(i + 1),
            SCHOOL_SHORT_NAME_FORMAT.format(i + 1),
            SCHOOL_PRETTY_NAME_FORMAT.format(i + 1),
            grade_pts=SCHOOL_GRADE_PTS,
        )
        for i in range(n)
    ]


@pytest.fixture
def class_statics() -> tuple[
    str, tuple[int, int], str, str, list[str], tuple[int, int], str
]:
    """Return all the values/formats used to build School instances.

    Returns:
        A tuple with the following in this order:
        - The dept format string (takes 1 param, a 1-indexed int in fixtures)
        - A tuple containing the half-open range of possible random numbers for a test
          Class, of the form [lo, hi)
        - The short_desc format string (takes 1 param, a 1-indexed int in fixtures)
        - The description format string (takes 1 param, a 1-indexed int in fixtures)
        - A list of the grades to use with test Classes
        - A tuple containing the half-open range of possible random hours for a test
          Class, of the form [lo, hi)
        - The tag format string (takes 1 param)

    """
    return (
        CLASS_DEPT_FORMAT,
        CLASS_NUMBER_RANGE,
        CLASS_SHORT_DESC_FORMAT,
        CLASS_DESCRIPTION_FORMAT,
        CLASS_GRADES,
        CLASS_HRS_RANGE,
        CLASS_TAG_FORMAT,
    )


@pytest.fixture
def mock_class() -> Class:
    """Get a single Class made with the static test values."""
    random_term = Term(
        TERM_NAME_FORMAT.format(1),
        int(RNG.integers(*TERM_YEAR_RANGE)),
        TERM_PARTS_OF_YEAR[0],
        part_of_year_names=TERM_PARTS_OF_YEAR,
    )
    return Class(
        CLASS_DEPT_FORMAT.format(1),
        int(RNG.integers(*CLASS_NUMBER_RANGE)),
        int(RNG.integers(*CLASS_HRS_RANGE)),
        random_term,
        SCHOOL_0,
    )


@pytest.fixture
def list_of_classes() -> tuple[int, list[Class]]:
    """Get a list of classes made with the static test values.

    The classes will all have the same school (SCHOOL_0) but a random term

    Returns:
        A tuple with the number of Classes, the list of Class instances

    """
    n = int(RNG.integers(*SMALL_RANGE))
    return n, [
        Class(
            CLASS_DEPT_FORMAT.format(i + 1),
            int(RNG.integers(*CLASS_NUMBER_RANGE)),
            int(RNG.integers(*CLASS_HRS_RANGE)),
            Term(
                TERM_NAME_FORMAT.format(i + 1),
                int(RNG.integers(*TERM_YEAR_RANGE)),
                TERM_PARTS_OF_YEAR[0],
                part_of_year_names=TERM_PARTS_OF_YEAR,
            ),
            SCHOOL_0,
        )
        for i in range(n)
    ]
