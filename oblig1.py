import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

# Load the data
df = pd.read_csv('./datasett_oppgave1.csv', delimiter=';', encoding='windows-1252')

# Ensure the DataFrame has 'latitude' and 'longitude' columns
if 'latitude' in df.columns and 'longitude' in df.columns:
    fig = px.scatter_geo(df, lat='latitude', lon='longitude', 
                         title='Geographical Scatter Plot',
                         hover_name='category')  # Assuming 'category' is a column you want to show on hover
else:
    raise ValueError("DataFrame does not have 'latitude' and 'longitude' columns.")

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div(children=[
    html.H1(children='Geographical Scatter Plot Dashboard'),

    dcc.Graph(
        id='geo-scatter-plot',
        figure=fig
    )
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)