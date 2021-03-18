import random


# написать генераторную функцию, которая принимает число N возвращает N рандомных чисел от 1 до 100
def gen(n):
    for _ in range(n):
        yield random.randint(1, 100)


# написать генераторное выражение, которое делает то же самое
m = random.randint(1, 10)
generator = (random.randint(1, 100) for _ in range(m))
