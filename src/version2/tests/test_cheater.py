import unittest

from src.version2.racer import Racer

class CheaterTest(unittest.TestCase):
    def __init__(self):
        self.racers = []
        self.groups = []

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

    

if __name__ == '__main__':
    unittest.main()
