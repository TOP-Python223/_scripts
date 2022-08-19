from pprint import pprint

def test_func(arg):
    pass

print(f"{test_func = }\n{type(test_func)}\n")
pprint(dir(test_func))


def func1():
    print('function 1 called')

def func2():
    print('function 2 called')

def func3():
    print('function 3 called')

functions = [func1, func2, func3]
for func in functions:
    func()
