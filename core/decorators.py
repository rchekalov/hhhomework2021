def cache_decorator(func):
    """
    Реализовать декоратор который кэширует результаты вызова функции (есть в лекции)
    Применить для функции calculator (в calculator.py уже есть import функции cache_decorator)
    Настоятельно прошу написать декоратор руками, а не копировать, т.к. важно запомнить как это работает
    """

    cache = {}

    def inner(*args):
        print(cache)
        cached_item = cache.get(args, None)
        if cached_item is None:
            print("запись в кэш")
            cache[args] = func(*args)
        return cache[args]

    return inner
