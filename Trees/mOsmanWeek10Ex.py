#!/usr/bin/env python3
# encoding: UTF-8

############################################################################
#
# CS 160 - Week 10 Exercise
# Purpose: Binary Trees Practice
#
# Author: Ahmad M. Osman
# Date: April 25, 2017
#
# Filename: mOsmanWeek10Ex.py
#
############################################################################

from tree_lst import build_tree_lst
from tree_oop import build_tree_oop
from bin_heap import BinaryHeap
from bin_heap_max import BinaryHeapMax


# main function - program execution instructions
def main():
    # Task number 1
    print("Task #1")
    r1 = build_tree_lst()
    print("\t", r1)
    print()

    # Task number 2
    print("Task #2")
    r2 = build_tree_oop()
    print()

    # Task number 3
    print("Task #3")
    print("\tThe height of the tree of Task #2 is:", r2.height(0))
    print()

    # Task number 4
    print("Task #4")
    lst = [5, 2, 44, 15, 10, 9, 56, 77, 1, 14, 34, 95, 115, 6, 260]
    binary_heap = BinaryHeap()
    binary_heap.heapify(lst)
    print("\tThe list: ", lst)
    print("\tMax Binary Heap: ", binary_heap)
    print()

    # Task number 5
    print("Task #5")
    binary_heap_max = BinaryHeapMax()
    binary_heap_max.heapify(lst)
    print("\tThe list: ", lst)
    print("\tMax Binary Heap of 8 elements: ", binary_heap_max)


# Calling main function for program execution
if __name__ == "__main__":
    main()
