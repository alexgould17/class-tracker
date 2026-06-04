from __future__ import annotations

import re
import string

from assignment import Assignment
from school import School
from term import Term
from utilities import CyclicalError


class Class:
    """class representing a single Class that a user takes in school."""

    _dept: str
    _number: int
    _short_desc: str
    _description: str
    _grade: str = ''
    _hrs: int
    _term: Term
    _school: School
    _tags: list[str]
    _ongoing: bool = False
    _assignments: list[Assignment]
    _assign_cats: list[str]
    _prereqs: list[Class]
    _postreqs: list[Class]

    grade_pattern = re.compile('[A-Z][+-]?')

    def __init__(
        self, dept: str, number: int, hrs: int, term: Term, school: School, *,
        tags: list[str], ongoing: bool = False, grade: str = '', short_desc: str = '', description: str = '',
    ):
        self.number = number
        self.dept = dept
        self.grade = grade[:2]
        self.hrs = hrs
        self.school = school
        if tags:
            self._tags = tags
        else:
            self._tags = []
        self.ongoing = ongoing
        if grade:
            self.grade = grade
        self._assignments = []
        self._assign_cats = []
        self._prereqs = []
        self._postreqs = []
        self.term = term
        self.short_desc = short_desc
        self.description = description

    @property
    def dept(self) -> str:
        return self._dept

    @dept.setter
    def dept(self, value: str) -> None:
        if type(value) is not str or value == '':
            raise ValueError('Class.dept must be a non-empty string')
        self._dept = value

    @property
    def number(self) -> int:
        return self._number

    @number.setter
    def number(self, value: int) -> None:
        if type(value) is not int:
            raise ValueError('Class.number must be an int')
        self._number = value

    @property
    def short_desc(self) -> str:
        return self._short_desc

    @short_desc.setter
    def short_desc(self, value: str) -> None:
        if type(value) is not str:
            raise ValueError('Class.short_desc must be a string')
        self._short_desc = value

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, value: str) -> None:
        if type(value) is not str:
            raise ValueError('Class.description must be a string')
        self._description = value

    @property
    def grade(self) -> str:
        return self._grade

    @grade.setter
    def grade(self, value: str) -> None:
        if type(value) is not str or not re.match(Class.grade_pattern, value):
            raise ValueError(f'Class.grade must be a string of format "{Class.grade_pattern.pattern}"')
        self._grade = value[:2]

    @property
    def hrs(self) -> int:
        return self._hrs

    @hrs.setter
    def hrs(self, value: int) -> None:
        if type(value) is not int:
            raise ValueError('Class.hrs must be an int')
        self._hrs = value

    @property
    def term(self) -> Term:
        return self._term

    @term.setter
    def term(self, value: Term) -> None:
        if type(value) is not Term:
            raise ValueError('Class.term must be a Term')
        self._term = value

    @property
    def school(self) -> School:
        return self._school

    @school.setter
    def school(self, value: School) -> None:
        if type(value) is not School:
            raise ValueError('Class.school must be a School')
        self._school = value

    @property
    def ongoing(self) -> bool:
        return self._ongoing

    @ongoing.setter
    def ongoing(self, value: bool) -> None:
        if type(value) is not bool:
            raise ValueError('Class.ongoing must be a bool')
        self._ongoing = value

    def add_prereq(self, c: Class) -> None:
        """Adds a Class as a prerequisite of this Class, i.e., the added Class must be taken before this Class"""

        if c in self._postreqs:
            raise CyclicalError('Cannot add a class to the prerequisites that is already a postrequisite')
        else:
            self._prereqs.append(c)

    def add_postreq(self, c: Class) -> None:
        """Adds a Class as a postrequisite of this Class, i.e., the added Class must be taken after this Class"""

        if c in self._prereqs:
            raise CyclicalError('Cannot add a class to the postrequisites that is already a prerequisite')
        else:
            self._postreqs.append(c)

    def term_sort_key(self) -> tuple[Term, str, int]:
        return self.term, self.dept, self.number

    def to_transcript_line(self) -> str:
        """Prints the class dept, number, short_desc, hours & grade to a single-line, fixed-width string"""
        numstr = str(self.number)
        strs = [self.dept, ' '*(5-len(self.dept)), numstr, ' '*(5-len(numstr)), self.short_desc[:25], f'   {self.hrs:1}.00   ', self.grade, ' '*(3-len(self.grade))]
        return ''.join(strs)

    def __lt__(self, other: Class):
        """Default ordering. Compares by dept first, then number, then year, then semester"""

        if self.dept != other.dept:
            return self.dept < other.dept
        elif self.number != other.number:
            return self.number < other.number
        else:
            return self.term < other.term

    def __eq__(self, other: Class):
        """Two Classes are equal iff their dept string and class number are the same."""

        return self.dept == other.dept and self.number == other.number

    def __str__(self):
        """Returns a simple string with the dept & number"""
        return f'{self.dept} {self.number}'

    def __repr__(self):
        """Returns a slightly more detailed string with the dept, number & short_desc"""
        return f'{self.dept} {self.number}: {self.short_desc}'
