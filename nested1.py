data = [
    [1, 2, (4, 5)],
    [2, 5, (1, 3)],
    [4, 3, (2, 1)]
]


data_flat = []
for row in data:
    for elem in row:
        if isinstance(elem, (list, tuple, dict)):
            for nest_elem in elem:
                data_flat += [nest_elem]
        else:
            data_flat += [elem]
print(data_flat, end='\n\n')

elem_rate = {elem: data_flat.count(elem) for elem in data_flat}
print(elem_rate, end='\n\n')


elem_rate2 = {}
for row in data:
    for elem in row:
        if isinstance(elem, (list, tuple, dict)):
            for nest_elem in elem:
                elem_rate2[nest_elem] = elem_rate2.setdefault(nest_elem, 0) + 1
        else:
            elem_rate2[elem] = elem_rate2.setdefault(elem, 0) + 1
print(elem_rate2, end='\n\n')
