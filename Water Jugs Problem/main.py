#!/usr/bin/env python3
# encoding: UTF-8

##########################################################################
#
# CS 160 - Week 12 Project
# Purpose: Water Jugs Problem
#
# Author: Ahmad M. Osman
# Date: May 4, 2017
#
# Filename: main.py
#
##########################################################################


class State:
    '''State Class'''

    def __init__(self, jug1_, jug2_):
        '''Initialize the state'''
        self._jug1 = jug1_
        self._jug2 = jug2_

    def fill_jug_1(self):
        '''Fill jug1 to capacity from the pump'''
        self._jug1 = 4
        return State(self._jug1, self._jug2)

    def fill_jug_2(self):
        '''Fill jug2 to capacity from the pump'''
        self._jug2 = 3
        return State(self._jug1, self._jug2)

    def empty_jug_1(self):
        '''Pour the water from jug1 onto the ground'''
        self._jug1 = 0
        return State(self._jug1, self._jug2)

    def empty_jug_2(self):
        '''Pour the water from jug2 onto the ground'''
        self._jug2 = 0
        return State(self._jug1, self._jug2)

    def pour_jug_1_jug_2(self):
        '''Pour as much water as you can from jug1 to jug2 without spilling'''
        while self._jug2 < 3 and self._jug1 > 0:
            self._jug2 += 1
            self._jug1 -= 1
        return State(self._jug1, self._jug2)

    def pour_jug_2_jug_1(self):
        '''Pour as much water as you can from jug2 to jug1 without spilling'''
        while self._jug1 < 4 and self._jug2 > 0:
            self._jug1 += 1
            self._jug2 -= 1
        return State(self._jug1, self._jug2)

    @property
    def jug1(self):
        '''Propery of jug1'''
        return self._jug1

    @property
    def jug2(self):
        '''Propery of jug2'''
        return self._jug2

    def clone(self):
        '''Make a clone of the State'''
        return State(self._jug1, self._jug2)

    def __eq__(self, other_):
        '''Compare two State(s)'''
        return self._jug1 == other_.jug1 and self._jug2 == other_.jug2

    def __str__(self):
        '''Print State'''
        return '(' + str(self._jug1) + ', ' + str(self._jug2) + ')'


def search(moves, start, goal):
    '''Find the moves from the start to the goal'''
    # Base case #1
    if start == goal:
        moves.append(start)
        return moves
    # Base case #2
    elif start in moves:
        pass
    # General Case
    else:
        moves.append(start)
        return search(moves, start.clone().fill_jug_1(), goal) or search(moves, start.clone().fill_jug_2(), goal) or search(moves, start.clone().empty_jug_1(), goal) or search(moves, start.clone().empty_jug_2(), goal) or search(moves, start.clone().pour_jug_1_jug_2(), goal) or search(moves, start.clone().pour_jug_2_jug_1(), goal)


# main function - program execution instructions
def main():
    # 2 gallons in the 4 gallon jar, 0 in the other
    goal = State(2, 0)
    # both jars start out empty
    start = State(0, 0)
    # when search returns, moves will contain the sequence of states
    moves = []
    search(moves, start, goal)
    print([str(x) for x in moves])


# Calling main function for program execution
if __name__ == "__main__":
    main()
