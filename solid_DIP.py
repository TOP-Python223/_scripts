"""Dependency Inversion Principle — Принцип Инверсии Зависимостей

Модуль верхнего уровня.
"""

from solid_DIP_lowlevel import db


class Research:
    def __init__(self, database):
        self.db = database

    # нарушение DIP — код верхнего уровня не должен зависеть от деталей реализации кода нижнего уровня
    # def find_all_children(self, name: str):
    #     for parent, relation, child in self.db.storage:
    #         if parent.name == name:
    #             if relation is Relation.PARENT:
    #                 yield child
    #
    # def find_all_parents(self, name: str):
    #     for child, relation, parent in self.db.storage:
    #         if child.name == name:
    #             if relation is Relation.CHILD:
    #                 yield parent


r = Research(db)

print(*r.db.find_all_parents('Олеся'))
print(*r.db.find_all_children('Олег'))

