import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

labels = ['Matemáticas','Lec. Critica.','C. Naturales','Sociales','Inglés']
values = [55.22, 56.01, 52.51, 50.77, 54.84]
labels1 = ['Matemáticas','Lec. Critica.','C. Naturales','Sociales','Inglés']
values1 = [507, 207, 133, 218,1173]

Saber_11_2019_a= pd.read_csv("Saber_11_2019_a.csv", 
                 sep = ',',
                 index_col=0,
                 )

columns = ['COLE_CARACTER',
          'ESTU_DEPTO_RESIDE',
          'PUNT_GLOBAL','COLE_NATURALEZA','PUNT_MATEMATICAS',            
          'PUNT_LECTURA_CRITICA',
          'PUNT_C_NATURALES', 
          'PUNT_SOCIALES_CIUDADANAS',
          'PUNT_INGLES',"ESTU_GENERO"]

base= Saber_11_2019_a.copy()
base = base[columns]

base=base[base.ESTU_GENERO.isin(['F','M'])]
base

basea=base[(base.PUNT_GLOBAL <= 150)]
basea=basea[basea.COLE_CARACTER.isin(["ACADÉMICO","TÉCNICO/ACADÉMICO","TÉCNICO","NO APLICA"])]
basea

import plotly.graph_objects as go

labels = ['Matemáticas','Lec. Critica.','C. Naturales','Sociales','Inglés']
values = [55.22, 56.01, 52.51, 50.77, 54.84]

fig5 = go.Figure(data=[go.Pie(labels=labels, values=values)])

labels1 = ['Matemáticas','Lec. Critica.','C. Naturales','Sociales','Inglés']
values1 = [507, 207, 133, 218,1173]

fig6= go.Figure(data=[go.Pie(labels=labels1, values=values1, hole=.6)])




app.layout = html.Div(
    children=[
        html.H1(children="Proyecto final",
            style = {
                        'textAlign': 'center',
            }),
        html.H2(children="Alex David Ballesteros"),
        html.H3(children="Pie Graph"),
        html.P(
            children="En ésta visualización se puede observar "
            "los valores promedio de los componentes evaluados "
            "en el ICFES 2019 para la ciudad de Bogotá "
            ),
    dcc.Graph(
        id='example-graph-1',
        figure=fig5
            ),
html.Div([
    html.Div([
       html.H1(children='Grafico donut'),#
        html.Div(children='''
           En este gráfico se muestran las proporciones de los estudiantes que sacaron 90 o más en cada componente evaluado
        '''),#
        dcc.Graph(
            id='example-graph-2',
            figure=fig6
        ),  
    ], className='six columns'),
])
])
if __name__ == "__main__":
    app.run_server(debug=True)