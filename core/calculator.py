from decorators import cache_decorator

operations = {"+" : lambda a,b : a + b, 
"-": lambda a,b : a - b, 
"/": lambda a,b : a / b, 
"*": lambda a,b : a*b, 
"**": lambda a,b : a**b}

@cache_decorator
def calculator(a, b, operation):
    # Здесь нужно реализовать функцию,
    # которая реализует основные арифметические операции между числами: +, -, /, *, **.
    # Так же следует сделать проверку, что поступивший оператор корректен (присутствует в этом списке +, -, /, *, **)
    if operation not in operations:
        raise Exception('Invalid operation')
    return operations[operation](a, b)


if __name__ == '__main__':
    try:
        a = int(input('Введите число: ')) # Тут было бы неплохо обрабатывать ошибку в случае передачи некорректных символов
        b = int(input('Введите число: '))
    except ValueError:
        raise ValueError('Invalid argument')

    operation = input('Введите операцию: ')

    print('Результат:', calculator(a, b, operation))