all_builtins = dir(__builtins__)
builtin_function = []
for obj_name in all_builtins:
    obj = getattr(__builtins__, obj_name)
    if '__call__' in dir(obj):
        builtin_function += [obj_name]
        # print(obj_name, obj, sep='\t')

a = 1
abc = 'avd'
type = f"{a} {type(a)}"

print(set(builtin_function), end='\n\n')
print(set(globals()), end='\n\n')

if set(builtin_function).isdisjoint(set(globals())):
    print('all names are valid')
else:
    print('there are invalid names:')
    print(set(builtin_function) & set(globals()))
