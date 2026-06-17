"""Module containing the Class class, which represents a class taken at school."""
from __future__ import annotations

import re

from assignment import Assignment
from school import School
from term import Term
from utilities import CyclicalError


class Class:
    """class representing a single Class that a user takes in school.

    Attributes:
        dept: A string representing the department, college, etc. a Class belongs to. For example: 'English'.
        number: An integer representing the class number, mostly relevant for college/university classes. For example: 101.
        short_desc: A short (truncated at 25 chars) string containing a brief description of the Class. For example: 'Intro to American Lit.'.
        description: A longer (not truncated) string allowing for a neater description of the Class. For example: 'Introduction to American Literature'.
        grade: A two-character string that represents the letter grade achieved in this class. Existence of a letter grade implies a completed Class. The first
        character should be the letter, always capital. The second, optional character, must be either a '+' or a '-'. For example: 'A-' or 'I'.
        hrs: An integer indicating the number of credit hours obtained from a class. Should be 1 if all classes at an institution count for the same credit
        per term.
        term: A Term object representing when the Class was taken. Enables sorting and grouping. For example: Term('semester', 2026, 'Spring')
        school: A School object representing the institution the Class was taken at. For example: School('UIUC')
        tags: A list of strings used to filter and categorize Classes. Can be empty at any point. The primary use for tags is for calculating different
        GPA's or program/degree requirements. For example: adding the tag 'major' to certain classes but not others will allow you to easily calculate your major GPA.
        ongoing: A boolean indicating whether the Class is currently ongoing/in progress or not. Gets set to False when a letter grade is assigned.
        assignments: List of Assignment objects belonging to this Class.
        assign_cats: List of categories of Assignments for this Class. For example: ['HW', 'Quiz', 'Lab']
        prereqs: List of Classes that must be taken before this Class can be taken. Will be refactored out to different logic eventually.
        postreqs: List of Classes that this Class is a potential prerequisite for. Will be refactored out to different logic eventually.

    Raises:
        ValueError on any attribute assignment (including during initialization) that violates the above conditions.
    """

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
        tags: list[str] | None, ongoing: bool = False, grade: str = '', short_desc: str = '', description: str = '',
    ):
        """Initializes a new Class object including generating empty lists for appropriate attributes.

        Minimum attributes needed to correctly initialize: dept, number, hrs, term, school.
        """
        self.number = number
        self.dept = dept
        self.grade = grade
        self.hrs = hrs
        self.school = school
        if tags:
            self.tags = tags
        else:
            self.tags = []
        self.ongoing = ongoing
        if grade:
            self.grade = grade
        self.assignments = []
        self.assign_cats = []
        self.prereqs = []
        self.postreqs = []
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
        self._short_desc = value[:25]

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
        if value != 'I':
            self.ongoing = False # If we have a letter grade (except 'I' for incomplete), the class is not ongoing.

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

    @property
    def tags(self) -> list[str]:
        return self._tags

    @tags.setter
    def tags(self, value: list[str]) -> None:
        if type(value) is not list:
            raise ValueError('Class.tags must be a list')
        for s in value:
            if type(s) is not str:
                raise ValueError('Class.tags must be a list of strings')
        self._tags = value

    @property
    def assignments(self) -> list[Assignment]:
        return self._assignments

    @assignments.setter
    def assignments(self, value: list[Assignment]) -> None:
        if type(value) is not list:
            raise ValueError('Class.assignments must be a list')
        for a in value:
            if type(a) is not Assignment:
                raise ValueError('Class.tags must be a list of Assignments')
        self._assignments = value

    @property
    def assign_cats(self) -> list[str]:
        return self._assign_cats

    @assign_cats.setter
    def assign_cats(self, value: list[str]) -> None:
        if type(value) is not list:
            raise ValueError('Class.assign_cats must be a list')
        for s in value:
            if type(s) is not str:
                raise ValueError('Class.assign_cats must be a list of strings')
        self._assign_cats = value

    @property
    def prereqs(self) -> list[Class]:
        return self._prereqs

    @prereqs.setter
    def prereqs(self, value: list[Class]) -> None:
        if type(value) is not list:
            raise ValueError('Class.prereqs must be a list')
        for c in value:
            if type(c) is not Class:
                raise ValueError('Class.tags must be a list of Class objects')
        self._prereqs = value

    @property
    def postreqs(self) -> list[Class]:
        return self._postreqs

    @postreqs.setter
    def postreqs(self, value: list[Class]) -> None:
        if type(value) is not list:
            raise ValueError('Class.prereqs must be a list')
        for c in value:
            if type(c) is not Class:
                raise ValueError('Class.tags must be a list of Class objects')
        self._postreqs = value

    def add_prereq(self, c: Class) -> None:
        """Adds a Class to this Class's list of prerequisites."""
        if c in self._postreqs:
            raise CyclicalError('Cannot add a class to the prerequisites that is already a postrequisite')
        else:
            self._prereqs.append(c)

    def add_postreq(self, c: Class) -> None:
        """Adds a Class to this Class's list of postrequisites."""
        if c in self._prereqs:
            raise CyclicalError('Cannot add a class to the postrequisites that is already a prerequisite')
        else:
            self._postreqs.append(c)

    def term_sort_key(self) -> tuple[Term, str, int]:
        """Returns a tuple of term, dept, number for use with sorting."""
        return self.term, self.dept, self.number

    def to_transcript_line(self) -> str:
        """Prints the class dept, number, short_desc, hours and grade to a single-line, fixed-width string."""
        numstr = str(self.number)
        strs = [self.dept, ' '*(5-len(self.dept)), numstr, ' '*(5-len(numstr)), self.short_desc, f'   {self.hrs:1}.00   ', self.grade, ' '*(3-len(self.grade))]
        return ''.join(strs)

    def __lt__(self, other: Class):
        """Default ordering for sorting. Compares by dept first, then number, then year, then semester."""
        if type(self) is not Class or type(other) is not Class:
            raise ValueError('Class object can only be compared (<) to another Class object.')
        if self.dept != other.dept:
            return self.dept < other.dept
        elif self.number != other.number:
            return self.number < other.number
        else:
            return self.term < other.term

    def __eq__(self, other: Class):
        """Two Classes are equal iff their dept string, class number, and term are the same."""
        if type(self) is not Class or type(other) is not Class:
            raise ValueError('Class object can only be compared (==) to another Class object.')
        return self.dept == other.dept and self.number == other.number

    def __str__(self):
        """Returns a simple string with the dept and number"""
        return f'{self.dept} {self.number}'

    def __repr__(self):
        """Returns a slightly more detailed string with the dept, number & short_desc"""
        return f'{self.dept} {self.number}: {self.short_desc}'
