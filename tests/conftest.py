"""Configurations to be used across all tests."""

import secrets

import numpy as np
import pytest
from numpy.random.mtrand import RandomState

from assignment import Assignment

# Static test vars, all ranges are half-open
SMALL_RANGE = (6, 10)
ASSIGN_NAME_FORMAT = 'assignment {}'
ASSIGN_CAT_FORMAT = 'category {}'
ASSIGN_POINTS_OUT_OF = 100.0
ASSIGN_POINTS_EARNED_RANGE = (50, 100)

# Initialize the random number generator with a good random seed
RNG = np.random.default_rng(secrets.randbits(128))


@pytest.fixture
def rng() -> np.random.Generator:
    return RNG


@pytest.fixture
def assign_statics() -> tuple[str, str, float, tuple[int, int]]:
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
