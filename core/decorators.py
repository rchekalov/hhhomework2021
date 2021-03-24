def cache_decorator(function):
    # Реализовать декоратор который кэширует результаты вызова функции (есть в лекции)
    # Применить для функции calculator
    # (в calculator.py уже есть import функции cache_decorator)
    # Настоятельно прошу написать декоратор руками, а не копировать,
    # т.к. важно запомнить как это работает
    cache = {}

    def num_searcher(*numbers):
        if numbers in cache:
            return cache.get(numbers)
        new_cached_value = function(*numbers)
        cache[numbers] = new_cached_value
        return new_cached_value
    return num_searcher
