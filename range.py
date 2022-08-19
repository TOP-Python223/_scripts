# 1 вариант: левая граница всегда 0, правая – задаётся аргументом
print('range(5)')
for i in range(5):
    print(i, end=' ')

print('\n\nrange(12)')
for i in range(12):
    print(i, end=' ')

# 2 вариант: левая граница задаётся первым аргументом, правая – задаётся вторым аргументом
print('\n\nrange(5, 15)')
for i in range(5, 15):
    print(i, end=' ')

print('\n\nrange(-10, 10)')
for i in range(-10, 10):
    print(i, end=' ')

# 3 вариант: левая граница задаётся первым аргументом, правая – задаётся вторым аргументом, шаг последовательности – третьим аргументом
print('\n\nrange(2, 40, 2)')
for i in range(2, 40, 2):
    print(i, end=' ')

print('\n\nrange(10, -11, -1)')
for i in range(10, -11, -1):
    print(i, end=' ')


