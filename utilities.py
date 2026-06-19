"""Exceptions & common functions used across modules."""
class CyclicalError(Exception):
    """Error representing a cycle in a graph that should be acyclical."""

    def __init__(self, msg: str) -> None:  # noqa: D107
        super().__init__(msg)


class AlreadyExistsError(Exception):
    """Error representing creation of a duplicate equivalent instance of a class."""

    def __init__(self, msg: str) -> None:  # noqa: D107
        super().__init__(msg)
