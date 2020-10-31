import gensim
from gensim.models import Word2Vec
import pandas as pd
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import time
from source import utils as ut

def crea_datalist():

    #scarico il pacchetto di stopwords se non presente
    nltk.download('stopwords')

    # leggo il dataset
    data = pd.DataFrame()
    data = pd.read_csv('../data/IMDB_Dataset.csv')

    # creo una lista vuota
    data_list = list()

    lines = data['review'].values.tolist()
    for line in lines:
        # rimuovo la punteggiatura
        rem_tok_punc = RegexpTokenizer(r'\w+')
        tokens = rem_tok_punc.tokenize(line)

        # converto le parole in minuscolo
        parole = [parola.lower() for parola in tokens]

        # rimuovo le stop words
        lista_stopwords = set(stopwords.words('english'))
        parole = [parola for parola in parole if not parola in lista_stopwords]

        # aggiungo le parole all lista
        data_list.append(parole)

    return data_list

def train_model(data_list):

    emb_dim = 100
    # addestro il modello word2vec
    modello = gensim.models.Word2Vec(sentences=data_list, size=emb_dim, workers=4, min_count=1)

    # dimensione vocabolario
    parole = list(modello.wv.vocab)
    print(f'Dimensione vocabolario: {len(parole)}')

    return modello

def training():

    inizio = time.time()

    data_list = crea_datalist()
    modello = train_model(data_list)

    #salvo il modello su file
    ut.scrivi_modello(modello)

    fine = time.time()
    tempo = fine - inizio

    print(f'Tempo impiegato per il training: {tempo} secondi')

    ut.costruisci_grafico(modello)



if __name__ == "__main__":
    training()