def div(num1, num2):
    '''Checks nums in a list which can be divided by 2 but not by 3

    :param str text: 2 numbers
    :rtype: list
    :return: List of numbers
    '''
    lst = []
    for num in range(num1, num2+1):
        lst.append(num)
    result = []
    for num in lst:
        if num % 2 == 0 and num % 3 != 0:
            result.append(num)
    return result


if __name__ == '__main__':
    print(div(1, 8))
    print(div(1, 100))
