from __future__ import annotations

default_terms = ['Winter', 'Spring', 'Summer', 'Fall']


class Term:
    """Unit corresponding to a single term of school instruction, e.g. semester or quarter
    """

    _name: str           # e.g. 'quarter', 'semester', etc.
    _year: int
    _part_of_year: str
    _part_of_year_index: int = -1

    term_names = default_terms

    def __init__(self, name: str, year: int, part_of_year: str):
        self.set_name(name)
        self.set_year(year)
        self.set_part_of_year(part_of_year)

    def set_name(self, name: str):
        if name == '':
            raise ValueError('Name cannot be blank')
        self._name = name

    def get_name(self) -> str:
        return self._name

    def set_year(self, year: int):
        if year < 0:
            raise ValueError('Year must be non-negative integer')
        self._year = year

    def get_year(self) -> int:
        return self._year

    def set_part_of_year(self, part_of_year: str):
        self._part_of_year = part_of_year
        self._part_of_year_index = Term.term_names.index(self._part_of_year)

    def get_part_of_year(self) -> str:
        return self._part_of_year

    def short_str(self) -> str:
        return f'{self._part_of_year[:2]}{self._year%100:2d}'

    def __lt__(self, other: Term):
        """Compares by year first, then part of year. If both self & other's part_of_year are in Term.term_names list,
        will compare by those indices (when years are even). Otherwise, defaults to lexicographic ordering.
        """

        if self._year == other._year:
            if self._part_of_year_index != -1 and other._part_of_year_index != -1:
                return self._part_of_year_index < other._part_of_year_index
            else:
                return self._part_of_year < other._part_of_year
        else:
            return self._year < other._year

    def __str__(self):
        return f'{self._part_of_year} {self._year:4d}'
