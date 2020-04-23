'''
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
'''
print('введите текст:\n')
inp_text = '123'
out_text = ''
while inp_text:
    inp_text = input()
    out_text = out_text + inp_text + '\n'

#print(out_text)
#my_file = open('my_text.txt','w')

out_f = open("my_text.txt", "w")
out_f.write(out_text)
out_f.close()