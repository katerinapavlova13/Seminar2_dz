# 1.Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

number = float(input("Введите вещественное число: "))

summa = 0
number = number * 10 ** 4

while number > 0:
    digit = number % 10
    if digit != 0:
        summa = summa + digit
    number = number // 10

print(int(summa))



# def float_int(number_b: float) -> int:
#     magic = int(1)
#     temp = float(number_b)
#     while not temp.is_integer():
#         temp = number_b * magic
#     return int(temp)
#
# def get_sum(number_a):
#     no_point_num = float_int(number_a)
#     no_point_num = abs(no_point_num)
#     sum = 0
#     while no_point_num > 0:
#         sum += no_point_num % 10
#         no_point_num //= 10
#     return sum
#
# print(get_sum(number))

