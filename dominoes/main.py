import random
import collections


class Domino:
    def __init__(self, first, second):
        self.first = first
        self.second = second

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
        # self.children = []
        self.left = None
        self.right = None
        self.top = None
        self.bottom = None

    def add_dnode(self, domino, location):
        if location not in ["left", "right", "top", "bottom"]:
            # TODO: Raise exception location must be legal location
            return False

        if domino.first not in [self.domino.first, self.domino.second] or domino.second not in [
            self.domino.first,
            self.domino.second,
        ]:
            # TODO: Raise exception illegal domino
            return False

        match location:
            case "top":
                if self.domino.first != self.domino.second:
                    # TODO: Raise exception trying to top or bottom of a non double domino
                    return False
                else:
                    # TODO: do double domino things with location set to top
                    return None

            case "bottom":
                if self.domino.first != self.domino.second:
                    # TODO: Raise exception trying to top or bottom of a non double domino
                    return False
                else:
                    # TODO: do double domino things with location set to bottom
                    return None

            case "left":
                if self.domino.first != domino.first:
                    domino = domino.inverted()

            case "right":
                if self.domino.second != domino.first:
                    domino = domino.inverted()


def get_leafs(root):
    # gets the leafs of the dominos that we
    # NOTE: this only works with a complete tree
    if not root:
        return []

    leafs = []
    stack = [root]
    while stack:
        dnode = stack.pop()

        # TODO: check if double that we can play on
        if len(dnode.children) <= 1:
            leafs.append(dnode)
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

    def get_ends(self):
        pass


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
