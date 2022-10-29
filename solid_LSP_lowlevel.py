"""Liskov Substitution Principle — Принцип Подстановки Лисков

Модуль низкого уровня.
"""

class Rectangle:
    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height

    @property
    def area(self):
        return self._width*self._height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value: int):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value: int):
        self._height = value


class Square(Rectangle):
    def __init__(self, side: int):
        super().__init__(side, side)

    # нарушение LSP — переопределение сеттеров необратимо изменяет поведение прямоугольника
    @Rectangle.width.setter
    def width(self, value: int):
        self._width = value
        self._height = value

    @Rectangle.height.setter
    def height(self, value: int):
        self._width = value
        self._height = value
