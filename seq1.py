s = 'Python is cool!'
print(s, type(s), sep='\n', end='\n\n')

# строки могут быть преобразованы в списки или кортежи
print(f'{list(s) = }')
print(f'{tuple(s) = }', end='\n\n')

l = [1, 'abc', 2.2, (10,)]
print(l, type(l), sep='\n', end='\n\n')

# списки могут быть преобразованы в кортежи, и наоборот
print(f'{tuple(l) = }')
# списки и кортежи могут быть представлены в строковом виде с сохранением всех синтаксических символов
print(f'{str(l) = }')
