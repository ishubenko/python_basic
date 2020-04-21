from itertools import (count,
                       cycle
                       )
from time import sleep

elements = input('введите элементы: \n')
с = 0
for el in cycle(elements):
    if с > 15:
        break
    print(el)
    sleep(1)
    с += 1