# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные
# должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

from googletrans import Translator

trans = Translator()
file_r = open('task_4_en.txt', 'r', encoding='utf-8')
file_wr = open('task_4_ru.txt', 'w', encoding='utf-8')
while True:
    str_content = file_r.readline().split()
    if not str_content:
        file_r.close()
        break
    str_content[0] = trans.translate(str_content[0], dest='ru', src='en').text
    file_wr.writelines(f'{" ".join(str_content)}\n')
file_wr.close()

