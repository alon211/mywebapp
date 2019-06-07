import dash
import dash_core_components as dcc
import dash_html_components as html
import os

print(os.getcwd())
external_stylesheets=['bWLwgP.css']
app=dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout=html.Div(children=[html.H1('hello dash'),dcc.Graph(
    id='example-dash',
    figure={
        'data':[
            {'x':[1,2,3],'y':[4,5,6],'type':'bar'},
            {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar'}
        ],
        'layout':{'title':'Dash Data visualision'}
    }

)])

if __name__ == 'main':
    app.run_server(debug=True)


