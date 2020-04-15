def my_func(fname, lname, birth, city, email, phone):
    output = fname + ' ' + lname + '\n' + birth + '\n' + city + '\n' + email + ' ' + phone
    return output


fname = input('Введите Ваше имя\n')
lname = input('Введите Вашу фамилию\n')
birth = input('Дата рождения\n')
city = input('Город рождения\n')
email = input('Ваш email\n')
phone = input('Ващ телефон\n')

profile = my_func(fname, lname, birth, city, email, phone)
print(profile)

# имя, фамилия, год рождения, город проживания, email, телефон