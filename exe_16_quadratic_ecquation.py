print('a*x**2 + b*x + c == 0')

num1 = int(input('Write your first number - a: '))
num2 = int(input('Write your second number - b: '))
num3 = int(input('Write your third number - c: '))

delta = num2**num2 - 4 * num1 * num3
print(f'Delta = {delta}')

square_root = delta * .5

if delta > 0:
    x_1 = (-num2 - square_root) / (2 * num1)
    x_2 = (-num2 + square_root) / (2 * num1)
    print(f'Roots of the quadratic equation are: \nx_1 = {x_1} \nx_2 = {x_2}')
elif delta == 0:
    x_0 = -num2 / (2 * num1)
    print(f'Roots of the quadratic equation are: \nx_1 = x_2 = {x_0}')
else:
    print('Delta is negative')

# wyświetlić na ekranie komunikat: Równanie w postaci a*x**2 + b*x + c == 0,
# wyświetlić na ekranie komunikat: Podaj a,
# pobrać wartość od użytkownika i zapisać ją do zmiennej a (pamiętaj o rzutowaniu na odpowiedni typ),
# wyświetlić na ekranie komunikat: Podaj b,
# pobrać wartość od użytkownika i zapisać ją do zmiennej b (pamiętaj o rzutowaniu na odpowiedni typ),
# wyświetlić na ekranie komunikat: Podaj c,
# pobrać wartość od użytkownika i zapisać ją do zmiennej c (pamiętaj o rzutowaniu na odpowiedni typ),
# policzy deltę,
# jeśli delta > 0, policzyć wartości x_1 i x_2, a następnie wyświetlić je w postaci: