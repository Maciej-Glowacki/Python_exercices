class Calculator:
    def __init__(self):
        self.operation = []

    def add(self, num1, num2):
        self.result = num1 + num2
        self.operation.append(f'added {num1} to {num2} got {self.result}')
        return self.result

    def multiply(self, num1, num2):
        self.result = num1 * num2
        self.operation.append(
            f'multiplied {num1} with {num2} got {self.result}')
        return self.result

    def print_operations(self):
        print('Current operations:')
        for operation in self.operation:
            print(operation)


myCalc = Calculator()

# myCalc.add(2, 3)
# myCalc.add(12, 3)
# myCalc.add(22, 3)
# myCalc.add(32, 3)
myCalc.multiply(23, 2)
myCalc.print_operations()
