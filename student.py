"""Contains the Student class."""
from collections.abc import Callable

from school import School
from school_class import Class


class Student:
    """class representing a single Student attending school.

    Attributes:
        classes: A list of Class instances the Student has taken, is taking, or will
            take.
        current_school: A School instance representing the school the Student currently
            attends.
        major: A string holding the Student's current major.
        program: A string holding the Student's current program of study.

    Raises:
        ValueError on any attribute assignment (including during initialization) that
        violates the above conditions.

    """

    _classes: list[Class]
    _current_school: School
    _major: str | None
    _program: str | None

    def __init__(
        self,
        current_school: School,
        major: str | None = None,
        program: str | None = None,
    ) -> None:
        """Create a new Student instance.

        Minimum attributes needed to correctly initialize: current_school.
        """
        self.classes = []
        self.current_school = current_school
        self.major = major
        self.program = program

    @property
    def classes(self) -> list[Class]:
        return self._classes

    @classes.setter
    def classes(self, value: list[Class]) -> None:
        if type(value) is not list:
            raise ValueError('School.classes must be a list.')
        for s in value:
            if type(s) is not str:
                raise ValueError('School.classes must be a list of strings.')
        self._classes = value

    @property
    def current_school(self) -> School:
        return self._current_school

    @current_school.setter
    def current_school(self, value: School) -> None:
        if type(value) is not School:
            raise ValueError('School.current_school must be a School instance.')
        self._current_school = value

    @property
    def major(self) -> str | None:
        return self._major

    @major.setter
    def major(self, value: str) -> None:
        if type(value) is not str and type(value) is not None:
            raise ValueError('School.major must be a string or None.')
        self._major = value

    @property
    def program(self) -> str | None:
        return self._program

    @program.setter
    def program(self, value: str) -> None:
        if type(value) is not str and type(value) is not None:
            raise ValueError('School.program must be a string or None.')
        self._program = value

    def add_class(self, new_class: Class) -> None:
        """Add a single class to the list of classes the Student has taken."""
        if type(new_class) is not Class:
            raise ValueError('Can only add a Class instance to School.classes.')
        self.classes.append(new_class)

    def add_classes(self, new_classes: list[Class]) -> None:
        """Add a list of new classes to the Student's classes list."""
        if type(new_classes) is not list:
            raise ValueError('Can only add Class instances to School.classes.')
        for c in new_classes:
            if type(c) is not Class:
                raise ValueError('Can only add a Class instance to School.classes.')
            self.add_class(c)

    def calculate_gpa(
        self, filter_func: Callable[[Class], bool] | None = None
    ) -> tuple[float, list[Class]]:
        """Calculate the Student's grade point average for all classes currently added.

        Args:
            filter_func: function that evaluates to False for any classes to skip, True
                for all to include in GPA calculation.

        Returns:
            A tuple containing gpa as an unrounded float, a list of classes not used in
            calculations.

        """
        if not callable(filter_func) and filter_func is not None:
            raise ValueError(
                'filter_func for calculate_gpa() must be callable or None.'
            )
        total_grade_pts, total_credit_hrs, not_calcd = 0.0, 0, []
        for cls in self._classes:
            if filter_func and not filter_func(cls):
                not_calcd.append(cls)
                continue
            if cls.grade in self.current_school.grade_pts:
                total_credit_hrs += cls.hrs
                total_grade_pts += cls.hrs * self.current_school.grade_pts[cls.grade]
            else:
                not_calcd.append(cls)
        return total_grade_pts / total_credit_hrs, not_calcd

    def calculate_total_gpa(self) -> tuple[float, list[Class]]:
        """Calculate the Student's GPA excluding ongoing classes."""
        return self.calculate_gpa(lambda c: not c.ongoing)

    def calculate_predicted_gpa(self) -> tuple[float, list[Class]]:
        """Calculate the Student's GPA including ongoing classes."""
        return self.calculate_gpa()

    def calculate_filtered_gpa(
        self,
        *,
        include: list[str] | None,
        exclude: list[str] | None,
        use_ongoing: bool = False,
    ) -> tuple[float, list[Class]]:
        """Calculate the Student's GPA using a custom filter.

        Args:
            include: An optional list of strings that each class must have all of in its
                tags to be included in calculations.
            exclude: An optional list of strings that each class must have none of in
                its tags to be included in calculations.
            use_ongoing: A boolean signifying whether ongoing classes should be used in
                calculations or not.

        Returns:
            A tuple containing gpa as an unrounded float, a list of classes not used in
            calculations.

        """

        def filter_func(c: Class) -> bool:
            if c.ongoing and not use_ongoing:
                return False
            if include:
                for tag in include:
                    if tag not in c.tags:
                        return False
            if exclude:
                for tag in exclude:
                    if tag in c.tags:
                        return False
            return True

        return self.calculate_gpa(filter_func)
