n, m = 10, 5
# вложенные циклы
for i in range(n):
    for j in range(m):
        print(f'{i = }\t{j = }')
    print()


# подобный подход нежелателен
for i in range(10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                for m in range(10):
                    for n in range(10):
                        print(i, j, k, l, m, n)
