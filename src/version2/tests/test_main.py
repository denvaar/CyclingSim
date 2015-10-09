import unittest
import wx
#from twisted.internet import wxreactor
#wxreactor.install()
#from twisted.internet import reactor
from src.version2.frmMain import MainController

class TestMain(unittest.TestCase):
    def setup(self):
        app = wx.App()
        #reactor.registerWxApp(app)
        frame = MainController(None)
        frame.Show()
        app.MainLoop()

if __name__ == '__main__':
    unittest.main()
