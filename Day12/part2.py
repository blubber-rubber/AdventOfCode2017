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

index = 1
visited = {}

for key in graph:
    if key not in visited:
        visited[key] = index
        stack = [key]

        while stack:
            node = stack.pop()
            for other in graph[node]:
                if other not in visited:
                    visited[other] = index
                    stack.append(other)

        index += 1

print(max(visited.values()))

print(time.time() - start_time)
