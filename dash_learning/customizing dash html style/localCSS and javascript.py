'''
导入本地css和js文件必须创建assets文件夹并和运行文件在同一目录下
'''
import dash
import dash_html_components as html

external_stylesheets = ['C://Users//admin//PycharmProjects//mywebapp//bWLwgP.css']

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Div(
        className="app-header",
        children=[
            html.Div('Plotly Dash', className="app-header--title")
        ]
    ),
    html.Div(
        children=html.Div([
            html.H5('Overview'),
            html.Div('''
                This is an example of a simple Dash app with
                local, customized CSS.
            ''')
        ])
    )
])
if __name__ == '__main__':
    app.run_server(debug=True)