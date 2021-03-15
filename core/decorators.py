def cache_decorator(any_function):
    # Реализовать декоратор который кэширует результаты вызова функции (есть в лекции)
    # Применить для функции calculator (в calculator.py уже есть import функции cache_decorator)
    # Настоятельно прошу написать декоратор руками, а не копировать, т.к. важно запомнить как это работает
    cache = {}
    def wrapper(*args):
        if args not in cache:
            print('miss')
            val = any_function(*args)
            cache[args] = val
        else:
            print('hit')
            val = cache.get(args)
        return val

    return wrapper

@cache_decorator
def func(a,b):
    return a + b

if __name__ == '__main__':
    print(func(2, 5))
    print(func(2, 3))
    print(func(1, 3))
    print(func(2, 5))
    print(func(3, 4))
    print(func(3, 1))
    print(func(1, 3))
