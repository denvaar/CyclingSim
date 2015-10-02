class Racer:
    def __init__(self, first, last, bib, team):
        self.first = first
        self.last = last
        self.bib = bib
        self.team = team
        self.lastSensor = None
        self.lastTime = 0

    def getName(self):
        return self.first + " " + self.last

    def getBib(self):
        return self.bib

    def getTeam(self):
        return self.team
   
