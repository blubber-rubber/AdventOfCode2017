import time
from functools import reduce

start_time = time.time()

with open('input.txt') as f:
    lijst = [ord(x) for x in f.readlines()[0].rstrip('\n')]

lijst += [17, 31, 73, 47, 23]

circle = list(range(256))
cp = 0
skip_size = 0

for _ in range(64):

    for x in lijst:
        circle = circle[cp:] + circle[:cp]
        circle[:x] = circle[:x][::-1]
        circle = circle[-cp:] + circle[:(len(circle) - cp) % len(circle)]
        cp = (cp + x + skip_size) % len(circle)
        skip_size += 1

dense_hash = []

for i in range(16):
    dense_hash.append(reduce(lambda a, b: a ^ b, circle[16 * i:16 * (i + 1)]))

hash = ''
for c in dense_hash:
    hash += f'{hex(c)[2:]:>02}'

print(hash)

print(time.time() - start_time)
