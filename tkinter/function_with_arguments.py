import tkinter as tk
from tkinter import ttk

def btn_fun(entry_var):
    print("button pressed")
    print(entry_var.get()) 

#setup
window = tk.Tk()
window.title("functions with arguments")

#widgets
entry_var = tk.StringVar()
entry = ttk.Entry(window, textvariable=entry_var)
entry.pack()

#lambda garante que so ira executar assm que pressionar realmente.
# por que por padrao lambd function nao é executada.
#sem lambda precisaria criar uma inner func dentro da outra pra rodar igual lambda.
button = ttk.Button(window, text = "button", command = lambda : btn_fun(entry_var))
button.pack()

#run 
window.mainloop()