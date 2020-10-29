import tkinter as tk
import tkinter.font as tkFont
from source import utils as ut
from source import train as tr
import nltk
from source.utils import frase_corretta


def elaboraFrase():
   frase_default= entry.get()
   frase,frase_tokenizzata = frase_corretta(frase_default)
   for i in range(len(frase)):
       frase_default = frase_default.replace(frase_tokenizzata[i],frase[i])
   entry.delete(0,tk.END)
   entry.insert(0,frase_default)

   button = []

   for testo in lower_frame.winfo_children():
       testo.destroy()
   for button in lower_frame.winfo_children():
           button.destroy()

   c=0
   for i in range(len(frase)):
    parola = frase[i]
    print(f'Parola: {parola}')
    if(i>8):
        c=5
    if(len(frase )<= 5):

      button.append(tk.Button(lower_frame, text='\U0001F603', font=fontStyle, command=lambda i=i: usaEmoji(frase,i)))
      testo = tk.Label(lower_frame, font=fontStyle, text=parola)
      testo.grid(row=i%9, column=c)
      button[i].grid(row=(i%9), column=c+1)
    else:
        fontStyleButton = tkFont.Font(family="Helvetica", size=12)
        button.append(tk.Button(lower_frame, text='\U0001F603', font=fontStyleButton,command=lambda i=i: usaEmoji(frase,i)))
        testo = tk.Label(lower_frame, font=fontStyleButton, text=parola)
        testo.grid(row=i%9, column=c)
        button[i].grid(row=(i%9), column=c+1)





def usaEmoji(frase,i):

    emoji = '\U0001F603'
    frase_default = entry.get()
    frase_default = frase_default.replace(frase[i], emoji)
    print(f'Frase: {frase}\nFrase default: {frase_default}')
    entry.delete(0, tk.END)
    entry.insert(0, frase_default)




#scarico il pacchetto di stopword(se non presente)
nltk.download('stopwords')

#provo a leggere il modello dal file; se non esiste,lo addestro e lo scrivo su file
try:
    modello = ut.leggi_modello()
    print('Modello gia presente')
except FileNotFoundError:
   tr.training()

#inizia l'applicazione
HEIGHT = 500
WIDTH = 600

root = tk.Tk()
fontStyle = tkFont.Font(family="Times", size=20)

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='../img/background.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Invia", font=40,   command=lambda: elaboraFrase())

button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg='#f0f0f0', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font= fontStyle,bg='#f0f0f0',anchor= 'nw')
label.place(relwidth=1, relheight=1,anchor= 'nw')


root.mainloop()


