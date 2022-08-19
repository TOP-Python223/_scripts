s = 'Python!'
print(f'{s = }')
print(f'{len(s) = }', end='\n\n')

# выводим отрицательные индексы
for i in range(-len(s), 0):
    print(i, end='\t')
print()
# выводим соответствующие символы
for i in range(len(s)):
    print(s[i], end='\t')
print()
# выводим положительные индексы
for i in range(len(s)):
    print(i, end='\t')
print()
