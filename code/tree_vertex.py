class Vertex:

    def __init__(self, numberOfRamifications, nextVertex, firstRamificationSubTreeLength):
        self.numberOfRamifications = numberOfRamifications
        self.nextVertices = [nextVertex]


    def addNewRamification(self, nextVertex):
        self.numberOfRamifications += 1
        self.nextVertices.append(nextVertex)
