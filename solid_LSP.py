"""Liskov Substitution Principle — Принцип Подстановки Лисков

Модуль верхнего уровня.
"""

from solid_LSP_lowlevel import *

def high_level_function(shape: Rectangle):
    w = shape.width
    shape.height = 10
    area_expected = w*10
    print(f'Ожидаемая площадь: {area_expected}\n'
          f'Вычисленная свойством: {shape.area}')


rc1 = Rectangle(4, 7)
high_level_function(rc1)

print()

sq1 = Square(5)
# LSP нарушен — объект Square ведёт себя иначе, чем объект Rectangle
high_level_function(sq1)

print()

sq2 = Rectangle(6, 6)
high_level_function(sq2)
