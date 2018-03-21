#!/usr/bin/env python3
# encoding: UTF-8

##########################################################################
#
# CS 160 - Week 8 Project
# Purpose: MAP ADT Implementation
#
# Author: Ahmad M. Osman
# Date: April 3, 2017
#
# Filename: Map.py
#
##########################################################################


class Map:
    '''Map ADT implementation'''

    def __init__(self, size_=8):
        '''Create a Map object'''
        self._items = [None] * size_
        self._size = size_
        self._keys = set()

    def rehash(self, key_, k_=0):
        '''Re-hash function'''
        return (key_ % self._size + k_ * k_) % self._size

    def put(self, key_, val_):
        '''Add a new key-value pair to the map. If the key is already in the map then replace the old value with the new value'''
        # Store key:value as a tuple (key, value) in the list of items
        pos = self.rehash(key_)
        # Adding a new item
        if not self._items[pos]:
            self._items[pos] = (key_, val_)
            self._keys.add(key_)
            return
        else:
            # Resolving a collision
            for k in range(self._size):
                pos = self.rehash(key_, k)
                # Found an empty spot
                if not self._items[pos]:
                    self._items[pos] = (key_, val_)
                    self._keys.add(key_)
                    return
                # Found an item to update
                elif self._items[pos][0] == key_:
                    self._items[pos] = (key_, val_)
                    return
        # Failing to add value processing
        if None not in self._items:
            raise IndexError("\tCould not add " + str(val_) + " with key " +
                             str(key_) + " to the hash table. The hash table is full!")
        else:
            raise IndexError("\tCould not add " + str(val_) + " with key " +
                             str(key_) + " to the hash table due to multiple collisions!")

    def __setitem__(self, key_, val_):
        '''Using [] to set item value'''
        return self.put(key_, val_)

    def get(self, key_):
        '''Given a key, return the value stored in the map or None otherwise'''
        # Return None if the key is not in the hash table
        if not key_ in self._keys:
            return None
        # Processing the table to find the value associated with key
        counter = 0
        while counter <= self._size:
            pos = self.rehash(key_, counter)
            if self._items[pos][0] == key_:
                return self._items[pos][1]
            counter += 1

    def __getitem__(self, key_):
        '''Using [] to retrieve item value'''
        return self.get(key_)

    def __contains__(self, key_):
        '''Return True for a statement of the form key in map, if the given key is in the map, False otherwise'''
        return key_ in self._keys

    def __len__(self):
        '''Return the number of key-value pairs stored in the map'''
        return self._size - self._items.count(None)

    def __str__(self):
        '''Return the string representation of the map object'''
        return str([i for i in self._items if i])
