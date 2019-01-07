#!/usr/bin/env python3
# encoding: UTF-8

############################################################################
#
# CS 160 - Week 9 Exercise
# Purpose: Sorting Algorithms & Their Performance
#
# Author: Ahmad M. Osman
# Date: April 8, 2017
#
# Filename: mOsmanWeek9Ex.py
#
############################################################################

import random
import time


# Selection Sort Algorithm Implementation
def selectionSort(alist):
    for fillslot in range(len(alist) - 1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillslot + 1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location

        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp


# Merge Sort Algorithm Implementation
def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1


# Buble Sort Algorithm Implementation
def bubbleSort(alist):
    for passnum in range(len(alist) - 1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp


# Buble Sort Algorithm Implementation - Simultaneous Assignment Version
def bubbleSortSim(alist):
    for passnum in range(len(alist) - 1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]


# Shell Sort Algorithm Implementation
def shellSort(alist, increment=2):
    sublistcount = len(alist) // increment
    while sublistcount > 0:

        for startposition in range(sublistcount):
            gapInsertionSort(alist, startposition, sublistcount)

        sublistcount = sublistcount // increment


# Shell Sort Algorithm Implementation
def gapInsertionSort(alist, start, gap):
    for i in range(start + gap, len(alist), gap):

        currentvalue = alist[i]
        position = i

        while position >= gap and alist[position - gap] > currentvalue:
            alist[position] = alist[position - gap]
            position = position - gap

        alist[position] = currentvalue


# Merge Sort Algorithm Implementation - Loop Version
def mergeSortLoop(alist):
    if len(alist) > 1:

        lefthalf = []
        righthalf = []

        for i in range(len(alist)):
            if i < len(alist) // 2:
                lefthalf.append(alist[i])
            else:
                righthalf.append(alist[i])

        mergeSortLoop(lefthalf)
        mergeSortLoop(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1


# Quick Sort Algorithm Implementation
def quickSort(alist):
    quickSortHelper(alist, 0, len(alist) - 1)


# Quick Sort Algorithm Implementation
def quickSortHelper(alist, first, last):
    if first < last:

        splitpoint = partition(alist, first, last)

        quickSortHelper(alist, first, splitpoint - 1)
        quickSortHelper(alist, splitpoint + 1, last)


# Quick Sort Algorithm Implementation
def partition(alist, first, last):
    pivotvalue = alist[first]

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark


# Quick Sort Algorithm - Median-Of-Three Pivot Value Implementation
def quickSortM(alist):
    quickSortHelperM(alist, 0, len(alist) - 1)


# Quick Sort Algorithm - Median-Of-Three Pivot Value Implementation
def quickSortHelperM(alist, first, last):
    if first < last:

        splitpoint = partitionM(alist, first, last)

        quickSortHelperM(alist, first, splitpoint - 1)
        quickSortHelperM(alist, splitpoint + 1, last)


# Quick Sort Algorithm - Median-Of-Three Pivot Value Implementation
def partitionM(alist, first, last):
    medianList = [alist[first], alist[((first + last) // 2)], alist[last]]
    medianList.sort()
    pivotvalue = medianList[1]

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark


# main function - program execution instructions
def main():
    # Task number 1
    print("Task #1")

    lst1 = [random.randint(1, 1000) for i in range(1000)]
    lst2 = lst1

    time_before = time.time()
    selectionSort(lst1)
    time_after = time.time()
    time_diff = time_after - time_before
    print("\tSelection sort took", time_diff, "second(s)!")

    time_before = time.time()
    mergeSort(lst2)
    time_after = time.time()
    time_diff = time_after - time_before
    print("\tMerge sort took", time_diff, "second(s)!")
    print()

    # Task number 2
    print("Task #2")
    lst1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    bubbleSort(lst1)
    print("\tBubble sort book implementation list sorted:", lst1)

    lst2 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    bubbleSortSim(lst2)
    print("\tSimultaneous assignment implementation list sorted:", lst2)
    print("\tBoth lists are equal?", lst1 == lst2)
    print()

    # Task number 3
    print("Task #3")
    lst1 = [random.randint(1, 1000) for i in range(1000)]
    for i in range(2, 7):
        lst = lst1
        time_before = time.time()
        shellSort(lst, i)
        time_after = time.time()
        time_diff = time_after - time_before
        print("\tShell sort with increments of size",
              i, "took", time_diff, "second(s)!")
    print()

    # Task number 4
    print("Task #4")
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print("\tMerge sort will be executed on: ", alist)
    mergeSortLoop(alist)
    print("\tList after sorting:", alist)
    print()

    # Task number 5
    print("Task #5")

    lst1 = [random.randint(1, 1000) for i in range(1000)]
    lst2 = lst1

    time_before = time.time()
    quickSort(lst1)
    time_after = time.time()
    time_diff1 = time_after - time_before
    print("\tQuick sort book implementation took", time_diff1, "second(s)!")

    time_before = time.time()
    quickSortM(lst2)
    time_after = time.time()
    time_diff2 = time_after - time_before
    print("\tMedian-of-three implementation took", time_diff2, "second(s)!")
    if time_diff1 > time_diff2:
        print("\tMedian-of-three implementation is faster!")
    elif time_diff2 > time_diff1:
        print("\tBook implementation is faster!")
    else:
        print("\tBoth implementations are equal!")


# Calling main function for program execution
if __name__ == "__main__":
    main()
