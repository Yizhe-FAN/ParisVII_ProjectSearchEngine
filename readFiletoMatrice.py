#! /usr/bin/python2

import sys
import re


class Matrice:
    nodesNumber = 0
    edgesNumber = 0
    dic_srcToDest = {}
    table_C = []
    table_L = []
    table_I = []

    def __init__(self, filePath):
        with open(filePath) as f:
            nodes_edges = re.findall(r'\d', f.readline())
            self.nodesNumber = int(nodes_edges[0])
            self.edgesNumber = int(nodes_edges[1])
            for lineNo in range(self.edgesNumber):
                nodes = re.findall(r'\d', f.next())
                src = int(nodes[0])
                dest = int(nodes[1])
                if self.dic_srcToDest.has_key(src):
                    self.dic_srcToDest[src].append(dest)
                else:
                    self.dic_srcToDest[src] = []
                    self.dic_srcToDest[src].append(dest)
        count = 0
        self.table_L.append(0)
        for i in range(self.nodesNumber):
            if self.dic_srcToDest.has_key(i):
                value = self.dic_srcToDest[i]
                partition = len(value)
                for i in range(partition):
                    self.table_C.append(1.0/partition)
                    count += 1
                    self.table_I.append(value[i])
            self.table_L.append(count)


    def printMatrice(self):
        print "Nodes Number: %d" % self.nodesNumber
        print "Edges Number: %d" % self.edgesNumber
        print "Dictionary source to Destination: ", self.dic_srcToDest
        print "Table C: ", self.table_C
        print "Table L: ", self.table_L
        print "Table I: ", self.table_I


m1 = Matrice(sys.argv[1])
m1.printMatrice()