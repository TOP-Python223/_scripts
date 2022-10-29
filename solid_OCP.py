"""Opened/Closed Principle — Принцип Открытости/Закрытости"""
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Iterable, Generator


@dataclass
class Product:
    """Хранение информации о продукте."""
    name: str
    color: str
    size: str

    def __post_init__(self):
        self.color = self.color.upper()
        self.size = self.size.upper()

    def __str__(self):
        return f'{self.name.title()}' \
               f' {self.color.title()}' \
               f' {self.size.title()}'


# нарушение OCP
# потребуется модификация класса при увеличении количества критериев
# взрывной рост количества методов при увеличении количества критериев
class ProductFilter:
    """Фильтрация по различным критериям, прописанным в коде класса."""
    def __init__(self, products: Iterable[Product]):
        self.products = products

    def filter_by_color(self, color: str) -> Generator:
        for product in self.products:
            if product.color == color.upper():
                yield product

    def filter_by_size(self, size: str) -> Generator:
        for product in self.products:
            if product.size == size.upper():
                yield product

    def filter_by_color_and_size(self, color: str, size: str) -> Generator:
        for product in self.products:
            if product.color == color.upper() and product.size == size.upper():
                yield product

    # 2 criteria — 3 combines
    # (s, c): s c sc

    # 3 criteria — 7 combines
    # (s, c, w): s c w sc sw cw scw

    # 4 criteria — 15 combines
    # (s, c, w, b): s c w b sc sw sb cw cb wb scw scb swb cwb scwb


class Specification(ABC):
    """Абстрактный базовый класс для реализации различных критериев."""
    @abstractmethod
    def is_satisfied(self, item: Product) -> bool:
        """Абстрактный метод для проверки соответствия параметров передаваемого объекта текущей спецификации."""


class Color(Specification):
    """Реализация критерия цвета."""
    def __init__(self, color: str):
        self.color = color.upper()

    def is_satisfied(self, item: Product) -> bool:
        return self.color == item.color


class Size(Specification):
    """Реализация критерия размера."""
    def __init__(self, size: str):
        self.size = size.upper()

    def is_satisfied(self, item: Product) -> bool:
        return self.size == item.size


class AndSpec(Specification):
    """Реализация комбинации критериев с помощью логического 'И'."""
    def __init__(self, *specs: Specification):
        self.specs = specs

    def is_satisfied(self, item: Product) -> bool:
        return all(map(
            lambda spec: spec.is_satisfied(item),
            self.specs
        ))


class OrSpec(Specification):
    """Реализация комбинации критериев с помощью логического 'ИЛИ'."""
    def __init__(self, *specs: Specification):
        self.specs = specs

    def is_satisfied(self, item: Product) -> bool:
        return any(map(
            lambda spec: spec.is_satisfied(item),
            self.specs
        ))


class Filter:
    """Реализация фильтра с хранением фильтруемых объектов в экземпляре фильтра."""
    def __init__(self, product_list: Iterable):
        self.products = product_list

    def filter(self, criteria: Specification):
        for product in self.products:
            if criteria.is_satisfied(product):
                yield product


goods = [
    Product('Apple', 'Green', 'Small'),
    Product('Tree', 'Green', 'Large'),
    Product('House', 'Blue', 'Large'),
]

green = Color('green')
blue = Color('blue')
small = Size('small')
large = Size('large')
green_and_large = AndSpec(green, large)
blue_or_small = OrSpec(blue, small)

catalog = Filter(goods)

print('All green products', *catalog.filter(green), sep='\n\t', end='\n\n')

print('All large products', *catalog.filter(large), sep='\n\t', end='\n\n')

print('All blue or small products',
      *catalog.filter(blue_or_small),
      sep='\n\t', end='\n\n')

print('All green and large products',
      *catalog.filter(green_and_large),
      sep='\n\t', end='\n\n')
