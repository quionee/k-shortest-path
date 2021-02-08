import sys
import math
from fibheap import *

from graph import Graph

def readFile(fileName):
    filePath = "../updated_instances/" + fileName

    instance = open(filePath)

    line = instance.readline().split()

    numberOfNodes = int(line[0])
    numberOfArcs = int(line[1])

    nodesSet = []

    for i in range(1, numberOfNodes + 1):
        nodesSet.append(i)

    arcsSet = []
    for i in range(numberOfArcs):
        line = instance.readline().split()
        arcsSet.append([int(line[0]), int(line[1]), int(line[2])])

    graph = Graph(fileName, numberOfNodes, numberOfArcs, nodesSet, arcsSet)

    return graph


def dijkstra(graph, source):
    dist = {}
    previous = {}

    Q = makefheap()

    for node in graph.getNodesSet():
        dist[node] = math.inf
        previous[node] = None

        fheappush(Q, (dist[node], node))

    dist[source] = 0
    network = graph.getNetwork()

    while Q.num_nodes:
        u = fheappop(Q)
        
        neighbours = graph.getNodeNeighbours(u[1])
        for neighbour in neighbours:
            alt = dist[u[1]] + network[u[1], neighbour]

            if alt < dist[neighbour]:
                dist[neighbour] = alt
                previous[neighbour] = u[1]

    return dist, previous


def setShortestPath(dist, previous, originNode, destinyNode):
    notFoundShortestPath = True
    shortestPath = [destinyNode, previous[destinyNode]]
    currentNode = previous[destinyNode]

    while notFoundShortestPath:
        if shortestPath[-1] != originNode:
            shortestPath.append(previous[currentNode])
            currentNode = previous[currentNode]
        else:
            notFoundShortestPath = False

    return shortestPath[::-1]


def deviationPathProcedure(originNode, destinyNode, k, graph):
    # 01: Calculate the first shortest path p1 between the O-D pair.
    dist, previous = dijkstra(graph, originNode)
    p1 = setShortestPath(dist, previous, originNode, destinyNode)

    # print('\nDIST: \n\n', dist)
    # print('\n\nP1: \n\n', p1)
    # 02: Set candidate path collection C: { = p1} and set determined path collection L: = VAZIO.
    C = makefheap()
    fheappush(C, (dist[destinyNode], p1))
    L = []

    for j in range(1, k + 1):
        # If C = VAZIO, Then stop and return L.
        if not(C.num_nodes):
            return L

        # Set pj as the path at the top of C; and remove pj from C.
        pj = fheappop(C)

        # Add pj into L.
        L.append(pj)

        # 07: Call CalDevPaths Procedure to calculate deviation path set Dj. (algorithms different here)
        Dj = yensAlgorithm()

        fheapunion(C, Dj)

    return L


def yensAlgorithm():
    print('Yen\'s Algorithm')


def mpsAlgorithm():
    print('M-P\'s Algorithm')


def main(args):
    fileName = args[1]

    graph = readFile(fileName)

    originNode = 1
    destinyNode = 100
    k = 2

    deviationPathProcedure(originNode, destinyNode, k, graph)


if __name__ == "__main__":
    main(sys.argv)
