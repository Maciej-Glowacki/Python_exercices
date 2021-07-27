class Lightsaber:
    def __init__(self, color):
        self._color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, new_color):
        if new_color not in ['red', 'blue', 'green', 'purple']:
            raise ValueError("Bad lightsaber color")
        self._color = new_color

    @property
    def force(self):
        if self.color == 'red':
            return 'dark'
        return 'light'

    def __str__(self):
        return f"Lightsaber: {self.color}. \nForce: {self.force}"


l = Lightsaber('red')
l2 = Lightsaber('blue')
print(l)
l2.color = 'pink'
print(l2)
