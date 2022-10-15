from dataclasses import dataclass
from datetime import date

# динамически формирует метод-конструктор на основе заявленных атрибутов класса
@dataclass
class Person:
    surname: str
    name: str
    patronymic: str
    birthdate: date = None


# выше мы получаем объект класса, практически идентичный объекту класса, объявленному классическим способом
class Person_classic:
    def __init__(self,
                 surname: str,
                 name: str,
                 patronymic: str,
                 birthdate: date = None):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.birthdate = birthdate
