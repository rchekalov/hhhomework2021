def cache_decorator(func):
    # Реализовать декоратор который кэширует результаты вызова функции (есть в лекции)
    # Применить для функции calculator (в calculator.py уже есть import функции cache_decorator)
    # Настоятельно прошу написать декоратор руками, а не копировать, т.к. важно запомнить как это работает
	cache = {}
	def inner(*arg, **kwarg):
		if arg not in cache:
			cache[arg] = func(*arg, **kwarg)
		return cache[arg]
	return inner
