from __future__ import annotations
from assignment import Assignment
from school import School
from term import Term
from utilities import CyclicalError


class Class:
    """class representing a single Class that a user takes in school."""

    dept: str
    number: int
    short_desc: str
    description: str
    grade: str = ''
    hrs: int
    term: Term
    school: School
    tags: list[str]
    ongoing: bool = False
    assignments: list[Assignment]
    assign_cats: list[str]
    prereqs: list[Class]
    postreqs: list[Class]

    def __init__(self, dept: str, number: int, hrs: int, term: Term, school: School, *,
                 tags: list[str], ongoing: bool=False, grade: str='', short_desc: str='', description: str=''):
        self.number = number
        self.dept = dept
        self.grade = grade[:3]
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

    def add_prereq(self, c: Class) -> None:
        """Adds a Class as a prerequisite of this Class, i.e., the added Class must be taken before this Class"""

        if c in self.postreqs:
            raise CyclicalError('Cannot add a class to the prerequisites that is already a postrequisite')
        else:
            self.prereqs.append(c)

    def add_postreq(self, c: Class) -> None:
        """Adds a Class as a postrequisite of this Class, i.e., the added Class must be taken after this Class"""

        if c in self.prereqs:
            raise CyclicalError('Cannot add a class to the postrequisites that is already a prerequisite')
        else:
            self.postreqs.append(c)

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
