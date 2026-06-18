"""
Design specs for grading app:

------------ Classes ------------
** Student **
Takes classes, has a major, program of study & preferences
Want to store past, current & future classes, name, password (eventually)
Calculates own GPA, takes classes, adds/changes degree

** Class **
Has name, dept, number, assignments, assignment categories, grade thresholds, pre/postreqs, list of tags, and a final grade
Also has description & notes
CRUDs all of the above (except final grade which is just a calculation), calculates grades

** Course of Study **
Has name, classes needed, other requirements (min GPA, etc.), degree or goal
Calculates progress, shows order of classes (difficult!)

** Assignment **
Has name, number, category, points, points out of, and belongs to a class (created from a view accessed from the class view)
basic CRUD ops only

** Preferences **
Specify user preferences: dark/light mode, 0/1 indexing, numbers after decimal place to show (0-6)

------------ App/Interface ------------
Start with CLI, move to using local webserver/html
First step, choose (or login) as a user
Load user data from disk or create new user

"""

###### Code samples copied from other scripts ######
### CS 341 ###
# Actual assignment scores (with weight factors as necessary), 1.0 == 100%
mp = 'Machine Problems'
mps = [
    21.0 / 21.0,
    35.0 / 40.0,
    29.0 / 29.0,
    57.0 / 57.0,
    (5.0 + 12.0 + 6.0) / (6.0 + 12.0 + 6.0),
    30.0 / 31.0,
    17.0 / 17.0,
    18.0 / 41.0,
    13.0 / 16.0,
]
mp_weights = [1, 1, 1, 1, 2, 1, 1, 1, 1, 3]
lp = 'Lab Programming'
lps = [1.0] * 10 + [22.0 / 23.0, 1]  # thru MMAP
la = 'Lab Attendance'
las = [1] * 11  # thru week 13, finished
quiz = 'Quizzes'
quizzes = [1.0] * 7
mt = 'Midterm'
stest, shw = 0.4285, 0.9142
mt_score = stest + 0.85 * (shw - stest)
final = 'Final'
final_score = 0.0

# Each grading category and its % contribution to the final grade total
percent_contributions = {
    mp: 0.42,
    lp: 0.14,
    la: 0.03,
    quiz: 0.12,
    mt: 0.09,
    final: 0.20,  # Assuming 9 lab attendances
}

# Total number of each assignment
num_assignments = {
    mp: 13,  # NOTE: # of weeks, not total # of assignments. Each week weights to 1
    lp: 13,
    la: 11,
    quiz: 7,
    mt: 1,
    final: 1,
}

# Number of drops per category
num_drops = {mp: 0, lp: 1, la: 2, quiz: 0, final: 0}

# Published grade thresholds (F always added for starting point)
grade_thresholds = {0.9: 'A-', 0.8: 'B-', 0.7: 'C-', 0.0: 'F'}

# Calculations

# mp_sofar = grade so far out of 100% (==1.0), mp_sofar_per = how much the work done so far contributes to your
mp_sofar = 0.0
mp_sofar_per = 0.0

# Only do calcs for this assignment group if we have at least one of this type of assignment graded so far
if mps:
    # Loop over each assignment, weighting its addition to the grade so far & percentage so far accordingly
    for i in range(len(mps)):
        mp_sofar += mps[i] * mp_weights[i]
        mp_sofar_per += mp_weights[i]

    # Special case since MP assignments have variable weights: make sure my hand-entered math is right
    assert sum(mp_weights) == num_assignments[mp], 'Weights not equal for ' + mp

    # 1-norm the grade so far so we get a percentage scaled to 100% or 1.0
    mp_sofar /= sum(mp_weights[: len(mps)])

    # Calculate how much of the total grade we've achieved so far, scaling each assignment/category to its overall final weight
    mp_sofar_per = (mp_sofar_per * percent_contributions[mp]) / num_assignments[mp]

    # Print the results
    print(
        '{} grade:\n\tGrade so far: {:.2%}\n\tContribution to final grade %: {:.2%}'.format(
            mp, mp_sofar, mp_sofar_per
        )
    )
else:
    # No contributions so far
    print(f'No grade contributions so far from {mp}s')

lp_sofar = 0.0
lp_sofar_per = 0.0
if lps:
    for i in range(len(lps)):
        lp_sofar += lps[i]
        lp_sofar_per += 1
    lp_sofar /= len(lps)
    lp_sofar_per = (lp_sofar_per * percent_contributions[lp]) / num_assignments[lp]
    print(
        '{} grade:\n\tGrade so far: {:.2%}\n\tContribution to final grade %: {:.2%}'.format(
            lp, lp_sofar, lp_sofar_per
        )
    )
else:
    print(f'No grade contributions so far from {lp}s')
### End CS 341 ###
###### End code samples ######
