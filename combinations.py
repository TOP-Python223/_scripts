from string import ascii_uppercase as letters
from itertools import permutations

perms = tuple(''.join(perm) 
              for perm in permutations(letters, 3))
print(len(perms))
print(*perms)
