first = float(input("введите первое число: "))
znak = input("введите команду(+, -, /, * ): ")
second = float(input("введите второе число: "))

if znak == "*":
	third = first * second
	print("Результат: " + str(third))

elif znak == "/":
	third = second / first
	print("Результат: " + str(third))

elif znak == "+":
	third = first + second
	print("Результат: " + str(third))

elif znak == "-":
	third = first - second
	print("Результат: " + str(third))

else:
	print("Результат: неверная операция")

input()