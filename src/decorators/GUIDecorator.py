from src.observers.observers import Observer
from src.views.clsUserInterfaceMixin import UserInterfaceMixin

from src.models.Racers import Racer

class BaseDecorator(Observer):
    def __init__(self, decorateMe):
        self.__observer = decorateMe

    def update(self, data):
        self.__observer.update(data) # Delegation

    def cleanup(self):
        self.__observer.cleanup() # Delegation


class GUIDecorator(BaseDecorator, UserInterfaceMixin):
    def __init__(self, decorateMe, parent):
        BaseDecorator.__init__(self, decorateMe)
        UserInterfaceMixin.__init__(self, parent)
        self.SetTitle('<<< J U M B O T R O N >>>')
        # Extra steps for GUI's.
        # Show the window.
        self.Show(True)
    
    def __repr__(self):
        return "Promoter"

    def update(self, data):
        BaseDecorator.update(self, data)
        # Extra update things for GUI's.

    def cleanup(self):
        pass
        #print "cleaning up"

    def addItem(self, item):
        self.olv.AddObject(item)
    
    def removeItem(self, items):
        self.olv.RemoveObjects(items)
