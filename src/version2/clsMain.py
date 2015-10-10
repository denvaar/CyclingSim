import wx
from ObjectListView import ObjectListView, ColumnDefn

class MainView(wx.Frame):
    '''
    This is the GUI for the main controller.
    It allows a user to initiate different roles,
    such as race official, race promoter, or race
    spectator.
    '''
    def __init__(self, parent, **kwargs):
        super(MainView, self).__init__(parent,
             id=wx.ID_ANY,
             pos=wx.DefaultPosition,
             size=(425,450),
             style=wx.DEFAULT_FRAME_STYLE,
             **kwargs)
        self.statusBar = wx.StatusBar(self, wx.ID_ANY, wx.STB_DEFAULT_STYLE)
        self.statusBar.SetFieldsCount(1)
        self.statusBar.SetStatusText('Status: Not listening.', 0)
        self.SetStatusBar(self.statusBar)

        self.SetSizeHints(425, 450)
        
        panel = wx.Panel(self, wx.ID_ANY)

        supa_sizer = wx.BoxSizer(wx.VERTICAL)
        
        sbSizer = wx.StaticBoxSizer(wx.StaticBox(panel, wx.ID_ANY, u"Race Setup"), wx.VERTICAL)
        
        self.instruct2Txt = wx.StaticText(panel, wx.ID_ANY,
            u"Choose which type of subscibers will recieve race updates.",
            wx.DefaultPosition, wx.DefaultSize, 0)
        
        bSizer = wx.BoxSizer(wx.HORIZONTAL)
        sbSizer.Add(self.instruct2Txt, 0, wx.ALL, 5)

        sbSizer.Add(bSizer, 0, wx.ALL, 5)
        
        choices = ['Race Official', 'Team Support', 'Spectator', 'Promoter']
        self.subscriberCombo = wx.ListBox(panel, wx.ID_ANY,
            wx.DefaultPosition, wx.DefaultSize,
            [], style=wx.LB_MULTIPLE)
        self.addBtn = wx.Button(panel, wx.ID_ANY, u"Add",
            wx.DefaultPosition, wx.DefaultSize, style=0)
        
        self.delBtn = wx.Button(panel, wx.ID_ANY, u"Remove",
            wx.DefaultPosition, wx.DefaultSize, style=0)
        
        bSizer.Add(self.subscriberCombo, 0, wx.ALL, 5)
        bSizer.Add(self.addBtn, 0, wx.ALL, 5)
        bSizer.Add(self.delBtn, 0, wx.ALL, 5)
        
        supa_sizer.Add(sbSizer, 0, wx.ALL|wx.EXPAND, 5)

        sbSizer2 = wx.StaticBoxSizer(wx.StaticBox(panel, wx.ID_ANY, u"Registered Subscribers"), wx.VERTICAL)
        
        self.olv = ObjectListView(panel, wx.ID_ANY,
            pos=wx.DefaultPosition, size=wx.DefaultSize,
            style=wx.LC_REPORT|wx.SUNKEN_BORDER)
        self.olv.SetObjects(None)
        self.olv.SetEmptyListMsg("No Subscribers")
        self.olv.SetColumns([
                    ColumnDefn('Type', 'left', 300, '__repr__'),
        ])
        sbSizer2.Add(self.olv, 1, wx.ALL|wx.EXPAND, 5)
        
        supa_sizer.Add(sbSizer2, 1, wx.ALL|wx.EXPAND, 5)

        self.beginBtn = wx.ToggleButton(panel, wx.ID_ANY, u"Begin Simulation",
            wx.DefaultPosition, wx.DefaultSize, 0)
        supa_sizer.Add(self.beginBtn, 0, wx.ALL|wx.CENTER, 5)

        
        
        panel.SetSizer(supa_sizer)

        self.Layout()
        self.Centre(wx.BOTH)

        self.Bind(wx.EVT_TOGGLEBUTTON, self.onBeginSim, self.beginBtn)
        self.Bind(wx.EVT_BUTTON, self.onAdd, self.addBtn)
        self.Bind(wx.EVT_BUTTON, self.onRemove, self.delBtn)
        self.Bind(wx.EVT_CLOSE, self.onClose)

    def __del__(self):
        pass

    def onBeginSim(self, event):
        event.Skip()
    def onClose(self, event):
        event.Skip()
    def onAdd(self, event):
        event.Skip()
    def onRemove(self, event):
        event.Skip()


