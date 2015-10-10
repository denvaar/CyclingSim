import wx

from src.version2.observer import Observer
from src.version2.clsEmailInput import EmailInputView
from src.version2.cheaterEmailer import CheaterEmailer
from src.version2.my_email import Email

class RaceOfficial(Observer):
    def __init__(self, parent, dataSource):
        self.view = EmailInputView(parent)
        self.view.okBtn.Bind(wx.EVT_BUTTON, self.onOK)
        self.view.cancelBtn.Bind(wx.EVT_BUTTON, self.onCancel)
        self.view.Bind(wx.EVT_CLOSE, self.onClosing)
        self.dataSource = dataSource

        self.racers = []
        self.possibleCheaters = []
        self.cheaters = []
        self.parent = parent
        [racer.addObserver(self) for racer in self.dataSource.getRacerList()]


    def getRacers(self):
        return self.racers

    def update(self, data):
        self.racers.append(data)
        self.cheaterCheck()
    
    def doEmail(self, event):
        if self.cheaters:
            self.emailer.doEmail(self.cheaters)
            self.cheaters = []
    
    def cheaterCheck(self):
        if len(self.racers) > 1:
            for i in range(-2, -1):
                if self.racers[-1].getSensor() == self.racers[i].getSensor():
                    if self.racers[-1].getTeam() != self.racers[i].getTeam():
                        if self.racers[-1].getTime() - self.racers[i].getTime() <= 3000:
                            if (self.racers[-1], self.racers[i]) in self.possibleCheaters or \
                               (self.racers[-2], self.racers[i]) in self.possibleCheaters:
                                
                                if (self.racers[-1], self.racers[i]) not in self.cheaters and \
                                   (self.racers[i], self.racers[-1]) not in self.cheaters:
                                    self.cheaters.append((self.racers[-1], self.racers[i]))
                            
                            self.possibleCheaters.append((self.racers[-1], self.racers[i]))
        
    # ===============================
    # Event Handlers
    # ===============================
    def onOK(self, event):
        emailAddr = self.view.emailTxtCtrl.GetValue()

        self.emailTimer = wx.Timer(self.view)
        self.emailTimer.Start(9000)
        self.view.Bind(wx.EVT_TIMER, self.doEmail)
    
        # Create a new decorated emailer.
        self.emailer = CheaterEmailer(Email(emailAddr))

        self.view.Show(False)
        event.Skip()
    
    def onCancel(self, event):
        self.view.Close()
        event.Skip()
    
    def onClosing(self, event):
        self.emailTimer.Stop()
        if self.view:
            self.view.Close()
        [racer.removeObserver(self) for racer in self.dataSource.getRacerList()]
        self.parent.olv.RemoveObject(self)
        event.Skip()

    def __repr__(self):
        return unicode('Race Official')
