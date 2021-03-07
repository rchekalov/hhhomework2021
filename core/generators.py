from random import randint

# написать генераторную функцию, которая принимает число N возвращает N рандомных чисел от 1 до 100
def gen(N):
    while N > 0:
        yield randint(0, 100)
        N -= 1

# написать генераторное выражение, которое делает то же самое
gen = (randint(0, 100) for i in range(N))