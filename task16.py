# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1
from random import randint
size = int(input('Введите размер массива: '))
list_1 = []
i = 0
count = 0
while i < size:
    list_1.append(randint(0, 10))
    i += 1
print(list_1)
find = int(
    input('Введите число: '))
for n in list_1:
    if n == find:
        count += 1
print(count)

# from random import randint
# N = int(input('Введите натуральное число: '))
# numbers = []
# for _ in range(N):
#     numbers.append(randint(1, N))
# print(numbers)
# X = int(input('Введите число X: '))
# c = numbers.count(X)
# print(c)
