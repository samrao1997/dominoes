import random
import collections


class Domino:
    def __init__(self, first, second):
        self.first = first
        self.second = second
        self.marked = "None"

    def inverted(self):
        return Domino(self.second, self.first)

    def __str__(self):
        return "[{0}|{1}]".format(self.first, self.second)

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return (self.first, self.second) == (other.first, other.second) or (
            self.first,
            self.second,
        ) == (other.second, other.first)

    def __ne__(self, other):
        return not self == other

    def __contains__(self, key):
        return key == self.first or key == self.second


class dNode:
    def __init__(self):
        self.domino = None
        # NOTE: If current node is a double domino then there will be 3 chilren [4 if it is first domino]
        # otherwise there is only 2
        self.children = []

    def set_domino(self, domino):
        pass

    def add_dNode(self, domino):
        pass


def get_leafs(root):
    # gets the leafs of the dominos that we
    if not root:
        return []

    leafs = []
    stack = [root]
    while stack:
        dnode = stack.pop()

        if dnode.children == []:
            leafs.append(dnode)
        else:
            stack.extend(dnode.children)

    return leafs


class Player(object):
    def __init__(self, board, starting_number_of_tiles=13):
        self.board = board
        self.score = 0
        self.hand = self.draw_dominos_from_graveyard(starting_number_of_tiles)

    def draw_dominos_from_graveyard(self, number_of_tiles):
        hand = []
        for _ in range(number_of_tiles):
            domino = self.board.graveyard.pop()
            hand.append(domino)
        return hand


class Board(object):
    def __init__(self):
        self.graveyard = self.gen_all_dominos()

    def gen_all_dominos(self):
        dominos = [Domino(i, j) for i in range(10) for j in range(i, 10)]
        random.shuffle(dominos)
        return dominos


class Game(object):
    def __init__(self, number_of_players=2):
        self.board = Board()
        self.players = [Player(self.board) for _ in range(number_of_players)]

    def print_all_dominos(self):
        for idx, player in enumerate(self.players):
            print(f"Player {idx}: {player.hand}")

        print(f"Graveyard: {self.board.graveyard}")

    def start_game(self):
        # init the number of players
        # start the games
        players = [Player(self.board) for _ in range(self.number_of_players)]


def main():
    game = Game()
    game.print_all_dominos()


if __name__ == "__main__":
    main()
