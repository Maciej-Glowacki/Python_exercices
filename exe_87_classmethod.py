import datetime


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def create_person(cls, name, year_of_birth):
        actual_year = datetime.datetime.now().year
        age = actual_year - year_of_birth
        return cls(name, age)

    def __str__(self):
        return f'{self.name} is {self.age} years old.'


John = Person.create_person('Jan', 1987)
Cindy = Person.create_person('Cindy', 1977)
print(John)
print(Cindy)

