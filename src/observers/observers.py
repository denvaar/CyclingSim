class Observer:
    def __init__(self):
        pass
    def update(self, data): 
        raise NotImplementedError
    def cleanup(self):
        raise NotImplementedError
