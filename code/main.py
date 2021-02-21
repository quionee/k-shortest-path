import sys
import math
import copy
from fibheap import *

from graph import Graph
from tree_of_paths import TreeOfPaths

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

    # Cria árvore de desvios
    L = TreeOfPaths()

    # print('L: ', L.getTreeOfPaths())
    # L.addNewPath((10, [1, 2, 4, 10]), 1)
    # L.addNewPath((12, [1, 3, 6, 8, 7, 10]), 3)
    # L.addNewPath((14, [1, 3, 6, 8, 9, 10]), 8)

    deviationVertex = 1

    for j in range(1, k + 1):
        # If C = VAZIO, Then stop and return L.
        if not(C.num_nodes):
            return L

        # Set pj as the path at the top of C; and remove pj from C.
        pj = fheappop(C)

        # Add pj into L.
        L.addNewPath(pj, deviationVertex)

        # print(graph.printGraphInfo())

        # 07: Call CalDevPaths Procedure to calculate deviation path set Dj. (algorithms different here)
        Dj, deviationVertex = yensAlgorithm(graph.getNodesSet(), graph.getNetwork(), pj, L)

        fheapunion(C, Dj)

    return L


def restoreNetwork():
    print('restore network')


def findDeviationVertex(path, L):
    deviationVertex = 1
    setOfAssociatedDeviationArcs = [(1, 3)]

    # for p in L.getTreeOfPaths().values():

    return 1, setOfAssociatedDeviationArcs


def yensAlgorithm(nodesSet, arcsSet, pj, L):
    numberOfArcsOfPj = len(pj[1])
    setOfDeviationPath = []

    # 01: Call FindFirstDevNode(p_j, L)
    # to determine the first deviation node nmj of pj and the associated deviation link set Emj at nmj.
    deviationVertex, setOfAssociatedDeviationArcs = findDeviationVertex(pj, L)

    m = nodesSet.index(deviationVertex)
    l = numberOfArcsOfPj - 1
    # print('\n\nl: ', pj[1], numberOfArcsOfPj, l, '\n\n')

    # 02: Remover os vértices do caminho raiz do problema até o nó de desvio
    currentVertices = nodesSet[m:]
    currentArcs = copy.copy(arcsSet)

    # 05: Remove all deviation links in Emj from G.
    arcPos = len(setOfAssociatedDeviationArcs)
    while arcPos > 0:
        arcPos -= 1
        del currentArcs[setOfAssociatedDeviationArcs[arcPos]]

    # 06: l is the number of links of pj
    for i in range(m, l - 1):
        # 07: Remove deviation link a_{i}^{j} = (n_{i}^{j}, n_{i+1}^{j}) from G.
        del currentArcs[(i, i + 1)]
        
        # 08: Set root path r_{i}^{j}.
        rootPath = []

        # 09: Calculate spur path s¯ij using forward one-to-all (or one-to-one) Dijkstra’s algorithm.

        # 10: Determine deviation path p¯ij := r_{i}^{j} concatenado s{i}^{j}.
        deviationPath = []

        # 11: Add p_{i}^{j} em D^{j}.
        setOfDeviationPath.append(deviationPath)

        # 12: Remove n_{i}^{j} from G.
        del nodes[i]
    
    # 14: Restore network G.
    restoreNetwork()

    # 15: Retun Dj
    return setOfDeviationPath, deviationVertex


def findSpurPathMP():
    print('findSpurPathMP')


def mpsAlgorithm(nodes, arcsSet, pj, L):
    print('M-P\'s Algorithm')

    numberOfArcsOfPj = len(pj)
    setOfDeviationPath = []

    # 01: Call FindFirstDevNode(p , L j )
    # to determine the first deviation node nmj of pj and the associated deviation link set Emj at nmj.
    firstDeviationNode = 1
    posOfDeviationNode = 1
    setOfAssociatedDeviationArcs = [] # deve ter a forma de (v_{i}, v_{i + 1})

    # 02: Remover os vértices e arestas do caminho raiz do problema até o nó de desvio
    for i in range(1, l - 1):
        del nodes[i]
        del arcsSet[(i, i + 1)] # revisar
    
    # 03: Remove all links in E_{m}^j de G
    for arc in setOfAssociatedDeviationArcs:
        del arcsSet[(arc)]
    
    # 06: Call the backward one-to-all Dijkstra’s algorithm to calculate
    # the shortest path p_{n_{v}d} from every node n{v} to destination d.

    for i in range(l - 1, m):
        # 08: Restore node n_{i}^j to G

        # 09: Set root path r_{i}^{j} = (n_{1}^j, ..., n_{i}^j).
        rootPath = []

        # 10: Call FindSpurPath-MP(n_{i}^j, a_{i}^j) to calculate s_{i}^j.
        findSpurPath-MP()

        # 10: Determine deviation path p¯ij := r_{i}^{j} concatenado s{i}^{j}.
        deviationPath = []
        
        # 11: Add p_{i}^{j} em D^{j}.
        setOfDeviationPath.append(deviationPath)
    
    # 14: Restore network G.
    restoreNetwork()

    # 15: Retun Dj
    return setOfDeviationPath


def main(args):
    fileName = args[1]

    graph = readFile(fileName)

    originNode = 1
    destinyNode = 10
    k = 2

    deviationPathProcedure(originNode, destinyNode, k, graph)


if __name__ == "__main__":
    main(sys.argv)
