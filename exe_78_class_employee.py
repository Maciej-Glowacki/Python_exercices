class Employee:
    
    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self._salary = 0.0

    def set_salary(self, salary):
        if not isinstance(salary, float) and salary <= 0.0:
            raise ValueError("Payment must be greater than 0")

        self._salary = salary

    def __str__(self):
        return f'Employee {self.first_name} {self.last_name} earns {self._salary} złotych'


e = Employee(1, 'Maciek', 'Głowacki')

e.set_salary(15000)
print(e)
