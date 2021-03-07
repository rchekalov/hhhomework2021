from core.decorators import cache_decorator
import operator

OPERATIONS = {
    '+': operator.add,
    '-': operator.sub,
    '/': operator.truediv,
    '*': operator.mul,
    '**': operator.pow,
}


@cache_decorator
def calculator(a, b, operation):
    if operation not in OPERATIONS:
        raise ValueError('Unknown operation. Valid operations are: %s' % OPERATIONS.keys())
    return OPERATIONS[operation](a, b)


if __name__ == '__main__':
    try:
        a = int(input('Введите число: '))
        b = int(input('Введите число: '))
    except ValueError:
        print('invalid number, please try again')
        exit(1)

    operation = input('Введите операцию: ')

    print('Результат: ', calculator(a, b, operation))
