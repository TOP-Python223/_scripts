from functools import wraps


def debug(func_object):
    @wraps(func_object)
    def wrapped(*args, **kwargs):
        p = 'asd'
        print(func_object.__name__)
        if doc := func_object.__doc__:
            print(f'\t{doc}')
        if args or kwargs:
            print('\t', end='')
        for arg in args:
            print(f'{arg!r}', end=', ')
        for param_name, arg_value in kwargs.items():
            print(f'{param_name}={arg_value!r}', end=', ')
        print('\b\b\n')
        res = func_object(*args, **kwargs)
        return res
    return wrapped


@debug
def func1(a, b: int, c: str):
    """Function for test."""


print(func1.__name__, 
      func1.__doc__, 
      func1.__annotations__, 
      sep='\n')

# До применения декоратора wraps, stdout:
#   wrapped
#   None
#   {}

# После применения декоратора wraps, stdout:
#   func1
#   Function for test.
#   {'b': <class 'int'>, 'c': <class 'str'>}
