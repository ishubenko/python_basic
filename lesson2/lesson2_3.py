num_month = input('Введите месяц:\n')

month_list = ['january','february','march',
              'april','may','june',
              'july','august','september',
              'october','november','december']

time_of_year = ['winter','spring','summer','autumn']

if int(num_month) == 1 or int(num_month) == 2 or int(num_month) == 12:
    print(month_list[(int(num_month) - 1)],' is ', time_of_year[0])
elif int(num_month) == 3 or int(num_month) == 4 or int(num_month) == 5:
    print(month_list[(int(num_month) - 1)],' is ', time_of_year[1])
elif int(num_month) == 6 or int(num_month) == 7 or int(num_month) == 8:
    print(month_list[(int(num_month) - 1)],' is ', time_of_year[2])
elif int(num_month) == 9 or int(num_month) == 10 or int(num_month) == 11:
    print(month_list[(int(num_month) - 1)],' is ', time_of_year[3])
else:
    print('Введено неверное значение')
