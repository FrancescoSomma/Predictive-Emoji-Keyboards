import tkinter as tk
import tkinter.font as tkFont

from source.utils import frase_corretta


def prova (input):
    print(input)
    return input

def correzioneFrase(input):
   corretta = frase_corretta(input)
   print(corretta)
   entry.delete(0,200)
   entry.insert(0,corretta)
   button1 =tk.Button(lower_frame, text="\U0001F603", font= fontStyle)
   button1.place(relx=0.001, relheight=0.3, relwidth=0.3)



HEIGHT = 500
WIDTH = 600

root = tk.Tk()
fontStyle = tkFont.Font(family="Lucida Grande", size=20)
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='../img/background.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')



entry = tk.Entry(frame, font=40)



entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Invia", font=40,   command=lambda:correzioneFrase(entry.get()))

button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


label = tk.Label(lower_frame, font= fontStyle,anchor= 'nw')


label.place(relwidth=1, relheight=1,anchor= 'nw')

root.mainloop()


