
data = {'a': {0.1: [0.01, {'z': 1}, {'y': 2}, {'x': 3}],
              0.2: {1: 'a', 2: 'b'},
              0.3: (('ab', 'ba'), ('cde', 'dec', 'ecd', 'dce', 'ced', 'edc'))},
        'b': tuple(range(10)),
        'c': 1.1,
        'd': {'.': ord('.'), ',': ord(',')}}

data2 = {'a': {1: {0.1: {(1, 2): {frozenset({1, 2}): {100: 'a', 200: 'b'}}}}}}


def get_nested_keys(iterator: tuple | list | dict) -> tuple:
    """Рекурсивное извлечение ключей вложенных словарей"""
    res = ()
    if isinstance(iterator, dict):
        res += tuple(iterator)
        for obj in iterator.values():
            if isinstance(obj, (tuple, list, dict)):
                res += get_nested_keys(obj)
    elif isinstance(iterator, (tuple, list)):
        for obj in iterator:
            if isinstance(obj, (tuple, list, dict)):
                res += get_nested_keys(obj)
    return res

def get_nested_values(iterator: tuple | list | dict) -> tuple:
    """Рекурсивное извлечение значений вложенных словарей и итерируемых объектов"""
    res = ()
    if isinstance(iterator, dict):
        iterator = iterator.values()
    for obj in iterator:
        if isinstance(obj, (tuple, list, dict)):
            res += get_nested_values(obj)
        else:
            res += (obj,)
    return res

def get_nested_elements(iterator: tuple | list | dict) -> tuple:
    """Рекурсивное извлечение ключей и значений вложенных словарей и итерируемых объектов"""
    res = ()
    if isinstance(iterator, dict):
        res += tuple(iterator)
        iterator = iterator.values()
    for obj in iterator:
        if isinstance(obj, (tuple, list, dict)):
            res += get_nested_elements(obj)
        else:
            res += (obj,)
    return res


print(get_nested_keys(data), end='\n\n')
print(get_nested_values(data), end='\n\n')
print(get_nested_elements(data), end='\n\n\n')

print(get_nested_keys(data2), end='\n\n')
print(get_nested_values(data2), end='\n\n')
print(get_nested_elements(data2), end='\n\n\n')
