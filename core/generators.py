# написать генераторную функцию, которая принимает число N возвращает N рандомных чисел от 1 до 100
from random import randint


def gen(N):
    while N > 0:
        yield randint(1, 100)
        N -= 1
    pass


# написать генераторное выражение, которое делает то же самое
gen_expr = (randint(1, 100) for i in range(N))
