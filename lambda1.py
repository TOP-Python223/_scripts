def f1(x):
    return x + 5

f2 = lambda x: x + 5

print(f"{f1}\n{type(f1)}\n")
print(f"{f2}\n{type(f2)}\n")

for attr1, attr2 in zip(dir(f1), dir(f2)):
    print(f"{attr1}   {attr2}")
    
print('\n\n', f2.__name__, sep='')
