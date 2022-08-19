for i in range(11):
    print(f'{i if i != 0 else "":>4}', end='')
print()
for num1 in range(1, 11):
    print(f'{num1:>4}', end='')
    for num2 in range(1, 11):
        print(f'{num1*num2:>4}', end='')
    print()
