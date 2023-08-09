import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

#window
window = ttk.Window(themename = 'darkly')
window.title("buttons")
window.geometry("600x400")

#button
def btn_fun():
    print("button pressed")
    print(check_var.get())
    print(radio_var.get())

btn_var = tk.StringVar(value = 'button with string var')
button = ttk.Button(window, text="simple button", command = btn_fun, textvariable=btn_var)
button.pack()

#checkbutton
#Para verificar estado do checkbutton
#precisamos da tkinter variable
#1 or 0 (string)
check_var = tk.StringVar() #can be booblean, string.. depending
check = ttk.Checkbutton(
    window, 
    text = "check box1", 
    command = lambda : print(check_var.get()),
    variable=check_var,
    onvalue = 10,
    offvalue = 5)
check.pack()

#conectar check2 com check1, para quando 1 estiver ativo
# setar o valor off para outro, "tipo um radio" 
# check2 = ttk.Checkbutton(
#     window, 
#     text = "check box2", 
#     command = lambda : check_var.set(5))
# check2.pack()


#radio buttons
#Apenas um valor vai ser selecionado de todos os radios buttons
# e será armazenado o value dele em radio_var

radio_var = tk.StringVar()

radio1 = ttk.Radiobutton(window, 
                         text="RadioButton 1", 
                         value = "radio1",
                         variable = radio_var,
                         command = lambda : print(radio_var.get()))
radio1.pack()
radio2 = ttk.Radiobutton(window, 
                         text="RadioButton 2",
                         variable = radio_var, 
                         value = "radio2",
                         command = lambda : print(radio_var.get()))
radio2.pack()


#EXEMPLO EXECICIO
#2 radios e um checkbox
#RADIO A E B
#CHECKBOX MARCADA SEMPRE VAI ATIVAR RADIO B
#E SE EU MARCAR A, SEMPRE VAI DESMARCA CHECKBOX.
#SE EU MARCAR B, SEMPRE VAI ATIVAR CHECKBOX.
# radio_var = tk.StringVar()

# radio1 = ttk.Radiobutton(window, 
#                          text="RadioButton 1", 
#                          value = "A",
#                          variable = radio_var,
#                          command = lambda :check_var2.set(False))
# radio1.pack()
# radio2 = ttk.Radiobutton(window, 
#                          text="RadioButton 2",
#                          variable = radio_var, 
#                          value = "B",
#                          command = lambda : check_var2.set(True))
# radio2.pack()

# check_var2 = tk.BooleanVar() #can be booblean, string.. depending
# check3 = ttk.Checkbutton(
#     window, 
#     text = "check box1", 
#     command = lambda : radio_var.set("B"),
#     variable= check_var2,
#     onvalue = 1,
#     offvalue = 0)
# check3.pack()

# run
window.mainloop()