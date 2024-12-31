import time

start_time = time.time()

with open('input.txt') as f:
    step_size = int(f.readline())

circular_buffer = [0]
cp = 0
for value in range(1, 2018):
    cp = (cp + step_size) % len(circular_buffer)
    cp += 1
    circular_buffer.insert(cp, value)

print(circular_buffer[(cp + 1) % len(circular_buffer)])
print(time.time() - start_time)
