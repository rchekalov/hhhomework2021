import random


# написать генераторную функцию, которая принимает число N возвращает N рандомных чисел от 1 до 100
def gen(N):
    for _ in range(N):
        yield random.randint(1, 100)


# написать генераторное выражение, которое делает то же самое
gen_lim = 5
my_gen = (random.randint(1, 100) for i in range(gen_lim))


if __name__ == '__main__':
    for i in gen(5):
        print(i)

    print('')

    for i in my_gen:
        print(i)
