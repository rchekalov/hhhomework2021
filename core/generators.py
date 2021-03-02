import random

def gen(N):
    for _ in range(N):
        yield random.uniform(1, 100)

(random.uniform(1, 100) for _ in range(N))
