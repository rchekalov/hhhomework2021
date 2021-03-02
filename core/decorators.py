from collections import defaultdict

def cache_decorator(func):
    cache = {}
    def inner_function(*args):
        if cache.get(tuple(args)) == None:
            cache[tuple(args)] = func(*args)
        return cache[tuple(args)]
    return inner_function