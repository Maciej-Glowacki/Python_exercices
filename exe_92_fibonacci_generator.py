class Fibonacci:
    def __init__(self, number):
        self.number = self.__validate_number(number)

    def __validate_number(self, new_number):
        if new_number < 0:
            raise ValueError("Wrong number")
        return new_number

    def __iter__(self):
        self.step_number = 0
        return self

    def __next__(self):
        if self.step_number >= self.number:
            raise StopIteration
        self.step_number += 1
        return self.fib()

    def fib(self):
        if self.step_number == 0:
            return 1
        if self.step_number == 1:
            return 1
        a = 0
        b = 1
        for i in range(1, self.step_number):
            a, b = b, a + b
        return b


def fib(n):
    for num in Fibonacci(n):
        yield num


print("Generator Fibonacci")
generated_fib = fib(13)
for num in generated_fib:
    print(num)