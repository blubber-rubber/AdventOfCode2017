import math
import time
import re

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

closest = None
closest_dist = math.inf

for i, line in enumerate(lines):
    m = re.match('p=<(-?\d+),(-?\d+),(-?\d+)>, v=<(-?\d+),(-?\d+),(-?\d+)>, a=<(-?\d+),(-?\d+),(-?\d+)>', line)
    px, py, pz, vx, vy, vz, ax, ay, az = (int(x) for x in m.groups())
    d = abs(ax) + abs(ay) + abs(az)
    if d < closest_dist:
        closest = i
        closest_dist = d

print(closest)
print(time.time() - start_time)
