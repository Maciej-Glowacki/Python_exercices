name = input('What is your name? ')
password = input('What is your password? ')
length = len(password)
length_hash = length * '*'

print(f'{name}, your password is {length_hash} and it is {length} letters long')