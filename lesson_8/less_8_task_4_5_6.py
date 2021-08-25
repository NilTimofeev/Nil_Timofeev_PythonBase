# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.

# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
# определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также
# других данных, можно использовать любую подходящую структуру, например словарь.

# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для
# указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

class Warehouse:
    def __init__(self):
        self.warehouse_list = []

    def into_warehouse(self, technique, num):
        try:
            if not isinstance(num, int):
                raise TypeError
            for i in range(num):
                if technique == 'scanner':
                    obj = Scanner('scanner')
                if technique == 'printer':
                    obj = Printer('printer')
                if technique == 'xerox':
                    obj = Xerox('xerox')
                self.warehouse_list.append(obj)
                print(f'на склад поступило: {num} <{obj.name}>')
        except TypeError:
            print(f'количество техники [{technique}] указано неверно. Должно быть целое число')

    def from_warehouse(self, technique, num):
        try:
            if not isinstance(num, int):
                raise TypeError
            for i in reversed(range(len(self.warehouse_list))):
                if technique == self.warehouse_list[i].name:
                    print(f'передано со склада в другое подразделение: {num} <{self.warehouse_list[i].name}>')
                    del self.warehouse_list[i]
                    num -= 1
                if num <= 0:
                    break
        except TypeError:
            print(f'количество техники <{technique}> указано неверно. Должно быть целое число')


class Technique:
    total_obj = 0

    def __init__(self, name):
        self.name = name
        Technique.total_obj += 1

    @classmethod
    def count_technique(cls):
        print(f'Всего на складе и других подразделениях {cls.total_obj} позиции')


class Printer(Technique):
    pass


class Scanner(Technique):
    pass


class Xerox(Technique):
    pass


warehouse = Warehouse()
warehouse.into_warehouse('scanner', 3)
warehouse.into_warehouse('xerox', 3)
warehouse.into_warehouse('printer', '2')

warehouse.from_warehouse('scanner', 2)
warehouse.from_warehouse('xerox', 1)

print(warehouse.warehouse_list)
Technique.count_technique()
