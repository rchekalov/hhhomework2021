from decorators import cache_decorator

@cache_decorator
def calculator(a, b, operation):
    # Здесь нужно реализовать функцию,
    # которая реализует основные арифметические операции между числами: +, -, /, *, **.
    # Так же следует сделать проверку, что поступивший оператор корректен (присутствует в этом списке +, -, /, *, **)

    if operation in ['+', '-', '/', '*', '**']:
        if operation == '+':
            return a + b
        elif operation == '-':
            return a - b
        elif operation == '/':
            return a / b
        elif operation == '*':
            return a * b
        else:
            return a ** b
    else: return 'Поступивший оператор некорректен'


if __name__ == '__main__':
    while True:
        a = input('Введите число: ') # Тут было бы неплохо обрабатывать ошибку в случае передачи некорректных символов
        b = input('Введите число: ')
        if a.isdigit() and b.isdigit():
            break
        print('Были введены не числа, попробуйте еще раз')
    a = int(a)
    b = int(b)
    operation = input('Введите операцию: ')

    print('Результат: ', calculator(a, b, operation))