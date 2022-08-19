from itertools import zip_longest as zipl

ir1, ir2 = range(6), range(11)
# встроенная функция zip с ограничением итерации по длине самого короткого аргумента
for pair in zip(ir1, ir2, range(100, 1, -10)):
    print(pair)
print()

# функция zip_longest из itertools с ограничением итерации по длине самого длинного аргумента
for pair in zipl(ir1, ir2, fillvalue=None):
    print(pair)
