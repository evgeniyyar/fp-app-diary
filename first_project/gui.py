import functions
import PySimpleGUI


label = PySimpleGUI.Text("Type in a to-do")
input_box = PySimpleGUI.InputText(tooltip="Enter todo", key="todo")
button_add = PySimpleGUI.Button("Add", key="ADD")

window = PySimpleGUI.Window('My To-Do App',
                            layout=[[label, input_box, button_add]],
                            font=('Italic', 14))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case 'ADD':
            todos = functions.read_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case PySimpleGUI.WINDOW_CLOSED:
            break

window.close()
