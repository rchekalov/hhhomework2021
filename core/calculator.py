from decorators import cache_decorator

calc_operations = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '/': lambda x, y: x / y,
    '*': lambda x, y: x * y,
    '**': lambda x, y: x ** y,
}


@cache_decorator
def calculator(a, b, operation):
    return calc_operations[operation](a, b)


def read_int():
    while True:
        try:
            return int(input('Введите число: '))
        except ValueError:
            print('Надо было число вводить, камон')


def read_operation():
    while True:
        try:
            operation = input('Введите операцию: ')
            if (operation in calc_operations):
                return operation
            else:
                raise KeyError()
        except KeyError:
            print('Попробуй снова, но с валидно математической опрерацией')


if __name__ == '__main__':
    a = read_int()
    b = read_int()
    operation = read_operation()

    print('Результат: ', calculator(a, b, operation))
