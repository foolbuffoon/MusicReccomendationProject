# by Lilly Pernichele
class Consumables:
    consumeType = 0

    def __init__(self):
        self.consumeType = 0

    def setType(self, x):
        self.consumeType = x

    def getType(self):
        return self.consumeType
