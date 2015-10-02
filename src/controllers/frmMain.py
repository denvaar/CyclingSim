import wx
from twisted.internet import wxreactor
wxreactor.install()
from twisted.internet import reactor

import csv

from src.views.clsMain import MainView
from src.subjects.SensorData import SensorData
from src.subjects.racer import Racer
from src.observers.Spectator import Spectator
from src.observers.Promoter import Promoter
from src.observers.observers import Observer
from src.decorators.GUIDecorator import GUIDecorator
from src.controllers.frmPromoterManager import PromoterManager
from src.controllers.frmSpectatorManager import SpectatorManager

class MainController(MainView):
    def __init__(self, parent, **kwargs):
        super(MainController, self).__init__(parent,
            title='Cycling Race Simulator Controller',
            **kwargs)
        self.parent = parent
        self.dataSource = SensorData()
        
        self.observers = ['Promoter', 'Spectator']
        self.subscriberCombo.InsertItems([i for i in self.observers], 0)
        
        self.host = '127.0.0.1'
        self.port = 14000

    def onBeginSim(self, event):
        widget = event.GetEventObject()
        if widget.GetValue():
            widget.SetLabel("Stop Simulation")
            self.SetStatusText('Status: Listening for UDP packets on %s:%d . . .' % (self.host, self.port))

            reactor.listenUDP(self.port, self.dataSource)
            reactor.run()
        else:
            widget.SetLabel("Begin Simulation")
            reactor.stop()
            widget.Enable(False) # Can't restart the reactor...
            self.SetStatusText('Status: Not listening.')
        event.Skip()

    def onClose(self, event):
        if reactor.running:
            reactor.stop()
        event.Skip()
    
    def onAdd(self, event):
        for i in self.subscriberCombo.GetSelections():
            if i == 0:
                pm = PromoterManager(self, self.dataSource)
            if i == 1:
                pm = SpectatorManager(self, self.dataSource)
                self.dataSource.addObserver(pm)
            #self.subject.addObserver(instance)
            self.olv.AddObject(pm)
        event.Skip()
    
    def onRemove(self, event):
        # Remove all selected items in the olv.
        # Unsubscibe from the subject.
        observers = self.olv.GetSelectedObjects()
        for i in observers:
            try:
                i.Close()
            except AttributeError:
                pass
                #self.subject.removeObserver(i)
        self.olv.RemoveObjects(observers)
        #self.olv.SetObjects(self.subject.getObservers())
        event.Skip()

    def onRemoveExternal(self, event):
        self.olv.RemoveObject(event.GetEventObject())
        self.subject.removeObserver(event.GetEventObject())
        self.olv.SetObjects(self.subject.getObservers())
        event.Skip()

if __name__ == '__main__':
    app = wx.App()
    reactor.registerWxApp(app)
    frame = MainController(None)
    frame.Show()
    app.MainLoop()
