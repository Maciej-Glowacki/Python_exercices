def check_character(string, letter):
    """Checks the number of the same letters
    
    :param str string: string to be checked
    :param string letter: letter we are looking for

    :rtype: int
    :return: number of same letters
    """
    str = string.lower()
    ltr = letter
    lst = []
    for i in str:
        if i == ltr:
            lst.append(i)
    return lst.count(letter)

if __name__ == '__main__':
    print(check_character('Order of the Phoenix', 'o'))
    print(check_character('Look for me son!', 'o'))

