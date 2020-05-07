'''
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
'''
class Date:
    def __init__(self, date_str):
        self.date_str = date_str

    @classmethod
    def abracadabra(cls, param):
        var_date_list = param.split('-')
        #print(var_hour)
        var_day = int(var_date_list[0])
        var_month = int(var_date_list[1])
        var_year = int(var_date_list[2])
        print(var_day, var_month, var_year)
        return var_day, var_month, var_year

    @staticmethod
    def valid (func):
        var_c = func
        if var_c[0] > 31 or var_c[0] < 1:
            print('error1')
        elif var_c[1] > 12 or var_c[1] < 1:
            print('error2')
        elif var_c[2] > 2022 or var_c[2] < 1970:
            print('error3')


var_a = Date('07-05-9920')
var_b = var_a.abracadabra('47-05-2020')
var_a.valid(var_b)


