import time

start_time = time.time()

with open('input.txt') as f:
    current_state = [int(line.rstrip('\n')) for line in f.readlines()[0].split('\t')]

states = set()
redists = 0


def redistribute(banks):
    largest_index = max(range(len(banks)), key=lambda x: banks[x])

    n = banks[largest_index]

    banks[largest_index] = 0

    for i in range(len(banks)):
        banks[(largest_index + i + 1) % len(banks)] += n // len(banks) + (i < n % len(banks))

    return banks


while tuple(current_state) not in states:
    states.add(tuple(current_state))
    current_state = redistribute(current_state)
    redists += 1


print(redists)
print(time.time() - start_time)
