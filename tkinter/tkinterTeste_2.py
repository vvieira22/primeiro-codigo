import tkinter as tk
from tkinter import ttk

def button_func():
    print("button was pressed")

def exercise_bt_fun():
    print("hello")

#create a window
window_root = tk.Tk()
window_root.title("Minha Janela")
window_root.geometry("800x600")

#ttk widgets (best method to widgets)
#ttk.label
label = ttk.Label(master = window_root, text = "This a test")
label.pack()

#create widgets
#tk widgets are old, but used here to understand it.
text = tk.Text(master = window_root)
text.pack() #place

#ttk entry
entry = ttk.Entry(master = window_root)
entry.pack()

#exercise label
exercise_label = ttk.Label(master = window_root, text = "my Label")
exercise_label.pack()

#ttk buttom
button = ttk.Button(master = window_root, text = "A button", command = button_func)
button.pack()

#exercise button
exercise_button = ttk.Button(master = window_root, text="exercise button", command = exercise_bt_fun)
exercise_button.pack()

#command its not necessary pass littery functio, it can be lambda
#EXAMPLE:
exercise_button = ttk.Button(master = window_root, text="lambd button", command = lambda : print('hello'))
exercise_button.pack()

#run
#MAINLOOP -update the gui | -checks for events (button clicks etc..)
window_root.mainloop() #code stop here, when close window run above.
