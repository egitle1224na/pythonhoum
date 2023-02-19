# Задача 36
# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент 
# по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, 
# которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Примечание: бинарной операцией называется любая операция, у которой
# ровно два аргумента, как, например, у операции умножения.

# Пример:

# Ввод:
# print_operation_table(lambda x, y: x * y)


# Вывод:
# 1 2 3 4 5 6
# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36


def find_rhythm(text: str):
    phrases = text.split()   
    vowels = 'аеиоуэюя'   
    phrases_vow = []   
    for i in phrases:   
        phrases_vow.append(list(filter(lambda x: x in vowels, list(i))))
    result_list = []   
    for i in range(len(phrases_vow) - 1):   
        result_list.append(len(phrases_vow[i]) == len(phrases_vow[i + 1]))
    return all(result_list)


song = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
if find_rhythm(song):
    print('Парам пам-пам')
else:
    print('Пам парам')