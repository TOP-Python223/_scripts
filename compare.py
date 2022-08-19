a = 1
print(' >', 3 > a + 2)
print(' <', 1 < a + 1)
print('>=', 1 >= a + 1)
print('<=', 1 <= a + 1)
print('==', a == 1)
print('!=', a != 1)
print()

b = 'abcdefghijklmnopqrstuvwxyz'
print('a', 'a' in b)
print('A', 'A' in b)
print('mno', 'mno' in b)
print('gtz', 'gtz' in b)
print('za', 'za' in b + b)
print()

c = 'ab12'
print('ac', 'ac' > c)
print('12', '12' < c)
print('ab2', 'ab2' >= c)
print('ab', 'ab' <= c)
