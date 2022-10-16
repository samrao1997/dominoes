from dataclasses import dataclass, field


@dataclass
class Domino():
    num1: int
    num2: int
    pips: tuple = field(init=False, repr=False)
    
    
    def __post_init__(self):
        self.pips = (self.num1, self.num2)
    
    
    def __eq__(self, other):
        # Dominoes are equal if they have the same pips
        return self.pips == other.pips or self.pips == other.pips[::-1]
