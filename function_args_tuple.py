# принимает любое количество строго позиционных аргументов
def func(*args) -> None:
    print(f"{type(args) = }\t{len(args) = }")
    if args:
        for arg in args[:-1]:
            print(arg, end=', ')
        print(args[-1], end='\n\n')


func()
func(1, 's')
func([1, 2], (3, 4), 5.5, '6')

l = list(range(100,1000))
# оператор распаковки итерируемого объекта:
#   каждый распакованный элемент списка станет отдельным аргументом
func(*l)

# приведёт к ошибке
# func(args=l)
print()


# менее удобен, т.к. ограничивает типы передаваемых объектов
def func2(args: list | tuple) -> None:
    print(f"{type(args) = }\t{len(args) = }")
    if args:
        for arg in args[:-1]:
            print(arg, end=', ')
        print(args[-1], end='\n\n')

func2([123])
# приведёт к ошибке
# func2(123)
