tasks=[]
while True:
    print("1. Add Tasks")
    print("2.View Tasks")
    print("3. Delete Tasks")
    print("4. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        task=input("Enter task: ")
        tasks.append(task)
        print("Task added! ")
    elif choice == "2":
        if len(tasks)==0:
            print("No tasks added")
        else:
            print("Your tasks are: ")
            for i in range(len(tasks)):
                print(i+1,". ",tasks[i])
    elif choice == "3":
        if len(tasks)==0:
            print("No tasks deleted")
        else:
            a=int(input("Enter task number to delete: "))
            tasks.pop(a-1)
            print("Task deleted! ")
    elif choice == "4":
        print("Goodbye")
        break
    else:
        print("Invalid choice")

