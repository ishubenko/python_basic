'''
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
'''
var_file = open('my_text_4.txt','r')
content = var_file.readlines()
var_file.close()  #Закрываем файл
print(content)
out_cont = []
for itm in content:
    var_cont = itm.split(' ')  # разделяем по пробелу
    out_cont += var_cont
print(out_cont)


for i in range(len(out_cont)): # заменяем английские на русские
    if out_cont[i] == 'One':
        out_cont[i] = 'Один'
    elif out_cont[i] == 'Two':
        out_cont[i] = 'Два'
    elif out_cont[i] == 'Three':
        out_cont[i] = 'Три'
    elif out_cont[i] == 'Four':
        out_cont[i] = 'Четыре'

print(out_cont)

out_f = open("out_file_4.txt", "w") # Открываем на запись
out_f.writelines(out_cont) # Записываем построчнг
out_f.close()
