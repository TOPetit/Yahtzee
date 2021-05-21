import random as rd


class Dice:

    def __init__(self) -> None:
        self.value = 0
    
    def throw(self) -> None:
        self.value = rd.randint(1, 6)

    def getValue(self) -> int:
        return self.value

    def setValue(self, value: int) -> None:
        self.value = value