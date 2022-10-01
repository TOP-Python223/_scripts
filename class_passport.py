from datetime import datetime as dt


class Passport:
    def __init__(self,
                 number: str,
                 surname: str,
                 name: str,
                 patronym: str,
                 birthdate: str):
        self.number = number
        self.surname = surname.title()
        self.name = name.title()
        self.patronym = patronym.title()
        self.birthdate = dt.strptime(birthdate, '%d.%m.%Y')

    @property
    def number(self):
        return

    @number.setter
    def number(self, value: str):
        self.__number = value


class Person:
    def get_passport(self, passport: Passport):
        self.passport = passport


class Police:
    def ask_document(self, person: Person):
        return person.passport._Passport__number



p1 = Passport('1212435362', 'Кирдык', 'Тимофей', 'Вахтангович', '19.11.1977')
p1.number = '7475291348'
print(p1.number)

tim = Person()
tim.get_passport(p1)

sergent = Police()
print(sergent.ask_document(tim))
