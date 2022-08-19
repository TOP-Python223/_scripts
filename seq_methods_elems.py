s = 'abcd efgh . ij'
l = ['abc', 'd', 1, '1', [1, 2], 1]
t = (0, '123', 'ab', 'c d', ['1', '2'], 'ab')


print(f'{s.count("a") = }', end='\n\n')
print(f'{s.count("ab") = }', end='\n\n')
print(f'{s.count(" ") = }', end='\n\n')
print(f'{s.count("abef") = }', end='\n\n')

print(f'{l.count("a") = }', end='\n\n')
print(f'{l.count("abc") = }', end='\n\n')
print(f'{l.count(1) = }', end='\n\n')

print(f'{t.count("c") = }', end='\n\n')
print(f'{t.count("ab") = }', end='\n\n')
print(f'{t.count("2") = }', end='\n\n')


print(f'{s.index(" ") = }', end='\n\n')
print(f'{l.index(1) = }', end='\n\n')
print(f'{t.index("ab") = }', end='\n\n')

print(f'{s.rindex(" ") = }', end='\n\n')
print(f'{len(l) - l[::-1].index(1) - 1 = }', end='\n\n')
print(f'{len(t) - t[::-1].index("ab") - 1 = }', end='\n\n')

