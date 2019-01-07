#!/usr/bin/env python3
# encoding: UTF-8

############################################################################
#
# CS 160 - Week 10 Exercise
# Purpose: Binary Trees Practice - Task #1
#
# Author: Ahmad M. Osman
# Date: April 25, 2017
#
# Filename: tree_lst.py
#
############################################################################


def BinaryTree(r):
    return [r, [], []]


def insertLeft(root, newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [newBranch, t, []])
    else:
        root.insert(1, [newBranch, [], []])
    return root


def insertRight(root, newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [newBranch, [], t])
    else:
        root.insert(2, [newBranch, [], []])
    return root


def getRootVal(root):
    return root[0]


def setRootVal(root, newVal):
    root[0] = newVal


def getLeftChild(root):
    return root[1]


def getRightChild(root):
    return root[2]


def build_tree_lst():
    r = BinaryTree("a")
    insertLeft(r, "b")
    insertRight(r, "c")
    insertRight(getLeftChild(r), "d")
    insertLeft(getRightChild(r), "e")
    insertRight(getRightChild(r), "f")
    return r
