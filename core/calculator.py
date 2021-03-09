from decorators import cache_decorator

@cache_decorator
def calculator(a, b, operation):
    """
    Здесь нужно реализовать функцию, которая реализует основные арифметические операции между числами: +, -, /, *, **.
    Так же следует сделать проверку, что поступивший оператор корректен (присутствует в этом списке +, -, /, *, **)

    :param a: int
    :param b: int
    :param operation: str "+, -, /, *, **"
    :return: mixed
    """

    if (operation == '+'):
        return a + b
    elif (operation == '-'):
        return a - b
    elif (operation == '/'):
        return a / b
    elif (operation == '*'):
        return a * b
    elif (operation == '**'):
        return a ** b
    else:
        raise ValueError(f"Операция #[{operation}] не поддерживается. Валидные операции [+, -, /, *, **]");


def inputNumber(label):
    """
    Тут было бы неплохо обрабатывать ошибку в случае передачи некорректных символов
    :param label: str
    :return: int
    """
    while (True):
        try:
            return int(input(f"Введите число {label}: "))
        except ValueError:
            print(f"Значение не принято. Надо ввести число")


if __name__ == '__main__':
    # Почему бы не написать сразу парсер выражений?
    while (True):
        a = inputNumber('a')
        b = inputNumber('b')
        operation = input('Введите операцию: ')
        try:
            print(f"Результат: {a} {operation} {b} =", calculator(a, b, operation))
        except ValueError as e:
            print(e)
        except ZeroDivisionError:
            print("Деление на 0")
        if (input(f"Для продолжения нажми 'y': ") != 'y'):
            break
