'''
6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:

Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря:

{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
'''
my_file = open('my_txt_6.txt', 'r')
content = my_file.readlines()
my_file.close()
var_dict = {}
out_dict = {}

for itm in content:
    hours = 0
    content_list = itm.split(' ')
#    print(content_list)
    var_dict = {content_list[0], 0}
    for itm2 in content_list[1:]:
        var_hours = itm2.split('(')
        hours += int(var_hours[0])
        var_dict = {content_list[0]: hours}
        out_dict.update(var_dict)
#        print(hours)
print(out_dict)



