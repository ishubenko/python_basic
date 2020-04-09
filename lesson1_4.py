num = input("Введите целое положительное число\n")
x = 1
biggest = 0
#y = 1
dig = 1
print(dig)
while dig > 0 :
    dig = (int(num) % ( x * 10)) // (1 * x)
    x *= 10
    if dig > biggest :
        biggest = dig
    print(dig)
print('Самая большая цифра из числа', num , 'это' , biggest)
#dig = (int(num) % 10) // 1
#dig2 = (int(num) % 100) // 10
#dig3 = (int(num) % 1000) // 100
#dig4 = (int(num) % 10000) // 1000

#print(dig)
#print(dig2)
#print(dig3)
#print(dig4)