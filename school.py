"""Module containing the School class and its default values."""

from utilities import AlreadyExistsError

MAX_SHORT_NAME_CHARS = 15
DEFAULT_GRADE_POINTS = {
    'A+': 4.0,
    'A': 4.0,
    'A-': 3.67,
    'B+': 3.33,
    'B': 3.0,
    'B-': 2.67,
    'C+': 2.33,
    'C': 2.0,
    'C-': 1.67,
    'D+': 1.33,
    'D': 1.0,
    'D-': 0.67,
    'F': 0,
}

__school_ids = set()


class School:
    """Represents a single School attended by a Student.

    Enforces a unique identifier for all School instances created within the program.

    Attributes:
        identifier: A string (unenforced length) that uniquely identifies the school.
            For example, UIUC
        short_name: A short string (truncated to 15 chars) representing the School name.
            For example, Illinois
        pretty_name: A string representing the full, long name of a School. For example,
            University of Illinois at Urbana-Champaign
        grade_pts: A dictionary mapping strings representing grades to the number of
            grade points each is worth as a float. See the module-level global default
            for an example. Individual grade points can be added or removed from the
            dict using the helper methods.

    Raises:
        ValueError on any attribute assignment (including during initialization) that
        violates the above conditions.
        AlreadyExistsError when trying to add a School with an identifier that matches
        that of an existing School instance.

    """

    _grade_pts: dict[str, float]
    _identifier: str
    _short_name: str
    _pretty_name: str

    def __init__(
        self,
        identifier: str,
        short_name: str = '',
        pretty_name: str = '',
        grade_pts: dict[str, float] | None = None,
    ) -> None:
        """Create a new School object.

        Minimum required attributes for successful creation: identifier
        """
        self.identifier = identifier
        self.short_name = short_name
        self.pretty_name = pretty_name
        self.grade_pts = grade_pts if grade_pts else DEFAULT_GRADE_POINTS.copy()

    @property
    def identifier(self) -> str:
        return self._identifier

    @identifier.setter
    def identifier(self, value: str) -> None:
        global __school_ids
        if value in __school_ids:
            raise AlreadyExistsError(f'School already exists with identifier: {value}.')
        if type(value) is not str or value == '':
            raise ValueError('School.identifier must be a non-empty string.')
        __school_ids.add(value)
        self._identifier = value

    @property
    def short_name(self) -> str:
        return self._short_name

    @short_name.setter
    def short_name(self, value: str) -> None:
        if value == '' or type(value) is not str:
            raise ValueError('School.short_name must be a non-empty string.')
        self._short_name = value[:MAX_SHORT_NAME_CHARS]

    @property
    def pretty_name(self) -> str:
        return self._pretty_name

    @pretty_name.setter
    def pretty_name(self, value: str) -> None:
        if value == '' or type(value) is not str:
            raise ValueError('School.pretty_name must be a non-empty string.')
        self._pretty_name = value

    @property
    def grade_pts(self) -> dict[str, float]:
        return self._grade_pts

    @grade_pts.setter
    def grade_pts(self, value: dict[str, float]) -> None:
        if type(value) is not dict:
            raise ValueError('School.grade_pts must be a dictionary.')
        for k, v in value.items():
            if type(k) is not str or type(v) is not float:
                raise ValueError(
                    'Each key/value pair in School.grade_points() must be a string '
                    '& a float, respectively.'
                )
        self._grade_pts = value

    def add_grade_points(self, grade_pts: dict[str, float]) -> None:
        """Copy all key-value pairs in the dict arg into the grade_pts dict."""
        if type(grade_pts) is not dict:
            raise ValueError(
                'The grade_pts passed to School.add_grade_points() must be a dict.'
            )
        for k, v in grade_pts.items():
            if type(k) is not str or type(v) is not float:
                raise ValueError(
                    'Each key/value pair passed to School.add_grade_points() must be '
                    'a string & a float, respectively.'
                )
            self._grade_pts[k] = v

    def remove_grade_points(self, grades: list[str]) -> None:
        """Remove all grades in the list arg from the grade_pts dict if they exist."""
        if type(grades) is not list:
            raise ValueError(
                'The grades passed to School.remove_grade_points() must be a list.'
            )
        for g in grades:
            if type(g) is not str:
                raise ValueError(
                    'Any grade removed from the School.grade_pts dict must be a string.'
                )
            if g in self._grade_pts:
                del self._grade_pts[g]

    def __eq__(self, other: School) -> bool:
        """Compare the identifier strings lexicographically."""
        return self._identifier == other._identifier

    def __lt__(self, other: School) -> bool:
        """Compare the identifier strings lexicographically."""
        return self._identifier < other._identifier

    def __del__(self) -> None:
        global __school_ids
        __school_ids.remove(self.identifier)
