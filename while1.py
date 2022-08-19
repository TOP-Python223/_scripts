# условие продолжения цикла
#   n > 0
# условие выхода из цикла
#   not n > 0
#   n <= 0


# 1 вариант: устаревший
n = int(input('number: '))
while n > 0:
    print(n % 10)
    n = int(input('number: '))
print('end of cycle\n')


# 2 вариант: для Python 3.8+
while (n := int(input('number: '))) > 0:
    print(n % 10)


# 3 вариант: условие выхода
while True:
    n = int(input('number: '))
    if n <= 0:
        break
    print(n % 10)
