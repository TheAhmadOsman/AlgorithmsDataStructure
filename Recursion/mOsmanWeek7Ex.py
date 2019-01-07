#!/usr/bin/env python3
# encoding: UTF-8

############################################################################
#
# CS 160 - Week 7 Exercise
# Purpose: Recursion Practice
#
# Author: Ahmad M. Osman
# Date: March 19, 2017
#
# Filename: mOsmanWeek7Ex.py
#
############################################################################


# Iterative algorithm to calculate n-th number of the Fibonacci sequence.
def iter_feb(seq_num):
    num_1 = 0
    num_2 = 1
    count = 0
    while count < seq_num:
        if count == 0:
            count += 1
            print('\t', num_1)
        elif count == 1:
            count += 1
            print('\t', num_2)
        else:
            feb_num = num_1 + num_2
            print('\t', feb_num)
            num_1 = num_2
            num_2 = feb_num
            count += 1


# Recursive algorithm to calculate n-th number of the Fibonacci sequence.
def rec_fib(num):
    if num == 0:
        return num
    elif num == 1:
        return num
    else:
        return rec_fib(num - 1) + rec_fib(num - 2)


# Iterative algorithm to calculate factorial of a number.
def iter_fac(num):
    if num < 0:
        raise ValueError("Can not resolve", num, "factorial!")
    fact_num = 1
    while num >= 1:
        fact_num = fact_num * num
        num = num - 1
    return fact_num


# Recursive algorithm to calculate factorial of a number.
def rec_fac(num):
    if num < 1:
        return 1
    else:
        return num * rec_fac(num - 1)


# Recursive algorithm to square list elements
def rec_sq_lst(lst):
    if len(lst) == 0:
        return []
    elif len(lst) == 1:
        return [lst[0]**2]
    else:
        return [lst[0]**2] + rec_sq_lst(lst[1:])


# main function - program execution instructions
def main():
    # Task number 1
    print("Task #1")
    iter_feb(10)
    print()

    # Task number 2
    print("Task #2")
    for i in range(10):
        print('\t', rec_fib(i))
    print()

    # Task number 3
    print("Task #3")
    for i in range(1, 10):
        print('\t', iter_fac(i))
    print()

    # Task number 4
    print("Task #4")
    for i in range(1, 10):
        print('\t', rec_fac(i))
    print()

    # Task number 5
    print("Task #5")
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("\tOriginal list:", lst)
    print('\tSquared List:', rec_sq_lst(lst))

 # Calling main function for program execution
if __name__ == "__main__":
    main()
