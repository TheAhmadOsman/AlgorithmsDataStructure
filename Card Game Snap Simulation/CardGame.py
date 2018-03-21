#!/usr/bin/env python3
# encoding: UTF-8

##########################################################################
#
# CS 160 - Week 6 Project
# Purpose: Card Game Snap Simulation
#
# Author: Ahmad M. Osman
# Date: March 16, 2017
#
# Filename: CardGame.py
#
##########################################################################

import random


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
    def __eq__(self, other):
        return self.ranks.find(self.rank) == self.ranks.find(other.rank)

    def __gt__(self, other):
        return self.ranks.find(self.rank) - self.ranks.find(other.rank) > 0

    def __lt__(self, other):
        return self.ranks.find(self.rank) - self.ranks.find(other.rank) < 0

    # string representation
    def __str__(self):
        return self.rank + " of " + self.suit


# a Deck of cards
class Deck:

    # initialize a deck
    def __init__(self):
        self.card_list = []
        for rank in "23456789TJQKA":
            for suit in ['spades', 'clubs', 'diamonds', 'hearts']:
                new_card = Card(rank, suit)
                self.card_list.append(new_card)

    # check if the deck is empty
    def is_empty(self):
        return len(self.card_list) == 0

    # draw a card from the deck
    def draw(self):
        return self.card_list.pop()

    # shuffle the deck
    def shuffle(self):
        random.shuffle(self.card_list)


# a Player
class Player:

    # init a Player with a name and skill level
    def __init__(self, name, skill_level):
        self.__name = name
        self.__skill = skill_level
        self.hand = []
        self.pile = []
        self.discard = []

    # is the hand empty?
    def is_empty_hand(self):
        return len(self.hand) == 0

    # is the discard pile empty?
    def is_empty_discard(self):
        return len(self.discard) == 0

    # is the active pile empty?
    def is_empty_pile(self):
        return len(self.pile) == 0

    # draw one card from the deck
    def draw_card(self, deck):
        new_card = deck.draw()
        self.hand.append(new_card)

    # play a card
    def play_card(self):
        card = self.hand.pop()
        self.pile.append(card)
        return card

    # discard a card to a pile
    def discard_card(self, card):
        self.discard.append(card)

    # take a discard pile
    def pick_discard(self):
        random.shuffle(self.discard)
        self.hand = self.hand + self.discard
        self.discard = []

    # take a pile
    def pick_pile(self):
        random.shuffle(self.pile)
        self.hand = self.hand + self.pile
        self.pile = []

    # win all cards on a  table
    def win_table(self, other):
        self.discard = self.discard + self.pile + other.pile
        self.pile = []
        other.pile = []

    # get name
    def get_name(self):
        return self.__name

    # get skills
    def get_skill(self):
        return self.__skill

    # create two properties
    name = property(get_name)
    skill = property(get_skill)
