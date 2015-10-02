import wx

from src.version2.clsPromoterManager import PromoterManagerView
from src.version2.promoter import Promoter

# Observer of Racer(s)
class PromoterManager(PromoterManagerView):
    def __init__(self, parent, dataSource, **kwargs):
        super(PromoterManager, self).__init__(parent,
            title='Promoter Controller',
            **kwargs)

        self.parent = parent
        #self.dataSource = dataSource
        self.olv.SetObjects(dataSource.getRacerList())

        self.jumbotron = Promoter(self) 
        
        self.Show(True)

    def __repr__(self):
        return unicode('Promoter')        

    def onAdd(self, event):
        objectsToAdd = self.olv.GetSelectedObjects()
        existingObjects = self.olv2.GetObjects()
        for obj in objectsToAdd:
            if obj not in existingObjects:
                self.olv2.AddObject(obj)
                self.jumbotron.addObject(obj)
                obj.addObserver(self.jumbotron)
        event.Skip()

    def onRemove(self, event):
        event.Skip()

    def update(self, data):
        self.refreshDisplay()

    def refreshDisplay(self):
        print "refreshing display"
        #self.jumbotron.olv.RepopulateList()
           

