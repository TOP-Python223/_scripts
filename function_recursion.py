def recur_func(x: int) -> int:
    print(f"вызов recur_func c аргументом {x}")
    if x > 0:
        res = recur_func(x - 1)
        print(f"возврат {res}")
        return res
    else:
        print(f"первый возврат {x}")
        return x

print(recur_func(int(input('глубина рекурсии: '))))
