from src.version2.observer import Observer
from src.version2.clsJumbotron import JumbotronUIMixin

class Promoter(Observer, JumbotronUIMixin):
    def __init__(self, parent):
        Observer.__init__(self)
        JumbotronUIMixin.__init__(self, parent)
        print "jumbotron created"
        #self.subject = subject

    def update(self, data):
        print "Promotor recieved: %s" % data
        self.olv.RepopulateList()

    def __repr__(self):
        return "Promoter"
   
    def addObject(self, obj):
        self.olv.AddObject(obj)
