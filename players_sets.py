
saved1 = ('Григорий', 'Андрей')
saved2 = ('Григорий', 'Андрей', 'Ярослав')

players = ('Андрей', 'Григорий')

# сложносочинённое условие
if ((players[0] == saved1[0] or players[0] == saved1[1]) 
    and (players[1] == saved1[0] or players[1] == saved1[1])):
    print('найдено сохранение')
else:
    print('не найдено сохранение')

# необходимо изменение условия при изменении длины одного из кортежей
if ((players[0] == saved2[0] or players[0] == saved2[1]) 
    and (players[1] == saved2[0] or players[1] == saved2[1])):
    print('найдено сохранение')
else:
    print('не найдено сохранение')

print()

if set(players) == set(saved1):
    print('найдено сохранение')
else:
    print('не найдено сохранение')

if set(players) == set(saved2):
    print('найдено сохранение')
else:
    print('не найдено сохранение')

