# написать генераторную функцию, которая принимает число N возвращает N рандомных чисел от 1 до 100
from random import randint


def gen(N):
    for i in range(N):
        yield randint(1, 100)


# написать генераторное выражение, которое делает то же самое
rand_gen = (randint(1, 100) for i in range(2))


if __name__ == '__main__':
    g = gen(3)
    print(next(g))
    print(next(g))
    print(next(g))
    # print(next(g)) # will cause StopIteration

    print('')

    print(next(rand_gen))
    print(next(rand_gen))
    # print(next(rand_gen)) # will cause StopIteration

