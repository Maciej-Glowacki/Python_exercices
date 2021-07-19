import random

computer = random.randint(1, 5)

while True:
    player = int(input('Choose the number from 1 to 5: '))
    if player == computer:
        print('You\'ve guesed!')
        break
    else:
        print('Try once again! ')