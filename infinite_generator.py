def inf_increment(x: int) -> int:
    while True:
        yield x
        x += 1

def repeat(obj):
    while True:
        yield obj


for i in inf_increment(1):
    if i > 10000:
        break
    print(i)

for x in repeat(123):
    print(x, end=' ')
