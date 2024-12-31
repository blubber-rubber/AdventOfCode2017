import time

start_time = time.time()

with open('input.txt') as f:
    line = f.readline().rstrip('\n')


def spin(lijst, n):
    return lijst[-n:] + lijst[:-n]


def exchange(lijst, a, b):
    lijst[a], lijst[b] = lijst[b], lijst[a]
    return lijst


def partner(lijst, a, b):
    ai = lijst.index(a)
    bi = lijst.index(b)
    lijst[ai] = b
    lijst[bi] = a
    return lijst


def perform_dance(lijst):
    for instr in line.split(','):
        if instr[0] == 's':
            lijst = spin(lijst, int(instr[1:]))
        elif instr[0] == 'x':
            a, b = (int(x) for x in instr[1:].split('/'))
            exchange(lijst, a, b)
        elif instr[0] == 'p':
            a, b = instr[1:].split('/')
            partner(lijst, a, b)
    return lijst


lijst = list('abcdefghijklmnop')

positions = {}

pos = ''.join(lijst)
count = 0
while pos not in positions:
    positions[pos] = count
    count += 1
    lijst = perform_dance(lijst)
    pos = ''.join(lijst)

dances = 1_000_000_000

dances -= positions[pos]
dances = dances % count

for _ in range(dances):
    lijst = perform_dance(lijst)
print(''.join(lijst))
print(time.time() - start_time)
