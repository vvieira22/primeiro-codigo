import tkinter as tk
from tkinter import ttk

#EVENTS
#KEYBOARD PRESSED, MOUSE CLICK AND MANY OTHERS
#WIDGETS GETS SELECT / UNSELECTED

# YOU NEED TO BIND THIS EVENTS TO A WIDGET
#EXAMPLE Widget.bind(event,function)


def get_pos_mouse(event):
    print(f'x{event.x} y: {event.y}')



#window
window = tk.Tk()
window.title("event binding")

#widgets
text = tk.Text(window)
text.pack()

entry = ttk.Entry(window)
entry.pack()

btn = ttk.Button(window, text = "button")
btn.pack()
#events
#https://www.pythontutorial.net/tkinter/tkinter-event-binding/
#<'modifer-type-detail'>
window.bind('<Alt-KeyPress-a>', lambda event: print(f"evento alt+a window\n{event}"))

#so vai pegar posicao do mouse encima do widget que voce setar. no caso text.
# text.bind("<Motion>", get_pos_mouse)

# window.bind('<KeyPress>', lambda event: print(f"tecla digitada\n{event.char}"))

# #verificar se usuario selecionou o campo
# entry.bind("<FocusIn>", lambda event : print(f"entry field was selected"))
# entry.bind("<FocusOut>", lambda event : print(f"entry field was out"))


#imprimir mousewhell quando o usuario pressionar shift e usar o mousewhell quando o texto estiver selecionado.

text.bind('<Shift-MouseWheel>', lambda event : print("MouseWhell"))

#run
window.mainloop()