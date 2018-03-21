#!/usr/bin/env python3
# encoding: UTF-8

########################################################################
#
# CS 160 - Week 5 Project
# Purpose: Cards Classes Implementation - Game's Players Initialization
#
# Author: Ahmad M. Osman
# Date: March 6, 2017
#
# Filename: main.py
#
########################################################################

import CardGame

RANK = '23456789TJQKA'
SUIT = ['spades', 'clubs', 'diamonds', 'hearts']


# main function - program execution instructions
def main():
    print("Let's play a game!")
    main_deck = CardGame.Deck()
    main_deck.shuffle()
    for c in main_deck.card_list:
        print(c)
    player1 = CardGame.Player("Alice", 5)
    player2 = CardGame.Player("Bob", 5)
    for _ in range(5):
        player1.draw_card(main_deck)
        player2.draw_card(main_deck)
    print("{}'s hand:".format(player1.name))
    player1.show_hand()
    print("{}'s hand:".format(player2.name))
    player2.show_hand()


# Calling main function for program execution
if __name__ == "__main__":
    main()
