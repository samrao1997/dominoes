
import random

from objects.domino import Domino
from objects.layout import Layout


class Board():
    def __init__(self):
        self.boneyard = []
        self.layout = Layout()
        self.generate_boneyard()


    def generate_boneyard(self, n = 9):
        for i in range(n + 1):
            for j in range(n + 1):
                domino = Domino(i, j)
                if domino not in self.boneyard:
                    self.boneyard.append(Domino(i, j))
                    
        return self.boneyard
            
                
    def draw_from_boneyard(self):
        idx = random.randint(0, len(self.boneyard) - 1)
        return self.boneyard.pop(idx)
    
    
    def get_tails(self):
        # get the ends of the layout
        return self.layout.tails
    
    def get_valid_placements(self, domino: Domino):
        placements = []
        for idx, tail in enumerate(self.get_tails()):
            if domino.num1 == tail or domino.num2 == tail:
                placements.append((idx, tail))
        return placements
    
    def play(self, domino: Domino):
        self.layout.layout.append(domino)
        self.layout.tails.append(domino.num1)
        self.layout.tails.append(domino.num2)
        self.layout.calc_value()

    
    
    