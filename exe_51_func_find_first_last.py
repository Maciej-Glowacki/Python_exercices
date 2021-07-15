def find_first_and_last(lst_or_tpl):
    res = [lst_or_tpl[i] for i in (0, -1)]
    return tuple(res)

print(find_first_and_last([0, 1, 2, 3, 4, 5]))
print(find_first_and_last((0, 1, 2, 3, 4, 5, 6, 7)))
print(find_first_and_last(range(0, 22)))
