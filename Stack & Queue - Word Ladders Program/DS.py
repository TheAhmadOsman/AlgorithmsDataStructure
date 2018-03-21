#!/usr/bin/env python3
# encoding: UTF-8

##########################################################################
#
# CS 160 - Week 9 Project
# Purpose: Stack & Queue Classes Implementation
#
# Author: Ahmad M. Osman
# Date: April 10, 2017
#
# Filename: DS.py
#
##########################################################################


class Stack:
    '''Stack Class Implementation'''

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def copy(self):
        new_stack = Stack()
        new_stack.items = list(self.items)
        return new_stack


class Queue:
    '''Queue Class Implementation'''

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
