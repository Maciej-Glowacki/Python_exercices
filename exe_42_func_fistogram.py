def histogram(lista):
    for element in lista:
        if type(element) is not int:
            return None
    a = """"""
    for i in range(len(lista)):
        k = lista[i]
        while k > 0:
            a += '#'
            k -= 1
        a += '\n'
    return a


h = histogram([22, 6, 3, 7])
print(h)
e = histogram([12, 22, 'error'])
print(e)

# Napisz funkcję histogram, która przyjmie listę liczb, po czym zwróci histogram ze znaków #. Jeśli użytkownik poda wartość nie będącą liczbą, funkcja powinna zwrócić wartość None.

# Wynikowy histogram ma być wielolinijkowym napisem składającym się ze znaków #. Jedna linijka = jeden słupek histogramu.

# Zadanie rozwiąż, nie korzystając z mnożenia stringów! Zamiast tego użyj dwóch pętli.