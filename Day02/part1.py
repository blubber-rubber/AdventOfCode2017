import time

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

som = 0
for line in lines:
    numbers = [int(x) for x in line.split('	')]
    som += max(numbers) - min(numbers)
print(som)
print(time.time() - start_time)
