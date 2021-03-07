from random import randint

# написать генераторную функцию, которая принимает число N возвращает N рандомных чисел от 1 до 100
def gen(N):
    for _ in range(N):
        yield randint(1, 100)

# написать генераторное выражение, которое делает то же самое
gen_expr = (randint(1, 100) for _ in range(N))
