import math
import time
import re
from collections import defaultdict
from itertools import combinations

start_time = time.time()

# x_n = x_0+v_0*n + a_0 * (n+1)*n/2


with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

particles = []

for i, line in enumerate(lines):
    m = re.match('p=<(-?\d+),(-?\d+),(-?\d+)>, v=<(-?\d+),(-?\d+),(-?\d+)>, a=<(-?\d+),(-?\d+),(-?\d+)>', line)
    particles.append(tuple(int(x) for x in m.groups()))

collisions = []
for i, j in combinations(range(len(particles)), 2):
    part1 = particles[i]
    part2 = particles[j]
    p1x, p1y, p1z, v1x, v1y, v1z, a1x, a1y, a1z = part1
    p2x, p2y, p2z, v2x, v2y, v2z, a2x, a2y, a2z = part2

    a = (a1x - a2x)
    b = (2 * v1x + a1x - 2 * v2x - a2x)
    c = (2 * p1x - 2 * p2x)

    moments = []
    if a != 0:
        D = b ** 2 - 4 * a * c

        if D >= 0 and D ** (1 / 2) - int(D ** (1 / 2)) == 0:
            t1 = (-b - int(D ** (1 / 2))) / (2 * a)
            t2 = (-b + int(D ** (1 / 2))) / (2 * a)

            moments = [t1, t2]
    elif b != 0:
        moments = [-c / b]

    for m in moments:
        if m > 0 and m - int(m) == 0:
            x1 = p1x + v1x * m + a1x * (m + 1) * m // 2
            x2 = p2x + v2x * m + a2x * (m + 1) * m // 2
            y1 = p1y + v1y * m + a1y * (m + 1) * m // 2
            y2 = p2y + v2y * m + a2y * (m + 1) * m // 2
            z1 = p1z + v1z * m + a1z * (m + 1) * m // 2
            z2 = p2z + v2z * m + a2z * (m + 1) * m // 2
            if y1 == y2 and z1 == z2 and x1 == x2:
                collisions.append((m, i, j))

removed = defaultdict(lambda: math.inf)
collisions.sort()
for t, i, j in collisions:
    if t <= removed[i] and t <= removed[j]:
        removed[i] = t

print(len(particles) - len(removed.keys()))

print(time.time() - start_time)
