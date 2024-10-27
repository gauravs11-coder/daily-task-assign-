# Daily Task chacking project

def task ():
    tasks =[]  # this is empty list
    print("Welcome to the daily task ")
    
    total_task = int(input("enter how many task do you want to add"))
    
    for i in range(1 ,total_task+1):
        task_name=input("enter task ", )
        tasks.append(task_name)
        
    print("Your today task is /n ",tasks)
    
    while True :
        Oper = int(input("enter 1 - > add /n enter 2 - > update /n enter 3 - > delete /n enter 4 - > view /n enter 5 - > exit"))
        
        if Oper== 1:
            addding =input("enter task name")
            tasks.append(addding)
            print("operation is successfully run ",tasks)
        elif Oper == 2:
            update_value= input("enter task name , you want to update ")
            if update_value in tasks:
                new_task = input("enter your task name ")
                indd = tasks.index(update_value)
                tasks[indd]=new_task
                print("Your task is Update ... ⭐ \n ", tasks)
        elif Oper==3:
            delete_value=input("which task you want to delete")
            if delete_value in tasks :
                indd = tasks.index(delete_value)
                del tasks[indd]
                print("Your task is deleted ... ⭐\n ", tasks)
                
        elif Oper == 4:
            print(tasks)
    
            
        else:
            print("Your Program is successfull Run ... ")
            break;
        
task()