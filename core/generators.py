from random import randrange
# написать генераторную функцию, которая принимает число N возвращает N рандомных чисел от 1 до 100
def gen(N):
    for i in range(N):
        yield randrange(1,100)

# написать генераторное выражение, которое делает то же самое
N = 5
gen_expr = (randrange(1, 100) for i in range(N))