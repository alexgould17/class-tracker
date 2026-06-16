"""Module containing Term class and its default values."""
from __future__ import annotations

DEFAULT_PARTS_OF_YEAR = ['Winter', 'Spring', 'Summer', 'Fall']


class Term:
    """Unit corresponding to a single term of school instruction.

    Only one instance should be created to represent each term at each School. Each instance should be reused for as many Classes as are taken that Term. Highly recommended to build the part_of_year_names list and pass it to the constructor if not using the module default for the best ordering (list should go earliest -> latest).

    Attributes:
        name: A non-empty string containing the name for a single unit of a Term. For example: 'semester' or 'quarter'.
        year: A non-negative integer containing the year the term started. For example: 2026.
        part_of_year: A non-empty string containing the part of the year or season the Term started. For example: 'Spring'
        part_of_year_index: An index of where the part_of_year occurs in the term_names list, automatically set when the part_of_names is set
        part_of_year_names: A list of strings representing all the possible Term names. Ideally, this should be the same list object for every instance of a Term at a specific School, and every part_of_year string should exist in this list for easy ordering.

    Raises:
        ValueError on any attribute assignment (including during initialization) that violates the above conditions.
    """

    _name: str           # e.g. 'quarter', 'semester', etc.
    _year: int
    _part_of_year: str
    _part_of_year_index: int
    _part_of_year_names: list[str]

    def __init__(self, name: str, year: int, part_of_year: str, *, part_of_year_names: list[str] | None = None):
        self.name = name
        self.year = year
        self.part_of_year_names = part_of_year_names if part_of_year_names else DEFAULT_PARTS_OF_YEAR
        self.part_of_year_index = 0
        self.part_of_year = part_of_year

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if type(value) is not str or value == '':
            raise ValueError('Term.name must be a non-empty string.')
        self._name = value

    @property
    def year(self) -> int:
        return self._year

    @year.setter
    def year(self, value: int):
        if type(value) is not int or value < 0:
            raise ValueError('Term.year must be a non-negative integer.')
        self._year = value

    @property
    def part_of_year(self) -> str:
        return self._part_of_year

    @part_of_year.setter
    def part_of_year(self, value: str):
        if type(value) is not str or value == '':
            raise ValueError('Term.part_of_year must be a non-empty string.')
        self._part_of_year = value
        self._part_of_year_index = Term.part_of_year_names.index(self._part_of_year)

    @property
    def part_of_year_index(self):
        return self._part_of_year_index

    @part_of_year_index.setter
    def part_of_year_index(self, value: int):
        if type(value) is not int or value < 0:
            raise ValueError('Term.part_of_year_index must be an integer.')
        self._part_of_year_index = value

    @property
    def part_of_year_names(self):
        return self._part_of_year_names

    @part_of_year_names.setter
    def part_of_year_names(self, value: list[str]):
        if type(value) is not list or not value:
            raise ValueError('Term.term_names must be a non-empty list.')
        for s in value:
            if type(s) is not str:
                raise ValueError('Term.term_names must be a list of strings.')
        self._part_of_year_names = value

    def __str__(self) -> str:
        """Returns a 4-char string: 1st 2 chars of part_of_year, capitalized + last 2 digits of year."""
        return f'{self.part_of_year[:2].upper()}{self.year%100:02d}'

    def __repr__(self) -> str:
        """Returns a string of the format 'part_of_year year' with year always 4 digits."""
        return f'{self.part_of_year} {self.year:04d}'

    def __lt__(self, other: Term) -> bool:
        """Compares by year first, then part of year.

        If both self and other's part_of_year_index are not -1, it will compare by those indices (when years are even).
        Otherwise, defaults to lexicographic ordering of the string value of part_of_year.

        Returns:
            The boolean result of the comparison
        """
        if type(self) is not Term or type(other) is not Term:
            raise ValueError('Term object can only be compared (<) to another Term object.')
        if self.year == other.year:
            if self.part_of_year_index != -1 and other.part_of_year_index != -1:
                return self.part_of_year_index < other.part_of_year_index
            else:
                return self.part_of_year < other._part_of_year
        else:
            return self.year < other.year

    def __eq__(self, other: Term) -> bool:
        """Two terms are equal iff their names, years & part_of_years are equal"""
        if type(self) is not Term or type(other) is not Term:
            raise ValueError('Term object can only be compared (<) to another Term object.')
        return self.year == other.year and self.name == other.name and self.part_of_year == other.part_of_year
