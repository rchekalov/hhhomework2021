from decorators import cache_decorator

operations = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '/': lambda x, y: x / y,
    '*': lambda x, y: x * y,
    '**': lambda x, y: x ** y,
}

@cache_decorator
def calculator(a, b, operation):
    try:
        return operations[operation](a, b)
    except KeyError:
        print('Неверная операция')
    except ZeroDivisionError:
        print('Деление на ноль')

def read_int():
    while True:
        try:
            return int(input('Введите целое число: '))
        except ValueError:
            print('Неверное целое число')

if __name__ == '__main__':
    while True:
        a = read_int()
        b = read_int()
        operation = input('Введите операцию (+, -, /, *, **): ').strip()

        print('Результат:', calculator(a, b, operation))
