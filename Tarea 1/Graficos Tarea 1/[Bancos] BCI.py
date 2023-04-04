import plotly.graph_objects as go

refs = ["https://www.bancoconsorcio.cl/nuestro-banco/estados-financieros", 
        "https://www.bancoestado.cl/content/bancoestado-public/cl/es/home/inicio---bancoestado-corporativo/antecedentes-financieros---bancoestado-corporativo/estados-financieros---bancoestado-corporativo/estados-financieros-anuales---bancoestado-corporativo.html#tabs-e67b8ffa37-item-9e4e68e5c0-tab", 
        "https://www.bci.cl/investor-relations/estados-financieros/"]

colores = ['#c11f1f', '#730000', '#1d9c34']

lineas = []
bci = [78049119, 69158634, 57156299, 50336620, 41350875, 33883396]
estado = [57090784, 53586003, 53119190, 43354976, 40221529, 37890236]
consorcio = [7939144, 7468745, 5916530, 5756872, 4610750, 3752719]
years=["2022", "2021", "2020", "2019", "2018", "2017"]


fig = go.Figure()
Activos= "Activos totales del año= "
fig.add_trace(go.Scatterpolar(
    r=bci,
    theta=years,
    fill='toself',
    name='Banco BCI',
    line_color='green'
))
fig.add_trace(go.Scatterpolar(
    r=estado,
    theta=years,
    fill='toself',
    name='Banco Estado',
    line_color='blue'
))
fig.add_trace(go.Scatterpolar(
    r=consorcio,
    theta=years,
    fill='toself',
    name='Banco Consorcio',
    line_color='red'
))
fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0,80000000]
        )),
    showlegend=True,
    title='Total de activos por banco al 31 de Diciembre de los ultimos 6 años(En M$)',
    font_size=16,
    legend_font_size=16,
    polar_radialaxis_tickprefix='',
    polar_angularaxis_rotation=90
)

fig.show()
