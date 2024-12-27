import time
from itertools import combinations

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

som = 0
for line in lines:
    numbers = [int(x) for x in line.split('	')]
    for a, b in combinations(numbers, 2):
        if a % b == 0:
            som += a // b
        elif b % a == 0:
            som += b // a
print(som)
print(time.time() - start_time)
