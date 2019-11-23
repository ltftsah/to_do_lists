todo_list = ""
inp = input("Welcome to the To Do List! Please enter your name:  ")

while True:
    inp = input("Please enter one of the following: addEvent, addTask, printList, completeNextItem, quit \n")

    if inp == 'addEvent':
        date = input("Date: ")
        time = input("Time: ")
        location = input("Location: ")
        todo_list += '\n' + 'EVENT/TASK' + '\n' + date + '\n' + time + '\n' + location + '\n'

    elif inp == 'addTask':
        date = input("Date: ")
        time = input("Time: ")
        duration = input("Duration: ")
        people = input("People: ")
        todo_list += '\n' + 'EVENT/TASK' + '\n' + date + '\n' + time + '\n' + duration + '\n' + people + '\n'

    elif inp == 'printList':
        print(todo_list)

    elif inp == 'completeNextItem':
        i = todo_list.find('EVENT/TASK')
        todo_list = todo_list[i+10:]
        i = todo_list.find('EVENT/TASK')
        todo_list = todo_list[i:]

    elif inp == 'quit':
        break

    else:
        print("Please enter a valid input!")
print("Goodbye!")
