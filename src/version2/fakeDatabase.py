import datetime
import json
import csv
from twisted.internet.protocol import DatagramProtocol

from src.version2.racer import Racer

class FakeDatabase(DatagramProtocol):
    def __init__(self):
        self.racers = {}
        self.cheaters = {}
        self.possibleCheaters = []
        self.groups = {}
        self.sensorSnapshot = {}
        self.loadRacers()

    def loadRacers(self):
        # TODO unit test this.
        # Load each racer from the CSV file.
        with open('/Users/denversmith/Downloads/SensorSimulator/SensorSimulator/bin/Debug/Racers.csv', 'rb') as f:
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

    def updateRacer(self, bib, data):
        racer = self.racers[str(bib)]
        racer.setTime(data['Timestamp'])
        racer.setSensor(int(data['SensorId']))
        racer.notifyObservers()

    def cheaterCheck4(self, racer, sensorGroup):
        '''
        cheaterCheck -- Check if given racer is close to
                        anyone else at a given sensor.
        '''
        for other_racer in self.sensorSnapshot[sensorGroup]:
            if racer.getTeam() != other_racer.getTeam():
                if racer.getTime() in range(other_racer.getTime()-3000, other_racer.getTime()+3000):
                    if racer in self.possibleCheaters:
                        print racer, " and ", other_racer, " might be cheating."
                        self.cheaters[racer.getTeam()] = racer.getBibAndName()
                        break
                    else:
                        self.possibleCheaters.append(racer)

    def getRacerList(self):
        # Return a list of the values from 
        # self.racers. (AKA the actual Racer objects.)
        return self.racers.values()

    # ----------------------------------------------
    # Methods inherited from DatagramProtocol class.
    # ----------------------------------------------

    def datagramReceived(self, data, (host, port)):
        #self.transport.write(data, (host, port))
        # Convert JSON data into a python dictionary.
        info = json.loads('%s' % data)
        self.updateRacer(str(info['RacerBibNumber']), info)
