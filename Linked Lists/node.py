#!/usr/bin/env python3
# encoding: UTF-8

##########################################################################
#
# CS 160 - Week 5 Exercise
# Purpose: Node Class Implementation
#
# Author: Ahmad M. Osman
# Date: March 4, 2017
#
# Filename: node.py
#
##########################################################################


class Node:

    def __init__(self, node_data=None):
        self._data = node_data
        self._next = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, node_data):
        self._data = node_data

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, node_next):
        self._next = node_next

    def __str__(self):
        return str(self._data)
