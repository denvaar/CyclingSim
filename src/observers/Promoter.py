from .observers import Observer

class Promoter(Observer):
    def __init__(self, subject):
        Observer.__init__(self)
        self.subject = subject

    def update(self, data):
        print "Promotor recieved: %s" % data

    def __repr__(self):
        return "Promoter"
   
    def cleanup(self):
        # Like saying, "Remove me from the list!"
        print "Remove me from the list!"
        #self.subject.removeObserver(self)

