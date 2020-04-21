# Первое решение
i=0
var_list = [1,2,0,4,5,7,13,9]
new_list = []
new_list_2 = []
#print(new_list[i])
for itm in var_list:
    if int(itm) > int(var_list[i-1]):
        new_list.append(int(itm))
    i+=1

print(new_list)

# Второе решение
var_list2 = [1,2,0,4,5,7,13,9]
output = [itm2 for itm2 in var_list2 if int(itm2) > int(var_list2[var_list2.index(itm2) -1]) ]
print(output)