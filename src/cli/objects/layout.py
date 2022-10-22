from objects.domino import Domino


class Layout:
    def __init__(self):
        self.layout = []
        self.tails = []
        self.value = 0

    def __str__(self):
        return str(self.layout)

    def moves(self, domino: Domino):
        # returns a list of indexes of the possible tails we can play on
        result = []
        for i, tail in enumerate(self.tails):
            if domino.num1 == tail or domino.num2 == tail:
                result.append(i)
        return result

    def calc_value(self):
        self.value = 0
        for tail in self.tails:
            self.value += tail
        return self.value
