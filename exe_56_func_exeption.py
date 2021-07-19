def safe_get(lst, index):
    try:
        print(lst[index])
    except IndexError:
        print('Index you wrote is out of list range')

print(safe_get([1, 2, 3], 0))
print(safe_get([1, 2, 3], 7))
