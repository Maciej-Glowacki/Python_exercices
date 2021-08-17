lst = [5, 4, 3, 6]

my_list = list(map(lambda num: num ** 2, lst))

print(my_list)

a = [(0, 2), (10, -1), (-3, -3), (7, 19)]

a.sort(key=lambda num: num[1])

print(a)