import tkinter as tk
from tkinter import ttk
# IMPORTANTE, W IDGETS PODEN SER ATUALIZADOS
# UTILIZANDO Label.configure(text="exemplo")
#temos uma abreviacao Label['text'] = 'some new text'

def button_fun():
    label.configure(text = entry.get())
    entry['state'] = 'disable' #disable interaction with entry
#window
window = tk.Tk()
window.title("getting and setting widgets")

#widgets
label = ttk.Label(master = window, text = "label")
label.pack()

#some widgets have methor .get() entry is it.
entry = ttk.Entry(master = window)
entry.pack()

button = ttk.Button(master = window, text = "A button", command = button_fun)
button.pack()

button = ttk.Button(master = window, text = "Disable Button", command = lambda : entry.configure(state = 'enable'))
button.pack()



#run
window.mainloop()