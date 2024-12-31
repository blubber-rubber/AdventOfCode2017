import time
from collections import defaultdict

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

REGISTERS = defaultdict(int)
OUTPUTS = []
RECOVERED = []


def get_value(v):
    if v in REGISTERS:
        return REGISTERS[v]
    return int(v)


def snd(x):
    OUTPUTS.append(get_value(x))


def set(x, y):
    REGISTERS[x] = get_value(y)


def add(x, y):
    REGISTERS[x] += get_value(y)


def mul(x, y):
    REGISTERS[x] *= get_value(y)


def mod(x, y):
    REGISTERS[x] %= get_value(y)


def rcv(x):
    if get_value(x) != 0:
        RECOVERED.append(OUTPUTS[-1])


def jgz(x, y):
    if get_value(x) > 0:
        return get_value(y)


pointer = 0

funcs = {'snd': snd, 'set': set, 'add': add, 'mul': mul, 'jgz': jgz, 'mod': mod, 'rcv': rcv}

while pointer < len(lines) and len(RECOVERED) == 0:
    f, *a = lines[pointer].split(' ')
    r = funcs[f](*a)
    if r:
        pointer += r
    else:
        pointer += 1

print(RECOVERED[-1])
print(time.time() - start_time)
