import time
def cache_decorator(func):
    cashe = {}
    # Реализовать декоратор который кэширует результаты вызова функции (есть в лекции)
    # Применить для функции calculator (в calculator.py уже есть import функции cache_decorator)
    # Настоятельно прошу написать декоратор руками, а не копировать, т.к. важно запомнить как это работает
    def inner(*args):
        if args in cashe:
            return cashe[args]
        else:
            ans = func(*args)
            cashe[args] = ans
            return ans
    return inner
