class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age

fluffy = Cat("Fluffy", 3)
kuku = Cat("Kuku", 5)
craken = Cat("Craken", 1)

def get_oldest_cat(*args):
    return max(args)

print(f"The oldest cat is {get_oldest_cat(fluffy.age, kuku.age, craken.age)} years old.")