'''
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
'''

my_file = open('my_text_5.txt','w') #Создаем файл
var_str = input('Введите чиосла через пробел\n')
my_file.write(var_str)
my_file.close() # Закрываем файл

var_file = open('my_text_5.txt','r')
content = var_file.read()
numbers_list = content.split(' ')
summary = 0
for itm in numbers_list:
    summary += (int(itm))
var_file.close()

print(summary)
