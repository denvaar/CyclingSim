# Local imports
from src.version2.observer import Observer
from src.version2.clsJumbotron import JumbotronUIMixin
from src.version2.clsPromoter import PromoterView

# TODO
# o If jumboron window is closed, also close the PromoterView window.


class Promoter(Observer, PromoterView):
    '''
        Promoter -- This is the class that represents
                    a race promoter. It allows one to
                    move racers in and out of a real-
                    time jumbotron display.

                    Promoter implements the Observer
                    interface, and gets its GUI
                    functionallity from PromoterView.
    '''
    def __init__(self, parent, dataSource):
        # Call the base class constructors.
        Observer.__init__(self)
        PromoterView.__init__(self, parent)
        
        # A promoter has a jumbotron display window.
        self.jumbotron = JumbotronUIMixin(parent)
        # Populate the object list view control on the left
        # with all of the racers in the database.
        self.olv.SetObjects(dataSource.getRacerList())

    def update(self, data):
        print "Promotor recieved: %s" % data
        # New data has been recieved!
        # Refresh the jumbotron display.
        #self.jumbotron.olv.RepopulateList()
        self.jumbotron.olv.RefreshObject(data)
    def __repr__(self):
        return "Promoter"
   
    #def addObject(self, obj):
    #    self.olv.AddObject(obj)

    def onAdd(self, event):
        '''
            onAdd -- The event handler for when
                     a user adds an object from
                     the list on the left into the
                     list on the right.
        '''
        objectsToAdd = self.olv.GetSelectedObjects()
        existingObjects = self.olv2.GetObjects()
        for obj in objectsToAdd:
            if obj not in existingObjects:
                # Add it to the list on the right side.
                self.olv2.AddObject(obj)
                # Add it to the jumbotron window.
                self.jumbotron.olv.AddObject(obj)
                # Subscribe the jumbotron window to
                # recieve updates when this object is
                # updated.
                obj.addObserver(self)
        event.Skip()

    def onRemove(self, event):
        '''
        onRemove -- The event handler for when a user 
                    removes an object from the list on
                    the right side.
        '''
        # We want to remove the object(s) from both the
        # list on the right side, and the jumbotron display.
        selected = self.olv2.GetSelectedObjects()
        self.olv2.RemoveObjects(selected)
        self.jumbotron.olv.RemoveObjects(selected)
        # Also we don't want updates from the selected
        # objects anymore, so for each of the selected
        # objects, AKA racers, we will stop observing them.
        [obj.removeObserver(self) for obj in selected]
        event.Skip()
