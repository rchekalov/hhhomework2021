from decorators import cache_decorator

@cache_decorator
def calculator(a, b, operation):
    # Здесь нужно реализовать функцию,
    # которая реализует основные арифметические операции между числами: +, -, /, *, **.
    # Так же следует сделать проверку, что поступивший оператор корректен (присутствует в этом списке +, -, /, *, **)
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "/" | operation == ":":
        if b == 0:
            return "Деление на 0"
        else:
            return a / b
    elif operation == "*":
        return a * b
    elif operation == "**" | operation == "^":
        return a ** b
    else:
        return "Введен некорректный оператор"

def numInput():
    while True:
        try:
            return int(input('Введите число: '))
        except ValueError:
            print('Некорректное значение')

if __name__ == '__main__':
    flag = 'да'
    while flag=='да':
        a = numInput() # Тут было бы неплохо обрабатывать ошибку в случае передачи некорректных символов
        b = numInput()
        operation = input('Введите операцию')
        print('Результат: ', calculator(a, b, operation))
        #print('Продолжаем? (да/нет)')
        flag=str(input('Продолжаем? (да/нет): '))