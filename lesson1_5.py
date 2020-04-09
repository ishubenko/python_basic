income = input('Введите выручку компании\n')
expenses = input('Введите затраты компании\n')

if(int(income) > int(expenses)):
    print('Компания приносит прибыль')
    margin = int(income) - int(expenses)
    profit = margin / int(income)
    print('Прибыль компании: ' , margin)
    print('Рентабельность компании составляет: ' , profit )
    worker = input("введите кол-во сотрудников\n")
    profit_per_worker = margin / int(worker)
    print('Прибыль компании в расчете на одного сотрудника: ', profit_per_worker)

if(int(income) == int(expenses)):
    print('Компания работает в ноль')

else:
    print('Компания работает в убыток')
