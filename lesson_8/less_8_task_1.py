# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
# и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Date:
    date_str = '01-01-2000'
    date_num = []

    def __init__(self, date):
        Date.date_str = date

    @classmethod
    def date_to_num(cls):
        cls.date_num = list(map(int, cls.date_str.split('-')))
        print(cls.date_num)

    @staticmethod
    def date_valid():
        Date.date_to_num()
        if 1 <= Date.date_num[0] <= 31:
            print('День указан верно')
        else:
            print('день должен иметь значение от 01 до 31')


Date.date_to_num()
date = Date('44-11-2012')
# date.date_to_num()
date.date_valid()
