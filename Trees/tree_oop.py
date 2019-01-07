#!/usr/bin/env python3
# encoding: UTF-8

############################################################################
#
# CS 160 - Week 10 Exercise
# Purpose: Binary Trees Practice - Task #2 & Task #3
#
# Author: Ahmad M. Osman
# Date: April 25, 2017
#
# Filename: tree_oop.py
#
############################################################################


class BinaryTree:

    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key

    def height(self, path):
        leftPath = 0
        rightPath = 0
        if self.key == None:
            return 0
        elif self.rightChild == None and self.leftChild == None:
            return path
        else:
            path += 1
            if self.rightChild != None:
                rightPath = self.rightChild.height(path)
            if self.leftChild != None:
                leftPath = self.leftChild.height(path)
            if rightPath > leftPath:
                return rightPath
            else:
                return leftPath


def build_tree_oop():
    r = BinaryTree("a")
    r.insertLeft("b")
    r.insertRight("c")
    r.getLeftChild().insertRight("d")
    r.getRightChild().insertLeft("e")
    r.getRightChild().insertRight("f")
    print("\tRoot: ", r.getRootVal())
    print("\t\tLeft Child:", r.getLeftChild().getRootVal())
    print("\t\t\tRight Child of the above root('b'):",
          r.getLeftChild().getRightChild().getRootVal())
    print("\t\tRight Child:", r.getRightChild().getRootVal())
    print("\t\t\tLeft Child of the above root('c'):",
          r.getRightChild().getLeftChild().getRootVal())
    print("\t\t\tRight Child of the above root('c'):",
          r.getRightChild().getRightChild().getRootVal())
    return r
