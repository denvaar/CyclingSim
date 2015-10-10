# System imports
import wx

class EmailInputView(wx.Frame):
    '''
    This is the GUI that allows a race official to
    enter their E-Mail address.
    '''
    def __init__(self, parent, **kwargs):
        super(EmailInputView, self).__init__(parent,
             id=wx.ID_ANY,
             pos=wx.DefaultPosition,
             size=(400,160),
             style=wx.DEFAULT_FRAME_STYLE,
             **kwargs)
        self.SetTitle("Race Official Setup") 
        self.SetSizeHints(400, 160)
        self.SetMaxSize((400, 160))
        panel = wx.Panel(self, wx.ID_ANY)
        supa_sizer = wx.BoxSizer(wx.VERTICAL)
        
        self.instruct2Txt = wx.StaticText(panel, wx.ID_ANY,
            u"Sign up to recieve alerts when cheaters are detected.",
            wx.DefaultPosition, wx.DefaultSize, 0)
        
        supa_sizer.Add(self.instruct2Txt, 0, wx.ALL, 5)
        
        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        bSizer4 = wx.BoxSizer(wx.HORIZONTAL) 
        self.emailTxt = wx.StaticText(panel, wx.ID_ANY, u"E-mail Address:",
            wx.DefaultPosition, wx.DefaultSize, style=0)
        self.emailTxtCtrl = wx.TextCtrl(panel, wx.ID_ANY, u"",
            wx.DefaultPosition, wx.DefaultSize, style=0)
        bSizer4.Add(self.emailTxt, 0, wx.ALL, 5)
        bSizer4.Add(self.emailTxtCtrl, 1, wx.ALL|wx.EXPAND, 5)
        bSizer2.Add(bSizer4, 0, wx.ALL|wx.EXPAND, 5)

        bSizer5 = wx.BoxSizer(wx.VERTICAL)
        bSizer3 = wx.BoxSizer(wx.HORIZONTAL)
        self.cancelBtn = wx.Button(panel, wx.ID_ANY, u"Cancel",
                    wx.DefaultPosition, wx.DefaultSize, style=0)
        self.okBtn = wx.Button(panel, wx.ID_ANY, u"OK",
                    wx.DefaultPosition, wx.DefaultSize, style=0)
        bSizer3.Add(self.cancelBtn, 0, wx.ALL, 5)
        bSizer3.Add(self.okBtn, 0, wx.ALL, 5)
        bSizer5.Add(bSizer3, 0, wx.ALL|wx.EXPAND, 5)
        
        supa_sizer.Add(bSizer2, 1, wx.ALL|wx.EXPAND, 5)
        supa_sizer.Add(bSizer5, 1, wx.ALL|wx.ALIGN_RIGHT, 5)
        panel.SetSizer(supa_sizer)

        self.Layout()
        self.Centre(wx.BOTH)
        
        self.Show(True)

    def __del__(self):
        pass
