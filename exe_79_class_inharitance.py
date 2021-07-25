# Zajrzyj do pliku exercise_1.py, znajdziesz tam klasę Dinosaur, która ma zaimplementowane następujące elementy:

# metodę walk(),
# metodę make_sound().
# Napisz klasę Bird, która będzie dziedziczyła po klasie Dinosaur. Klasa Bird ma:

# dostać nową metodę fly(), która będzie zwracała napis "Latam!",
# nadpisać metodę make_sound(), która ma zwracać napis "Ćwir ćwir!".
# Przetestuj nową klasę.

class Dinosaur:
    
    def walk(self):
        return "Chodzę!"

    def make_sound(self):
        return "Roar!"

class Bird(Dinosaur):
    def __init__(self):
        super().__init__()
    
    def fly(self):
        return "I'm flying"
    
    def make_sound(self):
        return "Fru Fru"

if __name__ == "__main__":
    d = Dinosaur()
    print("Dinosaur walks:")
    print(d.walk(), "\n") 

    print("Dinosaur makes a sound:")
    print(d.make_sound())

    f = Bird()
    print("Bird flies!")
    print(f.fly(), "\n")

    print("Bird makes a sound:")
    print(f.make_sound())