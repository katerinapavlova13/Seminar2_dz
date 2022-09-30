# 1.Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

number = float(input("Введите число: "))
sum = 0
number = number * 10 ** 4

while number > 0:
    digit = number % 10
    if digit != 0:
        sum = sum + digit
    number = number // 10
print(int(sum))
