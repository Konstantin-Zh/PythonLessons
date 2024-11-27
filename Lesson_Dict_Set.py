# Пример создания словаря (Dictionry). Словарь хранит элементы в виде "ключ:значение"
dict_ = {12: 'aa', 13: 'bb', 14: 22, 15: [00, 11, 22], 'ololo' : 101}
print (dict_)

my_dict = {'A': 0, 'B': 1, 'C': 2}
print (my_dict)

# Вывод значения. Такой доступ по отсутствующему ключу выдаст ошибку
print (my_dict['B'])
# Вывод значения по отсутствующему ключу без выдачи ошибки
print (my_dict.get('X', 'NULL'))

# Добавление элементов в словарь
my_dict['D'] = 3
print (my_dict)

my_dict.update({'E': 4, 'F': 5})
print (my_dict)


# Удаление элементов из словаря
print (my_dict.pop('E'))
print (my_dict)

del my_dict['D']
print (str(my_dict) + '\n')


# Пример создания переменной множества (set). Множество хранит только уникальные значения
myset = {1, 2, 3, 'a', 'b', 4, 'a', 2}
print (myset)

# Добавление элементов в множество
myset.add(5)
print (myset)
myset.add((22, 33))
print (myset)
myset.update({6, '44'})
print (myset)

myset.discard('b')
print (myset)
myset.remove('44')
print (myset)

# Метода discard не выдаёт исключений, при попытке удаления несуществующего элемента из множества
myset.discard('4555')
print (myset)
# Ошибка! Метод remove выдаёт исключение при удалении несуществующего элемента из множества
# myset.remove('4555')



