from decorators import cache_decorator

@cache_decorator
def calculator(a, b, operation):
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
        '**': lambda x, y: x ** y,
    }

    if operation not in operations:
        return 'операция некорректна'
    return operations[operation](a,b)


if __name__ == '__main__':
    try:
        a = int(input('Введите число: '))
        b = int(input('Введите число: '))
    except ValueError:
        print('Это не число.')
    else:
        operation = input('Введите операцию: ')
        print('Результат: ', calculator(a, b, operation))
