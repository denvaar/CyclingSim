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

class Spectator(Observer):
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
        # Get a handle to the parent window.
        self.parent = parent
        # Setup a view to handle the user interface.
        self.view = SpectatorView(parent)
        # Bind events to handlers.
        self.view.okBtn.Bind(wx.EVT_BUTTON, self.onOK)
        self.view.cancelBtn.Bind(wx.EVT_BUTTON, self.onCancel)
        self.view.Bind(wx.EVT_CLOSE, self.onClosing)

        self.view.olv.SetObjects(dataSource.getRacerList())
        self.selectedObjects = []
        self.updatedObjects = []
    
    def doEmail(self, event):
        if self.updatedObjects:
            self.emailer.doEmail(self.updatedObjects)
            self.updatedObjects = []
    
    def update(self, data):
        # If we have already added the object into 
        # the list, then just replace it rather than
        # append.
        if data in self.updatedObjects:
            self.updatedObjects[self.updatedObjects.index(data)] = data
        else:
            self.updatedObjects.append(data)
    
    def Close(self):
        self.view.Close()
 
    def __repr__(self):
        return unicode("Spectator")
    
    # =============================
    # Event handlers
    # =============================

    def onOK(self, event):
        selected = self.view.olv.GetSelectedObjects()
        emailAddr = self.view.emailTxtCtrl.GetValue()

        self.selectedObjects = selected
        self.emailAddr = emailAddr

        # Subscribe to each selected racer object.
        [obj.addObserver(self) for obj in self.selectedObjects]
        
        self.emailTimer = wx.Timer(self.view)
        self.emailTimer.Start(9000)
        self.view.Bind(wx.EVT_TIMER, self.doEmail)
        
        # Create a new decorated emailer.
        self.emailer = SpectatorEmail(Email(self.emailAddr))
       
        # Hide the GUI now.
        self.view.Show(False)
        event.Skip()

    def onCancel(self, event):
        self.view.Close()
        event.Skip()

    def onClosing(self, event):
        try:
            self.view.emailTimer.Stop()
        except AttributeError:
            pass 
        [obj.removeObserver(self) for obj in self.selectedObjects]
        self.parent.olv.RemoveObject(self)
        event.Skip()

