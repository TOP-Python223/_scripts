s = 'Python is cool!'
l = list(range(10))
t = tuple(range(11, -12, -2))

s_empty = ''
l_empty = []  # list()
t_empty = tuple()

min_len = min(len(s), len(l), len(t))

for i in range(min_len):
    print(s[i] + str(l[i]) + str(t[i]))
print()

for i in range(len(s)):
    print(s[i:i+3], end=' ')
print('\n')

for i in range(0, len(s), 3):
    print(s[i:i+3], end='_')
print('\n')

for char in s:
    print(char, end='.')
print('\n')

for elem in l:
    print(elem, end='\t')
print('\n')

for elem in t:
    print(elem, end=',')
print('\n')
