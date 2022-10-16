from dataclasses import dataclass
from typing import List

from domino import Domino


@dataclass
class Hand():
    dominoes : List[Domino] = []
    
    
    def play(self, domino: Domino):
        if domino in self.dominoes:
            self.dominoes.remove(domino)
            return True
        else:
            return False