# Есть список not_even_list, реализовать логику в функции even: создать новый список с четными элементами из списка not_even_list
not_even_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

def even(some_not_even_list):
  return list(filter(lambda x: x % 2 == 0, some_not_even_list))

# Следующий код с циклом, переписать с использованием спискового включения (list comprehension)
years_of_birth = [1990, 1991, 1990, 1990, 1992, 1991]
def get_ages(some_years_of_birth):
  # ages = []
  # for year in some_years_of_birth: 
  #   ages.append(2014 - year)
  def get_age(year):
    return 2014 - year
  ages = [get_age(year) for year in some_years_of_birth]
  return ages

# Есть список numbers, реализовать логику в функции get_first_n_last: вернуть новый список состоящий из первого и последнего элемента переданного списка
numbers = [5, 10, 15, 20, 25]
def get_first_n_last(some_list):
  return [some_list[0],some_list[-1]]

# Написать функцию, которая принимает список и возвращает новый список, состоящий из элементов принятого, но без повторений
list_with_repetition = [1, 1, 3, 4, 2, 2, 2, 6]
def get_list_without_repetition(some_list):
  return list(set(some_list))

# Написать функцию, которая возвращает словарь, ключи которого из списка keys, а значения из списка values
keys = ['red', 'green', 'blue']
values = ['#FF0000', '#00FF00', '#0000FF']
def map_keys_and_values(some_keys, some_values):
  Colors = dict()
  for i in range(len(keys)):
    Colors[some_keys[i]] = some_values[i]
  return Colors

# Написать функцию, которая принимает строку и возвращает словарь состоящий из ключей - символов из строки, значений - количество повторений этих символов в строке
s = 'some string'
def count_symbols(some_string):
  return {i: some_string.count(i) for i in some_string}