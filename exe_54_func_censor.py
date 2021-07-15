def censor(stri):
    wrong_words = ['Java', 'Ruby', 'PHP']
    lst = stri.split()
    lst2 = []
    for word in lst:
        if word in wrong_words:
            lst2.append('****')
        else:
            lst2.append(word)
        lst = ' '.join(lst2)
    return lst


print(censor('Java is the best, but PHP is the bestest!'))
