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


class AdvancedCalculator(Calculator):
    PI = 3.14159265

    def __init__(self):
        super().__init__()

    @staticmethod
    def computer_circle_field(r):
        return AdvancedCalculator.PI * r ** 2


myCalc = Calculator()
myCalc.add(6, 98)
myCalc.multiply(6, 98)
myCalc.print_operations()

print("Circle field:", AdvancedCalculator.computer_circle_field(4))