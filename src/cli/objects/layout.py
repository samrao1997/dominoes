from objects.domino import Domino


class Layout:
    def __init__(self):
        self.layout = []
        self.tails = []
        self.value = 0

    def __str__(self):
        return str(self.layout)

    def moves(self, domino: Domino):
        # returns a list of indexes of the possible tails we can play on
        result = []
        for i, tail in enumerate(self.tails):
            if domino.num1 == tail or domino.num2 == tail:
                result.append(i)
        return result

    def get_tails(self):
        # returns a list of the tails of the layout
        # only work for single line rn
        result = []
        for idx, line in enumerate(self.layout):
            result.append(line[0].num1)
            result.append(line[-1].num2)
        return result

    def calc_value(self):
        self.value = 0
        for idx, line in enumerate(self.layout):

            # deal with other lines that are the main line
            if idx != 0:
                n = len(line)

                # just the double
                if n == 1:
                    continue

                # situation where we have a double and another tile
                elif n == 2:
                    # just count one side of line
                    for idx, d in enumerate(line):
                        if d.num1 == d.num2:
                            continue
                        else:
                            # on the left
                            if idx == 0:
                                self.value += d.num1
                            # on the right
                            else:
                                self.value += d.num2
                # line has been build upon
                else:
                    self.value += line[0].num1 + line[-1].num2

            else:
                self.value += line[0].num1 + line[-1].num2
