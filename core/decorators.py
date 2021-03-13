def cache_decorator(func):
  cache = {}
  def inner(*args, **kwargs):
    if args not in cache:
      cache[args] = func(*args, **kwargs)
    return cache[args]
  return inner
