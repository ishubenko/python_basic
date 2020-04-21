from functools import reduce

def my_func(prev_el, el):
    # prev_el - предыдущий элемент
    # el - текущий элемент
    return prev_el * el


var_list = [itm for itm in range(100,1000) if not itm & 1]

output = reduce(my_func, var_list)

print(var_list)
print(output)

#numbers = range(100,1000)
#print(reduce())
#print(type(numbers))