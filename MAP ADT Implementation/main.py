#!/usr/bin/env python3
# encoding: UTF-8

##########################################################################
#
# CS 160 - Week 8 Project
# Purpose: MAP ADT Implementation
#
# Author: Ahmad M. Osman
# Date: April 3, 2017
#
# Filename: main.py
#
##########################################################################

from Map import Map


# main function - program execution instructions
def main():
    # Task #0 to #4 - Map ADT Implemented
    print("Creating hash table of size 8...")
    m = Map()

    # Task #5 - adding items
    print("Adding items...")
    m[54] = "cat"
    m[26] = "dog"
    m[93] = "lion"
    m[17] = "tiger"

    try:
        m[77] = "bird"
    except IndexError as ie:
        print(ie)

    m[31] = "cow"
    m[44] = "goat"
    m[55] = "pig"

    try:
        m[20] = "chicken"
    except IndexError as ie:
        print(ie)

        m[23] = "chicken"

    try:
        m[29] = "elephant"
    except IndexError as ie:
        print(ie)

    print("Printing hash table:", "\n\t", m)

    # Task #6 and #10 - retrieving items
    print("Retriving items...")
    for i in [54, 26, 93, 17, 31, 44, 55, 20, 23, 29, 55, 2]:
        print("\tKey", i, "has the value", m[i])

    # Task #7 - updating items
    print("Updating items...")
    print("\tKey", 31, "had the value", m[31], end="")
    m[31] = "eagle"
    print(" however, now it has the value", m[31], end="")
    print("!")
    print("Printing hash table after updating:", "\n\t", m)

    # Task #8 - hash table length
    print("The hash table length is:", len(m))

    # Task #9 - checking for keys belonging to the hash table
    print("Keys belonging to the hash table testing...")
    for i in [54, 55, 20, 23, 29, 55, 2]:
        print("\tIs", i, "in hashtable?", (i in m))


# Calling main function for program execution
if __name__ == "__main__":
    main()
