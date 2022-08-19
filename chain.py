from itertools import chain
from string import ascii_letters as al, digits, punctuation

s = 'ABCDEF'
l = range(1, 7)
t = (0.01, 0.02, -0.03, -0.01, 0.01, 0.03)

# итерирование по элементам нескольких контейнеров, передаваемых в качестве аргументов
for elem in chain(s, l, t):
    print(elem, end=' ')
print('\n')


c = [t, s, l]
for elem in chain(c):
    print(elem, end=' ')
print('\n')

# итерирование по элементам вложенных контейнеров одного переданного контейнера
for elem in chain.from_iterable(c):
    print(elem, end=' ')
print('\n')


for char in chain(al, digits, punctuation):
    print(char, end='')
print('\n')
