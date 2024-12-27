import time

start_time = time.time()

with open('input.txt') as f:
    captcha = [int(x) for x in f.readline().rstrip('\n')]

sol = 0
for c1, c2 in zip(captcha, captcha[len(captcha) // 2:] + captcha[:len(captcha) // 2]):
    sol += (c1 == c2) * c1

print(sol)
print(time.time() - start_time)
