import random

def random_average(n):
    lst = []
    while len(lst) < n:
        lst.append(random.randint(1, 100))
    average = sum(lst) / len(lst)
    return f'Your numbers are: {lst}. Average is {average}'

print(random_average(2))
