from typing import List
from dice import Dice



class DiceSet:

    dices = []
    nbDices = 5

    def __init__(self) -> None:
        for i in range(self.nbDices):
            self.dices.append(Dice())

    def throw(self, which) -> None:
        for i in range(self.nbDices):
            if which[i]:
                self.dices[i].throw()
    
    def getValue(self) -> List[int]:
        return list(map(lambda obj: obj.getValue(), self.dices))

    def sumValue(self) -> int:
        n = 0
        for dice in self.dices:
            n += dice.getValue()
        return n

    # TEST METHOD - use carefully
    def setValue(self, values: List[int]) -> None:
        for i in range(self.nbDices):
            self.dices[i].setValue(values[i])

    def printValue(self) -> None:
        print("\n------------------------------------")
        print("| Dices Values : {:d}".format(self.dices[0].getValue()), end="")
        for i in range(1, self.nbDices):
            print(" | {:d}".format(self.dices[i].getValue()), end="")
        print(" |")
        print("------------------------------------")