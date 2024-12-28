import math
import time
from collections import Counter

start_time = time.time()

with open('input.txt') as f:
    steps = list(f.readline().rstrip('\n').split(','))

DIRS = {
    'n': (0, 1),
    'ne': (1, 0),
    'se': (1, -1),
    's': (0, -1),
    'sw': (-1, 0),
    'nw': (-1, 1)

}

# v1 = (1,0) , v2 =(0,1) , v3 = (-1,1)
# => a=X+c, b =Y-c
# a*v1+b*v2+c*v3 = pos
# n_steps = min(abs(a)+abs(b)+abs(c))
# min(abs(X+c)+abs(Y-c)+abs(c))

max_steps = -math.inf

pos = [0, 0]
for step in steps:
    dx, dy = DIRS[step]
    pos[0] += dx
    pos[1] += dy

    c = list(sorted([-pos[0], pos[1], 0]))[1]
    a = pos[0] + c
    b = pos[1] - c
    n_steps = abs(a) + abs(b) + abs(c)
    if n_steps > max_steps:
        max_steps = n_steps

print(max_steps)
print(time.time() - start_time)
