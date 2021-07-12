def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

print(is_even(111))

def iterate_through(num):
    for i in range(1, num):
        if is_even(i):
            print(i, 'jest parzyste')
        else:
            print(i, 'jest nieparzyste')

print(iterate_through(11))
