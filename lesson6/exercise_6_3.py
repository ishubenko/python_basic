'''
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).
'''


class Worker:
    name = ''
    surname = ''
    position = 'engineer'
    _income = {'wage': 100000, 'bonus': 20000, }


class Position(Worker):

    def __init__(self, fname, lname, wage,):
        Worker._income['wage'] = wage
        Worker.surname = lname
        Worker.name = fname
        self.full_name = (Worker.surname + ' ' + Worker.name)
        self.total_income = int(Worker._income['wage']) + int(Worker._income['bonus'])


#    def get_total_income(self):
#        total_income = self.

var = Position('Ivan', 'Petrov', 90000)
print(var.full_name)
print(var.total_income)

var2 = Position('Alex', 'Ivanov', 75000)
print('\n',var2.full_name)
print(var2.total_income)