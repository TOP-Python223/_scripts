# экранированные последовательности (escaped characters)
'\n'    # Newline – новая строка
'\t'    # Tabulation – горизонтальная табуляция
'\r'    # carriage Retrun – возврат каретки
'\v'    # Vertical tab – вертикальная табуляция
'\f'    # line Feed – подача (разрыв) страницы

# a = f'string containing value {input()} got from input'
# print(a, end='\n\n')

n, m = int(input()), int(input())
# print(f'n = {n}, m = {m}, sum = {n + m}')
print(f'{n = }, {m = }, {n + m = }', end='\n\n')

print(f'{n / m:.4f}', end='\n\n')

from math import pi

for i in range(10):
    pi_f = f'{pi:.{i}f}'
    print(f'{pi_f:>12s}')
