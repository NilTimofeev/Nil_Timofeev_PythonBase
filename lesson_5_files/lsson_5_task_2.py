# Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов
# в каждой строке.

out_file = open('task_2.txt', 'r')
str_num = 0
while True:
    content = out_file.readline()
    if not content:
        out_file.close()
        break
    str_num += 1
    print(f'в строке {str_num} слов {len(content.split())}')
print(f'Всего {str_num} строк(-и)')
