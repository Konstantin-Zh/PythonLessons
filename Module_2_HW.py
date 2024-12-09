for l in range(3, 21):
    first_number = l #int(input('Введите первое число из загадки (3 - 20): '))
    if first_number < 3 or first_number > 20:
        print('Введено неверное число! Мы все умрём!')
    else:
        print(f'Число в первом поле - {first_number}')

        PairList_ = []

        for i in range(1, 20):
            for k in range (i, 20):
                if i == k:
                    continue
                elif first_number % (i + k) == 0:
                    #print(f'Число {first_number} кратно сумме ({i} + {k})')

                    PairList_.append([str(i), str(k)])

        #print(f'Итоговый список пар: {PairList_}\n')

        password = ''
        for pair in PairList_:
            password = password + pair[0] + pair[1]

        print(f'Пароль: {password}\n')
