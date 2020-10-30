import Levenshtein as lev
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import pickle
import pandas as pd

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

    print(f'Lista parole: {parole}')
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







