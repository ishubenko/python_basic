'''def my_func (a:int,b:int) -> float:
    try:
        result = int(a) / int(b)
    except ZeroDivisionError:
        result ='НЕможно так делить'
    return result

x = input('делимое: \n')
y = input('делитель: \n')

output = my_func(x,y)
print(output)
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
class Div:
    def my_func (a:int,b:int) -> float:
        try:
            result = int(a) / int(b)
        except ZeroDivisionError:
            result ='НЕможно так делить'
        return result

a = input('Введите первое число \n')
b = input('Введите второе число \n')
var_a = Div
print(var_a.my_func(a,b))
'''
class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

a = input('Введите первое число \n')
b = input('Введите второе число \n')

try:
    if int(b) == 0:
        raise OwnError('На ноль делить не желательно')
    result = int(a) / int(b)
except OwnError as err:
    print(err)
else:
    print(result)













