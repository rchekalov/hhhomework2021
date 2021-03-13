from decorators import cache_decorator

@cache_decorator
def calculator(a, b, operation):
    # Здесь нужно реализовать функцию,
    # которая реализует основные арифметические операции между числами: +, -, /, *, **.
    # Так же следует сделать проверку, что поступивший оператор корректен (присутствует в этом списке +, -, /, *, **)
    ops = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '/': lambda a, b: a / b,
        '*': lambda a, b: a * b,
        '**': lambda a, b: a ** b
    }
    if operation in ops:
        return ops[operation](a, b)
    else:
        raise ValueError


if __name__ == '__main__':
    while True:
        try:
            a = int(input('Введите число: '))
            b = int(input('Введите число: '))
            operation = input('Введите операцию: ')

            print('Результат: ', calculator(a, b, operation))
        except ZeroDivisionError:
            print('Делить на ноль нельзя')
        except ValueError as err:
            print('Ошибка ввода')
