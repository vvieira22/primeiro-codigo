import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

#window
window = ttk.Window(themename = 'darkly')
# window.eval('tk::PlaceWindow . center')
window.title("Demo")
window.geometry('300x200')

# Create the menu bar
menubar = ttk.Menu(window)

# Create the "File" menu
file_menu = ttk.Menu(menubar)
# Add menu items to the "File" menu
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")
file_menu.add_separator()
file_menu.add_command(label="Exit",command=window.destroy)

# Add the cascade menu to the "Say Hello" label
menubar.add_cascade(label="Menu", menu=file_menu )

# Add other menu items to the menu bar
menubar.add_command(label="Quit", command=window.destroy)
menubar.add_separator()

# Configure the window to use the menu bar
window.config(menu=menubar)


def convert():
    output_string.set(str(entry_int.get() *1.61))

#title (text)
title_label = ttk.Label(master = window, text = 'Miles to kilometers', font = 'Calibri 24 bold')
title_label.pack(pady = 5)

#input field
input_frame = ttk.Frame(master = window)
entry_int = tk.IntVar(value="")
entry = ttk.Entry(master = input_frame, textvariable = entry_int)
button = ttk.Button(master = input_frame, text = "Convert", command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 10)

#output
output_string = tk.StringVar()
output_label = ttk.Label(
    master = window, 
    text = 'Output:',
    font = 'Calibri 24 bold',
    textvariable = output_string)

output_label.pack(pady = 5)




#run
window.mainloop()