#!/usr/bin/env python3
# encoding: UTF-8

##########################################################################
#
# CS 160 - Week 9 Project
# Purpose: Word ladders program
#
# Author: Ahmad M. Osman
# Date: April 10, 2017
#
# Filename: main.py
#
##########################################################################

from DS import Stack, Queue


THREE_WORDS = set()
FOUR_WORDS = set()
FIVE_WORDS = set()


def read_words(file_name):
    with open(file_name, 'r') as file_in:
        for line in file_in:
            if len(line.rstrip()) == 3:
                THREE_WORDS.add(line.rstrip())
            elif len(line.rstrip()) == 4:
                FOUR_WORDS.add(line.rstrip())
            elif len(line.rstrip()) == 5:
                FIVE_WORDS.add(line.rstrip())


def similar_words(word, word_set):
    similar_words_lst = []

    for i in word_set:
        count = 0
        difference = 0
        for ch in word:
            if ch != i[count]:
                difference += 1
            count += 1
        if difference == 1:
            similar_words_lst.append(i)

    return similar_words_lst


# main function - program execution instructions
def main():

    starting_word = input("Enter starting word: ").lower()
    ending_word = input("Enter ending word: ").lower()
    if (len(starting_word) < 3 or len(starting_word) > 5) or (len(ending_word) < 3 or len(ending_word) > 5) or (len(starting_word) != len(ending_word)):
        print(
            "Both the starting and ending words have to be between three to five characters. Both words have to be in the same length too!")
        print("Please execute the program again if you want to use it! Program terminated!")
        exit()

    used_words = set()
    used_words.add(starting_word)
    read_words("words.txt")

    if len(starting_word) == 3:
        word_set = THREE_WORDS
    elif len(starting_word) == 4:
        word_set = FOUR_WORDS
    else:
        word_set = FIVE_WORDS

    lst = similar_words(starting_word, word_set)

    print("Processing...")

    words_queue = Queue()
    lst.sort()
    for i in lst:
        s = Stack()
        s.push(starting_word)
        s.push(i)
        used_words.add(i)
        words_queue.enqueue(s)

    loop_var = True
    current_stack = None
    found = False

    while loop_var and words_queue.size() > 1:
        current_stack = words_queue.dequeue()
        word = current_stack.pop()
        if word == ending_word:
            current_stack.push(word)
            loop_var = False
            found = True
            break
        else:
            lst = similar_words(word, word_set)
            lst.sort()
            used_words.add(word)
            current_stack.push(word)
            for i in lst:
                if i in used_words:
                    pass
                else:
                    s = current_stack.copy()
                    s.push(i)
                    used_words.add(i)
                    words_queue.enqueue(s)

    if found:
        # Please note the output is in LIFO order
        for i in range(current_stack.size()):
            print(current_stack.pop().upper())
    else:
        print("Could not find a word ladder for",
              starting_word.upper(), "and", str(ending_word.upper() + "!"))


# Calling main function for program execution
if __name__ == "__main__":
    main()
