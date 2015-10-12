import unittest

from src.version2.my_email import Email

class TestFakeDatabase(unittest.TestCase):
    def testSendmail(self):
        try:
            self.email = Email('denverpsmith@gmail.com')
            self.email.sendEmail("""<html><body>test message</body></html>""")
        except:
            self.fail('Error')
if __name__ == '__main__':
    unittest.main()
