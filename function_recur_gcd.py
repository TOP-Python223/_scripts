# (gcd) greatest common divider — наибольшой общий делитель (нод)

# 12, 6 -> 6, 0 -> 6
# 15, 12 -> 12, 3 -> 3, 0 -> 3

def gcd(number1: int, number2: int) -> int:
    """Рекурсивная функция вычисления наибольшего общего делителя двух чисел"""
    print(f"вызов power с аргументами {number1} и {number2}")
    if number2 != 0:
        res = gcd(number2, number1 % number2)
        print(f"возврат {res}")
        return res
    else:
        print(f"возврат {number1}")
        return number1


print('='*40)
print('  НАИБОЛЬШИЙ ОБЩИЙ ДЕЛИТЕЛЬ  ')
print('='*40)

while True:
    n = input('\n число 1 > ')
    if not n:
        break
    n = int(n)
    k = int(input(' число 2 > '))
    # n, k = max(n, k), min(n, k)
    if n < k:
        n, k = k, n
    print(f"\t\tНОД({n}, {k}) = {gcd(n, k)}")
