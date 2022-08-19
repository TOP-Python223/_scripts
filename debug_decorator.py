# from function_recur_gcd import gcd

def debug(func_object):
    def wrapped(*args, **kwargs):
        p = 'asd'
        print(func_object.__name__)
        if doc := func_object.__doc__:
            print(f'\t{doc}')
        if args or kwargs:
            print('\t', end='')
        for arg in args:
            print(f'{arg!r}', end=', ')
        for param_name, arg_value in kwargs.items():
            print(f'{param_name}={arg_value!r}', end=', ')
        print('\b\b\n')
        res = func_object(*args, **kwargs)
        return res
    return wrapped


@debug
def func1(a, b: int, c: str):
    """Function for test."""

@debug
def gcd(number1: int, number2: int) -> int:
    """Рекурсивная функция вычисления наибольшего общего делителя двух чисел"""
    if number2 != 0:
        res = gcd(number2, number1 % number2)
        return res
    else:
        return number1


func1(' abc 9 ', 10, c='AB\n')

print(gcd(121, 90))
