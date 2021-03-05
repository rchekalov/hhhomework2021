# Есть список not_even_list, реализовать логику в функции even: создать новый список с четными элементами из списка not_even_list
not_even_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Я подумал, что для функции логичнее обрабатывать аргумент, а не глобальную переменную. Надеюсь, ты просто
# забыл добавить 'some_' в предыдущем комментарии. Если нет, то напиши - исправлю.
def even(some_not_even_list):
  return [elem for elem in some_not_even_list if elem % 2 == 0]

years_of_birth = [1990, 1991, 1990, 1990, 1992, 1991]
def get_ages(some_years_of_birth):
  # Мы в 2014? :)
  return [2014 - year for year in some_years_of_birth]

numbers = [5, 10, 15, 20, 25]
def get_first_n_last(some_list):
  return [some_list[0], some_list[-1]]

list_with_repetition = [1, 1, 3, 4, 2, 2, 2, 6]
def get_list_without_repetition(some_list):
  return list(set(some_list))

keys = ['red', 'green', 'blue']
values = ['#FF0000', '#00FF00', '#0000FF']
def map_keys_and_values(some_keys, some_values):
  return {key:value for key, value in zip(some_keys, some_values)}

s = 'some string'
def count_symbols(some_string):
  return {symbol:some_string.count(symbol) for symbol in set(some_string)}
