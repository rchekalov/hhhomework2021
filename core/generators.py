# написать генераторную функцию, которая принимает число N возвращает N рандомных чисел от 1 до 100
import random

def gen(N):
    for i in range(N):
        yield random.randint(1, 100)
    
# написать генераторное выражение, которое делает то же самое
my_generator = (random.randint(1, 100) for i in range(4))

    