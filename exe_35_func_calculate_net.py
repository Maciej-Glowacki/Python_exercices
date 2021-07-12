def calculate_net(gross, vat = 0.23):
    net_price = gross / (1 + vat)
    return round(net_price, 2)

print(calculate_net(100))