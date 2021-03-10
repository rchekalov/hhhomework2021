from decorators import cache_decorator

def bad_op():
    raise Exception("Неверная операция")

dict_operation = {
    '+': lambda x, y: x + y,
    '*': lambda x, y: x * y,
    '-': lambda x, y: x - y,
    '/': lambda x, y: x / y,
    '**': lambda x, y: x ** y,
}

@cache_decorator
def calculator(a, b, operation):
    # Здесь нужно реализовать функцию,
    # которая реализует основные арифметические операции между числами: +, -, /, *, **.
    # Так же следует сделать проверку, что поступивший оператор корректен (присутствует в этом списке +, -, /, *, **)
    print(dict_operation[operation](a, b))
    a = dict_operation[operation](a, b)
    return a


if __name__ == '__main__':
    a = int(input('Введите число: ')) # Тут было бы неплохо обрабатывать ошибку в случае передачи некорректных символов
    b = int(input('Введите число: '))
    operation = input('Введите операцию: ')

    print('Результат: ', calculator(a, b, operation))