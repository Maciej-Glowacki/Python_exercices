from exe_78_class_employee import Employee

class HourlyEmploee(Employee):      
    def compute_payment(self, hours):
        self.hours = hours
        return f'Employee {self.first_name} {self.last_name} earns {self._salary * self.hours} złotych for {self.hours} already worked hours'


c = HourlyEmploee(2, 'John', 'Doe')
c.set_salary(50)
print(c.compute_payment(12))