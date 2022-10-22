from dataclasses import dataclass


from objects.board import Board
from objects.domino import Domino
from objects.hand import Hand




class Player():
    def __init__(self):
        self.hand =  Hand()
        self.score = 0    
        
    def play(self, board: Board, domino: Domino):
        pass
    
    def draw(self, board: Board):
        domino = board.draw_from_boneyard()
        self.hand.draw(domino)
    
    def draw_hand(self, board: Board, hand_count: int):
        for _ in range(hand_count):
            self.draw(board)
            
    
            
            
