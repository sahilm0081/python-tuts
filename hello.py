todos=[]

while True:
    action=input("Want to add or show:  ")
    match action:
        case "add":
            todo=input("add todo")
            todos.append(todo)
        case "show":
           print(todos)
        case "exit":
            break