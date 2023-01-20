# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# import math
#
# first_list = [float(input('Введите координату X первой точки ')), float(input('Введите координату Y первой точки '))]
# second_list = [float(input('Введите координату X второй точки ')), float(input('Введите координату Y второй точки '))]
# result = math.sqrt(pow(first_list[0] - second_list[0], 2) + (pow(first_list[1] - second_list[1], 2)))
# print(f'Расстояние между двумя точками = {round(result, 2)}')


from functools import reduce
first_list = list(map(int, input('Введите координаты X и Y первой точки: ').split()))
second_list = list(map(int, input('Введите координаты X и Y второй точки: ').split()))
def distance(values_1, values_2):
     result = reduce(lambda x, y: (x + y)**(1/2), (map(lambda n: (n[1] - n[0])**2, zip(values_1, values_2))))
     return round(result, 2)
print(distance(first_list, second_list))