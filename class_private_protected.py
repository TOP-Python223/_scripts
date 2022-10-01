from datetime import datetime as dt


class Organization:
    __budgets: dict = {}

    def __init__(self, name: str, inn: str):
        self.name = name
        if self._check_inn(inn):
            self._inn = inn
        self.__budget: int = 0

    @staticmethod
    def _check_inn(inn: str) -> bool:
        return inn.isdecimal()

    def __str__(self):
        return f'<{self.name}>'

    def set_budget(self, amount: int):
        cur_year = dt.now().year
        if cur_year not in self.__class__.__budgets:
            self.__budget += amount
            self.__class__.__budgets[cur_year] = self.__budget

    def get_budget(self):
        return self.__budget


zao = Organization('Геоптикс, ЗАО', '123456789')
print(zao.name)

zao._inn = '987654321'
print(zao._inn, end='\n\n')

print(zao.__dict__)

try:
    print(zao.__budget)
except AttributeError:
    print(zao._Organization__budget)

zao.__budget = 10000
print(f'{zao.get_budget() = }')
print(f'{zao.__budget = }\n')

zao.set_budget(213000)

print(zao.__dict__)

zao.set_budget(100000)
