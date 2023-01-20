# Орел и решка
#
# Дана строка текста, состоящая из букв русского алфавита "О" и "Р". Буква "О" –
# соответствует выпадению Орла, а буква "Р" – соответствует выпадению Решки.
# Напишите программу, которая подсчитывает наибольшее количество подряд выпавших Решек.

# text = input("Введите последовательность ")
# list = []
# for i in text.split('О'):
#     if (i != ''):
#        list.append(i)
# max = len(list[0])
# for j in list:
#     if (len(j) > max):
#         max = len(j)
# print(max)



text = input("Введите последовательность ")
list = [i for i in text.split('О') if (i != '')]
max = len(list[0])
for j in list:
    if (len(j) > max):
        max = len(j)
print(max)