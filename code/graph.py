class Graph:

    def __init__(self, name, numberOfNodes, numberOfArcs, nodesSet, arcsSet):
        self.__name = name
        self.__numberOfNodes = numberOfNodes
        self.__numberOfArcs = numberOfArcs
        self.__nodesSet = nodesSet
        self.__arcsSet = arcsSet

        adjacencyList = {}
        for node in self.__nodesSet:
            adjacencyList[node] = []

        self.__network, self.__adjacencyList = self.setNetwork(adjacencyList)


    def getName(self):
        return self.__name


    def getNumberOfNodes(self):
        return self.__numberOfNodes


    def getNumberOfArcs(self):
        return self.__numberOfArcs


    def getNodesSet(self):
        return self.__nodesSet


    def getArcsSet(self):
        return self.__arcsSet


    def getNetwork(self):
        return self.__network


    def getAdjacencyList(self):
        return self.__adjacencyList


    def setNetwork(self, adjacencyList):
        network = {}

        for arc in self.__arcsSet:
            network[arc[0], arc[1]] = arc[2]
            adjacencyList[arc[0]].append(arc[1])

        return network, adjacencyList
    

    def getNodeNeighbours(self, node):
        return self.__adjacencyList[node]


    def printGraphInfo(self):
        return 'File name: %s \nNumber of nodes: %d \nNodes: %s \nNumber of arcs: %d \nArcs set: %s \nMatrix: %s \nadjacency: %s' \
                % (self.__name, self.__numberOfNodes, self.__nodesSet, self.__numberOfArcs, self.__arcsSet, self.__network, self.__adjacencyList)
