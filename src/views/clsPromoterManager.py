import wx
from ObjectListView import ObjectListView, ColumnDefn


class PromoterManagerView(wx.Frame):
    def __init__(self, parent, **kwargs):
        super(PromoterManagerView, self).__init__(parent,
             id=wx.ID_ANY,
             pos=wx.DefaultPosition,
             size=(750,300),
             style=wx.DEFAULT_FRAME_STYLE,
             **kwargs)
        
        self.SetSizeHints(750, 300)
        
        panel = wx.Panel(self, wx.ID_ANY)

        supa_sizer = wx.BoxSizer(wx.VERTICAL)
        
        
        self.instruct2Txt = wx.StaticText(panel, wx.ID_ANY,
            u"Add or remove racers to the jumbotron display.",
            wx.DefaultPosition, wx.DefaultSize, 0)
        
        supa_sizer.Add(self.instruct2Txt, 0, wx.ALL|wx.CENTER, 5)

        buttonBox = wx.BoxSizer(wx.HORIZONTAL) 
        self.addBtn = wx.Button(panel, wx.ID_ANY, u">>",
            wx.DefaultPosition, wx.DefaultSize, style=0)
        self.delBtn = wx.Button(panel, wx.ID_ANY, u"<<",
            wx.DefaultPosition, wx.DefaultSize, style=0)
        
        
        buttonBox.Add(self.delBtn, 0, wx.ALL|wx.CENTER, 5)
        buttonBox.Add(self.addBtn, 0, wx.ALL|wx.CENTER, 5)
        supa_sizer.Add(buttonBox, 0, wx.ALL|wx.CENTER, 5)
        
        bSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.olv = ObjectListView(panel, wx.ID_ANY,
            pos=wx.DefaultPosition, size=wx.DefaultSize,
            style=wx.LC_REPORT|wx.SUNKEN_BORDER)
        self.olv.SetObjects(None)
        self.olv.SetEmptyListMsg("Loading...")
        self.olv.SetColumns([
                    ColumnDefn('Racer', 'left', 150, 'getName'),
                    ColumnDefn('Bib Number', 'left', 70, 'getBib'),
                    ColumnDefn('Team', 'left', 100, 'getTeam'),
        ])
        bSizer.Add(self.olv, 1, wx.ALL|wx.EXPAND, 5)
        
        self.olv2 = ObjectListView(panel, wx.ID_ANY,
            pos=wx.DefaultPosition, size=wx.DefaultSize,
            style=wx.LC_REPORT|wx.SUNKEN_BORDER)
        self.olv2.SetObjects(None)
        self.olv2.SetEmptyListMsg("None")
        self.olv2.SetColumns([
                    ColumnDefn('Racer', 'left', 150, 'getName'),
                    ColumnDefn('Bib Number', 'left', 70, 'getBib'),
                    ColumnDefn('Team', 'left', 100, 'getTeam'),
        ])
        bSizer.Add(self.olv2, 1, wx.ALL|wx.EXPAND, 5)
        supa_sizer.Add(bSizer, 1, wx.ALL|wx.EXPAND, 5)
        
        panel.SetSizer(supa_sizer)

        self.Layout()
        self.Centre(wx.BOTH)

        self.Bind(wx.EVT_BUTTON, self.onAdd, self.addBtn)
        self.Bind(wx.EVT_BUTTON, self.onRemove, self.delBtn)

    def __del__(self):
        pass

    def onAdd(self, event):
        event.Skip()
    def onRemove(self, event):
        event.Skip()
