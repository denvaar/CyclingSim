import wx

import smtplib
import email.utils
from email.mime.text import MIMEText

# Local imports
from src.version2.observer import Observer
from src.version2.clsSpectator import SpectatorView

class Spectator(Observer, SpectatorView):
    '''
    Spectator -- This is the class that represents
                 a race spectator. A spectator can
                 recieve race updates via E-mail for
                 specific racers.
                 
                 Spectator implements the Observer
                 interface.
    '''
    def __init__(self, parent, dataSource):
        # Call the base class constructors.
        Observer.__init__(self)
        SpectatorView.__init__(self, parent)

        self.olv.SetObjects(dataSource.getRacerList())

        self.selectedObjects = []
        self.updatedObjects = []

    def doEmail(self, event):
        print "sending email"
        self.updatedObjects = []

    def update(self, data):
        print "Spectator recieved: %s" % data
        self.updatedObjects.append(data)

        msg_body = "You've signed up to recieve updates for the following racers:\n\n\
                   %s\t%s" % (data.getBibAndName(), data.getTime())   
        print msg_body
        return
        # New data has been recieved!
        # Send an email
        msg = MIMEText('')
        msg['To'] = email.utils.formataddr(('Recipient', self.emailAddr))
        msg['From'] = email.utils.formataddr(('Cycling Simulation', 'denverpsmith@gmail.com'))
        msg['Subject'] = 'Race Updates'

        server = smtplib.SMTP('mail')
        server.set_debuglevel(True) # show communication with the server
        try:
            server.sendmail(self.emailAddr, [self.emailAddr], msg.as_string())
        finally:
            server.quit()

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
        self.emailTimer.Start(2000)
        self.Bind(wx.EVT_TIMER, self.doEmail)
        
        self.Show(False)
        event.Skip()

    def onCancel(self, event):
        self.Close()
        event.Skip()

    def onClosing(self, event):
        print "closing..."
        [obj.removeObserver(self) for obj in self.selectedObjects]
        event.Skip()
