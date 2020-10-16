import Levenshtein as lev
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import  BernoulliNB
from sklearn.metrics import accuracy_score

def correzione(cercata):

    file1 = open('paroleItaliane.txt','r')
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


    print(f'Iniziale: {cercata}, Simili: {simili}, Distanze: {distanze}')
    file1.close()

def training():

   df = pd.read_csv('dataset.csv')
   print(df)

   X = df['parola']
   y = df['emoji']

   vect = CountVectorizer()
   X = vect.fit_transform(X)

   x_train, x_test, y_train, y_test = train_test_split(X,y)

   model = BernoulliNB()
   model.fit(x_train,y_train)

   p_train = model.predict(x_train)
   p_test = model.predict(x_test)

   stringa = [input('Inserisci la parola: ')]
   stringa = vect.transform(stringa)

   predizione = model.predict(stringa)
   print(f'Predizione: {predizione}')
   #acc_train = accuracy_score(y_train,p_test)
   #acc_test = accuracy_score(y_test, p_test)

  # print(f'Train acc: {acc_train}, test acc: {acc_test}')

training()


