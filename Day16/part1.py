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


lijst = list('abcdefghijklmnop')

for instr in line.split(','):
    if instr[0] == 's':
        lijst = spin(lijst, int(instr[1:]))
    elif instr[0] == 'x':
        a, b = (int(x) for x in instr[1:].split('/'))
        exchange(lijst, a, b)
    elif instr[0] == 'p':
        a, b = instr[1:].split('/')
        partner(lijst, a, b)

print(''.join(lijst))
print(time.time() - start_time)
