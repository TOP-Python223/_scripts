t = (1, 'abc', 2.2, (10,))
print(t, type(t), sep='\n')
print(f'{len(t) = }', end='\n\n')

for i in range(len(t)):
    print(t[i], type(t[i]), sep='\t')
print()

print(f'{t[1:3]}')

print(f'{t[:1] + (323,) + t[2:] = }')
