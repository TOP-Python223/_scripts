text = "12-ый граф д'Эгильон потратил 12 экю в Париже. Ужасный скряга!"
word = 'Word'
word2 = 'lower'

print(f'{text.islower() = }')
print(f'{text.istitle() = }')
print(f'{word.istitle() = }')
print(f'{text.isupper() = }', end='\n\n')

print(f'{text.lower()}', end='\n\n')
print(f'{text.capitalize()}', end='\n\n')
print(f'{text.title()}', end='\n\n')
print(f'{text.upper()}', end='\n\n')

if text == text.lower():
    print(' > символов в верхнем регистре нет')
else:
    print(' > символы в верхнем регистре есть')

if word2 == word2.lower():
    print(' > символов в верхнем регистре нет')
else:
    print(' > символы в верхнем регистре есть')
