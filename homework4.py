immutable_var = (1,2,3, 'строка', True)
print(immutable_var)
# immutable_var[2]= 6 # Не работающая строка т.к. элементы кортежа не могут быть изменены
print(immutable_var)

mutable_list = ['кит', 'жук', 'кот']
print(mutable_list)
mutable_list[1] = 'бык'
print(mutable_list)
mutable_list.append('лось') # добавление в список
print(mutable_list)
mutable_list.extend('кот') # разделение на символы
print(mutable_list)
mutable_list.remove('бык') # удаленне
print(mutable_list)