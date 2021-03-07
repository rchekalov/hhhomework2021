from decorators import cache_decorator

class BadOperationException(Exception):
    pass

@cache_decorator
def calculator(a, b, operation):
    # Здесь нужно реализовать функцию,
    # которая реализует основные арифметические операции между числами: +, -, /, *, **.
    # Так же следует сделать проверку, что поступивший оператор корректен (присутствует в этом списке +, -, /, *, **)
    a = int(a)
    b = int(b)

    if operation not in ("+", "-", "/", "*", "**"):
        raise BadOperationException("Операция введена не верно")
    
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "/":
        return a / b
    elif operation == "*":
        return a * b
    return a ** b


if __name__ == '__main__':
    while True:
        a = input("Введите первое число: ").strip()
        b = input("Введите второе число: ").strip()
        operation = input("Введите операцию (+, -, /, *, **): ").strip()

        try:
            print("Результат: ", calculator(a, b, operation))
        except ValueError:
            print("Число введено не верно")
            continue
        except BadOperationException as e:
            print(f"{e}")
            continue
        except ZeroDivisionError:
            print("Деление на 0")
            continue

        is_exit = input("Чтобы закончить введите q: ")
        if is_exit == 'q':
            break