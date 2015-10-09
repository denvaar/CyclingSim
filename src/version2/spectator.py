import wx

#import smtplib
#import email.utils
#from email.mime.text import MIMEText
#from email.mime.multipart import MIMEMultipart

# Local imports
from src.version2.observer import Observer
from src.version2.clsSpectator import SpectatorView
from src.version2.spectatorEmail import SpectatorEmail
from src.version2.my_email import Email

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

        self.parent = parent
        self.olv.SetObjects(dataSource.getRacerList())

        self.selectedObjects = []
        self.updatedObjects = []
    
    def doEmail(self, event):
        print "tick.."
        if self.updatedObjects:
            self.emailer.doEmail(self.updatedObjects)
            self.updatedObjects = []
    
    def update(self, data):
        print "Spectator recieved: %s" % data
        # If we have already added the object into 
        # the list, then just replace it rather than
        # append.
        if data in self.updatedObjects:
            self.updatedObjects[self.updatedObjects.index(data)] = data
        else:
            self.updatedObjects.append(data)
        # Pass the updates to the emailer.
        #self.emailer.setUpdatedObjects(self.updatedObjects)
    
    def __repr__(self):
        return "Spectator"
    
    #--------------------------
    # Event handlers
    #--------------------------

    def onOK(self, event):
        selected = self.olv.GetSelectedObjects()
        emailAddr = self.emailTxtCtrl.GetValue()

        self.selectedObjects = selected
        self.emailAddr = emailAddr

        # Subscribe to each selected racer object.
        [obj.addObserver(self) for obj in self.selectedObjects]
        
        self.emailTimer = wx.Timer(self)
        self.emailTimer.Start(9000)
        self.Bind(wx.EVT_TIMER, self.doEmail)
        
        # Create a new decorated emailer.
        self.emailer = SpectatorEmail(Email(self.emailAddr))
       
        # Hide the GUI now.
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
