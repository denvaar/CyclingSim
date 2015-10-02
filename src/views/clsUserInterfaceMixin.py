import wx
from ObjectListView import ObjectListView, BatchedUpdate, ColumnDefn

class UserInterfaceMixin(wx.Frame):
    def __init__(self, parent, **kwargs):
        super(UserInterfaceMixin, self).__init__(parent,
             id=wx.ID_ANY,
             pos=(50,50),
             size=(600,400),
             **kwargs)
         
        panel = wx.Panel(self, wx.ID_ANY)

        supa_sizer = wx.BoxSizer(wx.VERTICAL)
        
        self.olv1 = ObjectListView(panel, wx.ID_ANY,
            pos=wx.DefaultPosition, size=(400,400),
            style=wx.LC_REPORT|wx.SUNKEN_BORDER)
        self.olv1.SetObjects(None)
        self.olv1.SetEmptyListMsg("Stay tuned for race updates!")
        self.olv1.SetColumns([
                    ColumnDefn('Racer', 'left', 300, 'getBibAndName'),
                    ColumnDefn('Team', 'left', 80, 'getTeam'),
                    ColumnDefn('Time', 'left', 80, 'lastTime'),
                    ColumnDefn('Sensor', 'left', 50, 'lastSensor'),
        ])
        
        supa_sizer.Add(self.olv1, 1, wx.ALL|wx.EXPAND, 5)
        
        self.olv = BatchedUpdate(self.olv1, 0.5)
        
        panel.SetSizer(supa_sizer)

        #self.Bind(wx.EVT_CLOSE, self.onClose)

        self.Layout()