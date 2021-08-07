# Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их
# окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тысяч,
# вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

out_file = open('task3.txt', 'r', encoding='utf-8')
worker_count = 0
profit_sum = 0
print('Сотрудники, чья зарплата меньше 20000:')
while True:
    content = out_file.readline()
    if not content:
        out_file.close()
        break
    name, profit = content.split()
    profit = float(profit)
    if profit < 20000:
        print(name)
    worker_count += 1
    profit_sum += profit
print(f'Средняя зарплата {profit_sum / worker_count}')


