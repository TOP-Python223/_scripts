while True:
    try:
        a, b = int(input('\nnum 1: ')), int(input('num 2: '))
    except ValueError:
        print('digits characters only!')
        continue
    print(a % b)
