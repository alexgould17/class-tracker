"""Tests for the school.py module."""

import pytest

from school import DEFAULT_GRADE_POINTS, MAX_SHORT_NAME_CHARS, School, _school_ids
from utilities import AlreadyExistsError


@pytest.mark.usefixtures("rand_str", "rng", "school_statics", "school")
class TestSchool:
    """Class to hold all the tests for the School class."""

    def test_init_minimum(self, rand_str) -> None:
        """Test the constructor with minimum variables provided"""

        # Minimum constructor
        identifier, short_name = rand_str(), rand_str()
        test_instance1 = School(
            identifier=identifier,
            short_name=short_name
        )

        # Test all values
        assert test_instance1._identifier == identifier
        assert test_instance1._short_name == short_name
        assert test_instance1._pretty_name == ''
        assert test_instance1._grade_pts == DEFAULT_GRADE_POINTS

    def test_init_maximum(self, rand_str, rng) -> None:
        """Test the constructor with all variables provided"""

        # Minimum constructor
        identifier, short_name, pretty_name = rand_str(), rand_str(), rand_str()
        grade_pt = float(rng.random()) + 4.0
        grade_pts = {'Z++': grade_pt}
        test_instance1 = School(
            identifier=identifier,
            short_name=short_name,
            pretty_name=pretty_name,
            grade_pts=grade_pts,
        )

        # Test all scalar values
        assert test_instance1._identifier == identifier
        assert test_instance1._short_name == short_name
        assert test_instance1._pretty_name == pretty_name

        # Test all grade points values
        assert 'Z++' in test_instance1._grade_pts
        assert test_instance1._grade_pts['Z++'] == grade_pt
        for grade in DEFAULT_GRADE_POINTS:
            assert grade not in test_instance1._grade_pts

    def test_eq(self, rand_str) -> None:
        """Test the __eq__ method for success, failure, and errors."""

        # Create two classes with identical short_ and pretty_names
        identifier1, identifier2 = rand_str(), rand_str()
        short_name, pretty_name = rand_str(), rand_str()
        test_instance1 = School(
            identifier=identifier1,
            short_name=short_name,
        )
        test_instance2 = School(
            identifier=identifier2,
            short_name=short_name,
        )

        # Compare
        assert test_instance1 == test_instance2

        # Change the pretty_name of one school and test for non-equality
        test_instance2.pretty_name = pretty_name
        assert not test_instance1 == test_instance2

        # Change the short_name of one school and test for non-equality
        test_instance2.pretty_name = test_instance1.pretty_name
        test_instance2.short_name = short_name[:-1]
        assert not test_instance1 == test_instance2

        # Test comparison to non-School
        with pytest.raises(ValueError, match=r'Class object'):
            assert test_instance1 == 1

    def test_lt(self, rand_str) -> None:
        """Test the __lt__ method for success, failure, and errors."""

        # Create two classes with identical short_ and pretty_names
        identifier1, identifier2 = rand_str(), rand_str()
        short_name_a, short_name_b = 'a', 'b'
        pretty_name_a, pretty_name_b = 'A', 'B'
        test_instance1 = School(
            identifier=identifier1,
            short_name=short_name_a,
            pretty_name=pretty_name_a,
        )
        test_instance2 = School(
            identifier=identifier2,
            short_name=short_name_a,
            pretty_name=pretty_name_a,
        )

        # Compare
        assert not test_instance1 < test_instance2

        # Change the pretty_name of one school and test < for success
        test_instance2.pretty_name = pretty_name_b
        assert test_instance1 < test_instance2

        # Change the short_name of one school and test < for success
        test_instance2.short_name = short_name_b
        assert test_instance1 < test_instance2

        # Test comparison to non-School
        with pytest.raises(ValueError, match=r'Class object'):
            assert test_instance1 < 1

    def test_school_ids(self, rand_str) -> None:
        """Test that creation puts a School's id in the global pool and deletion removes it."""

        # Create a school
        identifier, short_name = rand_str(), rand_str()
        _test_instance1 = School(
            identifier=identifier,
            short_name=short_name
        )

        # Make sure its id is in the global pool
        assert identifier in _school_ids

        # Try to create a second school with the same id & make sure it raises an error
        with pytest.raises(AlreadyExistsError, match=r'already exists'):
            _test_instance2 = School(
                identifier=identifier,
                short_name=short_name
            )

        # Delete it and make sure the id was removed
        del _test_instance1
        assert identifier not in _school_ids

    def test_rest(self, school_statics, school) -> None:
        """Test the rest of the School class methods."""
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
