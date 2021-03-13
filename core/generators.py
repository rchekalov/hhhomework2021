# написать генераторную функцию, которая принимает число N возвращает N рандомных чисел от 1 до 100
from random import randint


def gen(N):
    for i in range(N):
        yield randint(1, 100)


# написать генераторное выражение, которое делает то же самое
N = int(input())
gen_random_val = (randint(1, 100) for _ in range(N))
