from school import School
from student import Student
from school_class import Class
from term import DEFAULT_PARTS_OF_YEAR, Term

# GPA calculations for me
old, new, tech, major = 'old', 'new', 'technical', 'major'
uiuc = School(
    'UIUC',
    short_name='Illinois',
    pretty_name='University of Illinois at Urbana-Champaign',
)
parkland = School('Parkland', short_name='Parkland', pretty_name='Parkland College')
wi, sp, su, fa = DEFAULT_PARTS_OF_YEAR
sem = 'Semester'
fa07 = Term(sem, 2007, fa)
sp08, fa08 = Term(sem, 2008, sp), Term(sem, 2008, fa)
fa24 = Term(sem, 2024, fa)
sp25, fa25 = Term(sem, 2025, sp), Term(sem, 2025, fa)
sp26, fa26 = Term(sem, 2026, sp), Term(sem, 2026, fa)
sp27 = Term(sem, 2027, sp)
cs = 'CS'
alex = Student(
    uiuc, major='Computer Science', program='Bachelor of Science in Computer Science'
)

# Fall 2007 classes
chem102 = Class(
    'CHEM', 102, 3, fa07, uiuc, tags=[old], grade='B', short_desc='General Chemistry I'
)
chem103 = Class(
    'CHEM',
    103,
    1,
    fa07,
    uiuc,
    tags=[old],
    grade='F',
    short_desc='General Chemistry Lab I',
)
cs100 = Class(
    cs,
    100,
    1,
    fa07,
    uiuc,
    tags=[old, tech, major],
    grade='A',
    short_desc='Freshman Orientation in CS',
)
cs173 = Class(
    cs,
    173,
    3,
    fa07,
    uiuc,
    tags=[old, tech, major],
    grade='D',
    short_desc='Discrete Structures',
)
hist105 = Class(
    'HIST',
    105,
    3,
    fa07,
    uiuc,
    tags=[old],
    grade='C+',
    short_desc='Latin America to Independence',
)
math241 = Class(
    'MATH', 241, 4, fa07, uiuc, tags=[old, tech], grade='C+', short_desc='Calculus III'
)
alex.add_classes([chem102, chem103, cs100, cs173, hist105, math241])

# Spring 2008 classes
cs125 = Class(
    cs,
    125,
    4,
    sp08,
    uiuc,
    tags=[old, tech, major],
    grade='B',
    short_desc='Intro to Computer Science',
    description='Introduction to Computer Science',
)
math415 = Class(
    'MATH',
    415,
    3,
    sp08,
    uiuc,
    tags=[old, tech],
    grade='F',
    short_desc='Applied Linear Algebra',
)
phys211 = Class(
    'PHYS',
    211,
    4,
    sp08,
    uiuc,
    tags=[old],
    grade='D+',
    short_desc='University Physics: Mechanics',
)
psyc100 = Class(
    'PSYC', 125, 4, sp08, uiuc, tags=[old], grade='C', short_desc='Intro Psych'
)
alex.add_classes([cs125, math415, phys211, psyc100])

# Fall 2008 classes
cs225 = Class(
    cs,
    225,
    4,
    fa08,
    uiuc,
    tags=[old, tech, major],
    grade='D',
    short_desc='Data Structures',
)
cs231 = Class(
    cs,
    231,
    3,
    fa08,
    uiuc,
    tags=[old, tech, major],
    grade='F',
    short_desc='Computer Architecture I',
)
math461 = Class(
    'MATH',
    461,
    3,
    fa08,
    uiuc,
    tags=[old, tech],
    grade='F',
    short_desc='Probability Theory',
)
phys212 = Class(
    'PHYS',
    212,
    4,
    fa08,
    uiuc,
    tags=[old],
    grade='D-',
    short_desc='University Physics: Elec & Mag',
)
alex.add_classes([cs225, cs231, math461, phys212])

# Fall 2024 classes
csc123 = Class(
    'CSC',
    123,
    4,
    fa24,
    parkland,
    tags=[new, tech, major],
    grade='A',
    short_desc='Computer Science I: (C/C++)',
)
mat200 = Class(
    'MAT',
    200,
    3,
    fa24,
    parkland,
    tags=[new, tech],
    grade='A',
    short_desc='Intro to Discrete Math',
    description='Introduction to Discrete Mathematics',
)
mat228 = Class(
    'MAT',
    228,
    4,
    fa24,
    parkland,
    tags=[new, tech],
    grade='A',
    short_desc='Calculus/Analyt Geom III',
    description='Calculus & Analytical Geometry III',
)
phy141 = Class(
    'PHY', 141, 4, fa24, parkland, tags=[new], grade='A', short_desc='Mechanics'
)
alex.add_classes([csc123, mat200, mat228, phy141])

# Spring 2025 classes
csc125 = Class(
    'CSC',
    125,
    3,
    sp25,
    parkland,
    tags=[new, tech, major],
    grade='A',
    short_desc='Cmptr Sci II/Prog in C++',
    description='Computer Science II: Programming in C++',
)
csc140 = Class(
    'CSC',
    140,
    3,
    sp25,
    parkland,
    tags=[new, tech, major],
    grade='A',
    short_desc='Computer Science I: (java)',
)
csc220 = Class(
    'CSC',
    220,
    3,
    sp25,
    parkland,
    tags=[new, tech, major],
    grade='A',
    short_desc='Data Structures',
)
mat220 = Class(
    'MAT',
    220,
    3,
    sp25,
    parkland,
    tags=[new, tech],
    grade='A',
    short_desc='Linear Algebra',
)
alex.add_classes([csc125, csc140, csc220, mat220])

