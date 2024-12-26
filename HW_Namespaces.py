
calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(str_val):
    count_calls()
    return len(str(str_val)), str(str_val).upper(), str(str_val).lower()

def is_contains(str_val, list_val):
    count_calls()
    str_list = list(list_val)
    for i in range( len(str_list)):
        str_list[i] = str(str_list[i]).upper()
    return str_list.count(str(str_val).upper()) > 0


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)

