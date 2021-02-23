from tree_vertex import Vertex

class TreeOfPaths:

    def __init__(self):
        self.__treeOfPaths =  {}
        self.__nextPath = ['p', 1]


    def getTreeOfPaths(self):
        return self.__treeOfPaths


    def buildNewPath(self, path, deviationVertex, deviationVertexPath):
        treeOfPaths = {}
        pathLength = len(path) - 1

        for i in range(len(path) - 1):
            treeOfPaths[path[i]] = Vertex(1, path[i + 1], pathLength - i)
        
        treeOfPaths[path[-1]] = Vertex(0, -1, 0)

        self.__treeOfPaths[self.__nextPath[0] + str(self.__nextPath[1])] = [(deviationVertex, deviationVertexPath) , treeOfPaths]
        self.__nextPath = [self.__nextPath[0], self.__nextPath[1] + 1]

        # for p in self.__treeOfPaths:
        #     print('\n\n ---------- ', p, ' ----------\n')
        #     for vertex in self.__treeOfPaths[p][1]:
        #         print('V:', vertex, ' -  R:', self.__treeOfPaths[p][1][vertex].numberOfRamifications, ' -  T:', self.__treeOfPaths[p][1][vertex].nextVertices)


    def addNewPath(self, path):
        if (self.__treeOfPaths != {}):
            foundDeviationPath = False
            pathIndex = 0
            deviationVertexPath = ''
            deviationVertex = 1

            while not(foundDeviationPath):
                auxPath = path[1]

                while len(auxPath) > 1:
                    pathIndex += 1
                    if auxPath[0] in self.__treeOfPaths['p' + str(pathIndex)][1]:
                        if self.__treeOfPaths['p' + str(pathIndex)][1][auxPath[0]].numberOfRamifications > 1 or auxPath[1] in self.__treeOfPaths['p' + str(pathIndex)][1]:
                            nextVertices = self.__treeOfPaths['p' + str(pathIndex)][1][auxPath[0]].nextVertices
                            if auxPath[1] in nextVertices:
                                if auxPath[1] in self.__treeOfPaths['p' + str(pathIndex)][1]:
                                    pathIndex -= 1
                                auxPath = auxPath[1:]
                            else:
                                foundDeviationPath = True
                                deviationVertex = auxPath[0]
                                deviationVertexPath = 'p' + str(pathIndex)
                                auxPath = []
                                break
                        else:
                            foundDeviationPath = True
                            deviationVertex = auxPath[0]
                            deviationVertexPath = 'p' + str(pathIndex)
                            break

            indexOfDeviationVertexInPath = path[1].index(deviationVertex)
            pathAfterDeviationNode = path[1][(indexOfDeviationVertexInPath + 1):]

            self.__treeOfPaths[deviationVertexPath][1][deviationVertex].addNewRamification(pathAfterDeviationNode[0])

            self.buildNewPath(pathAfterDeviationNode, deviationVertex, deviationVertexPath)
        else:
            self.buildNewPath(path[1], 1, '')