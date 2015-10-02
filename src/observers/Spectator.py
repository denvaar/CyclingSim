from .observers import Observer

class Spectator(Observer):
    def __init__(self, subject):
        Observer.__init__(self)
        self.subject = subject
        #self.subject.addObserver(self)

    def update(self, data):
        print "I am a spectator and I just got this: %s" % data

    def cleanup(self):
        pass

    def __repr__(self):
        return "Spectator"
