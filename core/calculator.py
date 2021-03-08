from decorators import cache_decorator

operations_enum = {
    '+': 0,
    '-': 1,
    '/': 2,
    '*': 3,
    '**': 4
}

def calculator(a, b, operation):
    # Здесь нужно реализовать функцию,
    # которая реализует основные арифметические операции между числами: +, -, /, *, **.
    # Так же следует сделать проверку, что поступивший оператор корректен (присутствует в этом списке +, -, /, *, **)
    try:
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
            raise Exception("operation {} not supported".format(operation))
    except:
        print()

def read_number(name = ""):
    while True:
        try:
            s = int(input("Введите число {}: ".format(name)))
            return s
        except Exception:
            print("Вы ввели недопустимые символы: {}. Попробуйте еще раз".format(name))

def read_operation():
    while True:
        try:
            oper = input("Введите операцию: ")
            if operations_enum.get(oper) is not None:
                return oper
        except Exception:
                print("Операция {} не поддерживается. \r\nКоманды +, -, /, *, **".format(oper))

if __name__ == '__main__':
    # Тут было бы неплохо обрабатывать ошибку в случае передачи некорректных символов
    a = read_number("a")
    b = read_number("b")
    operation = read_operation()

    print("Результат операции a {} b = ".format(operation), calculator(a, b, operation))
