import dash
import dash_html_components as html
import dash_core_components as dcc
import user_module.fig_converter as fc
app=dash.Dash(__name__)
def run_markdown(markdown_text):
    app.layout=html.Div(
        dcc.Markdown(markdown_text))
    app.run_server(debug=True)