from time import perf_counter as pc, perf_counter_ns as pc_ns
from itertools import repeat


TRIES = 10**2
LIMIT = 10**2


total = 0
for _ in range(TRIES):
    start = pc_ns()
    for _ in range(LIMIT):
        a = None
    end = pc_ns()
    total += end - start
print(f"Elapsed time to range: {total//TRIES} ns")

total = 0
for _ in range(TRIES):
    start = pc_ns()
    for _ in repeat(None, LIMIT):
        a = None
    end = pc_ns()
    total += end - start
print(f"Elapsed time to repeat: {total//TRIES} ns\n")



start = pc()
for _ in range(TRIES):
    for _ in range(LIMIT):
        a = None
end = pc()
total = end - start
print(f"Elapsed time to range: {total/TRIES:.5f} s")

start = pc()
for _ in range(TRIES):
    for _ in repeat(None, LIMIT):
        a = None
end = pc()
total = end - start
print(f"Elapsed time to repeat: {total/TRIES:.5f} s\n")
