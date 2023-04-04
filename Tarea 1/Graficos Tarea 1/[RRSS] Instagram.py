import seaborn as sns
from poli_sci_kit import utils
import matplotlib.pyplot as plt

default_sat = 0.95

rrss=["Instagram", "Facebook", "Twitter", "Otras"]
porcentajes = [23, 7, 5, 65]
colores = ['#C13584', '#4267B2',   '#1DA1F2', '#FAFAD2']

allocations=porcentajes
labels=rrss
colors=colores
style="semicircle"
num_rows=5
marker_size=200
df_seat_lctns=None

sns.set_palette(colors)

df_seat_lctns = utils.gen_parl_points(
    allocations=allocations,
    labels=labels,
    style=style,
    num_rows=num_rows,
    speaker=False,
)

for g, lbl in enumerate(labels):
    df_subsetted = df_seat_lctns[df_seat_lctns["group"] == lbl]

    ax = sns.scatterplot(
        data=df_subsetted,
        x="x_loc",
        y="y_loc",
        color=colors[g],
        marker="o",
        s=marker_size,
        edgecolor="#D2D2D3",
    ) 

ax.axis("equal")
ax.axis("off")

plt.legend(labels=['Instagram=23%', 'Facebook=7%', 'Twitter=5%', 'Otros=65%'], title="RRSS favorita de las mujeres , Enero 2023",fontsize=13)
plt.show()
