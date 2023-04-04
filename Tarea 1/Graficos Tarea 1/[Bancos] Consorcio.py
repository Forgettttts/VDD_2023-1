import matplotlib.pyplot as plt

# definir los tamaños y colores de los círculos
# valores secun BE, BC,BCI
values = [23966.369 , 51449.000, 30874.908] #revisar si corresponde a millones o miles de pesos
bancos = ["Banco Estado", "Banco Consorcio", "BCI"]

sizes = values
colors = ['#000080', 'red', 'green'] # cambiar segun gama de colores que usemos
centers = [(sizes[0]/2, 0), ((sizes[0]+sizes[1]/1.5), 0), (sum(sizes), 0)]

# crear la figura y el objeto de los ejes
fig, ax = plt.subplots()

# trazar los círculos
for bn, c, s, color in zip(bancos,centers, sizes, colors):
    circle = plt.Circle(c, s/2, color=color, alpha = 0.5)
    ax.add_artist(circle)
    label = ax.annotate(bn, xy=(c[0],-max(sizes)/1.5), fontsize=10, ha="center")
    label = ax.annotate(s, xy=(c[0],max(sizes)/1.5), fontsize=10, ha="center")

# ajustar los límites de los ejes y las etiquetas
ax.set_aspect('equal')
plt.title("Ingreso por seguros en millones")
ax.set_xlim([0, sum(sizes)*1.2])
ax.set_ylim([-max(sizes), max(sizes)])

# mostrar la figura
plt.axis("off")
plt.show()



#https://www.bancoestado.cl/content/bancoestado-public/cl/es/home/inicio---bancoestado-corporativo/antecedentes-financieros---bancoestado-corporativo/estados-financieros---bancoestado-corporativo/estados-financieros-anuales---bancoestado-corporativo.html

#https://www.bciseguros.cl/la_compania/informacion-corporativa/estados-financieros/

#https://www.bancoconsorcio.cl/nuestro-banco/estados-financieros
"""
este grafico muestra el numero de ingresos gracias a seguros en el año 2022 por parte de los bancos.
El radio de los circulos esta relacionado directamente con este numero de ingresos, por lo cual, podemos notar que el banco consorcio es el que registra un ingreso(buscar sinonimo) mayor gracias a la cobranza y venta de seguros, seguido por el banco bci y en ultimo lugar de la comparacion el banco estado, notese que no necesariamente significa que alguno de estos bancos tuvo menos o mas ingresos que otros en general, solamente significa que gano menos o más gracias al apartado de seguros.

La informacion se pudo obtener gracias a que cada banco cuenta con una subempresa que corresponde a la corredora de seguros por lo que viendo los estados de resultados de cada empresa podemos ver cuanto gano cada banco gracias a los seguros.
"""