
def func(**kwargs):
    print(f"{type(kwargs)}\t{len(kwargs)}\n")
    if kwargs:
        q = tuple(kwargs.items())
        for k, v in q[:-1]:
            print(f"{k}={v}", end=', ')
        print(f"{q[-1][0]}={q[-1][1]}", end='\n\n')

func(arg1='test', arg2=15, last_arg=float('inf'))


# первые два строго позиционных аргумента
# следующие два позиционно-ключевых аргумента
# последние два строго ключевых аргумента
def full1(pos1, pos2, /, pos_or_key1, pos_or_key2, *, key1, key2):
    pass

# произвольное количество строго позиционных 
#   и произвольное количество строго ключевых
def full2(pos1, pos2, /, *args, key1, key2, **kwargs):
    pass

