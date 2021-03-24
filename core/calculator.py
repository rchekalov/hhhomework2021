from decorators import cache_decorator
import time


@cache_decorator
def calculator(a, b, operation):
    # Здесь нужно реализовать функцию,
    # которая реализует основные арифметические операции
    # между числами: +, -, /, *, **.
    # Так же следует сделать проверку, что поступивший оператор
    # корректен (присутствует в этом списке +, -, /, *, **)

    if operation == 'sum' or operation == '+':
        return a + b
    elif operation == 'min' or operation == '-':
        return a - b
    elif operation == 'del' or operation == '/':
        if b == 0:
            raise ValueError('Вам не стоит делить на ноль')
        return a / b
    elif operation == 'mul' or operation == '*':
        return a * b
    elif operation == 'mod' or operation == '**':
        return a ** b
    else:
        raise Exception('Я старалась найти эту функцию, но не смогла :(')


if __name__ == '__main__':
    try:
        a = int(input('Введите число: '))
        # Тут было бы неплохо обрабатывать ошибку в случае
        # передачи некорректных символов
        b = int(input('Введите число: '))
        operation = input('Введите операцию: ')
        start_time = time.time()
        print('Результат: ', calculator(a, b, operation))
        print("--- %s seconds ---" % (time.time() - start_time))
    except ValueError as ve:
        print('Ну и ну! Вы ввели некорректные значения!')
        print(ve)
    except Exception as e:
        print('Ну и ну! Вам нельзя таким заниматься!')
        print(e)
