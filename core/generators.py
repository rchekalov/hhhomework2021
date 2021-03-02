import random

def gen(N):
    for i in range(N):
        yield random.randint(1, 100)

N = 100
g = (random.randint(1, 100) for _ in range(N))