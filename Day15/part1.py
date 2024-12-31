import time
from tqdm import tqdm

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

VA = 618
VB = 814

MA = 16807
MB = 48271

M = 2147483647
m = 2 ** 16

count = 0

for _ in tqdm(range(40_000_000)):
    VA = (VA * MA) % M
    VB = (VB * MB) % M
    cA = VA % m
    cB = VB % m
    count += (cA == cB)

print(count)
print(time.time() - start_time)
