from threading import Thread, Timer, Event
import datetime
import time


from src.subjects.subjects import Subject
from src.subjects.SensorData import SensorData

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

        #self.dataSource = None

    def getName(self):
        return self.first + " " + self.last

    def getBib(self):
        return self.bib
    
    def getBibAndName(self):
        return '(' + str(self.bib) + ') ' + self.first + self.last

    def getTeam(self):
        return self.team

    def update(self, data):
        if data['RacerBibNumber'] == self.bib:
            print "I am racer %d and I just passed a sensor." % self.bib
            print "--->%s<---" % data
            self.lastSensor = data['SensorId']
            self.lastTime = datetime.timedelta(milliseconds=data['Timestamp'])

    # Implementing inherited methods
    # from the Subject interface:

    def addObserver(self, observer):
        self.observerList.append(observer)

    def removeObserver(self, observer):
        try:
            self.observerList.remove(observer)
        except ValueError:
            raise

    def notifyObservers(self):
        # Give each observer an instance of the current state.
        [observer.update(self) for observer in self.observerList]
