#! /usr/bin/python3

import re


class MatriceCLI:
    nodesNumber = 0
    edgesNumber = 0
    table_C = []
    table_L = []
    table_I = []

    def __init__(self, filePath):
        self.table_L.append(0)
        lastNode = 0
        count = 0
        nodeCount = 0
        nodeBegin = 0
        with open(filePath) as f:
            line = f.readline()
            while line:
                if re.search(r'#', line):
                    if re.search(r'Nodes:.*Edges:',line):
                        nodes_edges = re.findall(r'\d', line)
                        self.nodesNumber = int(nodes_edges[0])
                        self.edgesNumber = int(nodes_edges[1])
                    line = f.readline()
                    continue

                edges = re.findall(r'\d', line)
                src = int(edges[0])
                dest = int(edges[1])

                # finish reading the connections of a node and write them into C and L
                if src != lastNode:
                    nodeCount += 1
                    partition = count - nodeBegin
                    for i in range(partition):
                        self.table_C.append(1.0 / partition)
                    self.table_L.append(count)
                    nodeBegin = count

                    # if there are some nodes who have 0 connections
                    if src != lastNode + 1:
                        for i in range(src - lastNode - 1):
                            self.table_L.append(count)

                self.table_I.append(dest)
                count += 1
                lastNode = src
                line = f.readline()

        # write the last node of the file into the table C and L
        nodeCount += 1
        partition = count - nodeBegin
        for i in range(partition):
            self.table_C.append(1.0 / partition)
        self.table_L.append(count)

        # write the last nodes who do not have connections into L
        for i in range(self.nodesNumber - nodeCount):
            self.table_L.append(count)


    def printMatriceInfo(self):
        print("Nodes Number: %d" % self.nodesNumber)
        print("Edges Number: %d" % self.edgesNumber)
        print("Table C: "+str(self.table_C))
        print("Table L: "+str(self.table_L))
        print("Table I: "+str(self.table_I))


# test_m = MatriceCLI("data/tp1-n4e4.txt")
# test_m.printMatriceInfo()