"""Второй модуль многофайлового проекта."""
print(f'Начало выполнения: {__name__}\n')

from module1 import change_M1

import module1

M2 = 200

def change_M2():
    global M2
    M2 = 250


print(f'Завершение выполнения: {__name__}\n')
