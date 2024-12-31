import time
from tqdm import tqdm

start_time = time.time()

MOD = 2147483647
m = 2 ** 16


class Generator:

    def __init__(self, start_value, multiplier, condition):
        self.V = start_value
        self.M = multiplier
        self.C = condition

    def __next__(self):
        self.V = (self.V * self.M) % MOD
        while self.V % self.C != 0:
            self.V = (self.V * self.M) % MOD
        return self.V % m


VA = 618
VB = 814

MA = 16807
MB = 48271

GA = Generator(VA, MA, 4)
GB = Generator(VB, MB, 8)
count = 0

for _ in tqdm(range(5_000_000)):
    cA = next(GA)
    cB = next(GB)
    count += (cA == cB)

print(count)
print(time.time() - start_time)
