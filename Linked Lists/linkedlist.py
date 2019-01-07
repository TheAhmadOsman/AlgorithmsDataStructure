#!/usr/bin/env python3
# encoding: UTF-8

##########################################################################
#
# CS 160 - Week 5 Exercise
# Purpose: Linked List Class Implementation
#
# Author: Ahmad M. Osman
# Date: March 4, 2017
#
# Filename: linkedlist.py
#
##########################################################################

from abc import ABC, abstractmethod
from node import Node


class LinkedList(ABC):

    @abstractmethod
    def __init__(self):
        self._head = None
        self._count = 0

    def is_empty(self):
        return self._count == 0

    def __len__(self):
        return self._count

    @abstractmethod
    def add(self, new_node):
        pass

    @abstractmethod
    def append(self, new_node):
        pass

    @abstractmethod
    def insert(self, new_node, position=None):
        pass

    @abstractmethod
    def index(self, value):
        pass

    @abstractmethod
    def remove(self):
        pass

    def pop(self, position=None):
        current = self._head
        if not current:
            raise IndexError("The linked list is empty!")

        previous = None
        if position == None or position >= self._count - 1:
            while current.next:
                previous = current
                current = current.next

            previous.next = None
            return current.data

        for item in range(position):
            previous = current
            current = current.next

        previous.next = current.next
        return current.data

    def __getitem__(self, rng):
        if isinstance(rng, int):
            if rng >= self._count or not(self._head):
                raise IndexError("Index " + str(rng) + " is not found!")
            else:
                current = self._head
                for i in range(rng):
                    current = current.next
                return current
        elif isinstance(rng, slice):
            # return a slice
            slice_lst = UnorderedLinkedList()
            slice_rng = list(range(rng.start, rng.stop))
            slice_count = 0
            current = self._head
            while current and slice_count < rng.start:
                current = current.next
                slice_count += 1
            while current and slice_count < rng.stop:
                slice_lst.append(Node(current.data))
                current = current.next
                slice_count += 1
            return slice_lst

    def __str__(self):
        all_nodes = []
        current = self._head
        while current:
            all_nodes.append(current.data)
            current = current.next
        return str(all_nodes)
