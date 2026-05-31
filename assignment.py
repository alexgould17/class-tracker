from math import isnan


class Assignment:
    """class representing a single school assignment.

    Has a name, number, category, points earned, points out of, and belongs to a Class."""
    _name: str
    _number: int
    _category: str
    _points_earned: float
    _points_out_of: float
    
    @staticmethod
    def sum_assignments(assignments: list[Assignment]) -> tuple[float, float]:
        """Calculates the total points_earned & total points_out_of for a list of assignments.
        
        :param assignments list of assignments to calculate the sum of
        :returns a tuple with the total points_earned, total points_out_of
        """
        total_earned = 0.0
        total_out_of = 0.0
        for assignment in assignments:
            total_earned += assignment.points_earned
            total_out_of += assignment.points_out_of
        return total_earned, total_out_of

    @staticmethod
    def sum_assignments_by_category(assignments: list[Assignment]) -> dict[str, tuple[float, float]]:
        """Calculates the total points_earned & total points_out_of for a list of assignments, breaking them out by category.

        :param assignments list of assignments to calculate the sum of
        :returns a dictionary with category str's as keys and tuples with the total points_earned, total points_out_of as values
        """

        # Use a dictionary to group assignments by category
        assigns_dict = {}
        for assign in assignments:
            if assign.category not in assigns_dict.keys():
                assigns_dict[assign.category] = [assign]
            else:
                assigns_dict[assign.category].append(assign)

        # Loop over each category & calculate the sum of all assignments in that category, then return the finished dictionary
        sums_dict = {}
        for category in assigns_dict.keys():
            sums_dict[category] = Assignment.sum_assignments(assigns_dict[category])
        return sums_dict

    def __init__(self, name: str, number: int, category: str, points_out_of: float = 1.0, points_earned: float = 0.0) -> None:
        self.name = name
        self.number = number
        self.category = category
        self.points_out_of = points_out_of
        self.points_earned = points_earned

    def __lt__(self, other: Assignment) -> bool:
        """Compares two Assignments lexicographically by category first, then name, then number."""
        if type(other) is not Assignment:
            raise ValueError('Assignment cannot be compared to a non-Assignment object')
        if self.category != other.category:
            return self.category < other.category
        elif self.name != other.name:
            return self.name < other.name
        return self.number < other.number

    def __eq__(self, other: Assignment) -> bool:
        """Returns true iff both Assignments have the same category, name, and number."""
        if type(other) is not Assignment:
            raise ValueError('Assignment cannot be compared to a non-Assignment object')

        # Number is compared first because it is O(1) and `and` will short circuit if it fails.
        return self.number == other.number and self.name == other.name and self.category == other.category

    def __str__(self) -> str:
        """Returns a string with all the assignment info minus the scores."""
        return f'{self.category} - {self.name} {self.number}'

    def __repr__(self) -> str:
        """Returns a string with all the assignment info including the scores and a percent score, formatted neatly."""
        return f'{self.category} - {self.name} {self.number}: {self.points_earned:.2f}/ {self.points_out_of:.2f}, {self.points_earned/self.points_out_of:.2%}'

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
            raise ValueError('Assignment.points_out_of must be a non-negative, non-NaN float')
        self._points_out_of = value
