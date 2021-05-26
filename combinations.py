from diceSet import DiceSet

faces = 6


class Combinations:
    def __init__(self, diceSet: DiceSet) -> None:
        self.dices = diceSet
        self.one = self.digits(diceSet, 1)
        self.two = self.digits(diceSet, 2)
        self.three = self.digits(diceSet, 3)
        self.four = self.digits(diceSet, 4)
        self.five = self.digits(diceSet, 5)
        self.six = self.digits(diceSet, 6)
        self.three_of_a_kind = self.threeOfAKind(diceSet)
        self.four_of_a_kind = self.fourOfAKind(diceSet)
        self.small_straight = self.smallStraight(diceSet)
        self.large_straight = self.largeStraight(diceSet)
        self.full_house = self.full_house(diceSet)
        self.yahtzee = self.yahtzee(diceSet)
        self.chance = self.chance(diceSet)

    def digits(self, diceSet: DiceSet, digit: int) -> int:
        raw = diceSet.getValue().count(digit)
        points = digit * raw
        return raw, points

    def threeOfAKind(self, diceSet: DiceSet) -> None:
        raw = 0
        points = diceSet.sumValue()
        for i in range(faces):
            if diceSet.getValue().count(i + 1) == 3:
                raw = i + 1
        return raw, points

    def fourOfAKind(self, diceSet: DiceSet) -> None:
        raw = 0
        points = diceSet.sumValue()
        for i in range(faces):
            if diceSet.getValue().count(i + 1) == 4:
                raw = i + 1
        return raw, points

    def yahtzee(self, diceSet: DiceSet) -> None:
        raw = 0
        for i in range(faces):
            if diceSet.getValue().count(i + 1) == 5:
                raw = i + 1
        return raw, 50

    def full_house(self, diceSet: DiceSet) -> None:
        raw = []
        value = 0
        for i in range(faces):
            if diceSet.getValue().count(i + 1) == 3:
                for j in range(faces):
                    if diceSet.getValue().count(j + 1) == 2:
                        raw = [i + 1, j + 1]
        return raw, 25

    def smallStraight(self, diceSet: DiceSet) -> None:
        which = [False] * faces
        raw = []
        for i in range(diceSet.nbDices):
            which[diceSet.dices[i].getValue() - 1] = True
        if [True] * (diceSet.nbDices - 1) == which[:-2]:
            raw = [1, 2, 3, 4]
        if [True] * (diceSet.nbDices - 1) == which[1:-1]:
            raw = [2, 3, 4, 5]
        if [True] * (diceSet.nbDices - 1) == which[2:]:
            raw = [3, 4, 5, 6]
        return raw, 30

    def largeStraight(self, diceSet: DiceSet) -> None:
        raw = []
        which = [False] * faces
        for i in range(diceSet.nbDices):
            which[diceSet.dices[i].getValue() - 1] = True
        if [True] * (diceSet.nbDices) == which[:-1]:
            raw = [1, 2, 3, 4, 5]
        if [True] * (diceSet.nbDices) == which[1:]:
            raw = [2, 3, 4, 5, 6]
        return raw, 40

    def chance(self, diceSet: DiceSet) -> None:
        points = diceSet.sumValue()
        return points

    def printValue(self) -> None:
        print(f"Throw result : {self.dices.getValue()}.")

        if self.one[0] != 0:
            print("[{:02d}] - {:d}  : {:d}".format(self.one[1], 1, self.one[0]))
        if self.two[0] != 0:
            print("[{:02d}] - {:d}  : {:d}".format(self.two[1], 2, self.two[0]))
        if self.three[0] != 0:
            print("[{:02d}] - {:d}  : {:d}".format(self.three[1], 3, self.three[0]))
        if self.four[0] != 0:
            print("[{:02d}] - {:d}  : {:d}".format(self.four[1], 4, self.four[0]))
        if self.five[0] != 0:
            print("[{:02d}] - {:d}  : {:d}".format(self.five[1], 5, self.five[0]))
        if self.six[0] != 0:
            print("[{:02d}] - {:d}  : {:d}".format(self.six[1], 6, self.six[0]))
        if self.three_of_a_kind[0] != 0:
            print(
                "[{:02d}] - Three of a kind : {:d}".format(
                    self.three_of_a_kind[1], self.three_of_a_kind[0]
                )
            )
        if self.four_of_a_kind[0] != 0:
            print(
                "[{:02d}] - Four of a kind : {:d}".format(
                    self.four_of_a_kind[1], self.four_of_a_kind[0]
                )
            )
        if self.small_straight[0] != []:
            print(
                "[{:02d}] - Small Straight : {}".format(
                    self.small_straight[1], self.small_straight[0]
                )
            )
        if self.large_straight[0] != []:
            print(
                "[{:02d}] - Large Straight : {}".format(
                    self.large_straight[1], self.large_straight[0]
                )
            )
        if self.full_house[0] != []:
            print(
                "[25] - Full house : {:d} (x3)  {:d} (x2)".format(
                    self.full_house[0], self.full_house[1]
                )
            )
        print("[{:02d}] - Chance".format(self.chance))
