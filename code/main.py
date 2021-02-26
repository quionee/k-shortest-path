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


def buildGraph(currentVertices, currentArcs):
    arcsSet = []
    for i in currentArcs:
        arcsSet.append([i[0], i[1], currentArcs[i]])

    graph = Graph('', len(currentVertices), len(currentArcs), currentVertices, arcsSet)

    return graph


def dijkstra(graph, source):
    dist = {}
    previous = {}

    Q = makefheap()
    dist[source] = 0

    for node in graph.getNodesSet():
        if (node != source):
            dist[node] = math.inf
            previous[node] = None

        fheappush(Q, (dist[node], node))

    network = graph.getNetwork()

    while Q.num_nodes:
        u = fheappop(Q)

        neighbours = graph.getNodeNeighbours(u[1])
        for neighbour in neighbours:
            alt = dist[u[1]] + network[u[1], neighbour]

            if alt < dist[neighbour]:
                dist[neighbour] = alt
                previous[neighbour] = u[1]
            
            if (neighbour < u[1]):
                fheappush(Q, (dist[neighbour], neighbour))

    return dist, previous


def setShortestPath(dist, previous, originNode, destinyNode):
    if (previous[destinyNode] != None):
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
    else:
        None


def deviationPathProcedure(originNode, destinyNode, k, graph):
    dist, previous = dijkstra(graph, originNode)

    p1 = setShortestPath(dist, previous, originNode, destinyNode)

    C = makefheap()
    fheappush(C, (dist[destinyNode], p1))

    L = TreeOfPaths()

    deviationVertex = 1

    for j in range(1, k + 1):
        if not(C.num_nodes):
            return L

        pj = fheappop(C)

        print('\n\n\n\n           ---------------- Caminho p' + str(j) + ':', pj[1], '----------------')

        L.addNewPath(pj)

        Dj = yensAlgorithm(graph.getNodesSet(), graph.getNetwork(), pj, L, j)

        fheapunion(C, Dj)

    return L


def findDeviationVertex(path, L, j):
    deviationVertex = 1
    setOfAssociatedDeviationArcs = []

    pathName = 'p' + str(j)

    if len(L.getTreeOfPaths()) != 1:

        vertexWithMoreRamifications = 1
        foundDeviationVertex = False

        i = len(path[1]) - 2
        while i >= 0 and not(foundDeviationVertex):
            if path[1][i] in L.getTreeOfPaths()[pathName][1]:
                if L.getTreeOfPaths()[pathName][1][path[1][i]].numberOfRamifications > 1:
                    vertexWithMoreRamifications = path[1][i]
                    foundDeviationVertex = True
                    deviationVertex = path[1][i]
            else:
                i += 1
                pathName = L.getTreeOfPaths()[pathName][0][1]

            i -= 1

        i = path[1].index(deviationVertex)
        while i >= 0:
            if path[1][i] in L.getTreeOfPaths()[pathName][1]:
                for vertex in L.getTreeOfPaths()[pathName][1][path[1][i]].nextVertices:
                    setOfAssociatedDeviationArcs.append((path[1][i], vertex))
            else:
                i += 1
                pathName = L.getTreeOfPaths()[pathName][0][1]

            i -= 1

        setOfAssociatedDeviationArcs.remove((deviationVertex, path[1][path[1].index(deviationVertex) + 1]))

    print('\nVértice de desvio: ', deviationVertex)
    print('Conjunto de arcos de desvio: ', setOfAssociatedDeviationArcs)

    return deviationVertex, setOfAssociatedDeviationArcs


def removeIncidentArcsOfRemovedVertex(removedVertex, currentVertices, currentArcs, adjacencyList):
    for vertex in adjacencyList[removedVertex]:
        del currentArcs[(removedVertex, vertex)]
    
    for i in currentVertices:
        if (i, removedVertex) in currentArcs:
            del currentArcs[i, removedVertex]

    return currentArcs


def getDistanceOfPath(path, arcsSet):
    pathDistance = 0

    for i in range(len(path) - 1):
        pathDistance += arcsSet[(path[i], path[i + 1])]

    return pathDistance


def yensAlgorithm(nodesSet, arcsSet, pj, L, j):
    print('\n\n\t         ----------- Algoritmo de Yen, iteração ' + str(j) + ' -----------\n')

    numberOfArcsOfPj = len(pj[1])
    setOfDeviationPaths = makefheap()
    deviationVertex, setOfAssociatedDeviationArcs = findDeviationVertex(pj, L, j)

    arcsOfPj = []
    for i in range(len(pj[1]) - 1):
        arcsOfPj.append((pj[1][i], pj[1][i + 1]))

    m = pj[1].index(deviationVertex)
    l = numberOfArcsOfPj - 1

    print('\nm (índice do primeiro vértice de desvio): ', m, '\nl (quantidade de arestas do caminho p' + str(j) + '): ', l)

    currentVertices = copy.copy(nodesSet)

    i = 0
    while i < m:
        currentVertices.remove(pj[1][i])
        i += 1

    currentArcs = copy.copy(arcsSet)

    for arc in setOfAssociatedDeviationArcs:
        del currentArcs[arc]

    for i in range(m, l):
        del currentArcs[arcsOfPj[i]]

        print('\n\ni: ', i, '\nVértices da rede: ', currentVertices, '\nArcos da rede: ', currentArcs)

        rootPath = pj[1][:i + 1]

        print('\nCaminho raíz: ', rootPath)

        newGraph = buildGraph(currentVertices, currentArcs)
        originVertexPos = currentVertices.index(rootPath[-1])

        dist, previous = dijkstra(newGraph, currentVertices[originVertexPos])
        shortestPath = setShortestPath(dist, previous, currentVertices[originVertexPos], currentVertices[-1])

        if (shortestPath != None):
            spurPath = shortestPath[1:]
            print('Caminho derivado mais curto: ', spurPath)

            deviationPath = rootPath + spurPath
            deviationPathDistance = getDistanceOfPath(deviationPath, arcsSet)

            print('\nCaminho de desvio candidato: ', deviationPath, '\nDistância do caminho de desvio candidato: ', deviationPathDistance, '\n\n')

            fheappush(setOfDeviationPaths, (deviationPathDistance, deviationPath))
        else:
            print('\nA rede não possui caminhos possíveis da orgigem atual com os arcos existentes.')

        currentArcs = removeIncidentArcsOfRemovedVertex(pj[1][i], currentVertices, currentArcs, newGraph.getAdjacencyList())
        currentVertices.remove(pj[1][i])

    return setOfDeviationPaths


def main(args):
    fileName = args[1]

    graph = readFile(fileName)

    originNode = 1
    destinyNode = 10
    k = 4

    k_shortes_paths = deviationPathProcedure(originNode, destinyNode, k, graph)

    for p in k_shortes_paths.getTreeOfPaths():
        print('\n\n\t\t-------------------- ', p, ' --------------------\n')
        for vertex in k_shortes_paths.getTreeOfPaths()[p][1]:
            print('Vértice:', vertex, '  -   Quantidade de ramificações:', k_shortes_paths.getTreeOfPaths()[p][1][vertex].numberOfRamifications, '  -   Próximos vértices:', k_shortes_paths.getTreeOfPaths()[p][1][vertex].nextVertices)

    print('\n\n\n')


if __name__ == "__main__":
    main(sys.argv)
