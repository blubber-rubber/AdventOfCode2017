from collections import Counter

import time

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

n_passphrases = 0
for line in lines:
    if all(c == 1 for c in Counter(["".join(sorted(x for x in word)) for word in line.split(' ')]).values()):
        n_passphrases += 1

print(n_passphrases)
print(time.time() - start_time)
