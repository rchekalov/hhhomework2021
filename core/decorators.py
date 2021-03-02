from collections import defaultdict

def cache_decorator(func):
    cache = {}
    def inner_function(*args, **kwargs):
        sorted_kwargs = {key: kwargs[key] for key in sorted(kwargs.keys())}
        if cache.get(str([args, sorted_kwargs])) == None:
            cache[str([args, sorted_kwargs])] = func(*args, **kwargs)
        else:
            print("Cached")
        return cache[str([args, sorted_kwargs])]
    return inner_function
