#def zarplata(hours, rate, bonus):
#    var_temp = (int(hours) * int(rate)) + int(bonus)
#    return var_temp
from my_module.script_1 import zarplata


hours = 40
rate = 1000
bonus = 20000


output = zarplata(hours, rate, bonus)
print(output)
