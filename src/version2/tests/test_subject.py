import unittest

from src.version2.subject import Subject

class TestFakeDatabase(unittest.TestCase):
    def testUsingInterface(self):
        self.failUnlessRaises(NotImplementedError, Subject().addObserver, None)
        self.failUnlessRaises(NotImplementedError, Subject().removeObserver, None)
        self.failUnlessRaises(NotImplementedError, Subject().notifyObservers)
if __name__ == '__main__':
    unittest.main()
