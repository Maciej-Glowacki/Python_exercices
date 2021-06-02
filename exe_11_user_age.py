# Thanks to input() we can get information from users terminal

name = input('Write your name: ')
year = input('Write the year of your birth: ')
year = int(year)

age = 2021 - year
print(f'{name} is {age} years old')
