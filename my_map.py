def mymap(func_obj, iter):
    res = ()
    for elem in iter:
        res += (func_obj(elem),)
    return res


nums = list(range(-7, 8))

print(*map(abs, nums))
print(*mymap(abs, nums), end='\n\n')


def f(x):
    return round(3/(x - 10), 2)

print(*map(f, nums))
print(*mymap(f, nums), end='\n\n')

print(*map(lambda x: round(3/(x-10), 2), nums))
print(*mymap(lambda x: round(3/(x-10), 2), nums), end='\n\n')
