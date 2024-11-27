# Создание переменной типа кортеж (tuple)
immutable_var = (1, '321', True)

print (immutable_var)
print (type(immutable_var))

#Ошибка! tuple неизменяемая коллекция в отличие от списка, поэтому выражение ниже некорректно
#immutable_var[0] = 2

# Создание перменной типа список (list)
mutable_var = [1, 'wqer', False]

print (mutable_var)
print (type(mutable_var))

# Изменение элементов списка
mutable_var[0] = 2
mutable_var[1] = 'aaa'
mutable_var[2] = True
print (mutable_var)

mutable_var [1:3] = ['bbb', False]
print (mutable_var)

mutable_var.append('eee')
print (mutable_var)

mutable_var.extend('apple')
print (mutable_var)

mutable_var.extend([123, 234, 345])
print (mutable_var)

mutable_var.remove('bbb')
print (mutable_var)
