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
