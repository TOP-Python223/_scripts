# (
#     <вычисляемое выражение, возвращаемое на каждой итерации>
#     for <переменная цикла> in <итерируемый объект>
#     if <условие фильтра - выражение вычисляется если True>
# )

a = (i for i in range(10, 20))
print(f'{a = }\n{type(a) = }')

l1 = list(a)
print(f'{l1 = }\n{type(l1) = }')

l2 = list(i for i in range(10, 20))

# list enhancement - представление списка, генератор списка
l3 = [i for i in range(10, 20)]

print(f'{l1 == l2 == l3 = }\n')


s1 = set(i for i in range(10, 20))
print(f'{s1 = }\n{type(s1) = }')

# set enhancement - представление множества, генератор множества
s2 = {i for i in range(10, 20)}
print(f'{s1 == s2 = }\n')


a = ((i, i**2) for i in range(10, 20))

d1 = dict(a)
print(f'{d1 = }\n{type(d1) = }')

d2 = dict((i, i**2) for i in range(10, 20))

# dict enhancement - представление словаря, генератор словаря
d3 = {i: i**2 for i in range(10, 20)}

print(f'{d1 == d2 == d3 = }\n')
