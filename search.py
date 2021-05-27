from diceSet import DiceSet
import itertools


class Search:
    def __init__(self) -> None:
        pass

    def choices(self, diceSet: DiceSet):
        return list(itertools.product([True, False], repeat=diceSet.nbDices))
