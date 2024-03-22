phone_box = {'denis': [8888888888888, 544654657], 'max' : 80003332222}
phone_box.update({
    'sasha': 81236541232,
    'ron': 84521324499

})
print(phone_box)
print(phone_box.get('ron'))
a = phone_box.pop('sasha')
print(phone_box)
print(a)
print(phone_box.keys())
print(phone_box.values())
print(phone_box.items())
list_ = [1, 2, 3, 4, 5]
# list_.discard(1) - удаляет элемент, если он есть, если его нет, то не выдает ошибку
# list_.remove(1) - удаляет, если элемент есть, если его нет, то выдает ошибку
# list_.pop(1) - тоже удаляет
# list_.add(1) - что бы добавить элемент к множеству