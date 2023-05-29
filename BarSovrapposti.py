import matplotlib.pyplot as plt
import numpy as np

# future labels

labelle = ['Pino', 'Carlo', 'Sonda', 'Sigaro', "Totolo"]

# dati

caratteristiche = {
    'piso' : [9, 10, 7, 9, 3],
    'grodo' : [1, 9, 5, 2, 1],
    'forza' : [8, 20, 9, 5, 6]
}

width = 0.6  # the width of the bars: can also be len(x) sequence


fig, ax = plt.subplots()
bottom = np.zeros(5)

for labella, valore in caratteristiche.items():
    p = ax.bar(labelle, valore, width, label=labella, bottom=bottom)
    bottom += valore

    ax.bar_label(p, label_type='center')

ax.legend()

plt.show()