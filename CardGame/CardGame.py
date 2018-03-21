#!/usr/bin/env python3
# encoding: UTF-8

########################################################################
#
# CS 160 - Week 5 Project
# Purpose: Cards Classes Implementation
#
# Author: Ahmad M. Osman
# Date: March 6, 2017
#
# Filename: CardGame.py
#
########################################################################

import random

# Constant variables for Cards
NAMES = {'T': 'Ten', 'J': 'Jack', 'Q': 'Queen', 'K': 'King', 'A': 'Ace'}
RANK = '23456789TJQKA'
SUIT = ['spades', 'clubs', 'diamonds', 'hearts']


class Card:
    '''Card class'''

    def __init__(self, rank_, suit_):
        '''construction function'''
        if rank_ in RANK:
            self._rank = rank_
        else:
            raise ValueError('invalid rank')
        if suit_ in SUIT:
            self._suit = suit_
        else:
            raise ValueError('invalid suit')

    @property
    def rank(self):
        '''return card's rank'''
        return self._rank

    @property
    def suit(self):
        '''return card's suit'''
        return self._suit

    def __gt__(self, other_):
        '''comparing cards'''
        if self.suit == other_.suit:
            return RANK.index(self.rank) > RANK.index(other_.rank)
        elif SUIT.index(self.suit) > SUIT.index(other_.suit):
            return True
        else:
            return False

    def __str__(self):
        '''return card as a string'''
        return NAMES.get(self.rank, self.rank) + " of " + self.suit


class Deck:
    '''Deck class'''

    def __init__(self):
        '''construction function'''
        self._card_list = []
        for s in SUIT:
            for r in RANK:
                self._card_list.append(Card(r, s))

    @property
    def card_list(self):
        '''return the deck'''
        return self._card_list

    def draw(self):
        '''draw from the deck'''
        if len(self._card_list) > 0:
            return self._card_list.pop()
        else:
            raise IndexError("Error! Popping from an empty list!")

    def shuffle(self):
        '''shuffle the deck'''
        random.shuffle(self._card_list)

    def __str__(self):
        '''printing the deck's cards'''
        for card in self._card_list:
            print(card)


class Player:
    '''Player class'''

    def __init__(self, name_, hand_size_=0):
        '''construction function'''
        self._name = name_
        self._hand_size = hand_size_
        self._hand = []

    @property
    def name(self):
        '''return the player's name'''
        return self._name

    @property
    def hand_size(self):
        '''returns the player's hand size'''
        return self._hand_size

    @property
    def hand(self):
        '''return the player's hand'''
        return self._hand

    def draw_card(self, deck):
        '''drawing card from the deck'''
        if len(self._hand) < self._hand_size:
            self._hand.append(deck.draw())
        else:
            raise IndexError(
                "Could not draw from the card deck as the palyer's hand is full!")

    def show_hand(self):
        '''showing player's hand'''
        for card in self._hand:
            print(card)
