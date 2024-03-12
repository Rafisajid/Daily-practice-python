Todos = []

while True:
    user_action = input("Type add, show and exit: ")
    match user_action:
        case 'add':
            user_prompt = input("Enter a todo:")
            Todos.append(user_prompt)

        case 'show':
            print(Todos)

        case 'exit':
            break

print("You have written a great code block....")
