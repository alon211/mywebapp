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
def generate_line(mode='lines',type='bar',
                  orientation='v',y=[],x=[],
                  name='line1',visible='true',
                  xaxis='x',yaxis='y',
                  showlegend='true',
                  xcalendar	='gregorian',ycalendar='gregorian',
                  textposition='none',
                  ):
    return {'mode':mode,'type':type,'orientation':orientation,
            'x':x,'y':y,'name':name,'visible':visible,'xaxis':xaxis,
            'yaxis':yaxis,'showlegend':showlegend,'xcalendar':xcalendar,
            'ycalendar':ycalendar,'textposition':textposition}

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
def generate_graph(id,lines):

    return dcc.Graph(
        id=id,
        figure={
            'data':lines,
            'layout': {
                'plot_bgcolor': 'black',
                'paper_bgcolor': 'black',
                'font': {
                    'color': 'blue'
                },
                'barmode':'relative'
            }
        }
    )
d=eval(df.to_json())
df.to_json('1.json')
x=list(d['state'].values())
y_all_axis=[list(d[col_name].values()) for col_name in df.columns][1:]
lines=[generate_line(x=x,y=y_all_axis[i],name=df.columns[i]) for i in range(len(df.columns)-1)]
app=dash.Dash(__name__)

app.layout=html.Div([
                    # header
                    html.H1(['US Agriculture Exports(2011)'],style={'color':'black','textAlign':'center'}),
                    gernerate_table(df,10),
                    generate_graph('exports',lines)
                    ])

if __name__=='__main__':
    app.run_server(port=8050,debug=True)


    pass