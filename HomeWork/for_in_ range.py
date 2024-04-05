#while 1 > 0:
#    print('Ok')
#for i in 1, 2, 3, 4:
#    print('ok')
#for i in 'hello', 'two', 'three':
#    print(i)
#for i in 'hello':
#    print(i)
#list_ = ['one', 'two', 'three']
#for i in list_:
#    print(i)
    #one
    #two
    #three

#list_ = ['one', 'two', 'three']
#for i in list_:
#    if i == 'two':
#        list_.remove(i)
#print(list_) #['one', 'three']

#list_ = ['one', 'two', 'three']
#for i in range(5): # 0, 1, 2, 3, 4
#    print(i)
#print(list_)
#print(len(list_))

#list_ = ['one', 'two', 'three']
#for i in range(len(list_)):
#    print(list_[i])
# работа с элементом из списка
#list_ = ['one', 'two', 'three']
#for i in range(len(list_)):
#    list_[i] = ':)' #заменили перечисляемый элемент на смайлик
#print(list_)

#list_2 = [1, 2, 3, 4, 5]
#summ_ = 0
#for i in range(len(list_2)):
#    summ_ = summ_ + list_2[i]
#print(summ_)
# вычисляет сумму чисел из списка


#for i in range(1, 11): # если число в скобках одно, то оно говорит о количестве циклов до stop. Если два, то перове = начало последовательности, а второе = конец
# range (1, 11, 3) 1-start, 11-stop (второй элемент), 3 - step (шаг)
# последнее число не включается
#    print(i)
for i in range(1, 11):
    for j in range(1, 11):
        print(f'{i} х {j} = {i * j}')

dict_ = {'a': 1, 'b': 2, 'c': 3}
for i in dict_:
    print(i, dict_[i])

dict_ = {'a': 1, 'b': 2, 'c': 3}
for i, k in dict_.items():
    print(i, dict_[i])

