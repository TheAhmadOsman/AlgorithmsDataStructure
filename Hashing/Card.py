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
# Filename: Card.py
#
############################################################################


# a single Card class
class Card:
    ranks = "23456789TJQKA"
    suits = ['spades', 'clubs', 'diamonds', 'hearts']

    # initialize a card
    def __init__(self, rank, suit):
        self.__rank = rank
        self.__suit = suit

    # get card's rank
    def get_rank(self):
        return self.__rank

    # get card's suit
    def get_suit(self):
        return self.__suit

    # create two properties
    rank = property(get_rank)
    suit = property(get_suit)

    # card comparison methods
    # The equal comparison method compares both suits and ranks
    def __eq__(self, other):
        return (self.ranks.find(self.rank) == self.ranks.find(other.rank)) and (self.suit) == (other.suit)

    def __gt__(self, other):
        return self.ranks.find(self.rank) - self.ranks.find(other.rank) > 0

    def __lt__(self, other):
        return self.ranks.find(self.rank) - self.ranks.find(other.rank) < 0

    # string representation
    def __str__(self):
        return self.rank + " of " + self.suit
