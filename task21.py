# Задача №21. Решение в группах
# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
direction = {"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {
    "VII": " S005 "}, {" V ": " S009 "}, {" VIII": " S007 "}
y = set()
for i in direction:
    for j in i.values():
        # y.add(j.replace(" ",""))
        y.add(j.strip())
print(y)