# Fall 2025 classes
cs211 = Class(
    cs,
    211,
    3,
    fa25,
    uiuc,
    tags=[new, tech, major],
    grade='A',
    short_desc='Ethical & Professional Conduct',
    description='Ethical and Professional Conduct',
)
cs222 = Class(
    cs,
    222,
    1,
    fa25,
    uiuc,
    tags=[new, tech, major],
    grade='A',
    short_desc='Software Design Lab',
)
cs233 = Class(
    cs,
    233,
    4,
    fa25,
    uiuc,
    tags=[new, tech, major],
    grade='A+',
    short_desc='Computer Architecture',
)
cs357 = Class(
    cs,
    357,
    3,
    fa25,
    uiuc,
    tags=[new, tech, major],
    grade='A',
    short_desc='Numerical Methods I',
)
cs374 = Class(
    cs,
    374,
    4,
    fa25,
    uiuc,
    tags=[new, tech, major],
    grade='B+',
    short_desc='Intro to Algs & Models of Comp',
    description='Introduction to Algorithms & Models of Computation',
)
engl209 = Class(
    'ENGL',
    209,
    3,
    fa25,
    uiuc,
    tags=[new],
    grade='A',
    short_desc='Early British Lit and Culture',
    description='Early British Literature and Culture',
)
alex.add_classes([cs211, cs222, cs233, cs357, cs374, engl209])

# Spring 2026 classes (currently ongoing)
cs341 = Class(
    cs,
    341,
    4,
    sp26,
    uiuc,
    tags=[new, tech, major],
    grade='A',
    short_desc='System Programming',
)
cs361 = Class(
    cs,
    361,
    3,
    sp26,
    uiuc,
    tags=[new, tech, major],
    grade='A-',
    short_desc='Prob & Stat for Computer Sci',
    description='Probability and Statistics for Computer Science',
)
cs411 = Class(
    cs,
    411,
    3,
    sp26,
    uiuc,
    tags=[new, tech, major],
    grade='A',
    short_desc='Database Systems',
)
cs421 = Class(
    cs,
    421,
    3,
    sp26,
    uiuc,
    tags=[new, tech, major],
    grade='A',
    short_desc='Progrmg Languages & Compilers',
    description='Programming Languages & Compilers',
)
aas100 = Class(
    'AAS',
    100,
    3,
    sp26,
    uiuc,
    tags=[new],
    grade='A+',
    short_desc='Intro Asian American Studies',
)
alex.add_classes([cs341, cs361, cs411, cs421, aas100])

# Fall 2026 classes (registered for)
cs407 = Class(
    cs,
    407,
    4,
    fa26,
    uiuc,
    tags=[new, tech, major],
    ongoing=True,
    short_desc='Cryptography',
)
cs423 = Class(
    cs,
    423,
    3,
    fa26,
    uiuc,
    tags=[new, tech, major],
    ongoing=True,
    short_desc='Operating Systems Design',
)
cs438 = Class(
    cs,
    438,
    3,
    fa26,
    uiuc,
    tags=[new, tech, major],
    ongoing=True,
    short_desc='Computer Networks',
)
cs461 = Class(
    cs,
    461,
    4,
    fa26,
    uiuc,
    tags=[new, tech, major],
    ongoing=True,
    short_desc='Computer Security I',
)
clcv231 = Class(
    'CLCV',
    231,
    3,
    fa26,
    uiuc,
    tags=[new],
    ongoing=True,
    short_desc='Development of Ancient Cities',
)
alex.add_classes([cs407, cs423, cs438, cs461, clcv231])

# Spring 2027 classes (planned)
cs425 = Class(cs, 425, 4, sp27, uiuc, tags=[new, tech, major], ongoing=True)
cs433 = Class(cs, 433, 3, sp27, uiuc, tags=[new, tech, major], ongoing=True)
cs435 = Class(cs, 435, 3, sp27, uiuc, tags=[new, tech, major], ongoing=True)
cs463 = Class(cs, 463, 3, sp27, uiuc, tags=[new, tech, major], ongoing=True)
ggis106 = Class('GGIS', 106, 3, sp27, uiuc, tags=[new], ongoing=True)

# Print stuff/testing stuff
total_gpa, _ = alex.calculate_total_gpa()
predicted_gpa, _ = alex.calculate_predicted_gpa()
technical_gpa, _ = alex.calculate_filtered_gpa(include=[tech], exclude=[])
major_gpa, _ = alex.calculate_filtered_gpa(include=[major], exclude=[])

total_gpa_new, _ = alex.calculate_filtered_gpa(include=[], exclude=[old])
predicted_gpa_new, testlist = alex.calculate_filtered_gpa(
    include=[], exclude=[old], use_ongoing=True
)
technical_gpa_new, _ = alex.calculate_filtered_gpa(include=[tech], exclude=[old])
major_gpa_new, _ = alex.calculate_filtered_gpa(include=[major], exclude=[old])

print(f"""
Overall GPA:    {total_gpa:.2f}   New only: {total_gpa_new:.2f}
Predicted GPA:  {predicted_gpa:.2f}   New only: {predicted_gpa_new:.2f}
Major GPA:      {major_gpa:.2f}   New only: {major_gpa_new:.2f}
Technical GPA:  {technical_gpa:.2f}   New only: {technical_gpa_new:.2f}
""")
# print(csc125.to_transcript_line())
# print('testlist: [')
# sep = ',\n'
# for i, item in enumerate(sorted(testlist, key=Class.term_sort_key)):
#     print(f'\t{item}{sep}', end='')
# print(']')
