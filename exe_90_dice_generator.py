import random


class Dice:
    def __init__(self, dice_type, number_of_rolls=1):
        self.dice_type = self.__validate_dice_type(dice_type)
        self.number_of_rolls = number_of_rolls
        # self.roll_number = None

    def __validate_dice_type(self, new_dice_type):
        if new_dice_type not in [3, 4, 6, 8, 10, 12, 20, 100]:
            raise ValueError("Wrong dice type")
        return new_dice_type
    
    def __iter__(self):
        self.roll_number = 0
        return self

    def __next__(self):
        if self.roll_number >= self.number_of_rolls:
            raise StopIteration
        self.roll_number += 1
        return self.roll()

    def roll(self):
        return random.randint(1, self.dice_type)


def roll_the_dice(n):
    for throw in Dice(dice_type=6, number_of_rolls=n):
        yield throw


print("Generator dice")
generated_dice = roll_the_dice(3)
for throw in generated_dice:
    print(throw)

e = Dice(100, 3)
print("My dice")
for throw in e:
    print(throw)

print("Computer dice")
for throw in Dice(dice_type=6, number_of_rolls=3):
    print(throw)