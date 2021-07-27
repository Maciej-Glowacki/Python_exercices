class LightSaber:
    def __init__(self, color):
        self._color = color

    @property
    def force(self):
        if self._color == 'red':
            return 'dark'
        return 'light'

    def __str__(self):
        return f"Lightsaber: {self._color}. \nForce: {self.force}"


l = LightSaber('red')
l2 = LightSaber('blue')

print(l)
print(l2)
