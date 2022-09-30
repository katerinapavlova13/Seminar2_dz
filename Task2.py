# 2.Напишите программу, которая принимает на вход число N и
# выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4 -> [1, 2, 6, 24]
#         N = 6 -> [1, 2, 6, 24, 120, 720]

number = int(input("Введите число: "))
list = []
factorial = 1
for i in range(1, number + 1):
    factorial = factorial * i
    list.append(factorial)

print("Факториал числа ", number, " равен: ", factorial)

print(list)





