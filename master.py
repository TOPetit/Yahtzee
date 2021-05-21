from diceSet import DiceSet

faces = 6

class Master:

    def __init__(self) -> None:
        pass

    def evaluate(self, diceSet: DiceSet) -> int:
        self.ones(diceSet)
        self.twos(diceSet)
        self.threes(diceSet)
        self.fours(diceSet)
        self.fives(diceSet)
        self.sixes(diceSet)
        self.threeOfAKind(diceSet)
        self.fourOfAKind(diceSet)
        self.yahtzee(diceSet)
        self.full(diceSet)
        self.smallStraight(diceSet)
        self.largeStraight(diceSet)
        self.chance(diceSet)

    def ones(self, diceSet: DiceSet) -> None:
        print("ones   : {:d}".format(diceSet.getValue().count(1)))

    def twos(self, diceSet: DiceSet) -> None:
        print("twos   : {:d}".format(diceSet.getValue().count(2)))

    def threes(self, diceSet: DiceSet) -> None:
        print("threes : {:d}".format(diceSet.getValue().count(3)))

    def fours(self, diceSet: DiceSet) -> None:
        print("fours  : {:d}".format(diceSet.getValue().count(4)))

    def fives(self, diceSet: DiceSet) -> None:
        print("fives  : {:d}".format(diceSet.getValue().count(5)))

    def sixes(self, diceSet: DiceSet) -> None:
        print("sixes  : {:d}".format(diceSet.getValue().count(6)))

    def threeOfAKind(self, diceSet: DiceSet) -> None:
        for i in range(faces):
            if diceSet.getValue().count(i+1) == 3:
                print("three of a kind : {:d}".format(i+1))

    def fourOfAKind(self, diceSet: DiceSet) -> None:
        for i in range(faces):
            if diceSet.getValue().count(i+1) == 4:
                print("four of a kind : {:d}".format(i+1))
    
    def yahtzee(self, diceSet: DiceSet) -> None:
        for i in range(faces):
            if diceSet.getValue().count(i+1) == 5:
                print("yahtzee : {:d}".format(i+1))
    
    def full(self, diceSet: DiceSet) -> None:
        value = 0
        for i in range(faces):
            if diceSet.getValue().count(i+1) == 3:
                value = i + 1
                for j in range(faces):
                    if diceSet.getValue().count(j+1) == 2:
                        print("full house : {:d} (x3)  {:d} (x2)".format(value, j+1))

    def smallStraight(self, diceSet: DiceSet) -> None:
        which = [False] * faces
        for i in range(diceSet.nbDices):
            which[diceSet.dices[i].getValue() - 1] = True
        if [True] * (diceSet.nbDices - 1) in [which[: -2], which[1: -1], which[2:]]:
            print("small straight")

    def largeStraight(self, diceSet: DiceSet) -> None:
        which = [False] * faces
        for i in range(diceSet.nbDices):
            which[diceSet.dices[i].getValue() - 1] = True
        if [True] * (diceSet.nbDices) in [which[: -1], which[1:]]:
            print("large straight")

    def chance(self, diceSet: DiceSet) -> None:
        n = 0
        for dice in diceSet.dices:
            n += dice.getValue()
        print("Chance : {:d}".format(n))