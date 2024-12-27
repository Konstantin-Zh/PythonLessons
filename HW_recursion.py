
def get_multiplied_digits (number):
    str_num = str(number).replace('0', '').replace('-','').replace(',','').replace('.','')
    if str_num.isdigit():
        first = str_num[0]
        if len(str_num) > 1:
            return int(first) * get_multiplied_digits(str_num[1:])
        else:
            return int(first)
    else:
        return 0

print(get_multiplied_digits(40203))
print(get_multiplied_digits(402030))
print(get_multiplied_digits(-1000.11))
print(get_multiplied_digits(0))
print(get_multiplied_digits('qaq'))