def to_do():
    tasks= []   
    print("                       ======= TO-DO LIST =======             ")

    total_task=int(input("Enter the number of tasks you want to add: \n"))
    for i in range(1,total_task+1):
        task_name=input(f"Enter task {i} =")
        tasks.append(task_name)
    print(f"Total tasks are ->\n{tasks}")

    while True:
        operation=int(input("Enter the number: \n 1-Add\n 2-Update\n 3-Delete\n 4-Exit/Stop\n"))
        if operation==1:
            add=input("Enter the task you want to add:\n ")
            tasks.append(add)
            print(f"Task {add} has been added successfully...")
            print(f"Total tasks are ->\n{tasks}")

        elif operation==2:
            update=input("Enter task you want to update : \n")
            if update in tasks:
                updated_value=input("Enter new task : \n")
                ind=tasks.index(update)
                tasks[ind]=updated_value
                print(f"Task {update} updated to {updated_value} successfully...")
                print(f"Total tasks are ->\n{tasks}")
            else:
                print("This task is not present in list...")
        
        elif operation==3:
            delete=input("Enter the task you want to delete:\n")
            if delete in tasks:
                ind=tasks.index(delete)
                tasks.pop(ind)
                print(f"Task {delete } has been deleted succssfully...")
                print(f"Total tasks are ->\n{tasks}")
            else:
                print("This task is not present in list...")

        elif operation==4:
            print("             =======List closed=======             ")
            break

        else:
            print("INVALID INPUT")


to_do()