# Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет содержать данные
# о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1   ООО   10000   5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
# убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.

import json

firms_profit = [{}, {}]
profit = 0
sum_profit = 0

with open('task_7_firms.txt', 'r', encoding='utf-8') as firms_file:
    for line in firms_file:
        list_str = line.split()
        profit = (float(list_str[2]) - float(list_str[3]))
        firms_profit[0][list_str[0]] = profit

for val in firms_profit[0].values():
    sum_profit += val
firms_profit[1]['average_profit'] = sum_profit / len(firms_profit[0])
print(firms_profit)

with open('file.json', 'w') as serialize_file:
    json.dump(firms_profit, serialize_file)
