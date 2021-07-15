def format_date(day, month, year):
    if month > 12:
        return None
    if month == 1 and day > 31:
        return None
    elif day > 31 and month == 3:
        return None
    elif day > 31 and month == 5:
        return None
    elif day > 31 and month == 7:
        return None
    elif day > 31 and month == 8:
        return None
    elif day > 31 and month == 10:
        return None
    elif day > 31 and month == 12:
        return None
    elif day > 28 and month == 2:
        return None
    elif day > 30 and month == 4:
        return None
    elif day > 30 and month == 6:
        return None
    elif day > 30 and month == 9:
        return None
    elif day > 30 and month == 11:
        return None
    month_dict = {
        1: 'Styczeń', 2: 'Luty', 3: 'Marzec', 4: 'Kwiecień',
        5: 'Maj', 6: 'Czerwiec', 7: 'Lipiec', 8: 'Sierpień',
        9: 'Wrzesień', 10: 'Październik', 11: 'Listopad',
        12: 'Grudzień'
        }
    month = month_dict[month]
    return f'{day} {month} {year}'

print(format_date(28, 12, 2021))
