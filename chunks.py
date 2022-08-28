from random import randrange as rr
from typing import Generator

query_result = [rr(10, 100, 10) for _ in range(25)]


def chunks(data: list, chunk_size: int) -> Generator:
    
    for i in range(1, len(data) // chunk_size + 1):
        yield data[ (i-1)*chunk_size : i*chunk_size ]
    
    yield data[i*chunk_size:]


def chunks2(data: list, chunk_size: int) -> list:
    res = []
    for i in range(0, len(data), chunk_size):
        res += [data[ i : i+chunk_size ]]
    return res
    

gen = chunks(query_result, 10)

for chunk in gen:
    print(chunk)
print()

iter = chunks2(query_result, 10)
for chunk in iter:
    print(chunk)

