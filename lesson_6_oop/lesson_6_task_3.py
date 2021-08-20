# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии
# (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self, name, surname, positoon, income):
        self._income = income
        self.name = name
        self.surname = surname
        self.position = positoon


class Position(Worker):

    def get_full_name(self):
        print(f'{self.name} {self.surname}')

    def get_total_income(self):
        print(f'{self._income["wage"] + self._income["bonus"]}')


worker_1 = Position('Nil', 'Timofeev', 'operator', {"wage": 5000, "bonus": 111})

worker_1.get_full_name()
worker_1.get_total_income()
