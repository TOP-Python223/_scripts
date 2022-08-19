from random import random as rf, randrange as rr, choice as ch
from string import ascii_letters as alt

data = {round(rf()*10**rr(1, 4), 2): ''.join(ch(alt) for _ in range(rr(2,6))) 
        for _ in range(20)}
print(data, end='\n\n')

print(*sorted(data), end='\n\n')
print(*sorted(data.values()), end='\n\n')

print(*sorted(data.items()), end='\n\n')
print(*sorted(data.items(), key=lambda x: x[1]), end='\n\n')


for key, value in data.items():
    data[key] = ''.join(sorted(value))
print(*sorted(data.values(), key=lambda char: char.isupper()), end='\n\n')

for key, value in data.items():
    data[key] = ''.join(sorted(value))
print(*sorted(data.values()), end='\n\n')
