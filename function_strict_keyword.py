from shutil import get_terminal_size as gts

# последние два аргумента могут быть переданы только по ключу (не по позиции)
def func(arg1, arg2, *, arg3, arg4):
    print(locals(), end='\n\n')

func(arg1=1, arg2=2, arg3=3, arg4=4)
func(5, 6, arg3=7, arg4=8)
# приведёт к ошибке
# func(9, 10, 11, 12)


# последние четыре аргумента могут быть переданы только по ключу
#   т.к. эти аргументы однотипные
def pretty_print(text: str, *,
                 center: bool = False,
                 right: bool = False,
                 upper: bool = False,
                 frame: bool = True) -> None:
    half_width = (0, (gts()[0] - 1 - len(text)) // 2)[center]
    print(f"{' '*half_width}{text}")

# приведёт к ошибке
# неочвидные аргументы
# pretty_print('Important Text', True, False, True)

pretty_print('Important Text', center=True, upper=True)
