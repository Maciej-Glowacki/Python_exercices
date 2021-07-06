from random import randint

num = int(input('Write numbers from 1 to 3 which are: 1-stone, 2-scisores, 3-paper: '))
num2 = randint(1, 3)

if num == num2:
    print(f'Computer draws {num2}. Draw')
elif num == 1 and num2 == 2:
    print(f'Computer draws {num2}. You win!')
elif num == 1 and num2 == 3:
    print(f'Computer draws {num2}. Computer wins!')
elif num == 2 and num2 == 1:
    print(f'Computer draws {num2}. Computer wins!')
elif num == 2 and num2 == 3:
    print(f'Computer draws {num2}. You win!')
elif num == 3 and num2 == 1:
    print(f'Computer draws {num2}. You win!')
elif num == 3 and num2 == 2:
    print(f'Computer draws {num2}. Computer wins!')