def name_sorter(list):
    """Separates polish male names from polish female names.
    
    :param str text: list of names
    :rtype: dict 
    :return: dict with names separated
    """
    result = {
        'male': [],
        'female': []
    }
    for name in list:
        if name[-1] == 'a':
            result['female'].append(name)
        else:
            result['male'].append(name)
    return result
    

if __name__ == '__main__':
    input_data = ["Andrzej", "Henryk", "Alicja", "Cezary", "Barbara", "Marcin", "Genowefa"]
    print(name_sorter(input_data))
