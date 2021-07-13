def create_list(element1, element2):
    i = 1
    lst = []
    while i <= 4:
        lst.append(element1)
        lst.append(element2)
        i += 1
    return lst

print(create_list('Me', 1))

