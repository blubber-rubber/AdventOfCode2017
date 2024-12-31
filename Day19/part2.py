import time
import numpy as np

start_time = time.time()

with open('input.txt') as f:
    GRID = [line.rstrip('\n') for line in f.readlines()]

N_ROWS = len(GRID)
N_COLS = max(len(row) for row in GRID)

for i in range(len(GRID)):
    GRID[i] = GRID[i]+' '*(N_COLS-len(GRID[i]))


class Vector2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def __iter__(self):
        yield self.x
        yield self.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return f'({self.x}, {self.y})'


DIRS = [Vector2D(0, 1), Vector2D(1, 0), Vector2D(-1, 0), Vector2D(0, -1)]


def dfs(path):
    cp = path[-1]
    backwards = path[-2] - cp
    dirs = [d for d in DIRS if d != backwards]
    char = GRID[cp.y][cp.x]

    if char in '+|-':
        dirs = [d for d in dirs if (d * backwards == 0) == (char == '+')]

    final = True
    for dir in dirs:
        new_pos = cp + dir

        if 0 <= new_pos.x < N_COLS and 0 <= new_pos.y < N_ROWS and GRID[new_pos.y][new_pos.x] != ' ':
            steps = 1
            final = False
            while 0 <= new_pos.x < N_COLS and 0 <= new_pos.y < N_ROWS and GRID[new_pos.y][new_pos.x] in '|-':
                path.append(new_pos)
                steps += 1
                new_pos = new_pos + dir
            path.append(new_pos)

            dfs(path)
            del path[-steps]
    if final:
        print(len(path)-1)


start_pos = Vector2D(GRID[0].index('|'), 0)

path = [start_pos + Vector2D(0, -1), start_pos]


dfs(path)
print(time.time() - start_time)
