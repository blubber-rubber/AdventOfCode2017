import time

start_time = time.time()

with open('input.txt') as f:
    maze = [int(line.rstrip('\n')) for line in f.readlines()]

pos = 0
jumps = 0

while pos < len(maze):
    j = maze[pos]
    maze[pos] += 2 * (j < 3) - 1
    jumps += 1
    pos += j


print(jumps)
print(time.time() - start_time)
