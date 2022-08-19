from pprint import pprint

d = {'a': 1, 'b': 2, 'c': 3, 0.1: 'одна десятая'}
print("d = {'a': 1, 'b': 2, 'c': 3, 0.1: 'одна десятая'}")
print(f"{d}")
print(f"{type(d)}\n")

d['z'] = 26
print(f"{d['z'] = }")
print(f"{d}\n")

d[0.1] = 'one tenth'
print(f"{d[0.1] = }")

d1 = {}
print("\nd1 = {}")
print(f"{d1}")

d2 = {'1': 1, '2': 2, '2': 3}
print("\nd2 = {'1': 1, '2': 2, '2': 3}")
print(f"{d2 = }")

try:
    print("\nd3 = {[1, 2]: 'unhashable type'}")
    d3 = {[1, 2]: 'unhashable type'}
except TypeError as e:
    print(f"{e.__class__.__name__}: {e!s}\n")

d4 = {('0123f5a6', 'Andrey'): {'name': 'Andrey', 
                               'age': 50,
                               'sex': 'M'},
      ('1900c5b1', 'Grigoriy'): {'name': 'Grigoriy', 
                                 'age': 19,
                                 'sex': 'M'}}
pprint(d4)

iter = [str(i/100) for i in range(-3, 4)]
d5 = dict.fromkeys(iter)
print(f"\nd5 = dict.fromkeys({iter})")
print(f"{d5 = }")

iter = [i**2 for i in range(1, 10)]
d6 = dict.fromkeys(iter, tuple())
print(f"\nd6 = dict.fromkeys({iter}, tuple())")
print(f"{d6 = }")

d7 = dict([(1, 'a'), (2, 'b')])
print("\nd7 = dict([(1, 'a'), (2, 'b')])")
print(f"{d7 = }")

d8 = dict(red=(255, 0, 0), green=(0, 255, 0))
print("\nd8 = dict(red=(255, 0, 0), green=(0, 255, 0))")
print(f"{d8 = }")

d9 = {chr(i): i-96 for i in range(97, 123)}
print("\nd9 = {chr(i): i-96 for i in range(97, 124)}")
print(f"{d9 = }")

d10 = {v: k for k, v in d9.items()}
print("\nd10 = {v: k for k, v in d9.items()}")
print(f"{d10 = }")
