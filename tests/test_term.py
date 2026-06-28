"""Tests for the term.py module."""

import re

import pytest

from term import Term


def test_term(term_statics, term, rng) -> None:
    """Test creation, property assignment, and magic methods of Term class."""
    name_format, year_range, parts_of_year = term_statics
    test_instance1 = term

    # Test creation
    test_name = name_format.format(1)
    test_year = int(rng.integers(*year_range))
    test_part = parts_of_year[0]
    test_instance2 = Term(
        test_name, test_year, test_part, part_of_year_names=parts_of_year
    )
    assert test_instance2.name == test_name
    assert test_instance2.year == test_year
    assert test_instance2.part_of_year == test_part

    # Test property assignment
    new_name = name_format.format(2)
    new_year = int(rng.integers(*year_range))
    new_part = parts_of_year[1] if len(parts_of_year) > 1 else parts_of_year[0]
    test_instance2.name = new_name
    test_instance2.year = new_year
    test_instance2.part_of_year = new_part
    assert test_instance2.name == new_name
    assert test_instance2.year == new_year
    assert test_instance2.part_of_year == new_part

    # Test __str__
    term_str = str(test_instance1)
    assert isinstance(term_str, str)
    assert test_instance1.part_of_year[:2].upper() in term_str

    # Test __repr__
    term_repr = repr(test_instance1)
    assert isinstance(term_repr, str)
    assert test_instance1.part_of_year in term_repr

    # Test __eq__
    test_instance2 = Term(
        test_instance1.name,
        test_instance1.year,
        test_instance1.part_of_year,
        part_of_year_names=parts_of_year,
    )
    assert test_instance1 == test_instance2
    assert test_instance1 is not test_instance2
    test_instance2 = None
    with pytest.raises(
        ValueError,
        match=re.escape(
            'Term object can only be compared (==) to another Term object.'
        ),
    ):
        assert test_instance1 == test_instance2

    ## Test __lt__
    # test error from being passed incorrect type
    with pytest.raises(
        ValueError,
        match=re.escape('Term object can only be compared (<) to another Term object.'),
    ):
        assert test_instance1 < test_instance2
    test_instance2 = Term(
        test_instance1.name,
        test_instance1.year,
        parts_of_year[1],
        part_of_year_names=parts_of_year,
    )

    # should compare on index
    test_instance1.part_of_year = parts_of_year[0]
    assert test_instance1 < test_instance2

    # should compare on string val
    test_instance1.part_of_year, test_instance2.part_of_year = 'a', 'b'
    assert test_instance1 < test_instance2

    # Should compare on year
    test_instance2.year = test_instance1.year + 1
    assert test_instance1 < test_instance2

    ## Test improper assignments
    # name
    with pytest.raises(
        ValueError, match=re.escape('Term.name must be a non-empty string')
    ):
        test_instance2.name = ''
    with pytest.raises(
        ValueError, match=re.escape('Term.name must be a non-empty string')
    ):
        test_instance2.name = 1

    # year
    with pytest.raises(
        ValueError, match=re.escape('Term.year must be a non-negative integer.')
    ):
        test_instance2.year = -1
    with pytest.raises(
        ValueError, match=re.escape('Term.year must be a non-negative integer.')
    ):
        test_instance2.year = '1'

    # part_of_year
    with pytest.raises(
        ValueError, match=re.escape('Term.part_of_year must be a non-empty string.')
    ):
        test_instance2.part_of_year = ''
    with pytest.raises(
        ValueError, match=re.escape('Term.part_of_year must be a non-empty string.')
    ):
        test_instance2.part_of_year = 1

    # part_of_year_index
    with pytest.raises(
        ValueError, match=re.escape('Term.part_of_year_index must be an integer.')
    ):
        test_instance2.part_of_year_index = '1'

    # part_of_year_names
    with pytest.raises(
        ValueError,
        match=re.escape('Term.part_of_year_names must be a non-empty list.'),
    ):
        test_instance2.part_of_year_names = 'list'
    with pytest.raises(
        ValueError,
        match=re.escape('Term.part_of_year_names must be a non-empty list.'),
    ):
        test_instance2.part_of_year_names = []
    with pytest.raises(
        ValueError,
        match=re.escape('Term.part_of_year_names must be a list of non-empty strings.'),
    ):
        test_instance2.part_of_year_names = ['1', 2]
    with pytest.raises(
        ValueError,
        match=re.escape('Term.part_of_year_names must be a list of non-empty strings.'),
    ):
        test_instance2.part_of_year_names = ['1', '']
