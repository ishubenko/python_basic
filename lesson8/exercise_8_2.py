def my_func (a:int,b:int) -> float:
    try:
        result = int(a) / int(b)
    except ZeroDivisionError:
        result ='НЕможно так делить'
    return result


x = input('делимое: \n')
y = input('делитель: \n')

output = my_func(x,y)
print(output)