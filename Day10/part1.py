import time

start_time = time.time()

with open('input.txt') as f:
    lijst = [int(x) for x in f.readlines()[0].rstrip('\n').split(',')]

# lijst = [3, 4, 1, 5]

circle = list(range(256))
cp = 0
skip_size = 0

for x in lijst:
    circle = circle[cp:] + circle[:cp]
    circle[:x] = circle[:x][::-1]
    circle = circle[-cp:] + circle[:(len(circle)-cp)%len(circle)]
    cp = (cp+x + skip_size) % len(circle)
    skip_size += 1

print(circle[0]*circle[1])
print(time.time() - start_time)
