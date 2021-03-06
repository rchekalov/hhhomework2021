from decorators import cache_decorator


@cache_decorator
def calculator(__a, __b, __operation):
    if __operation == '+':
        return a + b
    elif __operation == '-':
        return a - b
    elif __operation == '/':
        try:
            return a / b
        except ZeroDivisionError:
            print('Cannot divide by 0')
            exit()
    elif __operation == '*':
        return a * b
    elif __operation == '**':
        return a ** b


def input_int():
    while True:
        try:
            return int(input('Введите число: '))
        except ValueError:
            print('Error. Try again...')


def input_operation():
    while True:
        i = input('Введите операцию: ').strip()
        if i in ('+', '-', '/', '*', '**'):
            return i
        print('Must be "+, -, /, *, **"')


if __name__ == '__main__':
    a = int(input_int())
    b = int(input_int())
    operation = input_operation()

    print('Результат: ', calculator(a, b, operation))
