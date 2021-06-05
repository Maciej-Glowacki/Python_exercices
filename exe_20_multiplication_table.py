num = int(input('Write a number from 1 to 10: '))

while num > 10 or num < 1:
    print('Your number is incorrect!')
    num = int(input('Write a number from 1 to 10: '))

for element in range(1, 11):
    result = element * num
    print(f"{element} * {num} = {result}")