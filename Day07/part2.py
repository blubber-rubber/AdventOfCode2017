import time
import re
from collections import defaultdict, Counter

start_time = time.time()

programs = set()
is_supported = set()
weights = {}
graph = defaultdict(list)

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

for line in lines:
    m = re.match(r'([a-z]+) \(([0-9]+)\) *(->)* *(.*)', line)
    prog, w, s, lijst = m.groups()
    weights[prog] = int(w)
    programs.add(prog)
    if s is not None:
        is_supported.update(lijst.split(', '))
        graph[prog] += lijst.split(', ')


def dfs(node, weights, graph):
    weight = weights[node]
    weight_lijst = []
    if graph[node]:
        for child in graph[node]:
            w = dfs(child, weights, graph)
            weight_lijst.append(w)

        if not all(x == w for x in weight_lijst):
            ws = Counter(weight_lijst)
            good_weight = [x for x in ws if ws[x] != 1][0]
            bad_weight = [x for x in ws if ws[x] == 1][0]
            bad_index = weight_lijst.index(bad_weight)
            bad_child = graph[node][bad_index]
            print(weights[bad_child] + good_weight - bad_weight)

            weight_lijst[bad_index] = good_weight

    return weight + sum(weight_lijst)

    return weight


base = list(programs.difference(is_supported))[0]
dfs(base, weights, graph)

print(time.time() - start_time)
