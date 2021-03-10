import random

# написать генераторную функцию, которая принимает число N возвращает N рандомных чисел от 1 до 100
def gen(N):
    for i in range(N):
        yield random.randint(1, 100)

# Проверка 
print(list(gen(10)))

# написать генераторное выражение, которое делает то же самое
N = 2
exp = (random.randint(1, 100) for i in range(N))

# Проверка
print(next(exp))
print(next(exp))