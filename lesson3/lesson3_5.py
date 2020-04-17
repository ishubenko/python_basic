# Символ f останавливает работу программы
finish = False
temp_sum = 0


def my_func(inp_str):
    global finish, temp_sum
    var_list = inp_str.split(' ')
    for itm in var_list:
        if itm == 'f':
            finish = True
            break
        temp_sum = temp_sum + int(itm)
    return temp_sum


while (finish == False):
    inp_str = input('Введите числа через пробел:\n')
    output = my_func(inp_str)
    print('Сумма введенных чисел: ', output)
print('Конец программы')

#first_sum = int(var_list[0]) + int(var_list[0])

