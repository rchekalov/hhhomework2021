import random


# написать генераторную функцию, которая принимает число N возвращает N рандомных чисел от 1 до 100
def gen(N):
    for _ in range(N):
        yield random.randint(1, 100)


# написать генераторное выражение, которое делает то же самое
n = 50
gen_expr = (random.randint(1, 100) for _ in range(n))
