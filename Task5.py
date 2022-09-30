# 5.Реализуйте алгоритм перемешивания списка.

import random

list = []
n = int(input("Введите размер списка: "))

for i in range(1, n + 1):
    list.append(random.randint(-10, 10))

def mix_list(list_orig):
    list = list_orig[:]
    list_length = len(list)
    for i in range(list_length):
        index = random.randint(0, list_length - 1)
        temp = list[i]
        list[i] = list[index]
        list[index] = temp
    return list

mixed_list = mix_list(list)

print("Исходный список ->", list)

print("Перемешанный список ->", mixed_list)
