from diceSet import DiceSet
from master import Master

def main():

    master = Master()

    dices = DiceSet()
    dices.throw([True]*DiceSet.nbDices)
    #dices.setValue([6, 2, 3, 4, 5])
    dices.printValue()
    master.evaluate(dices)


if __name__ == "__main__":
    main()

