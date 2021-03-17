def cache_decorator(f):
    cache = {}
    def inner(*args):
        if args in cache:
            return cache.get(args)
        value = f(*args)
        cache[args] = value
        return value
    return inner