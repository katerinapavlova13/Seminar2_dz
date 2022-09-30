# 4.Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.

import random

n = int(input("Введите размер списка: "))
numbers = []
for i in range(1, n + 1):
    numbers.append(random.randint(-10, 10))

print(numbers)

list = []

with open("file.txt", "r") as data:
    list = data.read().split("\n")

average = numbers[int(list[0])] * numbers[int(list[7])]

print(f"Приизведение элементов на позициях {list[0]} и {list[7]} равно {average}")




