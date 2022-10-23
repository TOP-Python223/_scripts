from datetime import datetime as dt


class Employee:
    def __init__(self, name: str, employment_date: str):
        self.name = name
        # используется сеттер
        self.employment_date = employment_date

    @property
    def employment_date(self) -> str:
        """Возвращает значение частного/защищённого одноимённого поля — геттер."""
        return self._employment_date.strftime('%d.%m.%Y')

    @employment_date.setter
    def employment_date(self, value: str):
        """Устанавливает значение частного/защищённого одноимённого поля — сеттер."""
        self._employment_date = dt.strptime(value, '%d.%m.%Y').date()

    @property
    def years_of_experience(self) -> int:
        """Возвращает количество полных лет стажа сотрудника."""
        return (dt.now().date() - self._employment_date).days // 365


potap = Employee('Потап', '15.09.2016')
print(potap.__dict__)
print(potap.employment_date)

potap.employment_date = '11.12.2016'
print(potap.employment_date)

print(potap.years_of_experience)
