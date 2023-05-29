import matplotlib.pyplot as plt
import numpy as np

# future labels

labelle = ['Pino', 'Carlo', 'Sonda', 'Sigaro', "Totolo"]

# dati

caratteristiche = {
    'piso' : [9, 10, 7, 9, 3],
    'grodo' : [1, 9, 5, 2, 1],
    'forza' : [8, 20, 9, 5, 6],
    'kollo' : [4, 6, 2, 1, 4]
}

posizioneBarreY = np.arange(len(labelle)) # estrae gli indici delle labels per settare la posizione nell'ascisse
larghezza = 0.10 # larghezza di ogni barra
moltiplicatore = 0 

fig, ax = fig, ax = plt.subplots(layout='constrained')

for labella, valore in caratteristiche.items():
    offset = larghezza * moltiplicatore # serve a spostare a destra una barra da quella precedente per non sovrapporle 
    barre = ax.barh(posizioneBarreY + offset, valore, larghezza, label=labella)
    ax.bar_label(barre, padding=2)
    moltiplicatore += 1

ax.set_xlabel('Voto') # Testo Asse Y 
ax.set_title('Potenza dei ragax') # Titolo fuori il grafico
ax.set_yticks(posizioneBarreY + larghezza, labelle) # Nome delle Labelle sull'asse X
ax.legend(loc='upper left', ncols=3) # ncols per non andare a capo prima dei 3 valore nella legenda


plt.show()