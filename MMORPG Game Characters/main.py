#!/usr/bin/env python3
# encoding: UTF-8

##########################################################################
#
# CS 160 - Week 7 Project
# Purpose: MMORPG Game Characters' Classes Implementation
#
# Author: Ahmad M. Osman
# Date: March 27, 2017
#
# Filename: main.py
#
##########################################################################

from Characters import Archer, Trojan, Wizard
from pythonds import Queue
import random


# main function - program execution instructions
def main():
    game_characters = [Archer, Trojan, Wizard]
    world_size = random.randint(10, 25)
    print("Initialized a game of a world map that can take " +
          str(world_size) + " characters!")

    characters = Queue()
    # Making as many characters as the world size can take
    for space in range(world_size):
        char_type = game_characters[random.randint(0, 2)]
        current_char = char_type(random.choice([True, False]))

        # Possible levels are between 1 and 130, leveling character
        for i in range(random.randint(1, 130)):
            current_char.level_up()

        characters.enqueue(current_char)

    # Printing the characters stored the in queue
    # from the older character to the most recently created one
    for game_character in range(characters.size()):
        print(characters.dequeue())

# Calling main function for program execution
if __name__ == "__main__":
    main()
