#!/usr/bin/env python3
# encoding: UTF-8

##########################################################################
#
# CS 160 - Week 5 Exercise
# Purpose: Palindrome Checker Extension To Ignore Spaces
#
# Author: Ahmad M. Osman
# Date: March 4, 2017
#
# Filename: palch.py
#
##########################################################################

from pythonds.basic.deque import Deque


# Extending the palindrome checker from the text book to ignore spaces
def palchecker(aString):
    chardeque = Deque()

    for ch in aString:
        chardeque.addRear(ch)

    stillEqual = True

    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()

        while (first == ' ' or last == ' ') and chardeque.size() >= 1:
            if first == ' ':
                first = chardeque.removeFront()
            else:
                last = chardeque.removeRear()

        if first != last and not (first == ' ' or last == ' '):
            stillEqual = False

    return stillEqual
