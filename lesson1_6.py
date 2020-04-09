current = input('Первая дистанция, км : \n')
target =  input('Цель пробежать, км : \n')
i = 1

while float(current) < int(target) and i < 10:
    current = float(current) * 1.1
    i += 1
    print(current)
print(i , 'дней Вам нужно, чтобы достигнуть цели')