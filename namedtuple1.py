from collections import namedtuple as nt
from random import random as r, randrange as rr

Point = nt('Point', ['x', 'y', 'z'])
p1 = Point(0.1, -0.5, 0)
p2 = Point(-1.5, 0.15, 1)

print(f"\n{p1[0] = }\t{p1[1:] = }")
print(f"\n{p1.x = }\t{p1.y = }\t{p1.z = }\n")

points = [p1, p2]
for _ in range(8):
    points += [Point(x=round(r()*rr(-15, 16), 1),
                     y=round(r()*rr(-15, 16), 1),
                     z=round(r()*rr(-15, 16), 1))]

for p in points:
    print(p)
