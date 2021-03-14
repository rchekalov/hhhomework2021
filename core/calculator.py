from decorators import cache_decorator


@cache_decorator
def calculator(a, b, operation):
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
        print('Enter a valid operator, please run the program again.')


if __name__ == '__main__':
    a = int(input('Введите число: '))  # Тут было бы неплохо обрабатывать ошибку в случае передачи некорректных символов
    b = int(input('Введите число: '))
    operation = input('Введите операцию')

    print('Результат: ', calculator(a, b, operation))
