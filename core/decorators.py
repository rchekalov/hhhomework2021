# Реализовать декоратор который кэширует результаты вызова функции
def cache_decorator(function):
    memo = {}

    def wrapper(*args):
        if args in memo:
            return memo[args]
        else:
            rv = function(*args)
            memo[args] = rv
            return rv

    return wrapper
