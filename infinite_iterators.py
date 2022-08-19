from itertools import count, repeat, cycle

cnt = count(0)
while True:
    # ...
    next(cnt)
    # ...
    if not input(' > '):
        break
print()


items, cnt = ['pen', 'car', 'cap'], 0
for item in cycle(items):
    if cnt >= 10:
        break
    print(item)
    cnt += 1
print()


for _ in repeat(None, 10):
    print('Hello 10 times!')
print()

matrix = list(repeat(list(repeat(0, 5)), 5))
print(matrix)
