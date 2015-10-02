class Subject:
    def __init__(self):
        pass
    def addObserver(self, observer):
        raise NotImplementedError
    def removeObserver(self, observer):
        raise NotImplementedError
    def notifyObservers(self):
        raise NotImplementedError
