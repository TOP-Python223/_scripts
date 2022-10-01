from math import pi, sqrt


class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    @property
    def area(self) -> float:
        return pi * self.radius**2

    @area.setter
    def area(self, new_area: float):
        self.radius = sqrt(new_area / pi)


cr1 = Circle(5)
print(cr1.area)

cr1.area = 157
print(cr1.radius)
print(cr1.area)
print('\n')


class Square:
    def __init__(self, side: float):
        self._side = side
        self._perimeter = 4*side
        self._area = side**2

    @property
    def side(self) -> float:
        return self._side

    @side.setter
    def side(self, new_side: float):
        self._side = new_side
        self._perimeter = 4*new_side
        self._area = new_side**2

    @property
    def perimeter(self) -> float:
        return self._perimeter

    @perimeter.setter
    def perimeter(self, new_perimeter: float):
        self._side = new_perimeter / 4
        self._perimeter = new_perimeter
        self._area = self._side**2

    @property
    def area(self) -> float:
        return self._area

    @area.setter
    def area(self, new_area: float):
        self._side = sqrt(new_area)
        self._perimeter = 4*self._side
        self._area = new_area

    def __str__(self):
        return f'S={self.side:.2f} P={self.perimeter:.2f} A={self.area:.2f}'


sq1 = Square(6)
print(sq1)

sq1.area = 30
print(sq1)

sq1.perimeter = 100
print(sq1)
