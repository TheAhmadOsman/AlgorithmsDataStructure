#!/usr/bin/env python3
# encoding: UTF-8

##########################################################################
#
# CS 160 - Week 11 Project
# Purpose: Morse Code Project
#
# Author: Ahmad M. Osman
# Date: April 26, 2017
#
# Filename: main.py
#
##########################################################################


class BinaryTree:
    """Binary Tree implementation as nodes and references"""

    def __init__(self, key):
        self._key = key
        self._child_left = None
        self._child_right = None

    def get_root_val(self):
        """Get root key value"""
        return self._key

    def set_root_val(self, new_key):
        """Set root key value"""
        self._key = new_key

    def get_child_left(self):
        """Get left child"""
        return self._child_left

    def set_child_left(self, new_child_left):
        """Set left child"""
        self._child_left = new_child_left

    def get_child_right(self):
        """Get right child"""
        return self._child_right

    def set_child_right(self, new_child_right):
        """Set right child"""
        self._child_right = new_child_right

    def is_leaf(self):
        """Check if a node is leaf"""
        return (not self._child_left) and (not self._child_right)

    def insert_left(self, new_node):
        """Insert left subtree"""
        new_subtree = BinaryTree(new_node)
        if self._child_left != None:
            new_subtree.set_child_left(self._child_left)
        self._child_left = new_subtree

    def insert_right(self, new_node):
        """Insert right subtree"""
        new_subtree = BinaryTree(new_node)
        if self._child_right != None:
            new_subtree.set_child_right(self._child_right)
        self._child_right = new_subtree


class Coder:
    """Morse code encoder and decoder"""

    def __init__(self, file_in):
        self.morse_tree = BinaryTree('')

        with open(file_in) as morse_file:
            for line in morse_file:
                letter, code = line.split()
                self.follow_and_insert(code, letter)

    def follow_and_insert(self, code_str, letter):
        """Follow the tree and insert a letter"""
        current = self.morse_tree
        for symbol in code_str:
            """if _dot_, go to to the left child, else go to the right child"""
            """create empty placeholder nodes (value of '') if necessary"""
            if symbol == '.':
                if current.get_child_left() == None:
                    current.insert_left('')
                current = current.get_child_left()
            else:
                if current.get_child_right() == None:
                    current.insert_right('')
                current = current.get_child_right()
        """set the node value to _letter_"""
        current.set_root_val(letter)

    def follow_and_retrieve(self, code_str):
        """Follow the tree and retrieve a letter"""
        current = self.morse_tree
        for symbol in code_str:
            """if _dot_, go to to the left child, else go to the right child"""
            if symbol == '.':
                current = current.get_child_left()
            else:
                current = current.get_child_right()
        """return the current node value"""
        return current.get_root_val()

    def find_path(self, tree, letter, path):
        """Find a key"""
        """Recursive function"""
        """Base case 1: letter found - return path"""
        """Base case 2: reached the end of a tree - return False"""
        """General case: update the path and search the left and/or right subtree"""
        if not tree:
            return False
        elif tree.get_root_val() == letter:
            return path
        else:
            return self.find_path(tree.get_child_left(), letter, path + '.') or self.find_path(tree.get_child_right(), letter, path + '-')

    def encode(self, msg):
        """Encode a message"""
        code = ''
        for word in msg.split():
            for letter in word:
                code = code + str(self.find_path(self.morse_tree, letter, '')) + ' '
        return code

    def decode(self, code):
        """Decode a message"""
        msg = ''
        for letter in code.split():
            msg = msg + self.follow_and_retrieve(letter)
        return msg


if __name__ == '__main__':
    morse_coder = Coder('morse.txt')
    print('Encoding "ahmad"')
    print('Expected: .- .... -- .- -..')
    print('Encoding: %s' % morse_coder.encode('ahmad'))
    print('Encoding "sos"')
    print('Expected: ... --- ...')
    print('Encoding: %s' % morse_coder.encode('sos'))
    print('Encoding "data structures"')
    print('Expected: -.. .- - .- ... - .-. ..- -.-. - ..- .-. . ... ')
    print('Encoding: %s' % morse_coder.encode('data structures'))
    print('Encoding "$$"')
    print('Expected: Error message')
    print('Encoding: %s' % morse_coder.encode('$$'))
    print('Decoding ".... . .-.. .-.. --- --..-- -.-. ... .---- -.... -----"')
    print('Expected: hello,cs160')
    print('Decoding: %s' % morse_coder.decode(
        '.... . .-.. .-.. --- --..-- -.-. ... .---- -.... -----'))
