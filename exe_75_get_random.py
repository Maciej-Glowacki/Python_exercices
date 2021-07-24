from random import randint


def get_random(num = 3):
    """Draws 3 nums from 100 and sorts them

    :param int integer: number of numbers 

    :rtype: list
    :return: sorted list of numbers
    """
    if not isinstance(num, int):
        raise Exception('Invalid data!')
    lst = []
    while len(lst) < num:
        lst.append(randint(1, 100))
    return sorted(lst)


if __name__ == '__main__':
    print(get_random(2))
    print(get_random(6))
    print(get_random('a'))
