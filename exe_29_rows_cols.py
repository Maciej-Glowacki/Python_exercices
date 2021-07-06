from random import randint

rows = randint(5, 15)
cols = randint(5, 15)

print(f'rows = {rows} and columns = {cols}')

num = 0
while rows > num:
    print(cols * '*')
    num += 1
