from decorators import cache_decorator

@cache_decorator
def calculator(a, b, operation):
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
        return 'некорректный оператор'

def GetValue():
    while True:
        sentence = input('Введите число: ')

        try:
            value = int(sentence)
        # Если полученный ввод не число, будет вызвано исключение
        except ValueError:
            # Цикл будет повторяться до правильного ввода
            print("Error! Это не число, попробуйте снова.")
        else:
            return value

if __name__ == '__main__':
    a = GetValue()
    b = GetValue()
    operation = input('Введите операцию ')

    print('Результат: ', calculator(a, b, operation))
