

class Event:

    def __init__(self, date, start_time, location):
        self.date = date
        self.start_time = start_time
        self.location = location

    def get_details(self):
        return self.date, self.start_time, self.location


class Task:

    def __init__(self, date, start_time, duration, people):
        self.date = date
        self.start_time = start_time
        self.duration = duration
        self.people = people

    def get_details(self):
        return self.date, self.start_time, self.duration, self.people


class Todo_list:

    def __init__(self, queue = []):
        self.queue = queue

    def add_to_queue(self, item): #adds item to end of 'queue'
        self.queue.append(item)

    def next_in_queue(self): #returns head of 'queue'
        return self.queue[-1].get_details()

    def next_item_completed(self): #removes head of 'queue'
        self.queue.pop(0)

    def print_list(self):
        print('TO DO LIST:')
        for item in self.queue:
            for details in item.get_details():
                print(details, end = " ") #prints details of item on same line
            print("")

def main():
    todo = Todo_list()
    inp = input("Welcome to the To Do List! Please enter your Name: ")
    while inp != 'quit': #loop for using to do list
        inp = input("\nPlease enter one of the following: addEvent, addTask, printList, completeNextItem, quit \n")
        if inp == 'addEvent':
            #Handle inputs for event
            date = input("Date: ")
            start_time = input("Start Time: ")
            location = input("Location: ")
            event = Event(date, start_time, location)
            todo.add_to_queue(event)

        elif inp == "addTask":
            #Handle inputs for task
            date = input("Date: ")
            start_time = input("Start Time: ")
            duration = input("Duration: ")
            people = input("People: ")

            people = people.split()
            task = Task(date, start_time, duration, people)
            todo.add_to_queue(task)

        elif inp == "printList":
            todo.print_list()

        elif inp == "completeNextItem":
            todo.next_item_completed()

        elif inp == "quit":
            break

        else:
            print("Please enter a valid input!")

    print("Thanks for using the to do list!")

if __name__ == "__main__":
    main()
