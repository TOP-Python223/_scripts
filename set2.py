from random import randrange as rr

nums = [rr(-7, 8) for _ in range(15)]
print(f"{nums = }")
nums_unique = set(nums)
print(f"{nums_unique = }\n")

for elem in nums_unique:
    print(elem, end=' ')
print()

nums_unique_t = tuple(nums_unique)
