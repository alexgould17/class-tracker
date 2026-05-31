from class_ import Class
from school import School
from collections.abc import Callable

grade_points = {
    'A+': 4.,   'A': 4.,    'A-': 3.67,
    'B+': 3.33, 'B': 3.,    'B-': 2.67,
    'C+': 2.33, 'C': 2.,    'C-': 1.67,
    'D+': 1.33, 'D': 1.,    'D-': 0.67,
    'F': 0
}


class Student:
    """Class representing a single student attending school.

    Current school is mandatory, everything else is optional (and intended for college/university vs. high school and lower)
    """
    _classes: list[Class]
    _school: School
    _major: str = ''
    _program: str = ''

    def __init__(self, school: School, *, major: str='', program: str= ''):
        """Creates a new Student.

        :param school string representing the name (short) of the school the Student currently attends
        :param major optional string representing the Student's major or field of study
        :param program optional string representing the Student's current instructional program or degree track
        """
        self._classes = []
        self._school = school
        self._major = major
        self._program = program

    def add_class(self, new_class: Class):
        """Adds a single class to the list of classes the Student has taken"""
        self._classes.append(new_class)

    def add_classes(self, class_list: list[Class]):
        """Adds a list of new classes to the Student's classes list"""
        for c in class_list:
            self.add_class(c)

    def calculate_gpa(self, filter_f: Callable[[Class], bool]=None) -> tuple[float, list[Class]]:
        """Calculates the Student's grade point average for all classes currently added.

        :param filter_f function that evaluates to False for any classes to skip, True for all to include in GPA calculation

        :returns gpa as a float, list of classes not used in calculations
        """
        total_grade_pts, total_credit_hrs, not_calcd = 0.0, 0, []
        for c in self._classes:
            if filter_f:
                if not filter_f(c):
                    not_calcd.append(c)
                    continue
            if c.grade in grade_points.keys():
                total_credit_hrs += c.hrs
                total_grade_pts += c.hrs * grade_points[c.grade]
            else:
                not_calcd.append(c)
        return total_grade_pts / total_credit_hrs, not_calcd

    def calculate_total_gpa(self) -> tuple[float, list[Class]]:
        """Calculates the Student's GPA excluding ongoing classes"""
        return self.calculate_gpa(lambda c: not c.ongoing)

    def calculate_predicted_gpa(self) -> tuple[float, list[Class]]:
        """Calculates the Student's GPA including ongoing classes"""
        return self.calculate_gpa()

    def calculate_filtered_gpa(self, *, include: list[str] | None, exclude: list[str] | None, use_ongoing: bool=False)\
            -> tuple[float, list[Class]]:
        """Calculates the Student's GPA using a custom filter

        :param include optional list of strings that each class must have all of in its tags to be included in calculations
        :param exclude optional list of strings that each class must have none of in its tags to be included in calculations
        :param use_ongoing boolean signifying whether ongoing classes should be used in calculations or not

        :returns same as calculate_gpa()
        """
        def filter_func(c: Class):
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
