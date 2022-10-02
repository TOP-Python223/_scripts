from math import sqrt


class Point:
    """Точка на плоскости в декартовой системе координат."""
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'<Point: x={self.x} y={self.y}>'

    def __str__(self):
        return f'({self.x}; {self.y})'

    def __sub__(point1, point2: 'Point') -> float:
        """Вычисляет и возвращает длину отрезка, заданного двумя точками."""
        if type(point2) is point1.__class__:
            x1, x2 = point1.x, point2.x
            y1, y2 = point1.y, point2.y
            return sqrt((x1 - x2)**2 + (y1 - y2)**2)
        else:
            raise TypeError


p1 = Point(0, 0)
p2 = Point(1, 1)
print(p2 - p1)
