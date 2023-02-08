# Задача 22: Даны два неупорядоченных набора целых чисел
#  (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа,
#  которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. 
# n - кол-во элементов первого множества. 
# m - кол-во
# элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

list_m = (2, 4, 6, 8, 10, 12, 10, 8, 6, 4, 2)
list_n = ( 8, 6, 4, 2, 3, 6, 9, 12, 15, 18)

def SortRevList(m, n):
    m = list_m(m)
    n = list_n(n)
    x = m.intersection(n)
    x = a (x = m.intersection(n))
    a = x
    print(x)

# в общем и целом я окончательно запуталась.

# mol = [int(x) for x in input().split()]
# n = mol[0]
# m = mol[1]
# set_1 = set()
# set_2 = set()
# list_1 = list()
# a = [int(x) for x in input().split()]
# k = set(a)
# for i in k:
#     set_1.add(i)
#     b = [int(x) for x in input().split()]
#     k1 = set(b)
# for i in k1:
#     set_2.add(i)
#     lok = set_1 & set_2
#     kool = list(lok)
#     kool.sort()
# for i in kool:
#     print(i, end=' ')

# a = {2, 4, 6, 8, 10, 12, 10, 8, 6, 4, 2}
# b = {3, 6, 9, 12, 15, 18}
def SortRevList(a, b):
    a = set(a)
    b = set(b)
    c = a.intersection(b)
    c = list(c)
    c.sort(reverse=False)
    return c


asize = int(input('Введите размер множества а: '))
bsize = int(input('Введите размер множества b: '))
a = []
b = []
print('Введите элементы первого списка')
for _ in range(asize):
    a.append(input())
print('Введите элементы второго списка')
for _ in range(bsize):
    b.append(input())
print(a)
print(b)
print(SortRevList(a, b))