'''
2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
'''

my_file = open('my_text_2.txt','r') #Открываем файл
content = my_file.readlines() # Присваиваем переменной текст. Метод readlines формирует список из строк
my_file.close() # Закрываем файл

str_count= len(content) #считаем кол-во элементов в списке content
print(content)
print('строк : ', str_count)
#words_list = content.split(' ')
i=1
for itm in content:
    words_list = itm.split(' ') # Разделяем строку по пробелу
    out=len(words_list) # считаем кол-во элементов
    print('в ',i,'строке ', int(out), ' слов')
    i+=1
