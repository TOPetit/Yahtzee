from diceSet import DiceSet

faces = 6

class Master:

    def __init__(self) -> None:
        pass

    def evaluate(self, diceSet: DiceSet) -> int:
        self.digits(diceSet, 1)
        self.digits(diceSet, 2)
        self.digits(diceSet, 3)
        self.digits(diceSet, 4)
        self.digits(diceSet, 5)
        self.digits(diceSet, 6)
        self.threeOfAKind(diceSet)
        self.fourOfAKind(diceSet)
        self.yahtzee(diceSet)
        self.full(diceSet)
        self.smallStraight(diceSet)
        self.largeStraight(diceSet)
        self.chance(diceSet)

    def digits(self, diceSet: DiceSet, digit: int) -> int:
        raw = diceSet.getValue().count(digit)
        points = digit * raw
        print("[{:02d}] - {:d}  : {:d}".format(points, digit, raw))
        return points

    def threeOfAKind(self, diceSet: DiceSet) -> None:
        points = diceSet.sumValue()
        for i in range(faces):
            if diceSet.getValue().count(i+1) == 3:
                print("[{:02d}] - Three of a kind : {:d}".format(points, i+1))
        return points

    def fourOfAKind(self, diceSet: DiceSet) -> None:
        points = diceSet.sumValue()
        for i in range(faces):
            if diceSet.getValue().count(i+1) == 4:
                print("[{:02d}] - four of a kind : {:d}".format(points, i+1))
        return points
    
    def yahtzee(self, diceSet: DiceSet) -> None:
        for i in range(faces):
            if diceSet.getValue().count(i+1) == 5:
                print("[50] - Yahtzee : {:d}".format(i+1))
        return 50
    
    def full(self, diceSet: DiceSet) -> None:
        value = 0
        for i in range(faces):
            if diceSet.getValue().count(i+1) == 3:
                value = i + 1
                for j in range(faces):
                    if diceSet.getValue().count(j+1) == 2:
                        print("[25] - Full house : {:d} (x3)  {:d} (x2)".format(value, j+1))
        return 25

    def smallStraight(self, diceSet: DiceSet) -> None:
        which = [False] * faces
        for i in range(diceSet.nbDices):
            which[diceSet.dices[i].getValue() - 1] = True
        if [True] * (diceSet.nbDices - 1) in [which[: -2], which[1: -1], which[2:]]:
            print("[30] - Small straight")
        return 30

    def largeStraight(self, diceSet: DiceSet) -> None:
        which = [False] * faces
        for i in range(diceSet.nbDices):
            which[diceSet.dices[i].getValue() - 1] = True
        if [True] * (diceSet.nbDices) in [which[: -1], which[1:]]:
            print("[40] - Large straight")
        return 40

    def chance(self, diceSet: DiceSet) -> None:
        points = diceSet.sumValue()
        print("[{:02d}] - Chance".format(points))
        return points