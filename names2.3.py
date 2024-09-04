calls = 0
def change_calls():
    global calls
    calls = 5, 6, 8

    change_calls()
    print(calls)

def string_info():
    sting = 'Capybara'
    string = 'Armageddon'
    print(string_info('Capybara'))
    print(string_info('Armageddon'))

def is_contains():
    string = 'Urban'
    list_to_search = 'Ban'

print(string_info())
print is_contains()
