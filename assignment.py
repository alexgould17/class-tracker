"""Module representing a school assignment and all related methods."""

from math import isnan
from typing import Sequence


def sum_assignments(assignments: Sequence[Assignment]) -> tuple[float, float]:
    """Calculate the total points for each Assignment in a Sequence.

    Args:
        assignments: a Sequence of assignments to calculate the sum of

    Returns:
         A tuple with two floats: total points_earned, total points_out_of

    """
    total_earned = 0.0
    total_out_of = 0.0
    for assignment in assignments:
        total_earned += assignment.points_earned
        total_out_of += assignment.points_out_of
    return total_earned, total_out_of


def sum_assignments_by_category(
    assignments: list[Assignment],
) -> dict[str, tuple[float, float]]:
    """Calculate the total points for each Assignment in a Sequence by category.

    Args:
        assignments: a Sequence of assignments to calculate the sum of by category.

    Returns:
         A dict mapping each distinct category string found in an assignment in the
         Sequence to a tuple of floats of the type returned by sum_assignments().
         For example:

         {'HW':   (45.0, 50.0)
          'Quiz': (82.5, 100.0)
          'Lab':  (170.0, 200.0)}

    """
    # Use a dictionary to group assignments by category
    assigns_dict = {}
    for assign in assignments:
        if assign.category not in assigns_dict:
            assigns_dict[assign.category] = [assign]
        else:
            assigns_dict[assign.category].append(assign)

    # Loop over each category & calculate the sum of all assignments in that
    # category, then return the finished dictionary
    sums_dict = {}
    for category in assigns_dict:
        sums_dict[category] = sum_assignments(assigns_dict[category])
    return sums_dict


class Assignment:
    """class representing a single school assignment.

    This is a broad class that can represent anything turned in and/or taken for a
    grade. Examples include: exams, tests, quizzes, homework, projects, labs, papers,
    and so on. Each assignment is intended to belong to one specific Class instance.

    Attributes:
        name: A non-empty string representing the name of the specific assignment, for
            example, "Acid-Base Titration"
        number: An integer representing the number assignment this is. Should be unique
            amongst categories to allow sorting to behave well, but this is unenforced
            currently. For example, if there are 6 labs in a Term, and this is the
            second, the number would be 2.
        category: A non-empty string representing the category of assignments this
            Assignment belongs to. For example, "Lab", or "Exam". For grouping
            assignments in a sequence by category, this value is checked by
            case-sensitive equality to other strings.
        points_earned: A non-NaN float representing the number of points earned on this
            particular assignment, initialized to zero by default.
        points_out_of: A non-NaN, non-zero float representing the "maximum" number of
            achievable points on this assignment. Note that for extra credit purposes,
            the value of points_earned may exceed this value.

    Raises:
        ValueError on any attribute assignment (including during initialization) that
        violates the above conditions.

    """

    _name: str
    _number: int
    _category: str
    _points_earned: float
    _points_out_of: float


    def __init__(
        self,
        name: str,
        number: int,
        category: str,
        points_out_of: float = 1.0,
        points_earned: float = 0.0,
    ) -> None:
        """Create a new Assignment object based on the provided values.

        Minimum required attributes for successful creation: name, number, category.
        """
        self.name = name
        self.number = number
        self.category = category
        self.points_out_of = points_out_of
        self.points_earned = points_earned

    def __lt__(self, other: Assignment) -> bool:
        """Compare two Assignments by category first, then name, then number.

        Comparison of category is lexicographic.

        Raises:
            ValueError if either self or other is not an Assignment object.

        """
        if type(self) is not Assignment and type(other) is not Assignment:
            raise ValueError('Assignment cannot be compared to a non-Assignment object')
        if self.category != other.category:
            return self.category < other.category
        if self.name != other.name:
            return self.name < other.name
        return self.number < other.number

    def __eq__(self, other: Assignment) -> bool:
        """Return true iff both Assignments have the same category, name, and number.

        Raises:
            ValueError if either self or other is not an Assignment object.

        """
        if type(self) is not Assignment and type(other) is not Assignment:
            raise ValueError('Assignment cannot be compared to a non-Assignment object')

        # number compared first because integer comparisons are faster than strings,
        # and `and` can be short-circuited on evaluating to False
        return (
            self.number == other.number
            and self.name == other.name
            and self.category == other.category
        )

    def __str__(self) -> str:
        """Return a short string of the form 'category number'."""
        return f'{self.category} {self.number}: {self.name}'

    def __repr__(self) -> str:
        """Return a string of the form 'category #humber: name'."""
        return f'{self.category} #{self.number}: {self.name}'

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if value == '' or type(value) is not str:
            raise ValueError('Assignment.name must be a non-empty string')
        self._name = value

    @property
    def number(self) -> int:
        return self._number

    @number.setter
    def number(self, value: int) -> None:
        if type(value) is not int:
            raise ValueError('Assignment.number must be an int')
        self._number = value

    @property
    def category(self) -> str:
        return self._category

    @category.setter
    def category(self, value: str) -> None:
        if value == '' or type(value) is not str:
            raise ValueError('Assignment.category must be a non-empty string')
        self._category = value

    @property
    def points_earned(self) -> float:
        return self._points_earned

    @points_earned.setter
    def points_earned(self, value: float) -> None:
        if isnan(value) or type(value) is not float:
            raise ValueError('Assignment.points_earned must be a non-NaN float')
        self._points_earned = value

    @property
    def points_out_of(self) -> float:
        return self._points_out_of

    @points_out_of.setter
    def points_out_of(self, value: float) -> None:
        if value <= 0.0 or type(value) is not float or isnan(value):
            raise ValueError(
                'Assignment.points_out_of must be a non-negative, non-NaN float'
            )
        self._points_out_of = value
