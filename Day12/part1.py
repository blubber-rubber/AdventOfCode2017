import time
from collections import defaultdict

start_time = time.time()

graph = defaultdict(set)

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

for line in lines:
    a, lijst = line.split(' <-> ')
    for x in lijst.split(', '):
        graph[a].add(x)
        graph[x].add(a)

visited = {'0'}
stack = ['0']

while stack:
    node = stack.pop()
    for other in graph[node]:
        if other not in visited:
            visited.add(other)
            stack.append(other)

print(len(visited))

print(time.time() - start_time)
