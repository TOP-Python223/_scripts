# 2**5 -> 2**4 * 2 -> 2**3 * 2 * 2 -> 2**2 * 2 * 2 * 2 -> 2 * 2 * 2 * 2 * 2

def power(base: float, exp: int) -> float:
    """Рекурсивная функция вычисления степени числа"""
    print(f"вызов power с аргументами {base} и {exp}")
    if exp > 1:
        res = base * power(base, exp-1)
        print(f"возврат {res}")
        return res
    else:
        print(f"возврат {base}")
        return base


print('='*40)
print('  РЕКУРСИВНОЕ ВЫЧИСЛЕНИЕ СТЕПЕНИ ЧИСЛА  ')
print('='*40)

while True:
    n = input('\n основание > ')
    if not n:
        break
    n = int(n)
    k = int(input(' показатель > '))
    print(f"\t\tn^k = {power(n, k)}")
