"""Tests for the assignment.py module."""

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
    rand_num = assign_points_earned_range[1]\
        - round(rng.random(), 2) * assign_points_earned_range[0]
    test_instance1 = Assignment(
        assign_name_format.format(1),
        1,
        assign_cat_format.format(1),
        assign_points_out_of,
        rand_num
    )
    test_instance2 = Assignment(
        assign_name_format.format(1),
        1,
        assign_cat_format.format(1),
        assign_points_out_of,
        rand_num
    )

    # Test all assignments happened properly
    assert test_instance1.name == assign_name_format.format(1)
    assert test_instance1.number == 1
    assert test_instance1.category == assign_cat_format.format(1)
    assert test_instance1.points_out_of == assign_points_out_of
    assert test_instance1.points_earned >= assign_points_earned_range[0]
    assert test_instance1.points_earned < assign_points_earned_range[1]

    # Test magic methods
    assert test_instance1 == test_instance2
    test_instance2.number = 2
    assert test_instance1 < test_instance2
    test_instance2.number = 1
    test_instance2.name = assign_name_format.format(2)
    assert test_instance1 < test_instance2
    test_instance2.name = assign_name_format.format(1)
    test_instance2.category = assign_cat_format.format(2)
    assert test_instance1 < test_instance2
    assert isinstance(str(test_instance1), str)
    assert isinstance(repr(test_instance1), str)

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
    expected_points_earned = 0.
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
        assign_points_earned_range,
    ) = assign_statics

    # Get a list of mock assignments & split into two lists with different categories
    n, test_instances = list_of_assignments
    cat1_len, cat2_len = n//2, n - n//2
    category_1, category_2 = test_instances[:cat1_len], test_instances[cat1_len:]
    for instance in category_2:
        instance.category = assign_cat_format.format(2)

    # TODO:Run the method, validate the results tuple
