i=0
goods_list =[]
while i < 2:
    var_dict = {'название': input('Введите название товара:\n'),
                 'цена': int(input('Ввелите стоимость товара:\n')),
                 'колличество': int(input('Введите кол-во:\n')),
                 'ед.изм': input('Введите единицы измерения:\n')}
#var_dict2 = {'название': 'принтер', 'цена': 6000, 'колличество': 2, 'ед.изм': 'шт'}
#var_dict3 = {'название': 'сканер', 'цена': 2000, 'колличество': 7, 'ед.изм': 'шт'}
    item_tuple = (i+1, var_dict)
    goods_list.insert(i,item_tuple)
    i += 1
print(goods_list)
#item_tuple_2 = (2, var_dict2)
#item_tuple_3 = (3, var_dict3)
#goods_list = [item_tuple_1, item_tuple_2, item_tuple_3]
#print(goods_list)
#var_set1 = {var_dict1['название'],var_dict2['название'],var_dict3['название']}
#var_set2 = {var_dict1['цена'],var_dict2['цена'],var_dict3['цена']}
#var_set3 = {var_dict1['колличество'],var_dict2['колличество'],var_dict3['колличество']}
#var_set4 = {var_dict1['ед.изм'],var_dict2['ед.изм'],var_dict3['ед.изм']}

#output_analize = {'название': var_set1,
#                  'цена': var_set2,
#                  'количество': var_set3,
#                  'ед.изм': var_set4
#                  }
#
#print(output_analize)