class Vertex:

    def __init__(self, numberOfRamifications, nextVertex, firstRamificationSubTreeLength):
        self.numberOfRamifications = numberOfRamifications
        self.eachRamificationSubTreeLength = { int(nextVertex): firstRamificationSubTreeLength }


    def setRamificationsSubTreeLength(self):
        print('set')
    
    def addNewRamification(self, nextVertex, ramificationSubTreeLength):
        self.numberOfRamifications += 1
        self.eachRamificationSubTreeLength[int(nextVertex)] = ramificationSubTreeLength
