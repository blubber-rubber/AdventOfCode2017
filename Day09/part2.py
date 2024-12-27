import time
import re

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]


def dfs_group(group, depth):
    score = depth
    group = group[1:-1].rstrip(',')
    if group == '':
        return score

    aantal = 0
    for index, c in enumerate(group):
        if c == '{':
            aantal += 1
            if aantal == 0:
                start_index = index
        elif c == '}':
            aantal -= 1

        if aantal == 0:
            score += dfs_group(group[start_index:index + 1], depth + 1)
    return score




cleaned = re.sub('<([^!>]|!.)*>', '<>', lines[0])



score = 0
aantal = 0

for char in cleaned:
    if char == '{':
        aantal += 1
        score += aantal

    elif char == '}':
        aantal -= 1

print(score)
