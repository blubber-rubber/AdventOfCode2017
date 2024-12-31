import time
from tqdm import tqdm

start_time = time.time()

with open('input.txt') as f:
    step_size = int(f.readline())

buffer_length = 1
cp = 0
after_zero = None
for value in tqdm(range(1, 50_000_000 + 1)):
    cp = (cp + step_size) % buffer_length
    if cp == 0:
        after_zero = value

    cp += 1
    buffer_length += 1

print(after_zero)
