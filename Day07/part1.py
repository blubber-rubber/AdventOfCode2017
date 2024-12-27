import time
import re

start_time = time.time()

programs = set()
is_supported = set()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

for line in lines:
    m = re.match(r'([a-z]+) \([0-9]+\) *(->)* *(.*)', line)
    prog, s, lijst = m.groups()
    programs.add(prog)
    if s is not None:
        is_supported.update(lijst.split(', '))

print(programs.difference(is_supported))
print(time.time() - start_time)
