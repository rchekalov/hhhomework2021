def cache_decorator(function):
    # Реализовать декоратор который кэширует результаты вызова функции (есть в лекции)
    # Применить для функции calculator (в calculator.py уже есть import функции cache_decorator)
    # Настоятельно прошу написать декоратор руками, а не копировать, т.к. важно запомнить как это работает
    cache = {}
    def inner_cache(*args):
        if args in cache:
            return cache.get(args)
        value = function(*args)
        cache[args] = value
        return value
    return inner_cache
