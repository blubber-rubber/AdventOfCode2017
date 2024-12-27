import time

start_time = time.time()

with open('input.txt') as f:
    number = [int(line.rstrip('\n')) for line in f.readlines()][0]



def get_position(number):
    n = int(number ** (1 / 2))

    remaining_steps = number - n ** 2

    if n % 2 == 0:
        pos = [-(n // 2 - 1), -(n // 2)]

        if remaining_steps > 0:
            pos[0] -= 1
            remaining_steps -= 1
            dirs = [(0, 1), (1, 0)]


    else:
        pos = [(n // 2), (n // 2)]
        if remaining_steps > 0:
            pos[0] += 1
            remaining_steps -= 1

        dirs = [(0, -1), (-1, 0)]

    index = 0
    while remaining_steps > 0:
        counter = 0
        dx, dy = dirs[index]
        while counter < n and remaining_steps > 0:
            counter += 1
            pos[0] += dx
            pos[1] += dy
            remaining_steps -= 1
        index = 1

    return pos


pos = get_position(number)
print(sum(abs(x) for x in pos))

print(time.time() - start_time)
