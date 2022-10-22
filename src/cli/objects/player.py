from dataclasses import dataclass


from objects.board import Board
from objects.domino import Domino
from objects.hand import Hand




class Player():
    def __init__(self):
        self.hand =  Hand()
        self.score = 0    
        
    def play(self, board: Board, domino: Domino):
        if board.layout.layout == []:
            board.play(domino)
            self.hand.play(domino)
            return True
    
    def draw(self, board: Board):
        domino = board.draw_from_boneyard()
        self.hand.draw(domino)
    
    def draw_hand(self, board: Board, hand_count: int):
        for _ in range(hand_count):
            self.draw(board)
            
            
    def get_valid_placements(self, board: Board):
        placements = []
        for idx, domino in enumerate(self.hand.dominoes):
            for placement in board.get_valid_placements(domino):
                placements.append((domino, placement))
        return placements
    
            
    
            
            
