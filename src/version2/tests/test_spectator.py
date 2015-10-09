import unittest

from src.version2.spectator import Spectator

class TestFakeDatabase(unittest.TestCase):
    def testImports(self):
        self.failUnlessRaises(NotImplementedError, Observer().update, 'aaa')
        self.failUnlessRaises(NotImplementedError, Observer().cleanup)
if __name__ == '__main__':
    unittest.main()
