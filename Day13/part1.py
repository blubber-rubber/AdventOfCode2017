import time

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

score = 0
for line in lines:
    depth, rng = (int(x) for x in line.split(': '))
    score += depth * rng * (depth % (2*(rng-1)) == 0)

print(score)
print(time.time() - start_time)
