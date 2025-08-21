tasks = []

def add_task():
    task = input("Add Task: ").title()
    if task not in tasks:
        tasks.append(task)
    else:
        print('Already Included')

def remove_task():
    remove = input("Remove Task: ").title()
    if remove in tasks:
        tasks.remove(remove)
    else:
        print('No task like that')

def show_task():
    for i, task in enumerate(tasks,start=1):
        print(f"{i}.{task}")


def main():
    while True:
        print('What Do You Want To Do? ')
        print('1: Add Task')
        print('2: Remove Task')
        print('3: Show Task')
        print('4: Quit')
        choice = input("(1,2,3,4): ")

        if choice == '1':
            add_task()
        
        elif choice == '2':
            remove_task()

        elif choice == '3':
            show_task()

        elif choice == '4':
            break

if __name__ == "__main__":
    main()