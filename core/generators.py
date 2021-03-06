import random


# написать генераторную функцию, которая принимает число N возвращает N рандомных чисел от 1 до 100
def gen(n):
    rand = []
    for i in range(n):
        rand.append(random.randint(1, 100))
    yield rand


# написать генераторное выражение, которое делает то же самое
num = 10
[random.randint(1, 100) for _ in range(num)]
