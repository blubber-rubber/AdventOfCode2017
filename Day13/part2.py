import time

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

info = [tuple(int(x) for x in line.split(': ')) for line in lines]

wait = 0
while not all((wait + depth) % (2 * (rng - 1)) for depth, rng in info):
    wait += 1
print(wait)
print(time.time() - start_time)
