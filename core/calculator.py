from decorators import cache_decorator


@cache_decorator
def calculator(a: float, b: float, operation):
    try:
        operation_result = eval(f'{a} {operation} {b}')
    except ZeroDivisionError:
        operation_result = "Division by zero is not allowed"
    return operation_result


def input_and_check_num():
    num = input('Enter number: ')
    try:
        num = float(num)
    except ValueError:
        print(f'Error. "{num}" is not a number. Try again..')
        return input_and_check_num()
    return num


def input_and_check_operation():
    operation = input('Enter operation: ')
    allowed_operations = ['+', '-', '/', '*', '**']
    while operation not in allowed_operations:
        operation = input('Incorrect. Supported operations: +, -, /, *, **.\nEnter the operation again: ')
    return operation


def main():
    print("This is simple calculator.\n"
          "Supported operations: +, -, /, *, **\n")
    a = input_and_check_num()
    b = input_and_check_num()
    operation = input_and_check_operation()
    result = calculator(a, b, operation)
    print(f'Result: {result}')


if __name__ == '__main__':
    main()
