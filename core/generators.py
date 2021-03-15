# написать генераторную функцию, которая принимает число N возвращает N рандомных чисел от 1 до 100
from random import randint

def gen(N):
    for i in range(N):
        yield randint(1, 100)

def numInput():
    while True:
        try:
            return int(input('Введите число N: '))
        except ValueError:
            print('Некорректное значение')

if __name__ == '__main__':
    N = numInput()
    for i in gen(N):
        print(i)

    # написать генераторное выражение, которое делает то же самое
    n = numInput()
new_generator = (randint(1, 100) for i in range(n))

for i in new_generator:
    print(i)