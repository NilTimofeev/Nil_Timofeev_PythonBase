# Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран

with open('task_5.txt', 'w') as file_num:
    file_num.write(input('введите числа, разделяя их пробелами: '))

with open('task_5.txt', 'r') as file_num:
    line_num = file_num.read().split()
    result = 0
    for el in line_num:
        result += float(el)
print(result)


