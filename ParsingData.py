
class ParsingData(object):

    def __init__(self):
        self._line = ''
        self.position = []
        self.x2 = 0
        self.x1 = 0
        self.c = 0
        return

    @property
    def line(self):
        return self._line

    @line.setter
    def line(self, new_line):
        self._line = new_line
        self.position = list(range(len(self.line)))
        pass

    

    def clean(self):
        self.x2 = 0
        self.x1 = 0
        self.c = 0
        return

     