import time
from functools import reduce

start_time = time.time()

with open('input.txt') as f:
    key = f.readline().rstrip('\n')


def get_knot_hash(chars):
    lijst = [ord(x) for x in chars]
    lijst += [17, 31, 73, 47, 23]

    circle = list(range(256))
    cp = 0
    skip_size = 0

    for _ in range(64):

        for x in lijst:
            circle = circle[cp:] + circle[:cp]
            circle[:x] = circle[:x][::-1]
            circle = circle[-cp:] + circle[:(len(circle) - cp) % len(circle)]
            cp = (cp + x + skip_size) % len(circle)
            skip_size += 1

    dense_hash = []

    for i in range(16):
        dense_hash.append(reduce(lambda a, b: a ^ b, circle[16 * i:16 * (i + 1)]))

    hash = ''
    for c in dense_hash:
        hash += f'{hex(c)[2:]:>02}'
    return hash


grid = []
for i in range(128):
    h = get_knot_hash(f'{key}-{i}')
    b = bin(int(h, 16))[2:]
    grid.append(f'{b:>0128}')

N_ROWS = N_COLS = 128

DIRS = [(0, 1), (1, 0), (-1, 0), (0, -1)]

colors = {}
current_color = 0
for y in range(N_COLS):
    for x in range(N_ROWS):
        if grid[y][x] == '1' and (x, y) not in colors:
            current_color += 1
            states = [(x, y)]
            colors[(x, y)] = current_color
            while states:
                cx, cy = states.pop()
                for dx, dy in DIRS:
                    nx, ny = cx + dx, cy + dy
                    if 0 <= nx < N_COLS and 0 <= ny < N_ROWS and grid[ny][nx] == '1' and (nx, ny) not in colors:
                        states.append((nx, ny))
                        colors[(nx, ny)] = current_color

print(current_color)

print(grid)
print(time.time() - start_time)
