task = []

while True:
    user_choice = input("What do you want to do: 1. Add task 2. print task : ")
    if user_choice == "1":
        task_name = input("Enter task name: ")
        task.append(task_name)
        print(task)

    elif user_choice == "2":
        for i in task:
            print(i)    