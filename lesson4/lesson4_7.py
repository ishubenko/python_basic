def fibo_gen(numb):
    for el in range(1,numb +1):
        yield el

numb = int(input('Введите значение:\n'))
#n = fibo_gen(fact)
i=0
f=1
for el in fibo_gen(numb):
    i+=1
    f= f*el
#    print(el)
#    print(f)
    if i > 15:
        break
print('Факториал числа ',numb, ' равен ',f)

