import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

twus = [251,339.6,353.1,436.4]
igus = [895,928.5,1220,1480]
fbus = [2121,1950,2180,2110]
years = [2020,2021,2022 ]
tl = np.diff(twus) / twus[:-1]
il = np.diff(igus) / igus[:-1]
fl = np.diff(fbus) / fbus[:-1]

print("twitter ",tl, "\ninstagram", il, "\nfacebook", fl)
colors = ['tab:cyan', 'tab:pink', 'tab:blue']

fig, ax = plt.subplots(figsize=(3, 6))

path = ax.stackplot(years, tl, il, fl, baseline='wiggle',
             labels=['twitter', 'instagram', 'facebook'], colors =colors, alpha =0.5)

ax.legend(loc='upper left')

ax.set_xlabel('Años')
ax.set_ylabel('Incremento porcentual')
ax.set_title('Incremento porcenetual de usuarios entre los años 2020-2022')
ax.xaxis.set_major_locator(MultipleLocator(1))
plt.show()


"""
el siguiente grafico muestra el incremento porcentual de usuarios, entonces, podemos notar como en terminos porcentuales twitter ha crecido mas que facebook e isntagram en el ultimo año, esto es porque al no contarlo como la cantidad total de usuarios no consideramos si una red social crecio un numero fijo, si no que es relativo en cuanto a la cantidad total de usuarios que tenia previamente ademas podemos ver que facebook en el 2020 y 2022 tiene un porcentaje negativo, lo cual significa que decreció, instagram por otra parte, creció, pero no tanto como twitter, esto se ve reflejado en la cantidad de espacio que ocupa en el grafico.

Además se añadió una linea roja y verde para denotar mejor cuando crece y decrece una red social, si la linea verde se encuentra sobre la roja, significa que la red social creció, caso contrario, la red decreció, los datos comienzan a partir del 2019 para poder calcular la cantidad de nuevos usuarios respecto al total.

deberia considerar añadir mas datos, para que se vea una tendencia mayor.
"""