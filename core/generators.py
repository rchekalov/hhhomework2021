import random

# написать генераторную функцию, которая принимает число N возвращает N рандомных чисел от 1 до 100
def gen(N):
    for i in range(N):
        yield random.randint(1, 100)
    pass

for i in gen(100):
    print(i)

# написать генераторное выражение, которое делает то же самое
ans = [random.randint(1, 100) for _ in range(100)]
print(ans)