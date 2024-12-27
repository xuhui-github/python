#!/usr/bin/python

from Tkinter import *


def pressOK():
    print("Ok button was pressed")


def processCancel():
    print("Cancel button was pressed")


window = Tk()
btOk = Button(window, text="OK", fg="red", command=pressOK)
btCancel = Button(window, text="Cancel", bg="yellow", command=processCancel)
btOk.pack()
btCancel.pack()
window.mainloop()
