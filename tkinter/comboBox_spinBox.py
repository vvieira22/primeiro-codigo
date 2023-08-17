import tkinter as tk
from tkinter import ttk


#window
window = tk.Tk()
window.title("Combo and Spin box")
window.geometry("600x400")

# comboBox
items = ['banana', 'maca', 'laranja']
food_string = tk.StringVar(value = items[0])
combo = ttk.Combobox(window, textvariable=food_string)

#samething
combo['values'] = items
# combo.configure(values = items)

combo.pack()

#events for combobox
combo.bind('<<ComboboxSelected>>', lambda event: combo_label.config(text=f'Selected: {food_string.get()}'))

combo_label = ttk.Label(window, text = '')
combo_label.pack()


# SpinBox
#numbers
spin_int = tk.IntVar(value = 12)
spin = ttk.Spinbox(
    window, 
    from_ = 0, 
    to = 20, 
    increment = 1, 
    command = lambda : print(spin_int.get()),
    textvariable = spin_int)

# spin['value'] = (1,2,3,4,5)
spin.pack()

#Spin event
spin.bind('<<Increment>>', lambda event: print("up arrow"))
spin.bind('<<Decrement>>', lambda event: print("down arrow"))



#exercise spin a,b,c,d
spin2 = ttk.Spinbox(
    window, 
    from_ = 0, 
    to = 20, 
    increment = 1, 
    command = lambda : print("arrow pressed"))

spin2['value'] = ['a', 'b', 'c', 'e']

spin2.pack()
spin.bind('<<Decrement>>', lambda event: print("down arrow"))


#setup
window.mainloop()