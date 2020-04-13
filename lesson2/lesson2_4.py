usr_string = input('Напишите строку:\n')

usr_str_list = usr_string.split(' ')
i = 1
for itm in usr_str_list:
    if len(itm) > 10:
        print(i,' ',itm[0:10])
    else:
        print(i,' ',itm)
    i += 1

