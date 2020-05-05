'''
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
'''
class Car:
    speed = 0
    color = ''
    name = ''
    is_police = False

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, where_to_turn):
        var = where_to_turn
        print('Машина повернула', where_to_turn)

    def show_speed(self, current_speed):
        Car.speed = current_speed
#        print(Car.speed)

#class TownCar(Car):
#    def speed_limit

#class SportCar(Car):

#class WorkCar(Car):

#class PoliceCar(Car):

var_car_1 = Car()
var_car_1.name = 'Toyota Celica'
var_car_1.color = 'black'
var_car_1.speed = 80
var_car_1.go()
#var_out = [var_car_1.speed, var_car_1.color]
print(var_car_1.name, var_car_1.color, '\n', var_car_1.speed )

var_car_2 = Car()
var_car_2.name = 'Honda Accord'
var_car_2.color = 'red'
var_car_2.speed = 65
var_car_2.turn('направо')
#var_out_2 = [var_car_2.speed, var_car_2.color]
print(var_car_2.name, var_car_2.color, '\n', var_car_2.speed)


#var.show_speed(70)
#print(var.show_speed())

