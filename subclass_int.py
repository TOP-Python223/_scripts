class NamedInt(int):
    __names = {
        0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'
    }

    def __init__(self, value: int):
        self.name = self.__class__.__names[value]

    def __add__(self, other):
        return NamedInt(super().__add__(other))

    def __sub__(self, other):
        return NamedInt(super().__sub__(other))

    def __mul__(self, other):
        return NamedInt(super().__mul__(other))

    def __str__(self):
        return f'{self.name}'


num1 = NamedInt(5)
num2 = NamedInt(7)

print(num1, num2)

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)

