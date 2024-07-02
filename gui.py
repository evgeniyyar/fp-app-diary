import functions
import PySimpleGUI


label = PySimpleGUI.Text("Type in a to-do")
input_box = PySimpleGUI.InputText(tooltip="Enter todo")
button_add = PySimpleGUI.Button("Add")

window = PySimpleGUI.Window('My To-Do App', layout=[[label, input_box, button_add]])
window.read()
window.close()

