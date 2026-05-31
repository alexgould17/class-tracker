# Class Tracker App

This is a small, locally hosted app written in Python that allows students to easily maintain a list of classes they've
taken, grades they've gotten, and update their assignments to calculate grades in real time.

## Interface

Currently, this project is in the extreme early stages, so there is no user interface. I have my own grade data from my
university experience entered manually in the `main.py` script for testing. Eventually, I plan to add a web-based
interface that allows the user to type things into a browser on their local machine. Potentially, this could lead to
a mobile app.

## To-Do List

- Document the codebase more thoroughly and properly.
- Add UV as a package manager & Ruff as a linter, and lint according to industry standard specifications
- Add robust unit testing for every module.
- Add disk i/o so that configurations can be saved to (probably json) files for storing state between program runs.
- Create a web-based interface in HTML/JavaScript/CSS and a simple server to run locally so the app can be deployed.

## Author's Note

Almost of the functionality is based on my personal experience, and thus derives chiefly from the way the University of
Illinois at Urbana-Champaign (~90%) handles its classes, grades, etc., based on my personal experience. Most of the
remaining ~10% is derived from my two semesters at Parkland College. If this project develops enough and a userbase
develops, I will certainly listen to feedback from any user.
