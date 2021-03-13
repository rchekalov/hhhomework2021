from decorators import cache_decorator


@cache_decorator
def calculator(a, b, operation):
    # Здесь нужно реализовать функцию,
    # которая реализует основные арифметические операции между числами: +, -, /, *, **.
    # Так же следует сделать проверку, что поступивший оператор корректен (присутствует в этом списке +, -, /, *, **)
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '/':
        return a / b
    elif operation == '*':
        return a * b
    elif operation == '**':
        return a ** b
    else:
        print('Неизвестная операция: \'{}\''.format(operation))
        pass


def get_number(message):
    while True:
        try:
            n = int(input(message))
            break
        except ValueError:
            print('Некорректный ввод. Попробуйте ещё раз.')
    return n


if __name__ == '__main__':
    a = get_number('Введите первое число: ')
    b = get_number('Введите второе число: ')
    operation = input('Введите операцию (+, -, /, *, **): ')

    print('Результат: ', calculator(a, b, operation))
