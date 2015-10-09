import unittest

from src.version2.observer import Observer

class TestFakeDatabase(unittest.TestCase):
    def testUsingInterface(self):
        self.failUnlessRaises(NotImplementedError, Observer().update, 'aaa')
        self.failUnlessRaises(NotImplementedError, Observer().cleanup)
if __name__ == '__main__':
    unittest.main()
