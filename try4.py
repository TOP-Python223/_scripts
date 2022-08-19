# LBYL (LBL) — Look Before You Leap — Смотри Куда Прёшь
a, b = input('num 1: '), input('num 2: ')
if a.isdigit() and b.isdigit():
    a, b = int(a), int(b)

# EAFP (AFP) — Easier Ask Forgivness than Permission — Проси Прощения, а не Разрешения
try:
    a, b = int(input('num 1: ')), int(input('num 2: '))
except:
    pass
