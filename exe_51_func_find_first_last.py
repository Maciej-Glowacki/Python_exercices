def find_first_and_last(lst_or_tpl):
    res = [lst_or_tpl[i] for i in (0, -1)]
    return tuple(res)

def find_first_and_last_v2(lst_or_tpl):
    return (lst_or_tpl[0],lst_or_tpl[-1])

print(find_first_and_last([0, 1, 2, 3, 4, 5]))
print(find_first_and_last((0, 1, 2, 3, 4, 5, 6, 7)))
print(find_first_and_last(range(0, 22)))

print(find_first_and_last_v2([0, 1, 2, 3, 4, 5]))
print(find_first_and_last_v2((0, 1, 2, 3, 4, 5, 6, 7)))
print(find_first_and_last_v2(range(0, 22)))
