class Graph:

    def __init__(self, name, numberOfNodes, numberOfArcs, matrix):
        self.name = name
        self.numberOfNodes = numberOfNodes
        self.numberOfArcs = numberOfArcs
        self.matrix = matrix


    def printGraphInfo(self):
        return 'File name: %s \nNumber of nodes: %d \nNumber of arcs: %d \nMatrix: %s' % (self.name, self.numberOfNodes, self.numberOfArcs, self.matrix)
