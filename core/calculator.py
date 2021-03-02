from decorators import cache_decorator

def get_numeric_value():
    while True:
        try:
            return int(input('Введите число: '))
        except Exception as e:
            print("Invalid numeric value. Try again")


def get_operation():
    while True:
        operation = input('Введите операцию: ').strip()
        if operation in ('+', '-', '/', '*', '**'):
            return operation
        print("Invalid numeric value. Try again")

    
def terminate_programm():
    while True:
        decision = input("Continue? [y/n] ")
        if decision == 'y':
            return False
        elif decision == 'n':
            return True

@cache_decorator
def calculator(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "/":
        if b == 0:
            return "inf"
        return a / b
    elif operation == "*":
        return a * b
    return a ** b


if __name__ == '__main__':
    while True:
        a = get_numeric_value()
        b = get_numeric_value()
        operation = get_operation()
        print('Результат: ', calculator(a, b, operation))
        if terminate_programm():
            break
        