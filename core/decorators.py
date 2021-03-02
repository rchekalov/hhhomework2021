from collections import defaultdict

def cache_decorator(func):
    cache = {}
    def inner_function(*args):
        if cache.get(args) == None:
            cache[args] = func(*args)
        return cache[args]
    return inner_function
