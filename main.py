from search import Search
from combinations import Combinations
from diceSet import DiceSet
from master import Master


def main():

    master = Master()

    dices = DiceSet()
    dices.throw([True] * DiceSet.nbDices)
    # dices.setValue([6, 2, 3, 4, 5])
    combinations = Combinations(dices)
    combinations.printValue()


if __name__ == "__main__":
    main()
