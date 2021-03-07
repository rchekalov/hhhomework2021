import functools


def cache_decorator(func):
    cache = {}

    @functools.wraps(func)
    def wrapped(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrapped
