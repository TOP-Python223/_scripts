class Rectangle:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height


class Square_Over(Rectangle):
    def __init__(self, side: int):
        self.side = side


class Square_Super(Rectangle):
    def __init__(self, side: int):
        super().__init__(side, side)


sq1 = Square_Over(5)
print(sq1.__dict__)

sq2 = Square_Super(5)
print(sq2.__dict__)


