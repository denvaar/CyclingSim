import json
import csv
from twisted.internet.protocol import DatagramProtocol

from src.version2.racer import Racer

class FakeDatabase(DatagramProtocol):
    def __init__(self):
        self.racers = {}
        self.loadRacers()
        print "Database:", self.racers

    def loadRacers(self):
        # TODO unit test this.
        # Load each racer from the CSV file.
        with open('/Users/denversmith/Downloads/SensorSimulator/SensorSimulator/bin/Debug/Racers.csv', 'rb') as f:
            read = csv.reader(f)
            for row in read:
                # Add new Racer instance to the dictionary.
                self.racers[row[2]] = Racer(row[0], row[1], int(row[2]), row[3])

    def updateRacer(self, bib, data):
        racer = self.racers[str(bib)]
        racer.setTime(data['Timestamp'])
        racer.setSensor(data['SensorId'])
        racer.notifyObservers()
    
    def getRacerList(self):
        # Return a list of the values from 
        # self.racers. (AKA the actual Racer objects.)
        return self.racers.values()

    # ----------------------------------------------
    # Methods inherited from DatagramProtocol class.
    # ----------------------------------------------

    def datagramReceived(self, data, (host, port)):
        #print "datagramReceived"
        # TODO
        # Add a unit test to see what type self.data is.
        #self.transport.write(data, (host, port))
        # Convert JSON data into a python dictionary.
        info = json.loads('%s' % data)
        self.updateRacer(str(info['RacerBibNumber']), info) 
