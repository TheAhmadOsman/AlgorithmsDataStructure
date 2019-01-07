#!/usr/bin/env python3
# encoding: UTF-8

############################################################################
#
# CS 160 - Week 8 Exercise
# Purpose: Searching Algorithms & Hash Function(s)
#
# Author: Ahmad M. Osman
# Date: April 1, 2017
#
# Filename: Student.py
#
############################################################################


# Student class
class Student:

    # initialize a student
    def __init__(self, name_, gpa_):
        self._name = name_
        self._gpa = gpa_

    # get student's name
    def get_name(self):
        return self._name

    # get student's GPA
    def get_gpa(self):
        return self._gpa

    # create two properties
    name = property(get_name)
    gpa = property(get_gpa)

    # student comparison methods
    def __eq__(self, other):
        return self.name == other.name and (self.gpa == other.gpa)

    def __gt__(self, other):
        return self.name > other.name

    def __lt__(self, other):
        return self.name < other.name

    # string representation
    def __str__(self):
        return self._name + " has " + str(self._gpa) + " GPA"
