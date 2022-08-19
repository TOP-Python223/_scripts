while num := input('\nnumber: '):
    num, dividers = int(num), []
    for div in range(1, num//2+1):
        if num % div == 0:
            dividers += [div]
    dividers += [num]
    print(dividers)
