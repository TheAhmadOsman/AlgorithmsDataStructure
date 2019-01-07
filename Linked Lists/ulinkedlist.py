#!/usr/bin/env python3
# encoding: UTF-8

##########################################################################
#
# CS 160 - Week 5 Exercise
# Purpose: Unordered Linked List Implementation
#
# Author: Ahmad M. Osman
# Date: March 4, 2017
#
# Filename: ulinkedlist.py
#
##########################################################################

from linkedlist import LinkedList


class UnorderedLinkedList(LinkedList):

    def __init__(self):
        # LinkedList.__init__(self)
        super().__init__()

    def add(self, new_node):
        '''Add a new node at the beginning of a list'''
        new_node.next = self._head
        self._head = new_node
        self._count += 1

    def append(self, new_node):
        '''Add a new node at the end of a list'''
        if not self._head:
            self._head = new_node
            self._count += 1
            return
        current = self._head
        while current.next:
            current = current.next
        current.next = new_node
        self._count += 1

    def insert(self, new_node, position=None):
        if position == None:
            self.append(new_node)
            return

        if not self._head:
            self._head = new_node
            self._count += 1
            return

        current = self._head

        if position >= self._count:
            while current.next:
                current = current.next
            current.next = new_node
            self._count += 1
            return

        prev = None

        for i in range(position):
            prev = current
            current = current.next
        prev.next = new_node
        new_node.next = current

    def index(self, value):
        current = self._head
        idx = 0
        while current:
            if current.data != value:
                current = current.next
                idx += 1
            else:
                return idx
        raise ValueError("Value " + str(value) +
                         " is not available in the linked list")

    def remove(self, value):
        '''Remove a node with the specified value from a list'''
        prev = None
        current = self._head
        while current and current.data != value:
            prev = current
            current = current.next
        if current:
            if prev:
                prev.next = current.next
            else:
                self._head = current.next
            del current
            self._count = self._count - 1
