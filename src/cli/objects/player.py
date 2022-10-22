from dataclasses import dataclass


from objects.domino import Domino
from objects.hand import Hand


class Player:
    def __init__(self, board):
        self.hand = Hand()
        self.score = 0
        self.board = board

    def play(self, domino: Domino):
        if self.board.layout.layout == []:
            go_again, score = self.board.play(domino)
            self.hand.play(domino)

            self.score += score
            return (True, go_again)
        
        

    def draw(self):
        domino = self.board.draw_from_boneyard()
        self.hand.draw(domino)

    def draw_hand(self, hand_count: int):
        for _ in range(hand_count):
            self.draw(self.board)

    def get_valid_placements(self):
        placements = []
        for idx, domino in enumerate(self.hand.dominoes):
            for placement in self.board.get_valid_placements(domino):
                placements.append((domino, placement))
        return placements
