file1 = 'cmd.exe'
file2 = 'msofficex86_2010.exe'
page1 = 'index.htm'

print(file1, file2, page1, sep='\n', end='\n\n')

# примеры явных срезов
print(f'{file1[:3] = }')
print(f'{file2[-3:] = }')
print(f'{page1[2:-2] = }', end='\n\n')

# использование переменной индекса для срезов
for i in range(len(file2) + 1):
    print(f'file2[:{i}] = {file2[:i]}')
print()

# использование переменной отрицательного индекса для срезов
for i in range(-len(page1), 0):
    print(f'page1[{i}:] = {page1[i:]}')
print()
