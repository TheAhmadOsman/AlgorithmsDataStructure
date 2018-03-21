#!/usr/bin/env python3
# encoding: UTF-8

########################################################################
#
# CS 160 - Week 3 Project
# Purpose: Different championships' statistics.
#
# Author: Ahmad M. Osman
# Date: February 20, 2017
#
# Filename: championship.py
#
########################################################################


class Championship():
    '''Championship class'''

    def __init__(self, year_, winner_, loser_, win_score_, lose_score_):
        self._year = year_
        self._winner = winner_
        self._loser = loser_
        self._win_score = win_score_
        self._lose_score = lose_score_
        self._score_dif = int(self._win_score) - int(self._lose_score)

    # Properties - getters
    @property
    def year(self):
        return self._year

    @property
    def winner(self):
        return self._winner

    @property
    def loser(self):
        return self._loser

    @property
    def win_score(self):
        return self._win_score

    @property
    def lose_score(self):
        return self._lose_score

    @property
    def score_dif(self):
        return self._score_dif

    # String magic function
    def __str__(self):
        return self._winner + " won in " + self._year + " against " + self._loser + " with score " + str(self._win_score) + "-" + str(self._lose_score)
