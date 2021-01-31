import sys
from fibheap import *

from graph import Graph

def readFile(fileName):
    instance = open(fileName)

    name = instance.readline().rstrip("\n").split()[-1]

    instance.readline()
    instance.readline()

    numberOfNodes = int(instance.readline().rstrip("\n").split()[-1])
    numberOfArcs = numberOfNodes**2

    instance.readline()
    instance.readline()
    instance.readline()

    matrix = []

    for i in range(numberOfNodes):
        line = instance.readline().split()
        line = list(map(int, line))

        row = []

        for j in range(numberOfNodes):
            row.append(line[j])
        
        matrix.append(row)

    graph = Graph(name, numberOfNodes, numberOfArcs, matrix)

    return graph


def deviationPathProcedure(O-D-pair, k):
    # 01: Calculate the first shortest path p1 between the O-D pair
    
    C = makefheap()
    fheappush(C, (pathCost, p1))

    L = []

    for j in range(k)
        if not(len(C) != 0):
            return L
        
        pj = getfheapmin(C)
        fheappop(C)

        L.append(pj)

        # 07: Call CalDevPaths Procedure to calculate deviation path set Dj. (algorithms different here)
        # Dj

        fheapunion(C, Dj)

    return L


# Input: O-D pair, k
# Return: Determined path collectionL
# 01: Calculate the first shortest path p1 between the O-D pair.
# 02: Set candidate path collection C: { = p1} and set determined path collection L: = .
# 03: For j := 1 to k
    # 04: If C = , Then stop and return L.
    # 05: Set p j as the path at the top of C; and remove p j from C.
    # 06: Add p j into L.
    # 07: Call CalDevPaths Procedure to calculate deviation path set Dj. (algorithms different here)
    # 08: Set C: C D = j.
# # 09: End for
# 10: Return L.


def main(args):
    # print('ARGS: ', args)
    # fileName = args[1]

    # filePath = "../instances/" + fileName

    # graph = readFile(filePath)

    # print(graph.printGraphInfo())




if __name__ == "__main__":
    main(sys.argv)
