def highest_even(lst):
    lst2 = []
    for item in lst:
        if item % 2 == 0:
            lst2.append(item)
    return max(lst2)


print(highest_even([1, 2, 3, 4, 5, 10, 99, 101]))