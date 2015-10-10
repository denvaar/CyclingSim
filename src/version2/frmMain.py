# System level imports
import os
import wx
from twisted.internet import wxreactor
wxreactor.install()
from twisted.internet import reactor

# Local imports
from src.version2.clsMain import MainView
from src.version2.fakeDatabase import FakeDatabase
from src.version2.promoter import Promoter
from src.version2.spectator import Spectator
from src.version2.raceofficial import RaceOfficial

class MainController(MainView):
    def __init__(self, parent, **kwargs):
        super(MainController, self).__init__(parent,
            title='Cycling Race Simulator Controller',
            **kwargs)
        
        self.parent = parent
        self.subscriberCombo.InsertItems(\
            ['Promoter', 'Spectator', 'Race Official'],
            0)
        self.fakeDatabase = FakeDatabase()
        self.getPath()
 
    def getPath(self):
        file_dlg = wx.FileDialog(self,
            message="Select the racer CSV data file.",
            defaultDir=os.getcwd(),
            defaultFile="",
            wildcard="CSV Racer data file (*.csv)|*.csv|",
            style=wx.OPEN|wx.CHANGE_DIR)
        file_dlg.SetTitle("Select the racer CSV data file")
        
        try:
            if file_dlg.ShowModal() == wx.ID_OK:
                self.fakeDatabase.loadRacers(file_dlg.GetPaths()[0])
            else:
                self.Close()
        except:
            msg = wx.MessageDialog(parent=None, message="Invalid path to racer CSV data file.",
                caption="Error", style=wx.OK|wx.ICON_QUESTION)
            msg.ShowModal()
            msg.Destroy()
            self.getPath()
         
    def onBeginSim(self, event):
        button = event.GetEventObject()
        if button.GetValue():
            button.SetLabel("Stop Simulation")
            self.SetStatusText('Status: Listening for UDP packets on 127.0.0.1:14000 . . .')

            reactor.listenUDP(14000, self.fakeDatabase)
            reactor.run()
        else:
            reactor.stop()
            button.Enable(False) # Can't restart the reactor...
            self.SetStatusText('Status: Not listening.')
        event.Skip()
    
    def onAdd(self, event):
        for choice in self.subscriberCombo.GetSelections():
            obj = None
            if choice == 0: # Promoter
                obj = Promoter(self, self.fakeDatabase)
            elif choice == 1: # Spectator
                obj = Spectator(self, self.fakeDatabase)
            elif choice == 2: # Race Official
                obj = RaceOfficial(self, self.fakeDatabase)
            self.olv.AddObject(obj)
        event.Skip()
    
    def onRemove(self, event):
        selected = self.olv.GetSelectedObjects()
        for subscriber in selected:
            try: 
                subscriber.Close()
            except AttributeError:
                pass
        self.olv.RemoveObjects(selected)
        event.Skip()

    def onClose(self, event):
        if reactor.running:
            reactor.stop()
        event.Skip()


# Application entry point.
if __name__ == '__main__':
    app = wx.App()
    reactor.registerWxApp(app)
    frame = MainController(None)
    frame.Show()
    app.MainLoop()

