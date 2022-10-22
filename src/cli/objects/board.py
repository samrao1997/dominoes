from dataclasses import dataclass, field
from typing import List
import random

from domino import Domino
from layout import Layout


@dataclass
class Board():


    def generate_boneyard(self, n = 9):
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                
                self.boneyard.append(Domino(i, j))
                
    
    
    boneyard: List[Domino] = field(default_factory=generate_boneyard)
    layout: Layout = Layout()
    
    # layout
    # This is the layout of the board. It is a list of dominoes. 
    # The first domino and the last domino are the ends of the layout where you can play
    # But also when people play doubled is make a new list of dominoes inside the layout
    
    
    
    
    
                
    def draw_from_boneyard(self):
        idx = random.randint(0, len(self.boneyard) - 1)
        return self.boneyard.pop(idx)
    
    
    def get_tails(self):
        # get the ends of the layout
        pass
    
    
    