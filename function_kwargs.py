def g(x, y, a, b, c):
    return a*x**2*y + b*x*y**2 + c

# неудобный вариант
print(g(2, -3, 1, 1, 0))

# передача аргументов по ключу
print(g(a=1, x=2, b=1, y=-3, c=0), end='\n\n')

# приведёт к ошибке: позционные аргументы указаны после ключевых
# print(g(a=1, b=1, c=0, 2, -3))


# значения по умолчанию
def h(x, y, a=1, b=1, c=1, d=0):
    return a*x**2 + b*x*y + c*y**2 + d

# передаются только значения для x и y
print(h(2, 2))

# переданное значение для d перезаписывает значение по умолчанию
print(h(2, 2, d=10))

# аргументы для параметров со значениями по умолчанию 
#   можно передавать и по по позиции и по ключу
print(h(2, 2, 2, d=10), end='\n\n')


# можно передавать int, а можно float
def hf(x: float, 
       y: float, 
       a: float = 1, 
       b: float = 1, 
       c: float = 1, 
       d: float = 0) -> float:
    return a*x**2 + b*x*y + c*y**2 + d

# или смешано
print(hf(1, 4, a=0.5, b=1.5, d=2), end='\n\n')
