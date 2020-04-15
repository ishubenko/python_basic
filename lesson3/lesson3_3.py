def my_func (var_1, var_2, var_3):
    if int(var_1) < int(var_2) and int(var_1) < int(var_3):
        var_sum = int(var_2) + int(var_3)
    elif int(var_2) < int(var_3) and int(var_2) < int(var_1):
        var_sum = int(var_1) + int(var_3)
    else:
        var_sum = int(var_1) + int(var_2)
    return var_sum


x = input('Число 1 \n')
y = input('Число 2 \n')
z = input('Число 3 \n')

output = my_func(x,y,z)
print('Сумма двух бОльших чисел равна ', output)