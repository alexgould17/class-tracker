"""Tests for the assignment.py module."""

import pytest

from assignment import Assignment, sum_assignments, sum_assignments_by_category


def test_assignment(assign_statics, rng) -> None:
    """Test all facets of the Assignment class."""
    # Unpack statics
    (
        assign_cat_format,
        assign_name_format,
        assign_points_out_of,
        assign_points_earned_range,
    ) = assign_statics

    # Create two fake instances, initially identical
    rand_num = (
        assign_points_earned_range[1]
        - round(rng.random(), 2) * assign_points_earned_range[0]
    )
    test_instance1 = Assignment(
        assign_name_format.format(1),
        1,
        assign_cat_format.format(1),
        assign_points_out_of,
        rand_num,
    )
    test_instance2 = Assignment(
        assign_name_format.format(1),
        1,
        assign_cat_format.format(1),
        assign_points_out_of,
        rand_num,
    )

    # Test all assignments happened properly
    assert test_instance1.name == assign_name_format.format(1)
    assert test_instance1.number == 1
    assert test_instance1.category == assign_cat_format.format(1)
    assert test_instance1.points_out_of == assign_points_out_of
    assert test_instance1.points_earned >= assign_points_earned_range[0]
    assert test_instance1.points_earned < assign_points_earned_range[1]

    # Test __eq__
    assert test_instance1 == test_instance2
    with pytest.raises(ValueError, match=r'^Assignment.*'):
        assert test_instance1 == 1

    ## Test __lt__
    # basic
    test_instance2.number = 2
    assert test_instance1 < test_instance2

    # wrong value
    with pytest.raises(ValueError, match=r'^Assignment.*'):
        assert test_instance1 < 1

    # same number, different name
    test_instance2.number = 1
    test_instance2.name = assign_name_format.format(2)
    assert test_instance1 < test_instance2

    # same name, different category
    test_instance2.name = assign_name_format.format(1)
    test_instance2.category = assign_cat_format.format(2)
    assert test_instance1 < test_instance2

    # test __str__
    instance1_str = str(test_instance1)
    assert isinstance(instance1_str, str)
    assert test_instance1.category in instance1_str

    # Test __repr__
    instance1_repr = repr(test_instance1)
    assert isinstance(instance1_repr, str)
    assert test_instance1.name in instance1_repr

    ## Test improper assignments
    # name
    with pytest.raises(ValueError, match=r'Assignment.name must be a non-empty string'):
        test_instance2.name = ''
    with pytest.raises(ValueError, match=r'Assignment.name must be a non-empty string'):
        test_instance2.name = 1

    # number
    with pytest.raises(ValueError, match=r'Assignment.number must be an int'):
        test_instance2.number = '1'

    # category
    with pytest.raises(
        ValueError, match=r'Assignment.category must be a non-empty string'
    ):
        test_instance2.category = ''
    with pytest.raises(
        ValueError, match=r'Assignment.category must be a non-empty string'
    ):
        test_instance2.category = 1

    # points_earned
    with pytest.raises(
        ValueError, match=r'Assignment.points_earned must be a non-NaN float'
    ):
        test_instance2.points_earned = float('NaN')
    with pytest.raises(
        ValueError, match=r'Assignment.points_earned must be a non-NaN float'
    ):
        test_instance2.points_earned = '1.0'

    # points_out_of
    with pytest.raises(
        ValueError, match=r'Assignment.points_out_of must be a positive, non-NaN float'
    ):
        test_instance2.points_out_of = 0.0
    with pytest.raises(
        ValueError, match=r'Assignment.points_out_of must be a positive, non-NaN float'
    ):
        test_instance2.points_out_of = '1.0'
    with pytest.raises(
        ValueError, match=r'Assignment.points_out_of must be a positive, non-NaN float'
    ):
        test_instance2.points_out_of = float('NaN')


def test_sum_assignments(list_of_assignments, assign_statics) -> None:
    """Test the sum_assignments logic."""
    # Unpack statics
    (
        _assign_cat_format,
        _assign_name_format,
        assign_points_out_of,
        _assign_points_earned_range,
    ) = assign_statics

    # Get a list of mock assignments & sum the properties manually
    n, test_instances = list_of_assignments
    expected_points_earned = 0.0
    expected_points_out_of = n * assign_points_out_of
    for instance in test_instances:
        expected_points_earned += instance.points_earned

    # Run the method and compare the results
    return_val = sum_assignments(test_instances)
    assert isinstance(return_val, tuple)
    assert len(return_val) == 2
    actual_points_earned, actual_points_out_of = return_val
    assert isinstance(actual_points_earned, float)
    assert isinstance(actual_points_out_of, float)
    assert actual_points_earned == expected_points_earned
    assert actual_points_out_of == expected_points_out_of


def test_sum_assignments_by_category(list_of_assignments, assign_statics) -> None:
    """Test the sum_assignments_by_category logic."""
    # Unpack statics
    (
        assign_cat_format,
        _assign_name_format,
        assign_points_out_of,
        _assign_points_earned_range,
    ) = assign_statics

    # Get a list of mock assignments & split into two lists with different categories
    n, test_instances = list_of_assignments
    cat1_len, cat2_len = n // 2, n - n // 2
    category_1, category_2 = test_instances[:cat1_len], test_instances[cat1_len:]
    for instance in category_2:
        instance.category = assign_cat_format.format(2)

    # Calculate the expected values
    cat1_expected_points_earned, cat2_expected_points_earned = 0.0, 0.0
    cat1_expected_points_out_of = cat1_len * assign_points_out_of
    cat2_expected_points_out_of = cat2_len * assign_points_out_of
    for instance in category_1:
        cat1_expected_points_earned += instance.points_earned
    for instance in category_2:
        cat2_expected_points_earned += instance.points_earned

    # Run the method, validate the returned value
    return_val = sum_assignments_by_category(test_instances)
    assert isinstance(return_val, dict)
    assert len(return_val) == 2

    # Validate types and values for category 1
    return_val1 = return_val[category_1[0].category]
    assert isinstance(return_val1, tuple)
    assert len(return_val1) == 2
    cat1_actual_points_earned, cat1_actual_points_out_of = return_val1
    assert isinstance(cat1_actual_points_earned, float)
    assert isinstance(cat1_actual_points_out_of, float)
    assert cat1_actual_points_earned == cat1_expected_points_earned
    assert cat1_actual_points_out_of == cat1_expected_points_out_of

    # Validate types and values for category 2
    return_val2 = return_val[category_2[0].category]
    assert isinstance(return_val2, tuple)
    assert len(return_val2) == 2
    cat2_actual_points_earned, cat2_actual_points_out_of = return_val2
    assert isinstance(cat2_actual_points_earned, float)
    assert isinstance(cat2_actual_points_out_of, float)
    assert cat2_actual_points_earned == cat2_expected_points_earned
    assert cat2_actual_points_out_of == cat2_expected_points_out_of
