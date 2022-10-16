from dataclasses import dataclass


from board import Board
from hand import Hand




@dataclass
class Player():
    hand: Hand = Hand()
    score: int = 0    
        
    def play(self, board: Board):
        pass
    
    def draw(self, board: Board):
        pass
    
    def draw_hand(self, board: Board, hand_count: int):
        for _ in range(hand_count):
            self.draw(board)
            
            
