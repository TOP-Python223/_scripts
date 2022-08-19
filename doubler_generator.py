def doubler(x: int, step: int) -> int:
    while abs(x) < 100:
        yield x
        yield x
        x += step


for n in doubler(50, 5):
    print(n, end=' ')
print()
