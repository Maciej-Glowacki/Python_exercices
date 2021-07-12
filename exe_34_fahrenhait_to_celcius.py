def to_celcius(fahrenheit):
    celcius = ((fahrenheit - 32) * 5) / 9
    return round(celcius, 1)

print(to_celcius(100))
