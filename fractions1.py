from fractions import Fraction as F
from pprint import pprint
from math import pi

nums = [F(i, j) for i, j in zip(range(1, 10), range(9, 0, -1))]

pprint(nums)
print()

for fn in nums:
    print(fn)

f1 = input('\nвведите десятичную дробь: ')
print(F(f1), end='\n\n\n')


print(pi)
print(f"{F(pi) = }")
print(f"\n{F(pi).limit_denominator(1000) = }")
print(f"~ {float(F(pi).limit_denominator(1000))}")

print(f"\n{F(pi).limit_denominator(100) = }")
print(f"~ {float(F(pi).limit_denominator(100))}")
