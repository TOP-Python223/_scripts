from abc import ABC, abstractmethod


class VectorGraphic(ABC):
    """Абстрактный базовый класс для объектов векторной графики."""
    @abstractmethod
    def render(self):
        """Выводит название типа объекта в stdout."""


class Line(VectorGraphic):
    """Описывает векторный объект отрезка."""
    def render(self):
        print('отрезок')


class Text(VectorGraphic):
    """Описывает векторный объект текста."""
    def render(self):
        print(self.__class__.__name__)


class Polygon(VectorGraphic):
    """Описывает векторный объект многоугольника."""
    def render(self):
        print('многоугольник')


# q = VectorGraphic()

l1 = Line()
l1.render()

t1 = Text()
t1.render()
