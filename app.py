# import dash
# import plotly
# import dash_core_components as dcc
# import dash_html_components as html
# import plotly.plotly as py
# import plotly.graph_objs as go
# import plotly.figure_factory as FF
#
# #import numpy as np
# import pandas as pd
#
# plotly.tools.set_credentials_file(username='daniel8247', api_key='••••••••••'
#
# #external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
#
# #app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
#
# #app.layout = html.H1('Dash tutorials')
#
# df = pd.read_csv('Vital_Statistics_Deaths_by_Region_and_Age-Group_by_Selected_Cause_of_Death___Beginning_2003.csv')
#
# sample_data_table = FF.create_table(df.head())
# py.plot(sample_data_table, filename='sample-data-table')
#
# #if __name__ == '__main__':
# #    app.run_server(debug=True)

import dash
import dash_table
import pandas as pd

df = pd.read_csv('Vital_Statistics_Deaths_by_Region_and_Age-Group_by_Selected_Cause_of_Death___Beginning_2003.csv')

app = dash.Dash(__name__)

app.layout = dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in df.columns],
    data=df.to_dict('records'),
)

if __name__ == '__main__':
    app.run_server(debug=True)