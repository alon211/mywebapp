import dash
import dash_core_components as dcc
import dash_html_components as html

app=dash.Dash(__name__)
print(help(dcc.Dropdown))
options=[{'label':'optionA',"value":0},{'label':'optionB',"value":1},{'label':'optionC',"value":2}]
value=1
app.layout=html.Div(children=[dcc.Dropdown(options=options,value=value,id='dropdown1')])
if __name__=='__main__':
    app.run_server(debug=True)