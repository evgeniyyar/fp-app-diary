import functions
import time
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"

        todos = functions.read_todos()

        todos.append(todo)

        functions.write_todos(todos_local=todos, filepath="todos.txt")

    elif user_action.startswith("show"):

        todos = functions.read_todos()

#new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.capitalize().strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            todos = functions.read_todos()

            number = int(user_action[5:])
            number = number - 1
            print(f"Меняем {number + 1}-ое действие")
            new_todo = input("Enter a new todo: ") + '\n'
            todos[number] = new_todo

            functions.write_todos(todos_local=todos, filepath="todos.txt")
        except ValueError:
            print("Команда не верна")

    elif user_action.startswith("complete"):
        try:
            todos = functions.read_todos()

            number = int(user_action[9:])
            todo_to_remove = todos[number - 1].strip('\n')
            todos.pop(number - 1)

            functions.write_todos(todos_local=todos, filepath="todos.txt")

            messages = f"Действие '{todo_to_remove}' выполнено и удалено"
            print(messages)
        except ValueError:
            print("Введите существующий номер действия")

    elif user_action.startswith("exit"):
        break
    else:
        print("Команда не верна.")
print("Bye!")
print("hi")
1


