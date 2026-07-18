"""Module containing the School class and its default values."""

from utilities import AlreadyExistsError

MAX_SHORT_NAME_CHARS: int = 15
DEFAULT_GRADE_POINTS: dict[str, float] = {
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
    'F': 0.0,
}

_school_ids: set[str] = set()


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
        short_name: str,
        pretty_name: str = '',
        grade_pts: dict[str, float] | None = None,
    ) -> None:
        """Create a new School object.

        Minimum required attributes for successful creation: identifier
        """
        self.identifier = identifier
        self.short_name = short_name
        self.pretty_name = pretty_name
        self.grade_pts = grade_pts.copy() if grade_pts else DEFAULT_GRADE_POINTS.copy()

    def __eq__(self, other: School) -> bool:
        """Compare short_name and pretty_name lexicographically."""
        if not isinstance(other, School):
            raise ValueError(
                'School object can only be compared (==) to another Class object.'
            )
        return (
            self._short_name == other._short_name
            and self._pretty_name == other._pretty_name
        )

    def __lt__(self, other: School) -> bool:
        """Compare short_name then pretty_name lexicographically."""
        if not isinstance(other, School):
            raise ValueError(
                'School object can only be compared (<) to another Class object.'
            )
        if self._short_name == other._short_name:
            return self._pretty_name < other._pretty_name
        return self._short_name < other._short_name

    def __del__(self) -> None:
        """Remove id from the global id's list on deletion."""
        global _school_ids
        _school_ids.remove(self.identifier)

    @property
    def identifier(self) -> str:
        return self._identifier

    @identifier.setter
    def identifier(self, value: str) -> None:
        global _school_ids
        if value in _school_ids:
            raise AlreadyExistsError(f'School already exists with identifier: {value}.')
        if not isinstance(value, str) or value == '':
            raise ValueError('School.identifier must be a non-empty string.')
        _school_ids.add(value)
        self._identifier = value

    @property
    def short_name(self) -> str:
        return self._short_name

    @short_name.setter
    def short_name(self, value: str) -> None:
        if value == '' or not isinstance(value, str):
            raise ValueError('School.short_name must be a non-empty string.')
        self._short_name = value[:MAX_SHORT_NAME_CHARS]

    @property
    def pretty_name(self) -> str:
        return self._pretty_name

    @pretty_name.setter
    def pretty_name(self, value: str) -> None:
        if not isinstance(value, str):
            raise ValueError('School.pretty_name must be a non-empty string.')
        self._pretty_name = value

    @property
    def grade_pts(self) -> dict[str, float]:
        return self._grade_pts

    @grade_pts.setter
    def grade_pts(self, value: dict[str, float]) -> None:
        if not isinstance(value, dict):
            raise ValueError('School.grade_pts must be a dictionary.')
        for k, v in value.items():
            if not (isinstance(k, str) and isinstance(v, float)):
                raise ValueError(
                    'Each key/value pair in School.grade_pts must be a string '
                    '& a float, respectively.'
                )
        self._grade_pts = value

    def add_grade_pts(self, grade_pts: dict[str, float]) -> None:
        """Copy all key-value pairs in the dict arg into the grade_pts dict.

        Overrides any existing keys.
        """
        if not isinstance(grade_pts, dict):
            raise ValueError(
                'The grade_pts passed to School.add_grade_pts() must be a dict.'
            )
        for k, v in grade_pts.items():
            if not (isinstance(k, str) and isinstance(v, float)):
                raise ValueError(
                    'Each key/value pair passed to School.add_grade_pts() must be '
                    'a string & a float, respectively.'
                )
            self._grade_pts[k] = v

    def remove_grade_pts(self, grades: list[str]) -> None:
        """Remove all grades in the list arg from the grade_pts dict if they exist."""
        if not isinstance(grades, list):
            raise ValueError(
                'The grades passed to School.remove_grade_pts() must be a list.'
            )
        for g in grades:
            if not isinstance(g, str):
                raise ValueError(
                    'Any grade passed to School.remove_grade_pts() must be a string.'
                )
            if g in self._grade_pts:
                del self._grade_pts[g]
