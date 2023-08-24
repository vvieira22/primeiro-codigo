#Canvas é um widget que permite voce desenhar
#"shapes", como circulos quadrados, lines.

#https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/index.html

import tkinter as tk
from tkinter import ttk

#setup
window = tk.Tk()
window.geometry('600x400')
window.title('Canvas')

#canvas
canvas = tk.Canvas(window, bg = 'blue')
canvas.pack()

#left, top, right, bottom
# canvas.create_rectangle((30, 50, 200, 300), fill = "red", width=5, dash=(10,2,2,3), outline='green')
# canvas.create_oval((200,0,100,100), fill ='yellow')
# canvas.create_arc((200,0,100,100), fill = "red", start = 45, outline='red') #angule 0 - 360.
# canvas.create_line((0,0,100,150),fill = 'black')
# canvas.create_polygon((0,0,100,200,300,50), fill='white')

# canvas.create_text((100,200), text='this some text', fill = 'red')

# canvas.create_window((150,100), window = ttk.Button(window, text = 'text in canvas'))

#event to binding create a basic paint app, move mouse and draw line.
def draw_on_canvas(event):
    x = event.x
    y = event.y
    canvas.create_oval((x - brush_size / 2, y - brush_size / 2, x+ brush_size / 2, y + brush_size/2), fill = 'black')
brush_size = 1

def brush_size_adjust(event):
    global brush_size
    if event.delta > 0:
        brush_size +=1
    else:
        brush_size -=1
    brush_size = max(0,min(brush_size,50))

canvas.bind('<Motion>', draw_on_canvas)
canvas.bind('<MouseWheel>', brush_size_adjust)
#run 
window.mainloop()