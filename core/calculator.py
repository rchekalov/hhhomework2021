from decorators import cache_decorator

@cache_decorator
def calculator(a, b, operation):
    # Здесь нужно реализовать функцию,
    # которая реализует основные арифметические операции между числами: +, -, /, *, **.
    # Так же следует сделать проверку, что поступивший оператор корректен (присутствует в этом списке +, -, /, *, **)
    if operation == '+':
        return a + b
    if operation == '-':
        return a - b
    if operation == '*':
        return a * b
    if operation == '/':
        if b == 0:
          raise ValueError("Can't divide by 0")
        return a / b
    if operation == '**':
        return a ** b
    raise ValueError('Undefined operation: {}'.format(operation))

if __name__ == '__main__':
    try:
        a = int(input('Введите число: ')) # Тут было бы неплохо обрабатывать ошибку в случае передачи некорректных символов
        b = int(input('Введите число: '))
        operation = input('Введите операцию ')

        print('Результат: ', calculator(a, b, operation))
    except ValueError as err:
        print(err)
