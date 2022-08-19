def gener_func(x: int) -> int:
    """Генераторная функция."""
    while x > 0:
        yield x
        x -= 1

q = gener_func(10)
print(next(q), '(с помощью next())')
print(next(q), '(с помощью next())')
print(next(q), '(с помощью next())')

for n in q:
    print(f'{n} (в цикле)')

print(f'\n{list(q) = }\n')

l = list(gener_func(6))
print(f'{l = }\n')