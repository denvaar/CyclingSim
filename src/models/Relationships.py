class ForeignKey:
    def __init__(self, to, id_):
        module = __import__('models.' + to + 's',
            fromlist=[to + 's'])
        _class = getattr(module, to)
        print id(_class)
