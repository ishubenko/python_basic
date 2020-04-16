def my_func (x,y):
#    result = x ** y
    z = -y
    i=1
    m=x
    while i<z:
        m=m*x
        i +=1
    result = 1/m
    return result


x = float(input('Введите действительное положительное число\n'))
y = int(input('Введите целое отрицательное число\n'))
if y > -1:
    print('"y" не отрицательное число')
else:
    output = my_func(x,y)
    print(output)
