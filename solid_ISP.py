"""Interface Segregation Principle — Принцип Разделения Интерфейсов"""

from abc import ABC


# нарушение ISP — от этого интерфейса могут наследоваться классы, использующие не все методы интерфейса
class MultiFunctionDevice(ABC):
    """Интерфейс МФУ"""
    def print(self, document):
        pass

    def scan(self, document):
        pass

    def fax(self, document, number):
        pass


# пока всё в порядке
class HP_MFP_M141(MultiFunctionDevice):
    """Конкретное МФУ"""


# обычному принтеру не нужны методы сканирования и отправки факсов
class BrotherHL5250_DN(MultiFunctionDevice):
    """Старый принтер"""
    # не лучший вариант решения проблемы
    def scan(self, document):
        """Не поддерживается данным устройством!"""
        raise NotImplementedError

    def fax(self, document, number):
        """Не поддерживается данным устройством!"""
        raise NotImplementedError


mf_device = HP_MFP_M141()
print([attr for attr in dir(mf_device) if not attr.startswith('__')])

old_printer = BrotherHL5250_DN()
print([attr for attr in dir(old_printer) if not attr.startswith('__')])



# разделение интерфейсов
class IPrinter(ABC):
    """Интерфейс для принтеров."""
    def print(self, document):
        pass

class IScan(ABC):
    """Интерфейс для сканеров."""
    def scan(self, document):
        pass

class IFax(ABC):
    """Интерфейс для факсов."""
    def fax(self, number, document):
        pass


# разделённые интерфейсы используются по необходимости
class Xerox_T35_N(IPrinter, IScan):
    """Реализация ксерокса."""

class Panasonic_PH123(IFax):
    """Реализация факса."""


copy_machine = Xerox_T35_N()
print([attr for attr in dir(copy_machine) if not attr.startswith('__')])

phone_fax = Panasonic_PH123()
print([attr for attr in dir(phone_fax) if not attr.startswith('__')])
