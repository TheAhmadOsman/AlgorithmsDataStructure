#!/usr/bin/env python3
# encoding: UTF-8

############################################################################
#
# CS 160 - Week 4 Exercise
# Purpose: Stack ADT Practice & Extending Some Of The Textbook Functions
#
# Author: Ahmad M. Osman
# Date: February 25, 2017
#
# Filename: mOsmanWeek4Ex.py
#
############################################################################

from pythonds import Stack


# Reverse characters in a string without using a stack
def rev_string(my_str):
    rev_str = []
    str_len = len(my_str)
    for character in range(str_len):
        rev_str.append(my_str[(str_len - 1) - character])

    return ''.join(rev_str)


# Reverse characters in a string using a stack
def rev_string_s(my_str):
    rev_str_stack = Stack()
    for character in my_str:
        rev_str_stack.push(character)

    rev_str = []
    while not rev_str_stack.isEmpty():
        rev_str.append(rev_str_stack.pop())

    return ''.join(rev_str)


# Textbook parentheses checker implementation
def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False


# File's parentheses checker
def par_file_check(file_name):
    with open(file_name, 'r') as par:
        for line in par:
            if(parChecker(line.rstrip())):
                print(line.rstrip(), "is Balanced")
            else:
                print(line.rstrip(), "is Unbalanced")


# Textbook base converter implementation - exception added
def baseConverter(decNumber, base):
    digits = "0123456789ABCDEF"

    if base not in [2, 8, 16]:
        raise ValueError(
            "The base has to be either binary(base 2), octal(base 8), or hexadecimal(base 16).")

    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base

    newString = ""
    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()]

    return newString


# Textbook postfix evaluator implementation - exception added
def rpn_calc():
    postfixExpr = input(
        "Please enter an expression in Reverse Polish notation: ")
    operandStack = Stack()
    tokenList = postfixExpr.split()

    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token, operand1, operand2)
            operandStack.push(result)

    if operandStack.size() > 1:
        raise Exception("The expression is invalid.")

    return operandStack.pop()


# Textbook postfix evaluator implementation continued
def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2


# main function - program execution instructions
def main():
    # Task number 1
    str_to_rev = "Hello without Stack"
    print(str_to_rev, "is reversed to", rev_string(str_to_rev))
    print()

    # Task number 2
    str_to_rev_stack = "Hello with Stack"
    print(str_to_rev_stack, "is reversed to", rev_string_s(str_to_rev_stack))
    print()

    # Task number 3
    par_file_check("parentheses.txt")
    print()

    # Task number 4
    while True:
        num = int(input("Please enter a number: "))
        if num == 0:
            break
        base = int(input("Please enter a base to convert to: "))
        if base == 0:
            break

        try:
            print(baseConverter(num, base))
        except ValueError as v:
            print("Error!", v)
    print()

    # Task number 5
    try:
        print(rpn_calc())
    except Exception as e:
        print("Error!", e)

 # Calling main function for program execution
if __name__ == "__main__":
    main()
