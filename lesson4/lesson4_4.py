def my_func(number, itm):
    out_1 = (i for i in number if i != itm)
    return out_1

var_list = [4, 2, 0, 4, 5]
new_list = []

for itm in var_list:
    my_func(new_list, itm)
    new_list.append(itm)

print(new_list)
