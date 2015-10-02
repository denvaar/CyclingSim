# System level imports
import wx
from twisted.internet import wxreactor
wxreactor.install()
from twisted.internet import reactor

# Local imports
from src.version2.clsMain import MainView
from src.version2.fakeDatabase import FakeDatabase
from src.version2.promoter import Promoter

class MainController(MainView):
    def __init__(self, parent, **kwargs):
        super(MainController, self).__init__(parent,
            title='Cycling Race Simulator Controller',
            **kwargs)
        self.parent = parent
        self.fakeDatabase = FakeDatabase()
        self.subscriberCombo.InsertItems(\
            ['Promoter', 'Spectator', 'Race Official'],
            0)
        
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
                #obj = PromoterManager(self, self.fakeDatabase)
                obj = Promoter(self, self.fakeDatabase)
            elif choice == 1: # Spectator
                pass
            elif choice == 2: # Race Official
                pass
            self.olv.AddObject(obj)
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

