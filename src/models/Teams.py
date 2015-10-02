class Team:
    def __init__(self, number, label=None, start=None,
        minBib=None, maxBib=None):
        self.number = number
        self.label = label
        self.start = start
        self.minBib = minBib
        self.maxBib = maxBib
        self.racers = []
    
    def getLabel(self):
        return self.label

    def getNumber(self):
        return self.number

    def getStartTime(self):
        return self.start

    def getMinBib(self):
        return self.minBib

    def getMaxBib(self):
        return self.maxBib
