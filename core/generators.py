from random import randint

def gen(N):
    for i in range(N):
        yield randint(1, 100)

gen_expr = (randint(1, 100) for i in range(N))