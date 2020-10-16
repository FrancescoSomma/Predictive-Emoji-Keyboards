import tkinter as tk
import tkinter.font as tkFont

def prova (input):
    print(input)
    return input

def scrivi(a):
    print(a)
    vuoto = '  '

    if  a == '1':
        str = 'AHAH \U0001F603 SI \U0001F44D  CIAO \U0001F64B  NO \U0001F645   \t\n' \
              'sad \U0001F62D \t\n SPAVENTATO \U0001F631 ' \
              '\t\n  PREGHIERA \U0001F64F	BOCCA \U0001F444 OCCHIO \U0001F440 \t\n' \
              '\t\n 	ORECCHIO \U0001F442 GATTO \U0001F63A	TESCHIO \U0001F480	ARRABBIATO \U0001F620 NATALE \U0001F385		'

        label['text'] = str
    else:
        label['text'] = vuoto




HEIGHT = 500
WIDTH = 600

root = tk.Tk()
fontStyle = tkFont.Font(family="Lucida Grande", size=20)
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='background.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')



entry = tk.Entry(frame, font=40)



entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Invia", font=40,   command=lambda: scrivi(entry.get()))

button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


label = tk.Label(lower_frame, font= fontStyle,anchor= 'nw')


label.place(relwidth=1, relheight=1,anchor= 'nw')

root.mainloop()


