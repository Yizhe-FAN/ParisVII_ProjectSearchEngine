#! /usr/bin/python3

import sys
import re


class MatriceCLI:
    nodesNumber = 0
    edgesNumber = 0
    table_C = []
    table_L = []
    table_I = []

    def __init__(self, filePath):
        with open(filePath) as f:
            nodes_edges = re.findall(r'\d', f.readline())
            self.nodesNumber = int(nodes_edges[0])
            self.edgesNumber = int(nodes_edges[1])
            last_node = -1
            count = 0
            lineBegin = 0
            line = f.readline()
            while line:
                nodes = re.findall(r'\d', line)
                src = int(nodes[0])
                dest = int(nodes[1])
                if last_node == -1:
                    self.table_L.append(0)
                elif src != last_node:
                    partition = count - lineBegin
                    for i in range(partition):
                        self.table_C.append(1.0 / partition)
                    self.table_L.append(count)
                    lineBegin = count
                self.table_I.append(dest)
                count += 1
                last_node = src
                line = f.readline()
            #write the last line of matrice into the table C and L
            partition = count - lineBegin
            for i in range(partition):
                self.table_C.append(1.0 / partition)
            self.table_L.append(count)


    def printMatriceInfo(self):
        print("Nodes Number: %d" % self.nodesNumber)
        print("Edges Number: %d" % self.edgesNumber)
        print("Table C: "+str(self.table_C))
        print("Table L: "+str(self.table_L))
        print("Table I: "+str(self.table_I))


m1 = MatriceCLI(sys.argv[1])
m1.printMatriceInfo()