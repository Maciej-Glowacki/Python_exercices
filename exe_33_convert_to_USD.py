def convert_to_usd(zlotys, USD = 3.85):
    result = zlotys / USD
    return round(result, 2)


print("385 PLN = ", convert_to_usd(385), "USD")