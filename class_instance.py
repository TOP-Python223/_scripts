from pprint import pprint


class Person:
    arms_count: int = 2

    firstname: str
    surname: str
    age: int = 0

    def fullname():
        return f'{Person.firstname} {Person.surname}'


# объект класса
print(f'\n{Person = }\n{type(Person) = }')

# объект экземпляра
pers1 = Person()
print(f'\n{pers1 = }\n{type(pers1) = }')

# тип объекта экземпляра — это объект класса
print(f'\n{type(pers1) is Person = }')


# атрибуты класса
Person.firstname = 'Иван'
Person.surname = 'Скорняков'

print(f'\n\n{Person.firstname = }\n{Person.surname = }')
print(f'\n{Person.fullname() = }')
print(f'\n{Person.fullname = }\n{type(Person.fullname) = }\n')

# создание атрибута для конкретного объект экземпляра pers1
pers1.country = 'Россия'
pers1.__dict__['height'] = 181

# внутреннее пространство имён объекта экземпляра
pprint(pers1.__dict__)
print()

# внутреннее пространство имён объекта класса
pprint(Person.__dict__)
print()

# область видимости объекта экземпляра
pprint(dir(pers1))
print()


print(f'{pers1.firstname = }\n{pers1.surname = }')

pers2 = Person()

print(f'{pers2.firstname = }\n{pers2.surname = }')

print(f'\n{Person.firstname is pers1.firstname is pers2.firstname = }\n')

pprint(pers2.__dict__)
print()
