"""Tests classes and methods in the utilities module."""

import pytest

from utilities import AlreadyExistsError, CyclicalError


def test_error_classes() -> None:
    """Test error creation and raising."""
    # Create errors
    ae_error = AlreadyExistsError('ae test')
    cyc_error = CyclicalError('cyc test')

    # Test values and raising
    assert ae_error.args[0] == 'ae test'
    assert cyc_error.args[0] == 'cyc test'
    with pytest.raises(AlreadyExistsError):
        raise ae_error
    with pytest.raises(CyclicalError):
        raise cyc_error
