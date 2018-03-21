#!/usr/bin/env python3
# encoding: UTF-8

########################################################################
#
# CS 160 - Week 4 Project
# Purpose: Reverse Polish Notation Expressions Evaluator.
#
# Author: Ahmad M. Osman
# Date: February 27, 2017
#
# Filename: mOsmanWeek4Project.py
#
########################################################################

from pythonds import Stack


def eval_expr(expr):
    s = Stack()
    for token in expr.split():
        if token in ['+', '-', '*', '/', '//', '%', '**']:
            if s.size() < 2:
                raise IndexError("Empty Stack, too few operands.")
            else:
                op2 = s.pop()
                op1 = s.pop()
                result = do_math(op1, op2, token)
                s.push(result)
        elif token == '=':
            if s.size() > 1:
                raise IndexError("Stack is not empty, too many operands.")
            else:
                return s.pop()
        # Unknown operator was not on the assignment but I accounted for it.
        # E.g. '?' would be seen as an unknown operator in any expression.
        elif token not in ['+', '-', '*', '/', '//', '%', '**', '='] and not token.isdigit():
            raise ValueError("Invalid operator.")
        else:
            s.push(int(token))


def do_math(op1, op2, op):
    if op == '+':
        return op1 + op2
    elif op == '-':
        return op1 - op2
    elif op == '*':
        return op1 * op2
    elif op == '/':
        if op2 == 0:
            raise ZeroDivisionError("Can not divide by zero.")
        else:
            return op1 / op2
    elif op == '//':
        if op2 == 0:
            raise ZeroDivisionError("Can not do integer division by zero.")
        else:
            return op1 // op2
    elif op == '%':
        if op2 == 0:
            raise ZeroDivisionError(
                "Can not get the reminder of a division by zero.")
        else:
            return op1 % op2
    elif op == '**':
        return op1 ** op2


# main function - program execution instructions
def main():
    # Files with expressions to read from
    # Added 2 files as a test case for invalid files
    files_names = ["expressions.txt", "expressions2.txt",
                   "failure.test", "failure_but_program_is_already_terminated"]

    # Processing expressions from each file in the list files_names
    for i in range(len(files_names)):
        checksum = 0
        print("Evaluating expression from file:", files_names[i])

        # Accessing file for expressions evaluation and catching exceptions
        try:
            with open(files_names[i], 'r') as source:
                for line in source:
                    # Printing expression
                    print("\t{:60}".format(line.strip()), end=' ')
                    # Processing expression and catching exceptions
                    try:
                        result = eval_expr(line.strip())
                        checksum += result
                        print(result)
                    except ZeroDivisionError as zde:
                        print("Zero Division Error!", zde)
                    except IndexError as ie:  # Well, ie could have been Internet Explorer but thanks god this is not a web programming course!
                        print("Operands Error!", ie)
                    except ValueError as ve:
                        print("Operator Error!", ve)
                    # Accounting for other possible exceptions - good practice for trial and
                    # error generally - helpful if something unexpected happend and is to
                    # be reported
                    except Exception as e:
                        print("Error!", e)
        except FileNotFoundError:
            print("\tFile Error! File name", files_names[
                  i], "is not found, program will be terminated.")
            # Calling quit function as the assignment asks for the program to
            # be terminated if the file is not valid. Keeping in mind that this
            # is required since I have a loop going through a list of all the
            # expressions' files
            quit()
        # Accounting for other possible exceptions
        except Exception as e:
            print("Error!", e)
            quit()

        print("\t\tChecksum: {:5.2f}".format(checksum))

        if(i != len(files_names) - 1):
            print("\n")


# Calling main function for program execution
if __name__ == "__main__":
    main()
