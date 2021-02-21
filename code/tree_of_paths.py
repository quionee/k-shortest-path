from tree_vertex import Vertex

class TreeOfPaths:

    def __init__(self):
        self.__treeOfPaths =  {}
        self.__nextPath = ['p', 1]


    def getTreeOfPaths(self):
        return self.__treeOfPaths


    def buildNewPath(self, path):
        treeOfPaths = {}
        pathLength = len(path) - 1

        for i in range(len(path) - 1):
            treeOfPaths[path[i]] = Vertex(1, path[i + 1], pathLength - i)
        
        treeOfPaths[path[-1]] = Vertex(0, -1, 0)

        self.__treeOfPaths[self.__nextPath[0] + str(self.__nextPath[1])] = treeOfPaths
        self.__nextPath = [self.__nextPath[0], self.__nextPath[1] + 1]

        for p in self.__treeOfPaths:
            print('p: ', p)
            for vertex in self.__treeOfPaths[p]:
                print('v: ', vertex, self.__treeOfPaths[p][vertex].numberOfRamifications, self.__treeOfPaths[p][vertex].eachRamificationSubTreeLength)


    def addNewPath(self, path, deviationVertex):
        if (self.__treeOfPaths != {}):
            foundDeviationVertex = False
            pathIndex = 1
            deviationVertexPath = ''

            while not(foundDeviationVertex):
                if deviationVertex in self.__treeOfPaths['p' + str(pathIndex)]:
                    foundDeviationVertex = True
                    deviationVertexPath = 'p' + str(pathIndex)
                
                pathIndex += 1
            
            indexOfDeviationVertexInPath = path[1].index(deviationVertex)
            pathAfterDeviationNode = path[1][(indexOfDeviationVertexInPath + 1):]
            ramificationSubTreeLength = len(pathAfterDeviationNode)

            self.__treeOfPaths[deviationVertexPath][deviationVertex].addNewRamification(pathAfterDeviationNode[0], ramificationSubTreeLength)

            self.buildNewPath(pathAfterDeviationNode)
        else:
            self.buildNewPath(path[1])