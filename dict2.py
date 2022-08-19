d = {'a': 1, 'b': 2, 'c': 3, 0.1: 'одна десятая'}
print(f"{d = }")

print(f"{d['a'] = }")
print(f"{d['b'] = }")
print(f"{d['c'] = }")
print(f"{d[0.1] = }\n")

try:
    print(d['z'])
except KeyError:
    print('недопустимо обращаться к значению по несуществующему ключу')

print(f"\n{'b' in d = }")
print(f"{'z' in d = }\n")

print(list(d.keys()))
for key in d:
    print(f"{key = }\t{d[key] = }")
print()

print(list(d.values()))
for value in d.values():
    print(f"{value = }")
print()

print(list(d.items()))
for key, value in d.items():
    print(f"{key = }\t{value = }")
print()
