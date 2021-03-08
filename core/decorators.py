import functools


def cache_decorator(func):
    # Реализовать декоратор который кэширует результаты вызова функции (есть в лекции)
    # Применить для функции calculator (в calculator.py уже есть import функции cache_decorator)
    # Настоятельно прошу написать декоратор руками, а не копировать, т.к. важно запомнить как это работает
    cache_dict = {}

    @functools.wraps(func)
    def inner(*args, **kwargs):
        if args not in cache_dict:
            cache_dict[args] = func(*args, **kwargs)
        return cache_dict[args]
    return inner
