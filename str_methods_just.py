s1 = 'abc'
s2 = 'A'
s3 = 'абвгд'

print(f"{s1.ljust(5) = }")
print(f"{s2.ljust(5) = }")
print(f"{s3.ljust(5) = }\n")

print(f"{s1.center(5) = }")
print(f"{s2.center(5) = }")
print(f"{s3.center(5) = }\n")

print(f"{s1.rjust(5) = }")
print(f"{s2.rjust(5) = }")
print(f"{s3.rjust(5) = }\n\n")


print(f"{s1.ljust(4, '~') = }")
print(f"{s2.ljust(4, '~') = }")
print(f"{s3.ljust(4, '~') = }\n")

print(f"{s1.center(4, '~') = }")
print(f"{s2.center(4, '~') = }")
print(f"{s3.center(4, '~') = }\n")

print(f"{s1.rjust(4, '~') = }")
print(f"{s2.rjust(4, '~') = }")
print(f"{s3.rjust(4, '~') = }\n\n")


print(f"{s1:_<5}")
print(f"{s2:_<5}")
print(f"{s3:_<5}\n")

print(f"{s1:_^5}")
print(f"{s2:_^5}")
print(f"{s3:_^5}\n")

print(f"{s1:_>5}")
print(f"{s2:_>5}")
print(f"{s3:_>5}\n")

