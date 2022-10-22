from objects.domino import Domino


class Layout():
    
    def __init__(self):
        self.layout = []
        self.tails = []
        self.value = 0
    
    
    
    def moves(self, domino: Domino):
        # returns a list of indexes of the possible tails we can play on
        result = []
        for i, tail in enumerate(self.tails):
            if domino.num1 == tail or domino.num2 == tail:
                result.append(i)
        return result



