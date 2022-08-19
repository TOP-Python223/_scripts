l = ['z', 0.59473, [' '], (1, 2)]
print(l, type(l), sep='\n')
print(f'{len(l) = }', end='\n\n')

for i in range(len(l)):
    print(l[i], type(l[i]), sep='\t')
print()

print(f'{l[:2] + ["Z"] = }', end='\n\n')

print(f'{id(l) = } до изменения')

for i in range(len(l)):
    l[i] = (i+2)**2
del l[1]

print(f'{id(l) = } после изменения')
print(l)
