import dash
import dash_core_components as dcc
import dash_html_components as html
import os
external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css']
app=dash.Dash(__name__, external_stylesheets=external_stylesheets)
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Hello Dash',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='Dash: A web application framework for Python.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id='example-graph-2',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                }
            }
        }
    )
])
# app.layout=html.Div(style={'backgroundColor':'black'},
#                     children=[html.H1(children='hello dash',
#                                       style={
#                                              'text-align':'center',
#                                             'color':'skyblue'
#                                         }),
#                     html.Div([html.P(children='Dash: A web application framework for Python.')
#                                 ,dcc.Graph(
#                                     id='example-dash',
#                                     figure={
#                                         'data':[
#                                             {'x':[1,2,3],'y':[4,5,6],'type':'bar','name':'A'},
#                                             {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar','name':'B'}
#                                         ],
#                                         'layout':{'title':'Dash Data visualision'}
#                                     }
#
#                     )])])
app.run_server(port=8052)



