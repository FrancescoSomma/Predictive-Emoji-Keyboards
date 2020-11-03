import tkinter as tk
import tkinter.font as tkFont
from source import utils as ut
from source import train as tr
import nltk
from source.utils import frase_corretta,predici, mostra_grafico,esistone_nuove_parole,leggi_nuove_parole
import pandas as pd


def elaboraFrase(df,modello):
   emoji_list = df.copy()
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
    emoji,presente = predici(emoji_list,modello,parola)
    button.append([])
    if presente:
        if(i>8):
            c=5
        if(len(frase )<= 5):

          for j in range(5):
              button[i].append(tk.Button(lower_frame, text=emoji['emoji'].iloc[j], font=fontStyle, command=lambda i=i,j=j,emoji=emoji: usaEmoji(frase,i,emoji['emoji'].iloc[j])))

          testo = tk.Label(lower_frame, font=fontStyle, text=parola)
          testo.grid(row=i%9, column=c)
          button[i][0].grid(row=(i%9), column=c + 1)
          button[i][1].grid(row=(i % 9), column=c + 2)
          button[i][2].grid(row=(i % 9), column=c + 3)

        else:
            fontStyleButton = tkFont.Font(family="Helvetica", size=12)
            for j in range(3):
                button[i].append(tk.Button(lower_frame, text=emoji['emoji'].iloc[j], font=fontStyleButton,command=lambda i=i: usaEmoji(frase,i,emoji['emoji'].iloc[j])))

            testo = tk.Label(lower_frame, font=fontStyleButton, text=parola)
            testo.grid(row=i%9, column=c)
            button[i][0].grid(row=(i % 9), column=c + 1)
            button[i][1].grid(row=(i % 9), column=c + 2)
            button[i][2].grid(row=(i % 9), column=c + 3)





def usaEmoji(frase,i,emoji):

    frase_default = entry.get()
    frase_default = frase_default.replace(frase[i], emoji)
    entry.delete(0, tk.END)
    entry.insert(0, frase_default)




#scarico il pacchetto di stopword(se non presente)
nltk.download('stopwords')

#controllo se esistono nuove parole dopo l'esecuzione precedente
if esistone_nuove_parole():
    risposta = input('Ci sono nuove parole, vuoi aggiornare il modello? s/n ->: ')
    if risposta == 's':
        nuoveParole = leggi_nuove_parole()
        print(f'Nuove parole: {nuoveParole}')
        f = open('../data/nuoveparole.txt','w')
        modello = tr.training(nuoveParole)

    else:
        #provo a leggere il modello dal file; se non esiste,lo addestro e lo scrivo su file
        try:
            modello = ut.leggi_modello()
            print('Modello gia presente')
            num = list(modello.wv.vocab)
            print(f'Dimensione vocabolario: {len(num)}')
        except FileNotFoundError:
           modello = tr.training(nuoveParole=[])
else:
    try:
        modello = ut.leggi_modello()
        print('Modello gia presente')
        num = list(modello.wv.vocab)
        print(f'Dimensione vocabolario: {len(num)}')

    except FileNotFoundError:
        modello = tr.training(nuoveParole=[])

#inizia l'applicazione
dataframe = {
    'parola': ['happy','laugh','smile','wink','love','kiss','tongue','hug','think','neutral','smirk',
               'lie','relieve','pensive','drool','sleep','mask','fever','nausea','vomit','hot','cold',
               'explode','cowboy','party','confuse','worried','sad','anxious','cry','fear','disappoint','tired',
               'nervous','angry','amazing','dead','shit','clown','alien','monkey','mouth','collision','water',
               'bomb','message','hello','ok','call','yes','punch','muscle','ear','nose','brain',
               'eyes','baby','boy','girl','man','woman','student','cook','science','sing','technology',
               'art','police','christmas','walk','train','bed','family','dog','cat','flower','tree',
               'banana','apple','pear','tomato','bread','chocolate','drink','world','house','train','bus',
               'taxi','school','car','moto','bike'],
    'emoji': ['\U0001F603','\U0001F602','\U0001F604','\U0001F609','\U0001F970','\U0001F618','\U0001F61B','\U0001F917','\U0001F914','\U0001F610','\U0001F60F',
              '\U0001F925','\U0001F60C','\U0001F614','\U0001F924','\U0001F634','\U0001F637','\U0001F912','\U0001F922','\U0001F92E','\U0001F975','\U0001F976',
              '\U0001F92F','\U0001F920','\U0001F973','\U0001F615','\U0001F61F','\U0001F641','\U0001F630','\U0001F62D','\U0001F631','\U0001F61E','\U0001F62B',
              '\U0001F621','\U0001F620','\U0001F929','\U0001F480','\U0001F4A9','\U0001F921','\U0001F47D','\U0001F435','\U0001F48B','\U0001F4A5','\U0001F4A6',
              '\U0001F4A3','\U0001F4AC','\U0001F44B','\U0001F44C','\U0001F919','\U0001F44D','\U0001F44A','\U0001F4AA','\U0001F442','\U0001F443','\U0001F9E0',
              '\U0001F440','\U0001F476','\U0001F466','\U0001F467','\U0001F468','\U0001F469','\U0001F270','\U0001F9D1','\U0001F52C','\U0001F3A4','\U0001F4BB',
              '\U0001F3A8','\U0001F46E','\U0001F385','\U0001F6B6','\U0001F3CB','\U0001F6CC','\U0001F46A','\U0001F415','\U0001F408','\U0001F33B','\U0001F332',
              '\U0001F34C','\U0001F34E','\U0001F350','\U0001F345','\U0001F35E','\U0001F36B','\U0001F964','\U0001F30D','\U0001F3D8','\U0001F684','\U0001F68C',
              '\U0001F695','\U0001F3EB','\U0001F697','\U0001F3CD','\U0001F6B2'],
    'similarity': [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                   0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                   0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                   0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                   0,0,0,0,0,0,0,0,0,0,0,0,0]
}

df = pd.DataFrame(dataframe)

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

buttoninv = tk.Button(frame, text="Invia", font=40,command=lambda: elaboraFrase(df,modello))
buttoninv.place(relx=0.68, relheight=1, relwidth=0.15)

button = tk.Button(frame, text="Mostra \nCluster", font=40,   command=lambda: mostra_grafico())
button.place(relx=0.85, relheight=1, relwidth=0.15)


lower_frame = tk.Frame(root, bg='#f0f0f0', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font= fontStyle,bg='#f0f0f0',anchor= 'nw')
label.place(relwidth=1, relheight=1,anchor= 'nw')


root.mainloop()


