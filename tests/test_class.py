"""Tests for the school_class.py module."""

import pytest

from school_class import Class
from term import Term


def test_class(class_statics, mock_class, rng, term) -> None:
    """Test the Class class initialization and methods."""
    # Unpack statics
    (
        dept_format,
        number_range,
        short_desc_format,
        description_format,
        grades,
        hrs_range,
        tag_format,
    ) = class_statics

    # Create a few tags for use later
    tag_1, tag_2 = tag_format.format(1), tag_format.format(2)

    # Assign one instance from the static and create another to test constructor
    test_instance1 = mock_class
    test_instance2 = Class(
        dept_format.format(2),
        int(rng.integers(*number_range)),
        int(rng.integers(*hrs_range)),
        term,
        test_instance1.school,
        ongoing=True,
        grade=grades[0],
        short_desc=short_desc_format.format(2),
        description=description_format.format(2),
        tags=[tag_2],
    )

    # Test creation
    assert test_instance2.dept == dept_format.format(2)
    assert number_range[0] <= test_instance2.number < number_range[1]
    assert hrs_range[0] <= test_instance2.hrs < hrs_range[1]
    assert test_instance2.term is term
    assert test_instance2.school is test_instance1.school
    assert tag_2 in test_instance2.tags
    assert test_instance2.ongoing
    assert test_instance2.grade == grades[0]
    assert test_instance2.assignments == []
    assert test_instance2.assign_cats == []
    assert test_instance2.prereqs == []
    assert test_instance2.postreqs == []
    assert test_instance2.short_desc == short_desc_format.format(2)
    assert test_instance2.description == description_format.format(2)

    # Test __lt__
    with pytest.raises(ValueError, match=r'Class object'):
        assert test_instance1 < 1
    test_instance2.number = test_instance1.number
    assert test_instance1 < test_instance2  # term same, number same, compare on dept
    test_instance2.dept = test_instance1.dept
    test_instance2.number = test_instance1.number + 1
    assert test_instance1 < test_instance2  # dept same, term same, compare on number
    test_instance2.number = test_instance1.number
    term2 = Term(term.name, term.year + 1, term.part_of_year)
    test_instance2.term = term2
    assert test_instance1 < test_instance2  # dept same, number same, compare on term

    # Test __eq__
    test_instance2.term = test_instance1.term
    assert test_instance1 == test_instance2
    with pytest.raises(ValueError, match=r'Class object'):
        assert test_instance1 == 1

    # Test __str__
    str_test = str(test_instance2)
    assert isinstance(str_test, str)
    assert test_instance2.dept in str_test
    assert str(test_instance2.number) in str_test

    # Test __repr__
    repr_test = repr(test_instance2)
    assert isinstance(repr_test, str)
    assert test_instance2.dept in repr_test
    assert str(test_instance2.number) in repr_test
    assert test_instance2.short_desc in repr_test
