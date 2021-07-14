def list_keys(dct):
    for key in dct:
        print(key)


list_keys(
    {
    'Book': 'Lord of the Rings',
    'Author': 'J.R.R. Tolkien',
    'Pages': 1000
    }
)

def list_keys_short(dct):
    return [key for key in dct]

print(list_keys_short(
    {
    'Book': 'Lord of the Rings',
    'Author': 'J.R.R. Tolkien',
    'Pages': 1000
    }
    )
)
