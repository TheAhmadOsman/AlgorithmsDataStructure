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
# Filename: mOsmanWeek8Ex.py
#
############################################################################

from Card import Card
from Student import Student
import random


# Sequential search algorithm
def seq_search(value, lst):
    for item in lst:
        if item == value:
            return True
    return False


# Binary search algorithm
def bin_search(value, lst):
    if len(lst) == 0:
        return False
    else:
        midpoint = len(lst) // 2
        if lst[midpoint] == value:
            return True
        elif value < lst[midpoint]:
            return bin_search(value, lst[:midpoint])
        else:
            return bin_search(value, lst[midpoint + 1:])


# Please note that I implemented the hash function(s) to take a list and
# process the value of that list size, this was helpful for understanding
# and processing collisions

# Hash function - simple remainder method
def hash_rem(value, lst):
    position = value % len(lst)
    if not lst[position]:
        lst[position] = value
    else:
        for k in range(len(lst)):
            position = (value % len(lst) + k * k) % len(lst)
            if not lst[position]:
                lst[position] = value
                break
            # The following condition can be useful if we do not our list to have repetitiv values
            # elif lst[position] == value:
                # break
    if (None not in lst) and (lst[position] != value):
        raise IndexError("The list is full. Could not add value!")
    if lst[position] == value:
        return position
    else:
        raise IndexError("Could not get position due to collision")


# Hash function - mid-square method
def hash_msq(value, lst):
    val_sqr = value ** 2
    sqr_lst = list(str(val_sqr))
    mid_val = val_sqr
    if len(sqr_lst) != 1:
        start_pos = len(sqr_lst) // 2 - 1
        end_pos = start_pos + 2
        mid_val = int("".join(sqr_lst[start_pos:end_pos]))
    position = mid_val % len(lst)
    if not lst[position]:
        lst[position] = value
    else:
        for k in range(len(lst)):
            position = (mid_val % len(lst) + k * k) % len(lst)
            if not lst[position]:
                lst[position] = value
                break
    if (None not in lst) and (lst[position] != value):
        raise IndexError("The list is full. Could not add value!")
    if lst[position] == value:
        return position
    else:
        raise IndexError("Could not get position due to collision")


# String hash function - character position as a weight implementation
def hash_str(str_value, lst):
    str_num = 0
    char_weight = 1
    for character in str_value:
        str_num = str_num + (ord(character) * char_weight)
        char_weight = char_weight + 1
    position = str_num % len(lst)
    if not lst[position]:
        lst[position] = str_value
    else:
        for k in range(len(lst)):
            position = (str_num % len(lst) + k * k) % len(lst)
            if not lst[position]:
                lst[position] = str_value
                break
    if (None not in lst) and (lst[position] != str_value):
        raise IndexError("The list is full. Could not add value!")
    if lst[position] == str_value:
        return position
    else:
        raise IndexError("Could not get position due to collision")


# main function - program execution instructions
def main():
    # Task number 1
    print("Task #1")
    card_list = []
    for rank in "246":
        for suit in ['spades', 'diamonds', 'hearts']:
            new_card = Card(rank, suit)
            card_list.append(new_card)
    card_list.append(Card('A', 'clubs'))
    search_for = Card('A', 'clubs')
    print("Here is the list:", [str(card) for card in card_list])
    print()
    print('\t', search_for, "was found in the list?",
          seq_search(search_for, card_list))
    search_for = Card('A', 'hearts')
    print('\t', search_for, "was found in the list?",
          seq_search(search_for, card_list))
    print()

    # Task number 2
    print("Task #2")
    student_list = []
    for name in ["Ahmad", "Alex", "Dave", "Erin", "Jesse", "John", "Kalie", "Mike", "Max", "Nim"]:
        new_student = Student(name, 4.0)
        student_list.append(new_student)
    search_for = Student("Nim", 4.0)
    print("Here is the list:", [str(student) for student in student_list])
    print()
    print('\t', search_for, " was found in the list?",
          bin_search(search_for, student_list))
    search_for = Student("Khaled", 4.0)
    print('\t', search_for, "was found in the list?",
          bin_search(search_for, student_list))
    search_for = Student("John", 4.0)
    print('\t', search_for, "was found in the list?",
          bin_search(search_for, student_list))
    print()

    # Task number 3
    print("Task #3")
    # The list size should be power of 2, but the assignment ask for 10 numbers
    lst = [None] * 10
    print("Here is the list:", lst)
    for i in range(10):
        try:
            value = random.randint(100, 999)
            print("\tThe value", value, "is in slot number", hash_rem(value, lst))
        except IndexError as ie:
            print("\t" + str(ie) + " for value " + str(value))
    print("Here is the list:", lst)
    print()

    # Task number 4
    print("Task #4")
    lst = [None] * 10
    print("Here is the list:", lst)
    for i in range(10):
        try:
            value = random.randint(100, 999)
            print("\tThe value", value, "is in slot number", hash_msq(value, lst))
        except IndexError as ie:
            print("\t" + str(ie) + " for value " + str(value))
    print("Here is the list:", lst)
    print()

    # Task number 5
    print("Task #5")
    lst = [None] * 5
    print("Here is the list:", lst)
    for i in ["cat", "algorithm", "logarithm", "dave", "deva"]:
        try:
            value = i
            print("\tThe value", value, "is in slot number", hash_str(value, lst))
        except IndexError as ie:
            print("\t" + str(ie) + " for value " + str(value))
    print("Here is the list:", lst)

 # Calling main function for program execution
if __name__ == "__main__":
    main()
