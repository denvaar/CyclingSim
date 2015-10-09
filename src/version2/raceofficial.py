import wx


# Local imports
from src.version2.observer import Observer
from src.version2.clsRaceOfficial import RaceOfficialView

class RaceOfficial(Observer, RaceOfficialView):
    '''
    '''
    def __init__(self, parent, dataSource):
        # Call the base class constructors.
        Observer.__init__(self)
        RaceOfficialView.__init__(self, parent)

        self.parent = parent

    def update(self, data):
        print "RaceOfficial recieved: %s" % data
    
    def __repr__(self):
        return "Spectator"
    
    #--------------------------
    # Event handlers
    #--------------------------

    def onOK(self, event):
        selected = self.olv.GetSelectedObjects()
        emailAddr = self.emailTxtCtrl.GetValue()
        print selected
        print emailAddr

        self.selectedObjects = selected
        self.emailAddr = emailAddr

        [obj.addObserver(self) for obj in self.selectedObjects]
        
        self.emailTimer = wx.Timer(self)
        self.emailTimer.Start(9000)
        self.Bind(wx.EVT_TIMER, self.doEmail)
        
        self.Show(False)
        event.Skip()

    def onCancel(self, event):
        self.Close()
        event.Skip()

    def onClosing(self, event):
        print "closing..."
        [obj.removeObserver(self) for obj in self.selectedObjects]
        self.parent.olv.RemoveObject(self)
        event.Skip()
