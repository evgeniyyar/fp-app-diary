import functions
import PySimpleGUI


label = PySimpleGUI.Text("Type in a to-do")
input_box = PySimpleGUI.InputText(tooltip="Enter todo", key="todo")
button_add = PySimpleGUI.Button("Add")
list_box = PySimpleGUI.Listbox(values=functions.read_todos(),
                               key='todos', enable_events=True,
                               size=[50, 10])
button_edit = PySimpleGUI.Button("Edit")
button_complete = PySimpleGUI.Button("Complete")

window = PySimpleGUI.Window('My To-Do App',
                            layout=[[label, input_box, button_add], [list_box, button_edit, button_complete]],
                            font=('Italic', 14))

while True:
    event, values = window.read()
    print("events:", event)
    print(type(event))
    print("values", values)
    print(type(values))
    match event:
        case 'Add':
            todos = functions.read_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case 'Edit':
            todo_to_edit = values['todos'][0]
            new_todo = values['todo'] + "\n"

            todos = functions.read_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case 'Complete':
            todo_to_complete = values['todos'][0]

            todos = functions.read_todos()
            index = todos.index(todo_to_complete)
            todos.pop(index)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case PySimpleGUI.WINDOW_CLOSED:
            break

window.close()
