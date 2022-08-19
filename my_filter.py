from random import randrange as rr

def myfilter(func_obj, iter):
    res = ()
    for elem in iter:
        if func_obj(elem):
            res += (elem,)
    return res

def iseven(x: int) -> bool:
    """Функция-предикат для проверки числа на чётность
    
    -> True если число чётное"""
    # if x % 2:
        # return False:
    # else:
        # return True
    return False if x % 2 else True

def isprime(x: int) -> bool:
    """Функция-предикат для проверки того, что число — простое"""
    for delim in range(2, x//2+1):
        if x % delim == 0:
            return False
    else:
        return True


nums = [rr(1, 100) for _ in range(30)]

print(*filter(iseven, nums))
print(*myfilter(iseven, nums), end='\n\n')

print(*filter(lambda x: False if x%2 else True, 
              nums))
print(*myfilter(lambda x: False if x%2 else True, 
                nums), end='\n\n')

print(*filter(isprime, nums))
print(*myfilter(isprime, nums), end='\n\n')


