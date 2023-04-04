# -*- coding: utf-8 -*-
"""Untitled14.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Tli_j7aPGvOIXRqG_UOfsR0UX-Y2wIgO
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

datos = pd.read_csv('oficial.csv', sep=';', index_col=0)
series = datos.values.transpose()
cols = ['#7f7fbf', '#7fbf7f', '#ff7f7f']

# Datos
x = datos.index.transpose()
serie1 = series[0]
serie2 = series[1]
serie3 = series[2]
y = np.vstack([serie1, serie2, serie3])

# Gráfico de áreas apiladas
fig, ax = plt.subplots(figsize=(20, 16))
ax.stackplot(x, y, labels = ["Estado", "BCI", "Consorcio"], colors = cols, alpha = 0.9)
ax.legend(loc = 'upper right')
ax.set(xlim = (min(x), max(x)), xticks = x)


# Ajustar el título del eje x y aumentar la distancia entre el título y las etiquetas
ax.set_xlabel('Período', fontsize=16, labelpad=20)
ax.set_ylabel('N° de tarjetas de débito', fontsize=16,labelpad=20)

plt.xticks(rotation=90)
plt.locator_params(axis='x', tight=True)
plt.ticklabel_format(style='plain', axis='y')

plt.show()