#!/usr/bin/env python3
# encoding: UTF-8

##########################################################################
#
# CS 160 - Week 5 Exercise
# Purpose: Linked List(s) Implementation & Extending
#          The Textbook Palindrome Checker
#
# Author: Ahmad M. Osman
# Date: March 4, 2017
#
# Filename: main.py
#
##########################################################################

from palch import palchecker
from ulinkedlist import UnorderedLinkedList
from node import Node
import random
from olinkedlist import OrderedLinkedList


# Task number 1 execution
def pal_ch():
    # Task number 1
    print("Task #1 - Palindrome Checker")
    pal_str = ["lsdkjfskf", "lsdkj fskf", "lsdkjfsk", "ls dkjf skf", "radar",
               "r adar", "IPR EF ERPI", "rad ar", "ra dar", "IPREFERPI", "I PREFER PI", "I P R EFE R PI"]

    for i in range(len(pal_str)):
        print('\t', pal_str[i] + ":", palchecker(pal_str[i]))
    print()


# Task number 2 execution
def ull_test():
    # Task number 2.1 - append
    print("Task #2.1 - ULL: append function")
    ull = UnorderedLinkedList()
    for ran_item in range(5):
        n = Node(random.randint(1, 10))
        ull.append(n)
        print("\t #{}: {}".format(len(ull), ull))
    print()

    # Task number 2.2 - insert
    print("Task #2.2 - ULL: insert function")
    ull.insert(Node(5))
    print("\t Inserting as append:", ull)
    ull.insert(Node(7), 10)
    print("\t Inserting out of reach:", ull)
    ull.insert(Node(44), 3)
    print("\t Inserting at index(3):", ull)

    ull2 = UnorderedLinkedList()
    ull2.insert(Node(55))
    print("\t Inserting at an empty Linked List:", ull2)
    print()

    # Task number 2.3 - index
    print("Task #2.3 - ULL: index function")
    print("\t The ULL:", ull)
    print("\t ull: The value of 44, is at index number:", ull.index(44))

    for ran_item in range(5):
        n = random.randint(1, 10)

        try:
            print("\t The value of", n,
                  "in ull, is at index number:", ull.index(n))
        except ValueError as ve:
            print("\t Error!", ve)

    try:
        print("\t The value of 30, in ull2, is at index number:", ull2.index(30))
    except ValueError as ve:
        print("\t ull2: Error!", ve)

    print()

    # Task number 2.4 - pop
    print("Task #2.4 - ULL: pop function")
    print("\t The ULL before popping:", ull)
    print("\t Popping value out of index 3:", ull.pop(3))
    print("\t The ULL after popping:", ull)
    ull3 = UnorderedLinkedList()
    try:
        print("\t Trying to pop from empty linked list: ", ull3.pop(2))
    except IndexError as ie:
        print("\t Error!", ie)
    print("\t Popping value without index:", ull.pop())
    print("\t The ULL after popping:", ull)
    print("\t Popping value out of index 100:", ull.pop(100))
    print("\t The ULL after popping:", ull)
    print()


# Task number 3 execution
def oll_test():
    # Task number 3.1 - append
    print("Task #3.1 - OLL: append function")
    oll = OrderedLinkedList()
    for ran_item in range(5):
        n = Node(random.randint(1, 10))
        oll.append(n)
        print("\t #{}: {}".format(len(oll), oll))
    print()

    # Task number 3.2 - insert
    print("Task #3.2 - OLL: insert function")
    for ran_item in range(5):
        n = Node(random.randint(1, 10))
        oll.insert(n, ran_item)
        print("\t #{}: {}".format(len(oll), oll))
    print()

    # Task number 3.3 - index
    print("Task #3.3 - OLL: index function")
    print("\t The OLL:", oll)
    for ran_item in range(5):
        n = random.randint(1, 10)

        try:
            print("\t The value of", n,
                  "in oll, is at index number:", oll.index(n))
        except ValueError as ve:
            print("\t Error!", ve)
    print()

    # Task number 3.4 - pop
    print("Task #3.4 - OLL: pop function")
    print("\t The OLL before popping:", oll)
    print("\t Popping value out of index 3:", oll.pop(3))
    print("\t The OLL after popping:", oll)
    oll2 = UnorderedLinkedList()
    try:
        print("\t Trying to pop from empty linked list: ", oll2.pop(2))
    except IndexError as ie:
        print("\t Error!", ie)
    print("\t Popping value without index:", oll.pop())
    print("\t The OLL after popping:", oll)
    print("\t Popping value out of index 100:", oll.pop(100))
    print("\t The OLL after popping:", oll)
    print()


# Task number 4 execution
def ll_str():
    # Task number 4.01 - print ULL in Python's list way
    print("Task #4.01 - ULL: getitem magic method")
    ull = UnorderedLinkedList()
    for ran_item in range(5):
        n = Node(random.randint(1, 10))
        ull.append(n)
    print("\t The ULL:", ull)
    print()

    # Task number 4.02 - print OLL in Python's list way
    print("Task #4.02 - ULL: getitem magic method")
    oll = OrderedLinkedList()
    for ran_item in range(5):
        n = Node(random.randint(1, 10))
        oll.append(n)
    print("\t The OLL:", oll)
    print()


# Task number 5 execution
def ll_get():
    # Task number 5.01 - getitem
    print("Task #5.01 - ULL: getitem magic method")
    ull = UnorderedLinkedList()
    for ran_item in range(5):
        n = Node(random.randint(1, 10))
        ull.append(n)
    print("\t The ULL:", ull)

    for ran_item in range(5):
        n = random.randint(1, 7)
        try:
            print("\t The index", n,
                  "in ull, has the value", ull[n])
        except IndexError as ie:
            print("\t Error!", ie)

    ull2 = UnorderedLinkedList()
    try:
        print("\t The index", n,
              "in ull, has the value", ull2[2])
    except IndexError as ie:
        print("\t Trying to getitem from an empty linked list!", ie)

    print()

    # Task number 5.02 - getitem
    print("Task #5.02 - OLL: getitem magic method")
    oll = OrderedLinkedList()
    for ran_item in range(5):
        n = Node(random.randint(1, 10))
        oll.append(n)
    print("\t The OLL:", oll)

    for ran_item in range(5):
        n = random.randint(1, 7)
        try:
            print("\t The index", n,
                  "in ull, has the value", oll[n])
        except IndexError as ie:
            print("\t Error!", ie)

    oll2 = OrderedLinkedList()
    try:
        print("\t The index", n,
              "in ull, has the value", oll2[2])
    except IndexError as ie:
        print("\t Trying to getitem from an empty linked list!", ie)


# main function - program execution instructions
def main():
    pal_ch()
    ull_test()
    oll_test()
    ll_str()
    ll_get()

# Calling main function for program execution
if __name__ == "__main__":
    main()
