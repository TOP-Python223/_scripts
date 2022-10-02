from math import sqrt
from numbers import Real


class Point:
    """Точка на плоскости в декартовой системе координат."""
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'<Point: x={self.x} y={self.y}>'

    def __str__(self):
        return f'({self.x}; {self.y})'

    # point1 - point2
    def __sub__(point1, point2: 'Point') -> float:
        """Вычисляет и возвращает длину отрезка, заданного двумя точками."""
        if type(point2) is point1.__class__:
            x1, x2 = point1.x, point2.x
            y1, y2 = point1.y, point2.y
            return sqrt((x1 - x2)**2 + (y1 - y2)**2)
        else:
            raise TypeError

    # self < other
    def __lt__(self, other) -> bool:
        if isinstance(other, self.__class__):
            return self.x < other.x and self.y < other.y
        elif isinstance(other, int):
            return self.x < other and self.y < other
        else:
            raise TypeError

    # self > other
    def __gt__(self, other) -> bool:
        if isinstance(other, self.__class__):
            return self.x > other.x and self.y > other.y
        elif isinstance(other, int):
            return self.x > other and self.y > other
        else:
            raise TypeError

    # self == other
    def __eq__(self, other) -> bool:
        if isinstance(other, self.__class__):
            return self.x == other.x and self.y == other.y
        elif isinstance(other, int):
            return self.x == other and self.y == other
        else:
            raise TypeError



p1 = Point(0, 0)
p2 = Point(1, 1)
print(p2 - p1, end='\n\n')

p3 = Point(2, 3)
p4 = Point(1, 4)
print(f'{p1 < p2 = }')
print(f'{p3 > p4 = }')
# то же самое, что и: not p1.__eq__(p4)
print(f'{p1 != p4 = }')
# не определено
# print(f'{p2 <= p4 = }')
