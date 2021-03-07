from decorators import cache_decorator

@cache_decorator
def calculator(a, b, operation):
    # Здесь нужно реализовать функцию,
    # которая реализует основные арифметические операции между числами: +, -, /, *, **.
    # Так же следует сделать проверку, что поступивший оператор корректен (присутствует в этом списке +, -, /, *, **)
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
		return "operation is not valid"

if __name__ == '__main__':
	try:
		a = int(input('Введите число: ')) # Тут было бы неплохо обрабатывать ошибку в случае передачи некорректных символов
		b = int(input('Введите число: '))
	except ValueError:
		print("Это не правильный ввод. Это не число вообще! Это строка, попробуйте еще раз.")
	operation = input('Введите операцию')
	print('Результат: ', calculator(a, b, operation))
