from pprint import pprint


class Person:
    arms_count: int = 2

    # переопределение встроенного метода конструктора
    def __init__(self, name: str, surname: str, age: int = 0) -> None:
        # создаём атрибуты экземпляра
        self.firstname = name
        self.surname = surname
        self.age = age


pers1 = Person('Георгий', 'Ковров', 30)
# Person(*args, **kwargs)
#     Person.__new__(Person) -> instance
#     Person.__init__(instance, *args, **kwargs) -> None
# -> instance

pers2 = Person('Анна', 'Миронова', 28)

print(f'\n{pers1.__dict__ = }')
print(f'{pers2.__dict__ = }\n')

pprint(Person.__dict__)
