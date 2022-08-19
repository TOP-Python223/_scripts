# функция декоратор
def decorator(func_object):
    print(locals(), end='\n\n')
    # служебная функция
    def wrapped():
        print("Код декоратора до вызываемой функции")
        func_object()
        print("Код декоратора после вызываемой функции\n")
    return wrapped

# декорируемая функция
def func1():
    print("Функция func1")

# применение декоратора
#   эквивалентно записи func2 = decorator(func2)
@decorator
def func2():
    print("Это func2!")


func1 = decorator(func1)
func1()

func2()