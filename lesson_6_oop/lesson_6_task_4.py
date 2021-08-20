# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
# is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar
# и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
# сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False
        print()

    def show_speed(self):
        print(f'Скорость автомобиля {self.name}: {self.speed}')

    def go(self, speed):
        self.speed = speed
        print(f'Машина {self.name} поехала. Скорость {self.speed}')

    def stop(self):
        self.speed = 0
        print(f'Машина {self.name} остановилась. Скорость {self.speed}')

    def turn(self, direction):
        print(f'Машина {self.name} повернула {direction}')


class TownCar(Car):

    def show_speed(self):
        Car.show_speed(self)
        if self.speed > 60:
            print(f'Скорость автомобиля {self.name} превышена (предел 60)')


class WorkCar(Car):

    def show_speed(self):
        self.show_speed()
        if self.speed > 40:
            print(f'Скорость автомобиля {self.name} превышена (предел 40)')


class SportCar(Car):
    pass


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name)
        self.is_police = True


town_car = TownCar(0, 'grey', 'skoda')
town_car.go(50)
town_car.speed = 70
town_car.show_speed()
town_car.turn('налево')
town_car.stop()

work_car = WorkCar(0, 'yellow', 'cat')

sport_car = SportCar(0, 'red', 'ferrari')
print(sport_car.name, sport_car.is_police)

police_car = PoliceCar(0, 'blue', 'reno')
print(police_car.name, police_car.is_police)
