from random import randrange as rr

set1 = {1, '1', 1.0, (1,2,3), '1'}
print(type(set1))
print(f"{set1 = }\n")

nums = [rr(-1, 2) for _ in range(15)]
print(f"{nums = }")
print(f"{set(nums) = }\n")

empty_set = set()
print(f"{empty_set = }\n")

try:
    print("\n{1, 2, 3, [4, 5]}")
    print({1, 2, 3, [4, 5]})
except TypeError:
    print('множества не могут содержать изменяемые объекты')

try:
    print("\n{1, 2, 3, {4: 'd', 5: 'e'}}")
    print({1, 2, 3, {4: 'd', 5: 'e'}})
except TypeError:
    print('множества не могут содержать изменяемые объекты')

try:
    print("\n{1, 2, 3, {4, 5}}")
    print({1, 2, 3, {4, 5}})
except TypeError:
    print('множества не могут содержать изменяемые объекты')

print(f"\n{frozenset(nums)!s}")

try:
    print("\n{1, 2, 3, frozenset([4, 5])}")
    print({1, 2, 3, frozenset([4, 5])})
except TypeError:
    print('множества не могут содержать изменяемые объекты')
