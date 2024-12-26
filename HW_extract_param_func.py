
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(2, 'str', False)
print_params(False, b = 10, c = 'srt1')
print_params(b = 11, a = 'rrr')
print_params()
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [11, True, 'str']
values_dict = {'a' : False, 'b' : 123, 'c' : 'val'}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)