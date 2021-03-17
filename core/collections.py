not_even_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
def even(some_not_even_list):
  return [elem for elem in some_not_even_list if elem % 2 == 0]

years_of_birth = [1990, 1991, 1990, 1990, 1992, 1991]
def get_ages(some_years_of_birth):
  return [2014 - year for year in some_years_of_birth]

numbers = [5, 10, 15, 20, 25]
def get_first_n_last(some_list):
  return [numbers[0], numbers[len(numbers) - 1]]

list_with_repetition = [1, 1, 3, 4, 2, 2, 2, 6]
def get_list_without_repetition(some_list):
  unique_elem = set()
  list_without_repetition = []
  for elem in some_list:
    if elem not in unique_elem:
      list_without_repetition.append(elem)
      unique_elem.add(elem)
  return list_without_repetition

keys = ['red', 'green', 'blue']
values = ['#FF0000', '#00FF00', '#0000FF']
def map_keys_and_values(some_keys, some_values):
  color_keys = {}
  for i in range(len(some_keys)):
    color_keys[keys[i]] = some_values[i]
  return color_keys

s = 'some string'
def count_symbols(some_string):
  counter = {}
  for elem in some_string:
    if elem != ' ':
      counter[elem] = counter.get(elem, 0) + 1
  return counter
