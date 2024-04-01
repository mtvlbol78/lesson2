a = 1
while a < 10:
    numbers = int(input('Введите число '))
    a = a + 1
    if numbers % 2 == 0:
        print('Число четное')
        continue
    if numbers == 13:
        break

    else:
        print('Число нечетное')


print('Программы завершена')

