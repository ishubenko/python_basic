def int_func(word):
    ''' Поднимает первую букву слова'''
    word_title = word.title()
    return word_title


output = ''
var_string = input('напишите строку :\n')
var_list = var_string.split(' ')

for itm in var_list:
    output = output + ' ' + int_func(itm)

print(output)

