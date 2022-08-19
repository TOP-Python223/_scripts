def high_level_func(function_object):
    print('high_level_func starts')
    function_object()
    print('high_level_func ends')

def simple_func():
    print('simple_func called')


print(f"{simple_func = }\n{high_level_func = }\n")

high_level_func(simple_func)



def journal(func_obj, *args, **kwargs):
    print(f"\n{func_obj.__name__} is called with args", end=' ')
    print(', '.join(f"{n}={v}" for n, v in kwargs.items()))
    res = func_obj(*args, **kwargs)
    print(f"\treturn -> {res}")

def g(*, x, a=1, b=1, c=0):
    return a*x**2 + b*x + c

def h(*, x, a=1, b=1, c=1, d=0):
    return a*x**3 + b*x**2 + c*x + d

journal(g, x=2)
journal(g, x=2, a=4, c=3)
journal(g, x=2, a=2, b=-5, c=3)
journal(h, x=2)
journal(h, x=2, d=5)
journal(h, x=2, d=5, a=2)
journal(h, x=2, d=-3, a=3, c=6, b=2)
