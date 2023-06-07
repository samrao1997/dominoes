class dTree:
    def __init__(self):
        self.root = None
        # NOTE: If current node is a double domino then there will be 3 chilren
        # otherwise there is only 2
        self.children = []
