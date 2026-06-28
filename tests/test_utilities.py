"""Tests classes and methods in the utilities module."""

import pytest

from utilities import AlreadyExistsError, CyclicalError


def test_error_classes() -> None:
    """Test error creation and raising."""
    # Create errors
    ae_error = AlreadyExistsError('ae test')
    cyc_error = CyclicalError('cyc test')

    # Test values and raising
    with pytest.raises(AlreadyExistsError, match='ae test'):
        raise ae_error
    with pytest.raises(CyclicalError, match='cyc test'):
        raise cyc_error
