from functools import lru_cache
from random import randrange

@lru_cache(maxsize=2)
def factorial(n: int) -> int:
    """Calculates factorial."""
    prod = 1
    for m in range(2, n+1):
        prod *= m
    return prod


a = factorial(15)
b = factorial(15)
print(f"{id(a) = }\n{id(b) = }")
print(f"{a is b = }\n")
c = factorial(16)
d = factorial(16)
print(f"{id(c) = }\n{id(d) = }")
print(f"{c is d = }\n")
e = factorial(17)
f = factorial(17)
print(f"{id(e) = }\n{id(f) = }")
print(f"{e is f = }\n")

g = factorial(15)
h = factorial(15)
print(f"{id(g) = }\n{id(h) = }")
print(f"{g is h = }\n")


# До применения декоратора, stdout:
#   id(a) = 2850017820176
#   id(b) = 2850017820128
#   a is b = False

#   id(c) = 2850017820272
#   id(d) = 2850017818880
#   c is d = False

#   id(e) = 2850017819168
#   id(f) = 2850017818976
#   e is f = False


# После применения декоратора, stdout:
#   id(a) = 2601461332128
#   id(b) = 2601461332128
#   a is b = True

#   id(c) = 2601461333424
#   id(d) = 2601461333424
#   c is d = True

#   id(e) = 2601461332416
#   id(f) = 2601461332416
#   e is f = True

#   id(g) = 2601461332224
#   id(h) = 2601461332224
#   g is h = True


@lru_cache(maxsize=2)
def r(n: int) -> int:
    return randrange(-1000, 1001)
