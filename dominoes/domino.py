import collections


# for convenience, immutability, and performance
DominoBase = collections.namedtuple("DominoBase", ["first", "second"])


class Domino(DominoBase):
    pass
