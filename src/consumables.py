# by Lilly Pernichele


class Consumables:
    consume_type = 0

    def __init__(self):
        self.consume_type = 0

    def set_type(self, x):
        self.consume_type = x

    def get_type(self):
        return self.consume_type
