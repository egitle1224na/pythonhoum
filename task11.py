"""По данному целому неотрицательному n вычислите
значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
чисел от 1 до N) 0! = 1 Решить задачу используя цикл
while
"""
# var 1
user_input = int(input('Введите целое положительное число: '))
result = 1
n = user_input
if user_input == 0:
    print(f'{n}! = 1')
else:
    while user_input > 0:
        result *= user_input
        user_input -= 1
    print(f'{n}! = {result}')

# var 2
user_input = int(input('Введите целое положительное число: '))
n1, n2 = 0, 1
n_num = 2
while n2 < user_input:
    n1, n2 = n2, n1 + n2
    n_num += 1
if n2 == user_input:
    print(f'{user_input} - число Фиббоначи №{n_num}')
else:
    print(f'{user_input} не является числом Фиббоначи')
