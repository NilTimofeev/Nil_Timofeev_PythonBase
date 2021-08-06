# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов


def max_arg(num1, num2, num3):
    if num1 < num2 and num1 < num3:
        return print(num2 + num3)
    elif num2 < num1 and num2 < num3:
        return print(num1 + num3)
    elif num3 < num1 and num3 < num2:
        return print(num1 + num2)
    else:
        print('Нет двух наибольших чисел среди введенных')


max_arg(4, 5, 4)
