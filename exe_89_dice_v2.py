import random


class Dice:
    def __init__(self, dice_type):
        self.dice_type = self.__validate_dice_type(dice_type)

    def __validate_dice_type(self, new_dice_type):
        if new_dice_type not in [3, 4, 6, 8, 10, 12, 20, 100]:
            raise ValueError("Wrong dice type")
        return new_dice_type

    def roll(self):
        return random.randint(1, self.dice_type)


e = Dice(100)
print(e.roll())
print(e.roll())
e1 = Dice(7)


# Napisz klasę Dice, która będzie miała własność dice_type. W tej własności będziesz przechowywać liczbę ścianek kostki. Kostka może być 3, 4, 6, 8, 10, 12, 20 lub 100-ścienna. Pamiętaj o sprawdzeniu, czy wartość parametru jest właściwa. Jeśli nie, wyrzuć błąd: ValueError.

# Napisz metodę roll(), która wylosuje liczbę z zakresu 1..dice_type, czyli zasymuluje rzut kostką.