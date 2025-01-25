import tkinter as tk
from tkinter import ttk

loaded = 0
current = 0

        
root = tk.Tk()
frame = ttk.Frame(root)
frame.grid()
screen = tk.Label(root, text="Welcome")
screen.grid(column=0, row=0, columnspan=4)

def updateLabel():
    screen.config(text=current)
def enter():
    global loaded, current
    loaded = current
    current = 0
    updateLabel()
def reset():
    global loaded, current
    loaded = 0
    current = 0
    updateLabel()

def sum():
    global loaded, current
    current = loaded+ current
    loaded = 0
    updateLabel()

def diff():
    global loaded, current
    current = loaded-current
    loaded = 0
    updateLabel()

def prod():
    global loaded, current
    current = loaded*current
    loaded = 0
    updateLabel()

def div():
    global loaded, current
    current = loaded/current
    loaded = 0
    updateLabel()


class NumberButton():
    def __init__(self, value : int, parent):
        self.value = value
        self.button = tk.Button(parent, text=str(value), command= self.click)
    def click(self):
        global current
        current *= 10
        current += self.value
        updateLabel()

    def grid(self, col, row):
        self.button.grid(column=col, row=row)
class ActionButton():
    def __init__(self, icon, action, parent):
        self.action = action
        self.button = tk.Button(parent, text=icon, command=self.action)
    def grid(self, col, row):
        self.button.grid(column=col, row=row)

NumberButton(7,root).grid(0,1)
NumberButton(8,root).grid(1,1)
NumberButton(9,root).grid(2,1)
ActionButton("+", sum, root).grid(3,1)
NumberButton(4,root).grid(0,2)
NumberButton(5,root).grid(1,2)
NumberButton(6,root).grid(2,2)
ActionButton("-", diff, root).grid(3,2)
NumberButton(1,root).grid(0,3)
NumberButton(2,root).grid(1,3)
NumberButton(3,root).grid(2,3)
ActionButton("x", prod, root).grid(3,3)
ActionButton("C", reset, root).grid(0,4)
NumberButton(0, root).grid(1,4)
ActionButton("↓", enter, root).grid(2,4)
ActionButton(":", div, root).grid(3,4)


root.mainloop()