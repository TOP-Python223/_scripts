from math import pi


class Mixin:
    @classmethod
    def user_class_attributes(cls) -> str:
        return ', '.join(
            repr(attr)
            for attr in dir(cls)
            if not attr.startswith('__') and not attr.endswith('__')
        )


class Mixin2:
    def user_instance_attributes(self) -> str:
        return ', '.join(
            repr(attr)
            for attr in dir(self)
            if not attr.startswith('__') and not attr.endswith('__')
        )


class Shape(Mixin, Mixin2):
    pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    @property
    def length(self):
        return 2*pi*self.radius


class Square(Shape):
    def __init__(self, side):
        self.side = side

    @property
    def perimeter(self):
        return 4*self.side


class Menu(Mixin, Mixin2):
    pass

class FileMenu(Menu):
    pass

class NewFile(FileMenu):
    pass


print(Square.user_class_attributes())

cr1 = Circle(5)
print(cr1.user_instance_attributes())
