import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

# Load the data
df = pd.read_csv('./datasett_oppgave1.csv', delimiter=';', encoding='windows-1252')

# print(df['date'])
# Print rows where 'isValidated' is False
print(df[df['isValidated'] == False])
# Convert latitude and longitude to numeric types
df['latitude'] = pd.to_numeric(df['latitude'], errors='coerce')
df['longitude'] = pd.to_numeric(df['longitude'], errors='coerce')

# Define latitude and longitude range
lat_min, lat_max = 58, 60.1  # Example range for latitude
lon_min, lon_max = 7.5, 11  # Example range for longitude

# Filter the DataFrame based on the latitude and longitude range
df_filtered = df[(df['latitude'] >= lat_min) & (df['latitude'] <= lat_max) &
                 (df['longitude'] >= lon_min) & (df['longitude'] <= lon_max)]

# Ensure the DataFrame has 'latitude' and 'longitude' columns
if 'latitude' in df_filtered.columns and 'longitude' in df_filtered.columns:
    fig = px.scatter_geo(df_filtered, lat='latitude', lon='longitude', 
                         title='Geographical Scatter Plot',
                         hover_name='category',
                         color='category',
                         scope='europe')  # Assuming 'category' is a column you want to show on hover
else:
    raise ValueError("DataFrame does not have 'latitude' and 'longitude' columns.")

# Extract the year from the date column using string slicing
df_filtered['year'] = df_filtered['date'].str[1:5].astype(int)

# Only keep data that has been validated
#df_filtered = df_filtered[df_filtered['isValidated'] == True]
# Group by 'category' and 'year' and count occurrences
category_year_counts = df_filtered.groupby(['category', 'year']).size().reset_index(name='count')

# Create a bar chart that shows the difference in years
fig_bar = px.bar(category_year_counts, x='category', y='count', color='year', barmode='group', 
                 title='Occurrence of Each Unique Category by Year')

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div(children=[
    html.H1(children='Geographical Scatter Plot Dashboard'),

    dcc.Graph(
        id='geo-scatter-plot',
        figure=fig
    ),

    dcc.Graph(
        id='category-bar-chart',
        figure=fig_bar
    )
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)