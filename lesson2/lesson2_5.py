i=0
rate_inp = [0]
while i < 5:
    var_itm = int(input('Введите рейтинг:\n'))
    j=0
    while int(var_itm) < int(rate_inp[j]):
        j+=1
    rate_inp.insert(j, var_itm)
#        rate_inp.insert(i, var_itm)
#    int(var_itm) > int(rate_inp[i+j]):
#        rate_inp.insert(i+1, var_itm)
    i += 1
print(rate_inp)

