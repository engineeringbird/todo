# I want to make a todo app

# Asks if wants to add anything

# The adds something and adds to list

# prints list


def todo_list():
    print('*' * 15)
    print('Please start recording your todos here. When you\'re done, just type QUIT')
    while True:
        todo_list_items = ['Here you go ']
        todo = input('What do you need to get done?  ')
        if todo.lower() == 'quit':
            print('Okay! See you later! Here are your todo items: ')
            print(todo_list_items)
            break
        elif todo == True:
            todo_list_items.append(todo)
            continue



print('Welome! This is a todo app. List things you need to get done and I\'ll make sure we keep track.')

start_app = input('So, would you like to try the app? Y/n  ')

if start_app.lower() == 'n' or start_app.lower() == 'no':
    print('Ok, no problem! Have a nice day!')
    quit()
else:
    todo_list()
