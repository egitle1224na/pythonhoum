# Задача 10
# На столе лежат n монеток. Некоторые из них лежат вверх решкой,
#  а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной.
#  Выведите минимальное количество монет, которые нужно перевернуть.

# Пример:

# 5 -> 1 0 1 1 0
# 2

# from random import randint
# x = 5
# list = []
# for i in range[x]:
#     list.append(randint(0, 1))
# print(list)
# zero = list.count(0)
# if len(list) - zero < zero:
#     print(len(list) - zero)
# else:
#     print(zero)

from random import randint
n = int(input('Введите количество монет: '))
list = []
i = 0
count_0 = 0
count_1 = 0
while i < n:
    list.append(randint(0, 1))
    if list[i] == 0:
        count_0 += 1
    if list[i] == 1:
        count_1 += 1
    i += 1
print(f'{n} -> {list}')
if count_0 > count_1:
    print(count_1)
else:
    print(count_0)