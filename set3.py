from random import randrange as rr

nums1 = [rr(-7, 8) for _ in range(15)]
nums2 = [rr(-7, 8) for _ in range(15)]
nums1_unique = set(nums1)
nums2_unique = set(nums2)
print(f"{nums1_unique = }")
print(f"{nums2_unique = }\n")

print('надмножество или подмножество')
print(f"{nums1_unique >= nums2_unique = }")
print(f"{nums1_unique <= nums2_unique = }\n")

print('разъединены ли множества')
print(f"{nums1_unique.isdisjoint(nums2_unique) = }\n")

print('объединение')
print(f"{nums1_unique | nums2_unique = }\n")

print('пересечение')
print(f"{nums1_unique & nums2_unique = }\n")

print('разность')
print(f"{nums1_unique - nums2_unique = }")
print(f"{nums2_unique - nums1_unique = }\n")

print('симметричная разность')
print(f"{nums1_unique ^ nums2_unique = }")
