"""Dependency Inversion Principle — Принцип Инверсии Зависимостей

Модуль низкого уровня.
"""

from dataclasses import dataclass
from enum import Enum


class Relation(Enum):
    PARENT = 0
    CHILD = 1


@dataclass
class Person:
    name: str

    def __repr__(self):
        return self.name


class Relationships:
    def __init__(self):
        # хранилище
        self.storage: list[tuple[Person, Relation, Person]] = []

    def add_relation(self, parent: Person, child: Person):
        # конкретная реализация структурирования данных в хранилище
        self.storage += [
            (parent, Relation.PARENT, child),
            (child, Relation.CHILD, parent)
        ]


# инверсия зависимости кода верхнего уровня от кода низкого уровня
class RelationshipsBrowser(Relationships):
    """Интерфейс."""
    def find_all_children(self, name: str):
        """Метод используется кодом верхнего уровня."""
        for parent, relation, child in self.storage:
            if parent.name == name:
                if relation is Relation.PARENT:
                    yield child

    def find_all_parents(self, name: str):
        """Метод используется кодом верхнего уровня."""
        for child, relation, parent in self.storage:
            if child.name == name:
                if relation is Relation.CHILD:
                    yield parent



oleg = Person('Олег')
olesya = Person('Олеся')
yulia = Person('Юлия')
nikita = Person('Никита')
stas = Person('Станислав')
sergey = Person('Сергей')

db = RelationshipsBrowser()
db.add_relation(oleg, olesya)
db.add_relation(oleg, nikita)
db.add_relation(yulia, olesya)
db.add_relation(yulia, nikita)
db.add_relation(stas, sergey)
