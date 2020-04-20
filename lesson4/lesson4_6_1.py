from itertools import (count,
                       cycle
                       )
from time import sleep

number = input('Введите число \n')

for el in count(int(number)):
    if el > 100:
        break
    else:
        print(el)
        sleep(0.5)
