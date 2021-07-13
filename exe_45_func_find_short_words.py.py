def find_short_words(lst):
    list_words = []
    for element in lst:
        if len(element) < 5: 
            list_words.append(element)
    return list_words

print(find_short_words(['Litwo', 'ojczyzno', 'moja', 'ty', 'jesteś', 'jak', 'zdrowie']))

def find_short_words_v2(words, max_len=5):
    return [word for word in words if len(word) < max_len]

print(find_short_words(['Litwo', 'ojczyzno', 'moja', 'ty', 'jesteś', 'jak', 'zdrowie']))
