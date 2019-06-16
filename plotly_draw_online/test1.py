import plotly.plotly as py
import plotly.graph_objs as go
from plotly import tools
tools.set_credentials_file(username='alon211', api_key='75DaXDV6HV7GZRxVo8eZ')
tools.set_config_file(world_readable=True,
                             sharing='public')
# tools.set_config_file(world_readable=False,
#                              sharing='private')
# tools.set_config_file(plotly_domain='https://plotly.your-company.com',
#                       plotly_streaming_domain='stream-plotly.your-company.com')

trace0 = go.Scatter(x=[1, 2, 3, 4],y=[10, 15, 13, 17])
trace1 = go.Scatter(
    x=[1, 2, 3, 4],
    y=[16, 5, 11, 9]
)
data = go.Data([trace0, trace1])

py.iplot(data)