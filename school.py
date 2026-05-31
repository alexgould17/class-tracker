from utilities import AlreadyExistsError

default_grade_points = {
    'A+': 4.,   'A': 4.,    'A-': 3.67,
    'B+': 3.33, 'B': 3.,    'B-': 2.67,
    'C+': 2.33, 'C': 2.,    'C-': 1.67,
    'D+': 1.33, 'D': 1.,    'D-': 0.67,
    'F': 0
}

class School:
    """Class that represents a School attended by a Student.

    _identifier: a string that uniquely identifies the school, e.g. UIUC
    short_name: a short [15 chars or less] way of referring to the school, e.g. Illinois
    pretty_name: the full, long name, e.g. University of Illinois at Urbana-Champaign
    """

    _grade_pts: dict[str, float]
    _identifier: str
    short_name: str = ''
    pretty_name: str = ''

    max_short_name_chars = 15
    school_ids = []

    def __init__(self, identifier: str, short_name: str='', pretty_name: str='',
                 grade_pts: dict[str, float]=default_grade_points):
        self.set_identifier(identifier)
        self.short_name = short_name[:School.max_short_name_chars]
        self.pretty_name = pretty_name
        self._grade_pts = {'': 0}
        self.add_grade_points(grade_pts)

    def set_identifier(self, identifier: str):
        """Validates identifier to be non-empty and unique to this application instance"""

        if identifier in School.school_ids:
            raise AlreadyExistsError('School already exists with identifier: ' + identifier)
        elif identifier == '':
            raise ValueError('identifier cannot be empty')
        else:
            School.school_ids.append(identifier)
        self._identifier = identifier

    def get_identifier(self) -> str:
        return self._identifier

    def add_grade_points(self, grade_pts: dict[str, float]):
        """Copies all key-value pairs in the passed dictionary into the _grade_pts dict"""

        for k, v in grade_pts.items():
            self._grade_pts[k] = v

    def remove_grade_points(self, grades: list[str]):
        """Removes all grades in the passed list from the _grade_pts dictionary if they exist"""

        for g in grades:
            if g in self._grade_pts.keys():
                del self._grade_pts[g]

    def reset_grade_points(self):
        """Resets the _grade_pts dict to an empty one with only the sentinel value '': 0"""

        self._grade_pts = {'': 0}

    def get_grade_points(self) -> dict[str, float]:
        """Returns a copy of the grade points dict (to prevent modification)"""

        return self._grade_pts.copy()

    def __eq__(self, other: School):
        """Compares the identifier strings lexicographically"""

        return self._identifier == other._identifier

    def __lt__(self, other: School):
        """Compares the identifier strings lexicographically"""

        return self._identifier < other._identifier
