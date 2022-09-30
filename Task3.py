# 3. Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
# Для n = 6: [2, 2, 2, 2, 2, 3] -> 13

number = int(input("Введите число: "))
list = []

for i in range(1, number + 1):
    list.append(round((1 + 1 / i) ** i))

sum = 0
for i in range(number):
    sum = sum + list[i]

print("Для числа", number, ":",list ,"сумма чисел в списке ->", sum)