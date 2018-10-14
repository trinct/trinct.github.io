import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from CO2Data1 import *
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# df = pd.read_csv(
#     'https://gist.githubusercontent.com/chriddyp/' +
#     '5d1ea79569ed194d432e56108a04d188/raw/' +
#     'a9f9e8076b837d541398e999dcbac2b2826a81f8/'+
#     'gdp-life-exp-2007.csv')
df = pd.DataFrame(abc.handl())



app.layout = html.Div([
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure={
            'data': [
                go.Scatter(
                    x=df[df['country_code'] == i]['year'],
                    y=df[df['country_code'] == i]['co2_number'],
                    text=df[df['country_code'] == i]['country_name'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in df.country_code.unique()
            ],
            'layout': go.Layout(
                xaxis={'type': 'log', 'title': 'Year'},
                yaxis={'title': 'Emission tracking'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server(port=8052)