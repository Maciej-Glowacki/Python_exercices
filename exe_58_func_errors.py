def div(a = 0, b = 0):
    try:
        a = int(input("Write first number: "))
        b = int(input("Write second number: "))
    except ValueError as val:
        print("Values you've wrote are not numbers!", val)
        return None
    try:
        result = a / b
        print(round(result, 2))
        return result
    except ZeroDivisionError as zeroerr:
        print("Division by 0!", zeroerr)

div()
