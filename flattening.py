def flat(container: tuple) -> tuple:
    """Элементы кортежей и списков первого уровня вложенности помещает в плоский кортеж."""
    res = ()
    for elem in container:
        # если элемент является кортежем или списком
        if isinstance(elem, (tuple, list)):
            res += tuple(elem)
        else:
            res += (elem,)
    return res


m = [[1, 2, 3, 4, 5],
     [6, 7, 8, 9, 0]]

print(flat(m))
