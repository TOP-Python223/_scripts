from typing import Callable

def test():
    print('выполняется функция test')

print(f'{test = }\n{type(test) = }')

var = test
print(f'{var = }\n{type(var) = }')


def high(func_obj: Callable):
    print('дополнительная функциональность')
    func_obj()
    print('дополнительная функциональность')

def test2():
    print('test2 выполняется здесь')


def decorator(func_obj: Callable) -> Callable:
    
    def cuckoo():
        print('дополнительная функциональность')
        func_obj()
        print('дополнительная функциональность')
    
    return cuckoo


res = decorator(test)
print(f'\n{res = }\n{type(res) = }\n')

print(f'\nдо подмены {test = }')
# выполняется подмена объектов функций
test = decorator(test)
print(f'после подмены {test = }')

print(f'\nдо подмены {test2 = }')
# выполняется подмена объектов функций
test2 = decorator(test2)
print(f'после подмены {test2 = }')


@decorator
def test3():
    print('функция test3 вызвана')
print(f'\nпосле подмены {test3 = }')

