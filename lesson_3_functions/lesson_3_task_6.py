# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но
# с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно
# начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().


def up_first_letter(word):
    # word = word[0].upper() + word[1:]
    word = f'{chr(ord(word[0]) - 32)}{word[1:]}'
    return word


print(up_first_letter('text'))


def up_first_letters(str1):
    list1 = str1.split()
    for i, val in enumerate(list1, 0):
        list1[i] = up_first_letter(val)
    str1 = " ".join(list1)
    return str1


print(up_first_letters('gddefr rgtth uj k rty'))
