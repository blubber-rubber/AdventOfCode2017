import time
from collections import defaultdict

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]


class Program:

    def __init__(self, id):
        self.REGISTERS = defaultdict(int)
        self.REGISTERS['p'] = id
        self.OUTPUTS = []
        self.pointer = 0
        self.pair = None
        self.heard = 0
        self.id = id
        self.funcs = {'snd': self.snd, 'set': self.set, 'add': self.add, 'mul': self.mul, 'jgz': self.jgz,
                      'mod': self.mod, 'rcv': self.rcv}

        self.waiting = False

    def get_value(self, v):
        if v in self.REGISTERS:
            return self.REGISTERS[v]
        return int(v)

    def snd(self, x):
        self.OUTPUTS.append(self.get_value(x))

    def set(self, x, y):
        self.REGISTERS[x] = self.get_value(y)

    def add(self, x, y):
        self.REGISTERS[x] += self.get_value(y)

    def mul(self, x, y):
        self.REGISTERS[x] *= self.get_value(y)

    def mod(self, x, y):
        self.REGISTERS[x] %= self.get_value(y)

    def rcv(self, x):
        if self.waiting:
            # print(self, self.pair)
            raise Exception

        if len(self.pair.OUTPUTS) < self.heard + 1:
            self.waiting = True
            self.pair.run()
            self.waiting = False
        self.REGISTERS[x] = self.pair.OUTPUTS[self.heard]
        self.heard += 1

    def jgz(self, x, y):
        if self.get_value(x) > 0:
            return self.get_value(y)

    def run_to_sound(self, desired_length):
        while len(self.OUTPUTS) < desired_length:
            f, *a = lines[self.pointer].split(' ')
            r = self.funcs[f](*a)
            if r:
                self.pointer += r
            else:
                self.pointer += 1

    def run(self):
        self.run_to_sound(len(self.OUTPUTS) + 1)

    def __str__(self):
        return f'Program {self.id} emitted {len(self.OUTPUTS)} sounds'


p0 = Program(0)
p1 = Program(1)
p0.pair = p1
p1.pair = p0

while True:
    try:
        p0.run()
    except Exception:
        break


print(len(p1.OUTPUTS))
print(time.time() - start_time)
