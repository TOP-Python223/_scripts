from numbers import Real


class NamedNumber:
    def __init__(self, name: str, number: Real):
        self.name = name
        self.number = number

    def __add__(self, other):
        if isinstance(other, Real):
            return NamedNumber('', self.number + other)
        elif isinstance(other, NamedNumber):
            return NamedNumber('', self.number + other.number)
        else:
            raise TypeError

    def __sub__(self, other):
        if isinstance(other, Real):
            return NamedNumber('', self.number - other)
        elif isinstance(other, NamedNumber):
            return NamedNumber('', self.number - other.number)
        else:
            raise TypeError

    def __radd__(self, other):
        if isinstance(other, Real):
            return NamedNumber('', self.number + other)
        elif isinstance(other, NamedNumber):
            return NamedNumber('', self.number + other.number)
        else:
            raise TypeError

    def __rsub__(self, other):
        if isinstance(other, Real):
            return NamedNumber('', self.number - other)
        elif isinstance(other, NamedNumber):
            return NamedNumber('', self.number - other.number)
        else:
            raise TypeError

    def __str__(self):
        return f'<{self.name} {self.number}>'


nn1 = NamedNumber('один', 1)
nn2 = NamedNumber('два', 2)

print(nn1 + nn2)
print(nn1 + 5)
print(nn1 - 5.8)

print(3.5 + nn2)
print(15 - nn2)

print('abc' + nn2)
