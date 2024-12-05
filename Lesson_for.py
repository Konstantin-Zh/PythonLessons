# for i in range(1, 11):
#     for j in range(1, 11):
#         print(f'{i} x {j} = {i * j}')

# dict = {'a' : 1, 'b': 2, 'c': 3}
# for i, k in dict.items():
#     print(i, k)

# Исходные данные
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
# Проход по всем числам
for i in numbers:
    if i > 1: # Отбрасываем 1, т.к. она не попадает под критерии простого и сложного числа
        is_prime = True
        # Попеременно делим от 2 до текущего значения
        for j in range(2, i):
            if i % j == 0: # Число поделилось без остатка
                is_prime = False # Число сложное
                break
        # Распределение чисел коллекциям
        if is_prime:
            # Добавляем число в простые
            primes.append(i)
        else:
            # Добавляем число в сложные
            not_primes.append(i)
# Вывод результатов
print (primes)
print (not_primes)

