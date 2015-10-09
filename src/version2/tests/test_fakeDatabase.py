import unittest

from src.version2.fakeDatabase import FakeDatabase

class TestFakeDatabase(unittest.TestCase):
    def test_load(self):
        try:
            FakeDatabase().loadRacers()
        except IOError:
            raise AssertationError('Invalid file path.')

    def test_get_racer_list(self):
        self.failUnlessEqual(type(FakeDatabase().getRacerList()), type([]))

if __name__ == '__main__':
    unittest.main()
