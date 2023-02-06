# Задача 14
# Требуется вывести все целые степени двойки 
# (т.е. числа вида 2**k), не превосходящие числа N.

# Пример:

# 10 -> 1 2 4 8

n = 10
N = int(input("Введите число N: "))
number = 0
result = 1
while result <= N:
    result = 2 ** number
    print(result, end=" ")
    number += 1
