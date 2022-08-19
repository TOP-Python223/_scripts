from functools import reduce

# [1, 2, 3, 4] -> reduce -> ((1+2)+3)+4

def myreduce(func_obj, iter):
    res = iter[0]
    for elem in iter[1:]:
        res = func_obj(res, elem)
    return res

def adder(x, y):
    return x + y

def producter(x: float, y: float) -> float:
    return x * y


nums = list(range(1, 10))

print(reduce(adder, nums))
print(myreduce(adder, nums), end='\n\n')

print(reduce(producter, nums))
print(myreduce(producter, nums), end='\n\n')

print(reduce(adder, [chr(i) for i in range(65, 91)]))
print(myreduce(adder, [chr(i) for i in range(65, 91)]), end='\n\n')

print(reduce(lambda x, y: 2*x + y, nums))
print(myreduce(lambda x, y: 2*x + y, nums), end='\n\n')
