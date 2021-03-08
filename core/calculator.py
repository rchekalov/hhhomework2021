from decorators import cache_decorator
import operator

OPERATIONS = {
    '+': operator.add,
    '-': operator.sub,
    '/': operator.floordiv,
    '*': operator.mul,
    '**': operator.pow
}


@cache_decorator
def calculator(a, b, operation):
    # Здесь нужно реализовать функцию,
    # которая реализует основные арифметические операции между числами: +, -, /, *, **.
    # Так же следует сделать проверку, что поступивший оператор корректен (присутствует в этом списке +, -, /, *, **)
    return OPERATIONS.get(operation)(a, b)


def main():
    try:
        a = int(input('Введите число: '))  # Тут было бы неплохо обрабатывать ошибку в случае передачи некорректных символов
        b = int(input('Введите число: '))
    except ValueError:
        print('Некорректное число')
        return 1

    operation = input('Введите операцию: ')
    if operation not in OPERATIONS:
        print('Некорректная операция. Поддерживаемые операции: +, -, /, *, **')
        return 1

    print('Результат: {}'.format(calculator(a, b, operation)))


if __name__ == '__main__':
    while True:
        main()
