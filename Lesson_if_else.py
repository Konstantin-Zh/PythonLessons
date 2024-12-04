first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))

print (f'Первое число: {first}\nВторое число: {second}\nТретье число: {third}')

if first == second and second == third and first == third:
    print ('3')
elif first == second or second == third or first == third:
    print('2')
else:
    print('0')

