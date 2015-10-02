import wx
import csv
from src.views.clsSpectatorManager import SpectatorManagerView
from src.subjects.racer import Racer
#from src.observers.Promoter import Promoter


# Observer of Racer(s)
class SpectatorManager(SpectatorManagerView):
    def __init__(self, parent, dataSource, **kwargs):
        super(SpectatorManager, self).__init__(parent,
            title='Spectator Configuration',
            **kwargs)

        self.parent = parent
        self.dataSource = dataSource
        self.racers = []
        self.loadRacers()
        #self.olv.SetObjects(self.racers)
        #self.listening = False

        #self.jumbotron = GUIDecorator(Promoter(None), self) 
        
        self.Show(True)

    def __repr__(self):
        return unicode('Spectator')        

    def loadRacers(self):
        with open('../models/Racers.csv', 'rb') as f:
            read = csv.reader(f)
            for row in read:
                self.racers.append(Racer(row[0], row[1], int(row[2]), int(row[3])))
    '''
    def onAdd(self, event):
        objectsToAdd = self.olv.GetSelectedObjects()
        existingObjects = self.olv2.GetObjects()
        for obj in objectsToAdd:
            if obj not in existingObjects:
                self.olv2.AddObject(obj)
                self.jumbotron.addItem(obj)
                self.dataSource.addObserver(obj)
        if not self.listening:
            self.dataSource.addObserver(self)
            self.listening = True
        event.Skip()

    def onRemove(self, event):
        selectedObjects = self.olv2.GetSelectedObjects()
        self.olv2.RemoveObjects(selectedObjects)
        self.jumbotron.removeItem(selectedObjects)
        [self.dataSource.removeObserver(obj) for obj in selectedObjects]
        if not self.jumbotron.olv.GetObjects():
            self.listening = False
            self.dataSource.removeObserver(self)
        event.Skip()
    '''
    def onGo(self, data):
        
        self.dataSource.addObserver()
        self.Show(False)
        event.Skip()
    def update(self, data):
        if str(data['RacerBibNumber']) == str(self.bibTxt.GetValue()):
            print self.bibTxt.GetValue()
           

