# System imports
import wx

# Local imports
from src.version2.observer import Observer
from src.version2.clsJumbotron import JumbotronUIMixin
from src.version2.clsPromoter import PromoterView

class Promoter(Observer):
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

        # Handle to parent window.
        self.parent = parent

        # Set up the user interface. 
        self.view = PromoterView(parent)
        self.view.addBtn.Bind(wx.EVT_BUTTON, self.onAdd)
        self.view.delBtn.Bind(wx.EVT_BUTTON, self.onRemove)
        self.view.Bind(wx.EVT_CLOSE, self.onClose) 
        
        # A promoter has a jumbotron display window.
        self.jumbotron = JumbotronUIMixin(self.view)
        self.jumbotron.Bind(wx.EVT_CLOSE, self.onClose) 
       
        # Populate the object list view control on the left
        # with all of the racers in the database.
        self.view.olv.SetObjects(dataSource.getRacerList())
    
    def update(self, data):
        # New data has been recieved!
        # Refresh the jumbotron display.
        self.jumbotron.olv.RefreshObject(data)
    
    def Close(self):
        self.view.Close()

    def __repr__(self):
        return "Promoter"
  
    # ===================================
    # Event Handlers
    # ===================================
 
    def onAdd(self, event):
        '''
            onAdd -- The event handler for when
                     a user adds an object from
                     the list on the left into the
                     list on the right.
        '''
        objectsToAdd = self.view.olv.GetSelectedObjects()
        existingObjects = self.view.olv2.GetObjects()
        for obj in objectsToAdd:
            if obj not in existingObjects:
                # Add it to the list on the right side.
                self.view.olv2.AddObject(obj)
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
        selected = self.view.olv2.GetSelectedObjects()
        self.view.olv2.RemoveObjects(selected)
        self.jumbotron.olv.RemoveObjects(selected)
        # Also we don't want updates from the selected
        # objects anymore, so for each of the selected
        # objects, AKA racers, we will stop observing them.
        [obj.removeObserver(self) for obj in selected]
        event.Skip()

    def onClose(self, event):
        if event.GetEventObject() == self.jumbotron:
            self.view.Close()
        self.parent.olv.RemoveObject(self)
        event.Skip()
