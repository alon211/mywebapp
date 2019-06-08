import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

# df=pd.read_csv('https://gist.githubusercontent.com/chriddyp/'
#             'c78bf172206ce24f77d6363a2d754b59/raw/'
#             'c353e8ef842413cae56ae3920b8fd78468aa4cb2/'
#             'usa-agricultural-exports-2011.csv')
# df.to_csv('table_data.csv')
df=pd.read_csv('table_data.csv')
cols=list(df.columns)
cols[0]='index'
df.columns=cols
df.set_index(cols)
df=df.iloc[:,2:]
# print(type(df.iloc[:,2:]))
def gernerate_table(dataframe,maxrow):
    table_style={'border':"5px solid blue",
                 "borderCollapse":"collapse",
                 "textAlign":'center',
                 'height':'50px',
                 'verticalAlign':'bottom',
                 'width':'100%',
                 'padding':'15px',
                 'borderSpacing':'10px 50px'}
    return html.Table(children=[#header
        html.Tr([html.Th([i]) for i in dataframe.columns])]+
                                # body
                               [html.Tr([html.Td([dataframe.iloc[r,c]]) for c in range(len(dataframe.columns))])
                                                                        for r in range(len(dataframe))]
                      )
def generate_graph(id,dataframe):
    data_json=dataframe.to_json()
    data=[]
    return dcc.Graph(
        id=id,
        figure={
            'data':eval(dataframe.to_json()),
            'layout': {
                'plot_bgcolor': 'black',
                'paper_bgcolor': 'black',
                'font': {
                    'color': 'blue'
                }
            }
        }
    )
app=dash.Dash(__name__)
              # external_scripts=external_scripts,
              # external_stylesheets=external_stylesheets)
app.layout=html.Div([
                    # header
                    html.H1(['US Agriculture Exports(2011)'],style={'color':'black','textAlign':'center'}),
                    gernerate_table(df,10),
                    generate_graph('exports',df)
                    ])
if __name__=='__main__':
    # app.run_server(port=8050,debug=True)
    d=eval(df.to_json())
    print(len(d['state']))
    # print(type(eval(d)))

    pass