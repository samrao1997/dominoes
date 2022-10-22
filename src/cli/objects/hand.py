from objects.domino import Domino



class Hand():
    
    def __init__(self):
        self.dominoes = []
    
    def __str__(self):
        return str(self.dominoes)
    
    def play(self, domino: Domino):
        if domino in self.dominoes:
            self.dominoes.remove(domino)
            return True
        else:
            return False
        
    def draw(self, domino: Domino):
        self.dominoes.append(domino)
        
        