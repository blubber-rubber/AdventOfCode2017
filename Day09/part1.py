import time
import re

start_time = time.time()

with open('input.txt') as f:
    line = [line.rstrip('\n') for line in f.readlines()][0]

n_garbage = 0
for garbage in re.finditer('<([^!>]|!.)*>', line):
    garbage = garbage.group()[1:-1]
    n_garbage += len([s for s in re.findall('([^!]|!.)', garbage) if s[0] != '!'])


print(n_garbage)
