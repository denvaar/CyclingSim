import wx
from ObjectListView import ObjectListView, BatchedUpdate, ColumnDefn

class JumbotronUIMixin(wx.Frame):
    '''
    This is the GUI that displays a giant list of racers
    that the race promoter has decided to watch.
    '''
    def __init__(self, parent, **kwargs):
        super(JumbotronUIMixin, self).__init__(parent,
             id=wx.ID_ANY,
             pos=(50,50),
             size=(600,400),
             **kwargs)
        self.parent = parent
        self.SetTitle('~ ~ ~ J U M B O T R O N ~ ~ ~') 
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
                    ColumnDefn('Time', 'left', 80, 'getPrettyTime'),
                    ColumnDefn('Sensor', 'left', 50, 'getSensor'),
        ])
        
        supa_sizer.Add(self.olv1, 1, wx.ALL|wx.EXPAND, 5)
        self.olv = BatchedUpdate(self.olv1, 0.5)
        panel.SetSizer(supa_sizer)

        self.Layout()
        self.Show(True)

