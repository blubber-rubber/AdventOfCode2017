import time
from collections import defaultdict

start_time = time.time()

with open('input.txt') as f:
    number = [int(line.rstrip('\n')) for line in f.readlines()][0]


def get_position(number):
    n = int(number ** (1 / 2))

    remaining_steps = number - n ** 2

    if n % 2 == 0:
        pos = [-(n // 2 - 1), -(n // 2)]

        if remaining_steps > 0:
            pos[0] -= 1
            remaining_steps -= 1
            dirs = [(0, 1), (1, 0)]


    else:
        pos = [(n // 2), (n // 2)]
        if remaining_steps > 0:
            pos[0] += 1
            remaining_steps -= 1

        dirs = [(0, -1), (-1, 0)]

    index = 0
    while remaining_steps > 0:
        counter = 0
        dx, dy = dirs[index]
        while counter < n and remaining_steps > 0:
            counter += 1
            pos[0] += dx
            pos[1] += dy
            remaining_steps -= 1
        index = 1

    return pos


memory = defaultdict(int)

pos = tuple(get_position(1))

memory[pos] = 1

score = 1
index = 2
neighbours = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

while score < number:
    pos = tuple(get_position(index))
    score = 0
    cx, cy = pos
    for dx, dy in neighbours:
        score += memory[(cx + dx, cy + dy)]
    memory[pos] = score
    index += 1

print(score)
print(time.time() - start_time)
