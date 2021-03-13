from random import randint

# написать генераторную функцию, которая принимает число N возвращает N рандомных чисел от 1 до 100
def gen(N):
    for i in range(0, N):
        yield randint(1, 100)

# написать генераторное выражение, которое делает то же самое
N = 10
gen_expression = (randint(1, 100) for i in range(0, N))
