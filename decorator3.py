# функция декоратор
def decorator(func_object):
    # служебная функция
    def wrapped(*args, **kwargs):
        res = func_object(*args, **kwargs)
        return res
    return wrapped

# декорируемая функция
@decorator
def power(num1: int, num2: int) -> int:
    return num1**num2


print(power(2, num2=10))
