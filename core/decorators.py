def cache_decorator(func):
    cache = {}

    def inner(*args):
        if args in cache:
            return cache[args]
        else:
            value = func(*args)
            cache[args] = value
            return value
    return inner
