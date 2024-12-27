import math
import time
from collections import defaultdict
import re

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

registers = defaultdict(int)

test = {'<': lambda a, b: a < b,
        '<=': lambda a, b: a <= b,
        '>': lambda a, b: a > b,
        '>=': lambda a, b: a >= b,
        '==': lambda a, b: a == b,
        '!=': lambda a, b: a != b,
        }

funcs = {'inc': lambda a, b: a + b, 'dec': lambda a, b: a - b}
higest_ever = -math.inf

for line in lines:
    m = re.match('([^ ]+) (inc|dec) ([^ ]+) if ([^ ]+) ([^ ]+) ([^ ]+)', line)

    r1, f, n, c1, cf, c2 = m.groups()

    if test[cf](registers[c1], int(c2)):
        new_value = funcs[f](registers[r1], int(n))
        registers[r1] = new_value
        if new_value>higest_ever:
            higest_ever = new_value

print(higest_ever)

print(time.time() - start_time)
