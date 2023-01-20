# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# import random
#
# list = []
# for i in range(random.randint(3, 6)):
#     list.append(random.randint(-9, 9))
# print(list)
#
# new_list = [i for i in range(len(list)) new_list.append(list[index] * list[len(list) - index - 1]), ]
# index = 0
# while(len(list) / 2 > index):
#     new_list.append(list[index] * list[len(list) - index - 1])
#     index += 1
# print(new_list)


import math
first_list = list(map(int, input('Введите числа ').split()))
print(first_list)
print('Произведение пар чисел первого списка: ',list([a*b for a,b in zip(first_list[0:math.ceil(len(first_list)/2)],first_list[::-1])]))
