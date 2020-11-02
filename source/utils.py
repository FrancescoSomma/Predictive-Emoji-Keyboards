import Levenshtein as lev
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import pickle
import pandas as pd
from sklearn.manifold import TSNE
import bokeh.plotting as bp
from bokeh.models import HoverTool, BoxSelectTool
from bokeh.plotting import figure, show, output_notebook, output_file
import os

def leggi_dizionario():
    file1 = open('../data/words.txt', 'r')
    dizionario = file1.readlines()

    file1.close()
    return dizionario

def correzione(cercata,dizionario):

    distanzaEffettiva = 5
    simili = ['','','','','','','','','','']
    distanze = [distanzaEffettiva,distanzaEffettiva,distanzaEffettiva,distanzaEffettiva,distanzaEffettiva,distanzaEffettiva,distanzaEffettiva,distanzaEffettiva,distanzaEffettiva,distanzaEffettiva]

    f=0
    for parola in dizionario:
        if  cercata == parola[:-1].lower():
            f=1
            break
        else:
            distanza = lev.distance(cercata,parola)
            m = max(distanze)
            if distanza < m:
                indice = distanze.index(m)
                distanze[indice] = distanza
                simili[indice] = parola

    if(f==0):
        m = min(distanze)
        indice = distanze.index(m)

        print(f'Iniziale: {cercata}, Simili: {simili}, Distanze: {distanze}, Piu simile: {simili[indice]}')
        return simili[indice]
    else:
        print(f'Parola invariata: {parola}')
        return parola.lower()

def tokenizza_frase(frase):

    # rimuovo la punteggiatura
    rem_tok_punc = RegexpTokenizer(r'\w+')
    tokens = rem_tok_punc.tokenize(frase)

    #converto le parole in minuscolo
    parole = [parola.lower() for parola in tokens]

    #rimuovo le stopwords
    lista_stopwords = set(stopwords.words('italian'))
    parole = [parola for parola in parole if not parola in lista_stopwords]

    return parole

def frase_corretta(frase):

    dizionario = leggi_dizionario()
    frase_tokenizzata = tokenizza_frase(frase)
    frase = [correzione(parola,dizionario)[:-1] for parola in frase_tokenizzata]

    return frase,frase_tokenizzata

def scrivi_modello(modello):

    with open('../data/modello','wb') as file:
        pickle.dump(modello,file)

    file.close()

def leggi_modello():

    with open('../data/modello','rb') as file:
        modello = pickle.load(file)

    file.close()
    return modello

def rimuovi_punteggiatura(frase):

    return frase

def leggi_emoji():
    df = pd.DataFrame()
    df = pd.read_csv('../data/emoji.csv')

    return df

def predici(emoji_list,modello,parola):
    for j in range(len(emoji_list['parola'])):
        try:
            emoji_list['similarity'][j] = modello.wv.similarity(parola,emoji_list['parola'][j])
        except KeyError:
            print(f'Non va')

    emoji_list.sort_values(by=['similarity'], ascending=False, inplace=True)

    return emoji_list.head(3)

def costruisci_grafico(modello):
    output_notebook()
    grafico = bp.figure(plot_width=700, plot_height=600, title='Grafico', tools='pan,wheel_zoom,box_zoom, reset,hover',
                        x_axis_type=None, y_axis_type=None, min_border=1)

    # estraggo la lista dei vettori di parole
    vettori = [modello[parola] for parola in list(modello.wv.vocab.keys())[:5000]]

    # converto i vettori in 2d

    modello_tsne = TSNE(n_components=2, verbose=1, random_state=0)
    w2v_tsne = modello_tsne.fit_transform(vettori)

    df_tsne = pd.DataFrame(w2v_tsne, columns=['x', 'y'])
    df_tsne['words'] = list(modello.wv.vocab.keys())[:5000]

    # mostro la parola corrispondente al punto su cui passo il cursore
    grafico.scatter(x='x', y='y', source=df_tsne)
    hover = grafico.select(dict(type=HoverTool))
    hover.tooltips = {'word': '@words'}

    output_file('../data/grafico.html')

def mostra_grafico():

    os.system("start ../data/grafico.html")








