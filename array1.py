from array import array, typecodes

print(f"{typecodes = }")

ints = array('H', range(10))
print(f"\n{ints = }")

try:
    ints.append(0.01)
except TypeError as e:
    print(f"\nints.append(0.01)\nTypeError: {e}")

try:
    ints.append(-1)
except OverflowError as e:
    print(f"\nints.append(-1)\nOverflowError: {e}")

try:
    ints.append(66000)
except OverflowError as e:
    print(f"\nints.append(66000)\nOverflowError: {e}")

print()
print(ints.tolist())
print(list(ints))
