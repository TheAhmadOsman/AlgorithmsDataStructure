#!/usr/bin/env python3
# encoding: UTF-8

##########################################################################
#
# CS 160 - Week 5 Exercise
# Purpose: Ordered Linked List Implementation
#
# Author: Ahmad M. Osman
# Date: March 4, 2017
#
# Filename: olinkedlist.py
#
##########################################################################

from linkedlist import LinkedList


class OrderedLinkedList(LinkedList):

    def __init__(self):
        super().__init__()

    def add(self, new_node):
        if not self._head:
            new_node.next = self._head
            self._head = new_node
            self._count += 1
            return

        if self._head.data > new_node.data:
            new_node.next = self._head
            self._head = new_node
            self._count += 1
            return

        current = self._head

        while current.next and new_node.data > current.next.data:
            current = current.next
        new_node.next = current.next
        current.next = new_node

        self._count += 1

    def append(self, new_node):
        self.add(new_node)

    def insert(self, new_node, position=None):
        self.add(new_node)

    def index(self, value):
        if not self._head or self._head.data > value:
            raise ValueError("Value " + str(value) +
                             " is not available in the linked list")

        current = self._head
        idx = 0
        while current.data < value:
            if current.next:
                current = current.next
                idx += 1
            else:
                raise ValueError("Value " + str(value) +
                                 " is not available in the linked list")

        if current.data == value:
            return idx
        else:
            raise ValueError("Value " + str(value) +
                             " is not available in the linked list")

    def remove(self, value):
        '''Remove a node with the specified value from a list'''
        pass
