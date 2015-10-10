import datetime
import json
import csv
from twisted.internet.protocol import DatagramProtocol

from src.version2.racer import Racer

class FakeDatabase(DatagramProtocol):
    '''
    This class would  be the 'model' in the
    MVC pattern. Its purpose is to maintain
    a list of racer objects.
    '''
    def __init__(self):
        self.racers = {}
        self.possibleCheaters = []
        self.groups = {}
        self.sensorSnapshot = {}

    def loadRacers(self, path):
        # Load each racer from the CSV file.
        #with open('/Users/denversmith/Downloads/SensorSimulator/SensorSimulator/bin/Debug/Racers.csv', 'rb') as f:
        try:
            with open(path, 'rb') as f:
                read = csv.reader(f)
                lastGroup = None
                prev = None
                for row in read:
                    # Add new Racer instance to the dictionary.
                    racer = Racer(row[0], row[1], int(row[2]), row[3])
                    self.racers[row[2]] = racer
                    if lastGroup == None and prev != int(row[3]):
                        self.groups[int(row[3])] = []
                        prev = int(row[3])
                    else:
                        lastGroup = None
                    self.groups[int(row[3])].append(racer)
        except:
            raise

    def updateRacer(self, bib, data):
        # This method is called every time that
        # new data comes in from the sensor.
        # The appropriate racer object is updated
        # with the data, and then all of his
        # observers are notified.
        racer = self.racers[str(bib)]
        racer.setTime(data['Timestamp'])
        racer.setSensor(int(data['SensorId']))
        racer.notifyObservers()

    def getRacerList(self):
        # Return a list of the values from 
        # self.racers. (AKA the actual Racer objects.)
        return self.racers.values()

    # ----------------------------------------------
    # Methods inherited from DatagramProtocol class.
    # ----------------------------------------------

    def datagramReceived(self, data, (host, port)):
        # This method is called when a UDP packet is recieved.
        # The JSON data is converted to a python dictionary
        # and then the appropriate racer's updateRacer method
        # is called.

        #self.transport.write(data, (host, port))
        info = json.loads('%s' % data)
        self.updateRacer(str(info['RacerBibNumber']), info)
