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
# Filename: main.py
#
##########################################################################

from CardGame import *


# main function - program execution instructions
def main():

    # Keeping scores
    player_1_score = 0
    player_2_score = 0

    # Simulating 100 games
    for game in range(100):

        # Creating a new deck of cards and shuffling it
        deck_of_cards = Deck()
        deck_of_cards.shuffle()

        # Creating players
        player_1 = Player("Jesse", 0.50)
        player_2 = Player("Erin", 0.50)

        # Disturbing cards evenly among players
        for card in range(52):
            if card % 2 == 0:
                player_1.draw_card(deck_of_cards)
            else:
                player_2.draw_card(deck_of_cards)

        # Keeping track of the game's rounds
        rounds = 0

        # Playing a game
        while True:
            rounds = rounds + 1

            # Playing cards and checking on snap condition
            if player_1.play_card() == player_2.play_card():
                sum_skill = player_1.skill + player_2.skill
                player_1_skill_ratio = player_1.skill / sum_skill
                if(random.random() < player_1_skill_ratio):
                    player_1.win_table(player_2)
                else:
                    player_2.win_table(player_1)

            # Checking on player 1's cards status
            if player_1.is_empty_hand():
                if not player_1.is_empty_discard():
                    player_1.pick_discard()
                else:
                    if not player_1.is_empty_pile():
                        player_1.pick_pile()
                    else:
                        # Losing condition
                        player_2_score = player_2_score + 1
                        break

            # Checking on player 2's cards status
            if player_2.is_empty_hand():
                if not player_2.is_empty_discard():
                    player_2.pick_discard()
                else:
                    if not player_2.is_empty_pile():
                        player_2.pick_pile()
                    else:
                        # Losing condition
                        player_1_score = player_1_score + 1
                        break

        # Checking on who won this
        if player_1.is_empty_hand() and player_1.is_empty_discard() and player_1.is_empty_pile():
            print(player_2.name, "won game number",
                  (player_1_score + player_2_score), "in", rounds, "rounds.")
        else:
            print(player_1.name, "won game number",
                  (player_1_score + player_2_score), "in", rounds, "rounds.")

    # Who won the simulation
    if player_1_score > player_2_score:
        print(player_1.name, "won the game with overall score",
              player_1_score, "vs", player_2_score)
    elif player_2_score > player_1_score:
        print(player_2.name, "won the game with overall score",
              player_2_score, "vs", player_1_score)
    else:
        print("The game was a tie between", player_1.name, "and", player_2.name,
              "with overall score", player_2_score, "vs", player_1_score)


# Calling main function for program execution
if __name__ == "__main__":
    main()
