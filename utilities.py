class CyclicalError(Exception):
    """Error representing a cycle in a graph that should be acyclical."""
    def __init__(self, msg: str):
        super(msg)


class AlreadyExistsError(Exception):
    """Error representing a duplicate creation of an object that shouldn't have duplicates."""
    def __init__(self, msg: str):
        super(msg)
