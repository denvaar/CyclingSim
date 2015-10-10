
class Emailer:
    '''
    This is the tiny interface for
    something that sends an email.
    '''
    def __init__(self):
        pass
    def sendEmail(self, body_txt):
        raise NotImplementedError

