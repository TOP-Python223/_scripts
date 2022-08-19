CALLS_CNT = {}

def calls_counter(func_obj):
    # объект в глобальном пространстве имён
    global CALLS_CNT
    # объект в локальном пространстве имён функии декоратора
    # CALLS_CNT = {}
    def wrapped(*args, **kwargs):
        # ссылка на объект в локальном пространстве имён функии декоратора
        # nonlocal CALLS_CNT
        res = func_obj(*args, **kwargs)
        CALLS_CNT[func_obj.__name__] = \
            CALLS_CNT.setdefault(func_obj.__name__, 0) + 1
        return res
    return wrapped


@calls_counter
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

@calls_counter
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


while True:
    n = input('\n число 1 > ')
    if not n:
        break
    n = int(n)
    k = int(input(' число 2 > '))
    # n, k = max(n, k), min(n, k)
    if n < k:
        n, k = k, n
    print(f"\t\t{n}**{k} = {power(n, k)}")
    print(f"\t\tНОД({n}, {k}) = {gcd(n, k)}")
    print(f"\t\t{CALLS_CNT = }")
