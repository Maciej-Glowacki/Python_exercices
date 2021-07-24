def shorten(text):
    """Make text shortened.
    
    :param str text: some text
    :rtype: str 
    :return: shortened text
    """
    text_split = text.split()
    result = []
    for word in text_split:
        result.append(word[0])
    short = ''.join(result).upper()
    return short

def shorten2(text):
    """Make text shortened.
    
    :param str text: some text
    :rtype: str 
    :return: shortened text
    """
    return ''.join(word[0] for word in text.split()).upper()


if __name__ == '__main__':
    shortened = shorten("Don't repeat yourself")
    print(shortened)

    shortened = shorten("Rage Against The Machine")
    print(shortened)

    shortened = shorten2("Don't repeat yourself")
    print(shortened)

    shortened = shorten("Rage Against The Machine")
    print(shortened)
