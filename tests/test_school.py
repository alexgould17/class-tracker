"""Tests for the school.py module."""

import pytest

from school import MAX_SHORT_NAME_CHARS, School, _school_ids
from utilities import AlreadyExistsError


def test_school(school_statics, school) -> None:
    """Test the School class initialization and methods."""
    # Unpack statics
    (
        identifier_format,
        short_name_format,
        pretty_name_format,
        grade_points,
    ) = school_statics

    # Get a test instance from the fixture and create a test instance here, they should
    # be identical except for identifier. Test the values of the created instance
    test_instance1 = school
    test_instance2 = School(
        identifier_format.format(2),
        short_name_format.format(1),
        pretty_name_format.format(1),
        grade_pts=grade_points,
    )
    assert test_instance2.identifier == identifier_format.format(2)
    assert test_instance2.identifier in _school_ids
    assert test_instance2.short_name == short_name_format.format(1)
    assert test_instance2.pretty_name == pretty_name_format.format(1)
    assert test_instance2.grade_pts == grade_points

    # Test __eq__ by setting short_name and pretty_name to be identical first
    test_instance2.short_name = test_instance1.short_name
    test_instance2.pretty_name = test_instance1.pretty_name
    assert test_instance1 == test_instance2
    with pytest.raises(ValueError, match=r'Class object'):
        assert test_instance1 == 1

    # Change the short_name and pretty_name, and test __lt__ for each
    test_instance2.short_name = short_name_format.format(2)
    assert test_instance1 < test_instance2
    test_instance2.short_name = short_name_format.format(1)
    test_instance2.pretty_name = pretty_name_format.format(2)
    assert test_instance1 < test_instance2
    with pytest.raises(ValueError, match=r'Class object'):
        assert test_instance1 < 1

    # Try to make the schools' identifiers the same and test for AlreadyExistsError
    with pytest.raises(AlreadyExistsError, match=r'already exists'):
        test_instance2.identifier = test_instance1.identifier

    # Test short_name truncation
    test_instance2.short_name = 'a' * (MAX_SHORT_NAME_CHARS + 1)
    assert len(test_instance2.short_name) == MAX_SHORT_NAME_CHARS
    assert test_instance2.short_name == 'a' * MAX_SHORT_NAME_CHARS

    ## Test improper assignments
    # identifier
    with pytest.raises(ValueError, match=r'School\.identifier'):
        test_instance2.identifier = ''
    with pytest.raises(ValueError, match=r'School\.identifier'):
        test_instance2.identifier = 123

    # short_name
    with pytest.raises(ValueError, match=r'School\.short_name'):
        test_instance2.short_name = ''
    with pytest.raises(ValueError, match=r'School\.short_name'):
        test_instance2.short_name = 123

    # pretty_name
    with pytest.raises(ValueError, match=r'School\.pretty_name'):
        test_instance2.pretty_name = ''
    with pytest.raises(ValueError, match=r'School\.pretty_name'):
        test_instance2.pretty_name = 123

    # grade_points
    with pytest.raises(ValueError, match=r'School\.grade_pts'):
        test_instance2.grade_pts = ''
    with pytest.raises(ValueError, match=r'School\.grade_pts'):
        test_instance2.grade_pts = {123: 'abc'}

    # test add_grade_points
    test_instance1.add_grade_pts({'Z-': 67.0})
    assert 'Z-' in test_instance1.grade_pts
    assert test_instance1.grade_pts['Z-'] == 67.0
    with pytest.raises(ValueError, match=r'School\.add_grade_pts'):
        test_instance2.add_grade_pts('')
    with pytest.raises(ValueError, match=r'School\.add_grade_pts'):
        test_instance2.add_grade_pts({'a': 'b'})

    # test remove_grade_points
    test_instance1.remove_grade_pts(['Z-', 'not in dict'])
    assert 'Z-' not in test_instance1.grade_pts
    assert 67.0 not in test_instance1.grade_pts.values()
    with pytest.raises(ValueError, match=r'School\.remove_grade_pts'):
        test_instance2.remove_grade_pts('')
    with pytest.raises(ValueError, match=r'School\.remove_grade_pts'):
        test_instance2.remove_grade_pts([123])

    # Test deleting a school
    test_instance2_id = test_instance2.identifier
    del test_instance2
    assert test_instance2_id not in _school_ids
