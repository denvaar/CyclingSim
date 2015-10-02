import wx
#from ObjectListView import ObjectListView, ColumnDefn


class SpectatorManagerView(wx.Frame):
    def __init__(self, parent, **kwargs):
        super(SpectatorManagerView, self).__init__(parent,
             id=wx.ID_ANY,
             pos=wx.DefaultPosition,
             size=(270,200),
             style=wx.DEFAULT_FRAME_STYLE,
             **kwargs)
        
        self.SetSizeHints(270, 200)
        
        panel = wx.Panel(self, wx.ID_ANY)

        supa_sizer = wx.BoxSizer(wx.VERTICAL)
        
        
        self.instruct2Txt = wx.StaticText(panel, wx.ID_ANY,
            u"Racer's Bib Number:",
            wx.DefaultPosition, wx.DefaultSize, 0)
        supa_sizer.Add(self.instruct2Txt, 0, wx.ALL, 5)

        self.bibTxt = wx.TextCtrl(panel, id=wx.ID_ANY, value="", pos=wx.DefaultPosition,
            size=(250,-1), style=0)
        supa_sizer.Add(self.bibTxt, 0, wx.ALL, 5)
        
        self.instructTxt = wx.StaticText(panel, wx.ID_ANY,
            u"E-Mail Address:",
            wx.DefaultPosition, wx.DefaultSize, 0)
        supa_sizer.Add(self.instructTxt, 0, wx.ALL, 5)
        
        self.emailTxt = wx.TextCtrl(panel, id=wx.ID_ANY, value="", pos=wx.DefaultPosition,
            size=(250,-1), style=0)
        supa_sizer.Add(self.emailTxt, 0, wx.ALL, 5)
        
        self.goBtn = wx.Button(panel, id=wx.ID_ANY, label="Get Updates!", pos=wx.DefaultPosition,
            size=wx.DefaultSize, style=0)
        supa_sizer.Add(self.goBtn, 0, wx.ALL, 5)
        
        panel.SetSizer(supa_sizer)

        self.Layout()
        self.Centre(wx.BOTH)

        self.Bind(wx.EVT_BUTTON, self.onGo, self.goBtn)
        #self.Bind(wx.EVT_BUTTON, self.onRemove, self.delBtn)

    def __del__(self):
        pass
    def onGo(self, event):
        event.Skip()

