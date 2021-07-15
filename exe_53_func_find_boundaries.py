def find_boundaries(lst):
    if lst == []:
        return None
    for element in lst:
        if type(element) is str:
            lst.remove(element)
    tpl = (min(lst), max(lst))
    return tpl

print(find_boundaries([1, 3, 111]))
print(find_boundaries([]))
print(find_boundaries([1, 3, 'tata', 111]))


# Napisz funkcję find_boundaries, która przyjmie listę liczb. Funkcja powinna zwrócić krotkę z najmniejszą i największą liczbą w zestawie. Jeśli na liście będzie element, nie będący liczbą, powinien zostać zignorowany. W przypadku wprowadzenia pustej listy, funkcja powinna zwrócić None.