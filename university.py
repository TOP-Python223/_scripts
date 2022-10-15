"""Заготовка для реализации модели классов university."""

from enum import Enum
from dataclasses import dataclass
from abc import ABC
from datetime import date
from decimal import Decimal


class Gender(Enum):
    MALE = 0
    FEMALE = 1


@dataclass
class Person(ABC):
    surname: str
    name: str
    patronymic: str
    gender: Gender
    birthdate: date

    def __str__(self):
        return f'{self.name} {self.patronymic} {self.surname}'


@dataclass
class Employee(Person):
    employment_date: date
    salary: Decimal
    position: str
    head: 'Administrator'

    def __str__(self):
        return super().__str__() + f': {self.position}'

