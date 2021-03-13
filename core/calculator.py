from decorators import cache_decorator

operations = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '/': lambda x, y: x / y,
    '*': lambda x, y: x * y,
    '**': lambda x, y: x ** y,
}


def calculator(a, b, operation):
    # Здесь нужно реализовать функцию,
    # которая реализует основные арифметические операции между числами: +, -, /, *, **.
    # Так же следует сделать проверку, что поступивший оператор корректен (присутствует в этом списке +, -, /, *, **)
    try:
        return operations[operation](a, b)
    except KeyError:
        print('unknown operation')
    except ZeroDivisionError:
        print('division by zero')


def reading_numbers():
    while True:
        try:
            return int(input('enter a natural number: '))
        except ValueError:
            print('this number is not natural')


if __name__ == '__main__':
    a = reading_numbers()  # Тут было бы неплохо обрабатывать ошибку в случае передачи некорректных символов
    b = reading_numbers()
    operation = input('Введите операцию').strip()

    print('Результат: ', calculator(a, b, operation))
