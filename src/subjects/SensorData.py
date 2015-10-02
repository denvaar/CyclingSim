from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

from src.observers.observers import Observer
from .subjects import Subject

from src.models.Racers import Racer

import json

class SensorData(Subject, DatagramProtocol):
    def __init__(self):
        Subject.__init__(self)
        self.observerList = []
        self.data = ""

    def getObservers(self):
        return [observer for observer in self.observerList]

    def addObserver(self, observer):
        # TODO
        # Add a unit test to test if the same observer
        # instance is being added multiple times.
        self.observerList.append(observer)
    
    def removeObserver(self, observer):
        # TODO
        # add a unit test to test removing existing
        # objects works, and if non-existing items
        # throws a ValueError exception.
        try:
            self.observerList.remove(observer)
            #observer.cleanup()
        except ValueError:
            raise

    def notifyObservers(self):
        [observer.update(self.data) for observer in self.observerList]

    def datagramReceived(self, data, (host, port)):
        #print "datagramReceived"
        # TODO
        # Add a unit test to see what type self.data is.
        #self.transport.write(data, (host, port))
        self.data = json.loads('%s' % data)
        self.notifyObservers()



