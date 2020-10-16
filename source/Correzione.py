def correzione(cercata):
    import Levenshtein as lev

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

correzione('carenza')