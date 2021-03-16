from random import randint
# написать генераторную функцию, которая принимает число N возвращает N рандомных чисел от 1 до 100

def gen(N):
    count = N     
    while count > 0:
        yield randint(0, 100)
        count -= 1
            
# написать генераторное выражение, которое делает то же самое
N = 5
gen2 = (randint(0, 100) for _ in range(N))
