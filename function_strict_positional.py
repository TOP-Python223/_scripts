# первые два аргумента можно передать только по позиции (без ключа)
def func(arg1, arg2, /, arg3, arg4):
    print(globals(), end='\n\n')
    print(locals(), end='\n\n')

func(1, 2, 3, 4)
# глобальная переменная
a = 1
func(5, 6, arg3=7, arg4=8)
# приведёт к ошибке
# func(arg1=1, arg2=2, arg3=3, arg4=4)


# аргумент можно передать только по позиции
def myinput(prompt: str = '', /) -> str:
    print(prompt, end='')
    return input()


# все аргументы можно передать только по позиции
def mymin(n1: float, 
          n2: float = float('inf'), 
          n3: float = float('inf'), 
          n4: float = float('inf'), 
          n5: float = float('inf'), /) -> float:
    nums, mn = [n1, n2, n3, n4, n5], float('inf')
    for n in nums:
        if n < mn:
            mn = n
    return mn

print(mymin(5))
print(mymin(1, 2, 3))
# приведёт к ошибке
# print(mymin(n3=1, n1=2, n2=3))


