import datetime

from src.version2.subject import Subject

class Racer(Subject):
    def __init__(self, first, last, bib, team):
        Subject.__init__(self)
        self.first = first
        self.last = last
        self.bib = bib 
        self.team = team
        # A list to keep track of the subscribed observers.
        self.observerList = []

        self.lastSensor = '-' 
        self.lastTime = '-' 

    def __repr__(self):
        return unicode("Racer Bib#" + str(self.bib))

    def getName(self):
        return self.first + " " + self.last

    def getBib(self):
        return self.bib
            
    def getBibAndName(self):
        return '(' + str(self.bib) + ') ' + self.first + self.last

    def getTime(self):
        return self.lastTime
    
    def getSensor(self):
        return self.lastSensor
    
    def getTeam(self):
        return self.team
    
    def setTime(self, t):
        self.lastTime = datetime.timedelta(milliseconds=t)

    def setSensor(self, s):
        self.lastSensor = s

    # Implementing inherited methods
    # from the Subject interface:

    def addObserver(self, observer):
        print "Racer #%s here - adding a %s observer" % (self.bib, observer)
        self.observerList.append(observer)

    def removeObserver(self, observer):
        try:
            self.observerList.remove(observer)
        except ValueError:
            raise

    def notifyObservers(self):
        if self.observerList:
            print "Racer #%s here - telling %s about myself" % (self.bib, self.observerList)
        # Give each observer an instance of the current state.
        [observer.update(self) for observer in self.observerList]
