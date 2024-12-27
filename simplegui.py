import PySimpleGUI as sg

layout = [[sg.Text("Enter a Number")], [sg.Input()], [sg.OK()]]

with sg.FlexForm("简单的PySimpleGUI设计") as form:
    button, (number,) = form.LayoutAndRead(layout)
    sg.MsgBox(button, numb)
