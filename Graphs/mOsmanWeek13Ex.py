#!/usr/bin/env python3
# encoding: UTF-8

############################################################################
#
# CS 160 - Week 13 Exercise
# Purpose: Graphs' Practices
#
# Author: Ahmad M. Osman
# Date: May 8, 2017
#
# Filename: mOsmanWeek13Ex.py
#
############################################################################

from pythonds.graphs import PriorityQueue, Vertex


class Graph:
    '''Graph Class Implementation - Copied from Pythonds Book'''

    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self, f, t, cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

    def __str__(self):
        '''Task #3: printing all the edges of a graph in the following format: (vertex_from, vertex_to, cost)'''
        for k in self.vertList.keys():
            for ver in self.vertList[k].getConnections():
                print("\t(" + k + ", " + ver.getId() + ", " +
                      str(ver.getWeight(self.vertList.get(k))) + ")")
        return ""

    def count_vert(self):
        '''Task #4: printing the number of vertices in a graph'''
        print("\tThis graph has", self.numVertices, "vertices!")

    def find_hub(self):
        '''Task #5: printing the vertex with the most connections (edges)'''
        current = None
        count = 0
        for k in self.vertList.keys():
            if count < len(self.vertList[k].getConnections()):
                count = len(self.vertList[k].getConnections())
                current = k
        print("\tThe vertex '" + current +
              "' has the most connections with", count, "edges!")


def dijkstra(aGraph, start):
    '''Dijkstra’s Algorithm Implementation - Copied from Pythonds Book'''
    '''Edited for Task #1 and Task #2'''
    '''Finding the shortest path from any 'x' vertex to all other vertices in the network.'''
    '''Showing the change after each iteration.'''

    pq = PriorityQueue()
    start.setDistance(0)
    pq.buildHeap([(v.getDistance(), v) for v in aGraph])

    vert_lst = []
    dct = {}
    while not pq.isEmpty():
        lst = []
        currentVert = pq.delMin()
        vert_lst.append(currentVert.getId())
        for nextVert in currentVert.getConnections():
            newDist = currentVert.getDistance() \
                + currentVert.getWeight(nextVert)
            if newDist < nextVert.getDistance():
                nextVert.setDistance(newDist)
                nextVert.setPred(currentVert)
                pq.decreaseKey(nextVert, newDist)
                lst.append((nextVert.getId(), newDist))
        dct[currentVert.getId()] = lst

    # The printed changes are in the form of changes occured through a certain
    # vertex that led to a connection with (vertex, cost)
    # Notice that the output may slightly differ in execution(s) due to the
    # implementation of Graph Class using Dictionaries
    iter_count = 1
    for vert in vert_lst:
        print("\tIteration #" + str(iter_count) + "." + " Changes occured through vertex '" + vert +
              "' to find the shortest paths to other vertices for '" + start.getId() + "' are: " + str(dct[vert]))
        iter_count += 1


# Building the "network_1.PNG" graph
def build_graph():
    g = Graph()
    g.addEdge("t", "u", 2)
    g.addEdge("t", "v", 4)
    g.addEdge("t", "y", 7)
    g.addEdge("u", "v", 3)
    g.addEdge("u", "w", 3)
    g.addEdge("v", "w", 4)
    g.addEdge("v", "x", 3)
    g.addEdge("v", "y", 8)
    g.addEdge("w", "x", 6)
    g.addEdge("x", "y", 6)
    g.addEdge("x", "z", 8)
    g.addEdge("y", "z", 12)
    g.addEdge("u", "t", 2)
    g.addEdge("v", "t", 4)
    g.addEdge("y", "t", 7)
    g.addEdge("v", "u", 3)
    g.addEdge("w", "u", 3)
    g.addEdge("w", "v", 4)
    g.addEdge("x", "v", 3)
    g.addEdge("y", "v", 8)
    g.addEdge("x", "w", 6)
    g.addEdge("y", "x", 6)
    g.addEdge("z", "x", 8)
    g.addEdge("z", "y", 12)

    return g


# main function - program execution instructions
def main():

    # Task number 1
    print("Task #1")
    g = build_graph()
    dijkstra(g, g.getVertex("x"))
    print()

    # Task number 2
    print("Task #2")
    g = build_graph()
    dijkstra(g, g.getVertex("t"))
    print()

    # Task number 3
    print("Task #3")
    print(g)

    # Task number 4
    print("Task #4")
    g.count_vert()
    print()

    # Task number 5
    print("Task #5")
    g.find_hub()


# Calling main function for program execution
if __name__ == "__main__":
    main()
