import Levenshtein as lev
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import pickle

def correzione(cercata):

    file1 = open('../data/paroleItaliane.txt', 'r')
    parole = file1.readlines()
    distanzaEffettiva = len(cercata)
    simili = ['','','']
    distanze = [distanzaEffettiva,distanzaEffettiva,distanzaEffettiva]


    for parola in parole:
        distanza = lev.distance(cercata,parola)
        m = max(distanze)
        if distanza < m:
            indice = distanze.index(m)
            distanze[indice] = distanza
            simili[indice] = parola

    m = min(distanze)
    indice = distanze.index(m)

    #print(f'Iniziale: {cercata}, Simili: {simili}, Distanze: {distanze}, Piu simile: {simili[indice]}')
    file1.close()
    return simili[indice]

def tokenizza_frase(frase):

    #scarico il pacchetto di stopword(se non presente)
    nltk.download('stopwords')

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

    frase = tokenizza_frase(frase)
    frase = [correzione(parola) for parola in frase]
    frase_nuova = ' '.join(frase)
    print(f'Frase corretta: {frase_nuova}')

def salva_modello(modello):

    with open('../data/modello','wb') as file:
        pickle.dump(modello,file)

def carica_modello():

    with open('../data/modello','rb') as file:
        modello = pickle.load(file)

    return modello










