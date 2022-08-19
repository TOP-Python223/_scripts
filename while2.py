# суперцикл для командной строки
while True:
    comm = input('_> ')
    if comm == 'exit' or comm == 'quit':
        break
    elif comm == 'line':
        print('='*40)
    elif comm == 'square':
        print('='*40)
        # когда переменная цикла не используется в теле цикла:
        for _ in range(18):
            print('=' + ' '*38 + '=')
        print('='*40)
