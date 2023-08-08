import tkinter as tk
from tkinter import ttk

def button_fun():
    print(string_var.get())
    string_var.set("button pressed")
#window
window = tk.Tk()
window.title("Tkinter variables")

#tkinter variable
string_var = tk.StringVar(value = 'start value')
#this object if pass to text label
#its "connect" and update the data of label.
 
#widgets
label = ttk.Label(master = window, textvariable = string_var)
label.pack()

entry = ttk.Entry(master = window, textvariable = string_var)
entry.pack()

button = ttk.Button(master = window, text = 'button', command = button_fun)
button.pack()

# 2 entry and 1 label, value is connect by string_2, when
# string_2 is update, all textvariable appont to then will be
# upgrade value
string_2 = tk.StringVar(value = 'teste')
entry = ttk.Entry(master = window, textvariable = string_2)
entry.pack()

entry = ttk.Entry(master = window, textvariable = string_2)
entry.pack()

label = ttk.Label(master = window, textvariable = string_2)
label.pack()

#run
window.mainloop()