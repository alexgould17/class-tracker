from __future__ import annotations

default_terms = ['Winter', 'Spring', 'Summer', 'Fall']


class Term:
    """Unit corresponding to a single term of school instruction, for example, a semester or quarter."""

    _name: str           # e.g. 'quarter', 'semester', etc.
    _year: int
    _part_of_year: str
    _part_of_year_index: int = -1

    term_names = default_terms

    def __init__(self, name: str, year: int, part_of_year: str):
        self.name = name
        self.year = year
        self.part_of_year = part_of_year

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str):
        if name == '':
            raise ValueError('Name cannot be blank')
        self._name = name

    @property
    def year(self) -> int:
        return self._year

    @year.setter
    def year(self, year: int):
        if year < 0:
            raise ValueError('Year must be non-negative integer')
        self._year = year

    @property
    def part_of_year(self) -> str:
        return self._part_of_year

    @part_of_year.setter
    def part_of_year(self, part_of_year: str):
        self._part_of_year = part_of_year
        self._part_of_year_index = Term.term_names.index(self._part_of_year)

    @property
    def part_of_year_index(self):
        return self._part_of_year_index

    def __str__(self) -> str:
        """Converts the term into a very brief string.

        Capitalizes the first 2 letters of part_of_year, then takes year % 100, and combines them.
        For example, Term('Semester', 2009, 'Spring') becomes 'SP09'
        :returns max 4 character string as described above"""
        return f'{self.part_of_year[:2].upper()}{self.year%100:02d}'

    def __lt__(self, other: Term) -> bool:
        """Compares by year first, then part of year.

        If both self and other's part_of_year_index are -1, it will compare by those indices (when years are even).
        Otherwise, defaults to lexicographic ordering of the string value of part_of_year.
        :returns bool result of comparison
        """

        if self.year == other.year:
            if self.part_of_year_index != -1 and other.part_of_year_index != -1:
                return self.part_of_year_index < other.part_of_year_index
            else:
                return self.part_of_year < other._part_of_year
        else:
            return self.year < other.year

    def __repr__(self) -> str:
        """Returns a string of the format 'part_of_year year' with year always 4 digits."""
        return f'{self.part_of_year} {self.year:04d}'
