from random import randrange as rr

s = 'string for sorting'
l = []
for _ in range(12):
    l += [rr(-5, 6)]
t = tuple()
for _ in range(11):
    t += (rr(10, 100),)

print(s, l, t, sep='\n')

print('\nпосле сортировки: ')
print(sorted(s), sorted(l), sorted(t, reverse=True), sep='\n')

if l == sorted(l):
    print('\nсписок l уже отсортирован')
else:
    print('\nсписок l ещё не отсортирован')
