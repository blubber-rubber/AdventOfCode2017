import time

start_time = time.time()

with open('input.txt') as f:
    maze = [int(line.rstrip('\n')) for line in f.readlines()]

pos = 0
jumps = 0

while pos < len(maze):
    jumps += 1
    maze[pos] += 1
    pos += maze[pos] - 1

print(jumps)
print(time.time() - start_time)
